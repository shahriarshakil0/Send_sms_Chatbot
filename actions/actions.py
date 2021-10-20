# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from twilio.rest import Client

class ActionSubmit(Action):

    def name(self) -> Text:
        return "action_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        account_sid = 'from twilio'
        auth_token = 'from twilio'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            from_='from twilio get a phone number',
            body=tracker.get_slot("message"),  #'hello, this is a test message for automation',
            to = tracker.get_slot("mobile_number")     # '+918209829808'
        )

        print(message.sid)

        dispatcher.utter_message(text="Message has been sent successfully to {}".format(tracker.get_slot("mobile_number")))

        return []

from rasa_sdk.events import AllSlotsReset

class ActionHelloWorld(Action):

     def name(self) -> Text:
            return "action_another"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message("Want to send another SMS")

         return [AllSlotsReset()]