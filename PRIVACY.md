# Privacy

The Python server listens on 127.0.0.1. Browser requests require same-origin validation and
a local session token. HTTP request bodies are not logged. No chat history, recordings,
microphone capture, camera data, analytics or API credentials are saved by this app.

The current tab holds the displayed conversation; the latest 12 messages are sent to Ollama on localhost for context.
The app does not invoke Ollama cloud aliases. Ollama's own configuration and diagnostics
remain under your control. Speech uses browser voices marked as local; install a local
voice in your OS if none is listed. No microphone permission is requested.

Closing/reloading the tab or selecting a new conversation clears this app's in-memory chat.
There is no account system, public hosting or remote access in the supported launcher.
