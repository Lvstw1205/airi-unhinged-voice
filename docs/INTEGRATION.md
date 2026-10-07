# Reuse the tone layer

Copy `persona.py` into a personal/noncommercial project, preserving its license and attribution.

```python
from persona import system_prompt, output_text

mode = "unhinged"  # Only after the user selects this tone.
guest = False
messages = [{"role": "system", "content": system_prompt(mode, guest)},
            {"role": "user", "content": "Help me get through this chaotic day."}]
# Send messages to your configured model, then:
# spoken = output_text(model_answer, mode, guest)
```

For AIRI Assistant, add this as a separate optional style layer after its core working
protocol. Keep the default calm, expose guest/stop controls and apply the selected mode at
generation and playback. The standalone app demonstrates that flow. This release does not
silently overwrite an existing Assistant installation or its private persona files.

Pass the returned text to a voice the user is licensed to use. No voice clone or model
weights are bundled. Do not reuse someone's private voice recording without permission.
Tone settings do not authorize external actions or relax the host's tool controls.
