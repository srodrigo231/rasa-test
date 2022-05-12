# This files contains your custom actions which can be used to run
# custom Python code. API calls
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"]
#

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=f'La hora es {str(datetime.now())}')

        return []

from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

ALLOWED_PIZZA_SIZES = ["pequeña", "mediana", "grande", "extra grande", "p", "m", "g", "xg"]
ALLOWED_PIZZA_TYPES = ["muzzarella", "vegetariana", "pepperoni", "hawaiana"]

class ValidateSimplePizzaForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_simple_pizza_form"

    def validate_pizza_size(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `pizza_size` value."""
        if slot_value.lower() not in ALLOWED_PIZZA_SIZES:
            dispatcher.utter_message(text=f"Solo aceptamos pizzas de tamaño : p/m/g/xg.")
            return {"pizza_size": None}
        dispatcher.utter_message(text=f"Listo! Quieres una pizza {slot_value}.")
        return {"pizza_size": slot_value}

    def validate_pizza_type(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `pizza_type` value."""
        if slot_value not in ALLOWED_PIZZA_TYPES:
            dispatcher.utter_message(text=f"No conozco ese tipo de pizza. Tenemos {'/'.join(ALLOWED_PIZZA_TYPES)}.")
            return {"pizza_type": None}
        dispatcher.utter_message(text=f"Perfecto! Quieres una pizza {slot_value}.")
        return {"pizza_type": slot_value}


# from rasa_sdk.forms import FormValidationAction

# class ValidateHealthForm(FormValidationAction):
#     def name(self) -> Text:
#         return "validate_health_form"

#     async def validate_confirm_exercise(
#         self,
#         value: Text,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> Dict[Text, Any]:
#         if value:
#             return {"confirm_exercise": True}
#         else:
#             return {"exercise": "None", "confirm_exercise": False }


# class ActionSubmitResults(Action):
#     def name(self) -> Text:
#         return "action_submit_results"
#     def run(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict]:

#         confirm_exercise = tracker.get_slot("confirm_exercise")
#         exercise = tracker.get_slot("exercise")
#         sleep = tracker.get_slot("sleep")
#         stress = tracker.get_slot("stress")
#         diet = tracker.get_slot("diet")
#         goal = tracker.get_slot("goal")

#         response = create_health_log(
#                 confirm_exercise=confirm_exercise,
#                 exercise=exercise,
#                 sleep=sleep,
#                 stress=stress,
#                 diet=diet,
#                 goal=goal
#             )

#         dispatcher.utter_message("Thanks, your answers have been recorded!")
#         return []