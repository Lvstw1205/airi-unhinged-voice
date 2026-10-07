# AIRI Unhinged Voice

### Expressive Local AI Voice & Persona Studio

A lightweight companion studio for choosing how your local AI speaks: calm, playful, or
irreverent with optional profanity. Includes a reusable Python persona layer, local Ollama
chat and speech through voices installed on your own computer.

**Community source release · v0.1.1 · Python 3.11+ · Explicit language is opt-in**

## What you can try

- **Calm** starts by default. **Playful** adds light humor. **Unhinged** permits natural swearing.
- One-click **guest mode** overrides the selected persona with the calm tone.
- Choose an installed local voice, preview a sample, change speaking speed and stop playback.
- Type a message to a local Ollama model; optionally have the answer read aloud.
- Reuse `persona.py` in your own assistant without adding tool permissions or voice cloning.

This is a text-to-speech persona application, not a new speech model or a microphone-driven
realtime call system. No private voice likeness, conversation history or API key is included.
The exact accent, delivery and language coverage depend on installed OS/browser voices.

## Start in three steps

1. Install Python 3.11+ and [Ollama](https://ollama.com/). Start Ollama and install a local model,
   for example `ollama pull qwen3:4b`.
2. Download the [release ZIP](https://github.com/Lvstw1205/airi-unhinged-voice/releases/latest),
   extract it, and run `python3 run.py`. On macOS, you can double-click `Start.command`.
3. Open **http://127.0.0.1:8771**, select your model and voice, then send a message.

The application itself uses only Python's standard library. Model weights are downloaded
separately and keep their own licenses. If no local voice is available, install one in your
OS accessibility/speech settings; text chat still works. Voice previews do not require Ollama.

## Privacy and behavior

The server binds to localhost, validates the local browser session and does not save chats.
Conversation stays in the current browser tab; the latest 12 messages are sent to local Ollama for
context. **새 대화** clears that tab's context. Only voices marked local by the browser are
offered; Ollama cloud aliases are excluded. See [PRIVACY.md](PRIVACY.md).

Unhinged changes style, not truthfulness or authorization. It does not unlock files, accounts,
tools or external actions. Guest/calm output includes a small profanity-pattern backstop;
it is not a universal moderation or language-classification system. Model behavior varies. Repeated or unfinished answers get one bounded retry, then a clear
error instead of being read aloud. Changing tone cancels the pending reply in the browser;
guest mode also blocks replay of earlier Unhinged replies.

## Documentation

- [한국어 안내](README.ko.md)
- [Reuse the persona layer](docs/INTEGRATION.md)
- [Verification and limitations](docs/VALIDATION.md)
- [Third-party notices](THIRD_PARTY_NOTICES.md)

## License

Original code is source-available under [PolyForm Noncommercial 1.0.0](LICENSE.md).
Personal and noncommercial use, modification and redistribution are subject to those terms.
Commercial use needs separate permission. This is not an OSI-approved open-source license.

Part of [AIRI Community Projects](https://github.com/users/Lvstw1205/projects/1).
