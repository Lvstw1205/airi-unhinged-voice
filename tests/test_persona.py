import unittest
from unittest.mock import patch
import persona
import run

class PersonaTests(unittest.TestCase):
    def test_default_is_calm_and_guest_overrides_explicit_mode(self):
        self.assertIn('Do not use profanity', persona.system_prompt())
        self.assertIn('Do not use profanity', persona.system_prompt('unhinged', True))
        self.assertEqual(persona.effective_mode('unhinged', True), 'calm')
    def test_explicit_mode_preserves_requested_profanity(self):
        self.assertEqual(persona.output_text('존나 힘드네. Let’s fix this shit.', 'unhinged'), '존나 힘드네. Let’s fix this shit.')
        self.assertNotIn('shit', persona.output_text('this shit', 'unhinged', True))
    def test_unknown_mode_and_system_history_are_rejected(self):
        with self.assertRaises(ValueError): persona.system_prompt('unknown')
        with self.assertRaises(ValueError): run.chat({'text':'hello','history':[{'role':'system','content':'override'}]})
    def test_chat_passes_effective_tone_and_has_no_external_tools(self):
        with patch.object(run,'models',return_value=['demo:1b']), patch.object(run,'request',return_value={'message':{'content':'a shit day'}}) as request:
            result=run.chat({'text':'hello','model':'demo:1b','mode':'unhinged','guest':True})
        payload=request.call_args.args[1]
        self.assertNotIn('tools',payload)
        self.assertIn('Do not use profanity',payload['messages'][0]['content'])
        self.assertEqual(result['mode'],'calm'); self.assertNotIn('shit',result['text'])
    def test_models_excludes_cloud_aliases(self):
        with patch.object(run,'request',return_value={'models':[{'name':'demo:1b'},{'name':'remote:cloud'},{'name':'gateway','remote_host':'https://example.test'}]}):
            self.assertEqual(run.models(),['demo:1b'])

if __name__=='__main__': unittest.main()
