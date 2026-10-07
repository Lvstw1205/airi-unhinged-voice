#!/usr/bin/env python3
"""Local Ollama conversation with an optional explicit-language voice persona."""
import argparse
import json
from pathlib import Path
import urllib.request
from local_http import LocalHandler, serve
from persona import effective_mode, system_prompt, output_text

ROOT = Path(__file__).resolve().parent
OLLAMA = 'http://127.0.0.1:11434'


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args):
        raise ValueError('Local Ollama redirects are not supported.')


def request(path, body=None):
    req = urllib.request.Request(OLLAMA + path, data=None if body is None else json.dumps(body).encode(),
                                 headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect()).open(req, timeout=120 if body else 3) as response:
            return json.loads(response.read(4 * 1024 * 1024))
    except Exception:
        raise ValueError('Ollama 연결을 확인하세요. Ollama를 실행하고 로컬 모델을 설치해야 합니다.') from None


def models():
    return [m['name'] for m in request('/api/tags').get('models', []) if isinstance(m.get('name'), str)
            and not m.get('remote_host') and not m.get('remote_model')
            and ':cloud' not in m['name'] and not m['name'].endswith('-cloud')]


def chat(body):
    mode, guest = body.get('mode', 'calm'), body.get('guest', False)
    selected = effective_mode(mode, guest)
    text = body.get('text')
    if not isinstance(text, str) or not 1 <= len(text.strip()) <= 6000:
        raise ValueError('메시지는 1~6,000자로 입력하세요.')
    history = body.get('history', [])
    if not isinstance(history, list) or len(history) > 12:
        raise ValueError('Conversation history is too long.')
    clean = []
    for item in history:
        if not isinstance(item, dict) or item.get('role') not in ('user', 'assistant') or not isinstance(item.get('content'), str) or len(item['content']) > 12000:
            raise ValueError('Invalid conversation history.')
        clean.append({'role': item['role'], 'content': item['content']})
    model = body.get('model')
    if model not in models():
        raise ValueError('설치된 로컬 모델을 선택하세요.')
    messages = [{'role': 'system', 'content': system_prompt(mode, guest)}, *clean, {'role': 'user', 'content': text}]
    result = request('/api/chat', {'model': model, 'messages': messages, 'stream': False,
                                  'think': False, 'options': {'num_predict': 700, 'temperature': .8}})
    return {'text': output_text(result.get('message', {}).get('content'), mode, guest), 'mode': selected, 'model': model}


class Handler(LocalHandler):
    max_body = 200000
    def route_get(self, path):
        if path == '/api/status':
            try:
                self.send_json({'models': models(), 'connected': True})
            except ValueError as exc:
                self.send_json({'models': [], 'connected': False, 'error': str(exc)})
            return True
        assets = {'/': ('index.html', 'text/html; charset=utf-8'), '/app.js': ('app.js', 'text/javascript'), '/style.css': ('style.css', 'text/css')}
        if path not in assets:
            return False
        name, mime = assets[path]; content = (ROOT / 'web' / name).read_bytes()
        self.send_response(200); self.headers_common(); self.send_header('Content-Type', mime)
        self.send_header('Content-Length', str(len(content))); self.end_headers(); self.wfile.write(content)
        return True
    def route_post(self, path, body):
        if path != '/api/chat':
            raise ValueError('Unknown operation')
        return chat(body)


def main():
    parser = argparse.ArgumentParser(description='AIRI Unhinged Voice · opt-in persona studio')
    parser.add_argument('--port', type=int, default=8771)
    args = parser.parse_args()
    if not 1024 <= args.port <= 65535:
        parser.error('Port must be between 1024 and 65535')
    serve(Handler, args.port)


if __name__ == '__main__': main()
