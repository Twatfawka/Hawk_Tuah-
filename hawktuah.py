from ask_sdk_model import ui

class AskQuestionIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("AskQuestionIntent")(handler_input)

    def handle(self, handler_input):
        # Example of retrieving an audio file URL from S3
        audio_url = "https://drive.google.com/file/d/16mECNZC95dGZ_eNNck71bf7vbMq-_4Ze/view?usp=drivesdk"
        
        # Building the response with audio playback
        response_builder = handler_input.response_builder
        response_builder.speak("Here's an audio response.")
        response_builder.add_directive(ui.PlayDirective(ui.AudioItem(audio_url)))
        
        return response_builder.response
