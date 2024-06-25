from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.utils import is_intent_name
from ask_sdk_model import ui

sb = SkillBuilder()

class AskQuestionIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("AskQuestionIntent")(handler_input)

    def handle(self, handler_input):
        # Example of retrieving an audio file URL from S3
        audio_url = "https://drive.google.com/file/d/16mECNZC95dGZ_eNNck71bf7vbMq-_4Ze/view?usp=drivesdk"
        "
        
        # Building the response with audio playback
        response_builder = handler_input.response_builder
        response_builder.speak("Here's an audio response.")
        response_builder.add_directive(ui.PlayDirective(ui.AudioItem(audio_url)))
        
        return response_builder.response

class BuyIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("BuyIntent")(handler_input)

    def handle(self, handler_input):
        # Check entitlement status
        entitlement = handler_input.service_client_factory.get_monetization_service().get_in_skill_products()
        if entitlement.status == "ENTITLED":
            speak_output = "You are already entitled to use this skill."
        else:
            # Initiate buy process with $1.99 price
            speak_output = "To purchase this skill for $1.99, please check your Alexa app."

        return handler_input.response_builder.speak(speak_output).response

class CancelIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("CancelIntent")(handler_input)

    def handle(self, handler_input):
        # Initiate cancel process
        speak_output = "To cancel this skill, please check your Alexa app."

        return handler_input.response_builder.speak(speak_output).response

# Add all request handlers to the skill builder
sb.add_request_handler(AskQuestionIntentHandler())
sb.add_request_handler(BuyIntentHandler())
sb.add_request_handler(CancelIntentHandler())

# Lambda handler function
lambda_handler = sb.lambda_handler()
