# Release validation — 2026-10-07

- Eight Python tests passed: tone defaults, guest override, explicit profanity, invalid
  input/history roles, cloud-alias filtering and the Ollama request/response boundary, repetition detection and bounded retries.
- Python and JavaScript syntax checks passed; no private paths, account data or secret
  material is part of the source export.
- Browser startup, installed voice list and an actual local Ollama response were checked.
- An actual local model produced repetitive output during testing; regression tests now
  reject that pattern and unfinished generations rather than playing them.
- The shared localhost HTTP boundary uses the same tested implementation as Stock101.

The persona is model-dependent. Profanity matching is a limited backstop, not an exhaustive
language classifier. Voice availability and quality depend on browser/OS. No personal voice
cloning, microphone recognition or cross-browser speech certification is claimed.

Run `python3 -m unittest discover -s tests -v` from this repository.
