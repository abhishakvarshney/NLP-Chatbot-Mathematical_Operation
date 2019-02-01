from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging
import re

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet, FollowupAction

logger = logging.getLogger(__name__)

#TODO age validation,Transpose matrix
class ActionFirstNameSlot(Action):
    def name(self):
        return "action_first_name_slot"

    def run(self, dispatcher, tracker, domain):
        first_name = tracker.latest_message['text']
        return [SlotSet("first_name", first_name), FollowupAction("utter_lastname")]

class ActionLastNameSlot(Action):
    def name(self):
        return "action_last_name_slot"

    def run(self, dispatcher, tracker, domain):
        last_name = tracker.latest_message['text']
        return [SlotSet("last_name", last_name), FollowupAction("utter_gender")]

class ActionAge(Action):
    def name(self):
        return "action_age"

    def run(self, dispatcher, tracker, domain):
        gender = tracker.latest_message['text']
        dispatcher.utter_message("May I know your age?")
        return [SlotSet("gender", gender), FollowupAction("action_listen")]

class ActionAgeValidation(Action):
    def name(self):
        return "action_age_validation"

    def run(self, dispatcher, tracker, domain):
        age_string = tracker.latest_message['text']
        age = re.findall('\d+', age_string)
        if age_string.isdigit() is True:
            return [SlotSet("age", age_string), FollowupAction("action_registration")]
        else:
            if isinstance(age, int) is True:
                age = int(age[0])
                return [SlotSet("age", age), FollowupAction("action_registration")]
            else:
                dispatcher.utter_message("I couldn't quite get how that response can be your age :/ Please enter your valid age.")
                return [SlotSet("validation", "invalid"), FollowupAction("action_listen")]

class ActionRegistration(Action):
    def name(self):
        return "action_registration"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Congratulations! Registration Successful.")
        return [FollowupAction("action_work")]

class ActionWork(Action):
    def name(self):
        return "action_work"

    def run(self, dispatcher, tracker, domain):
        first_name = tracker.get_slot("first_name")
        last_name = tracker.get_slot("last_name")
        dispatcher.utter_message("Hello {} {}, How are you? For a sample of my work I can show you how to make a transpose of a 3X3 matrix.".format(first_name, last_name))
        return[FollowupAction("utter_firstrow")]

class ActionFirstRow(Action):
    def name(self):
        return "action_first_row"

    def run(self, dispatcher, tracker, domain):
        first_row = tracker.latest_message['text']
        return [SlotSet("first_row", first_row), FollowupAction("utter_secondrow")]

class ActionSecondRow(Action):
    def name(self):
        return "action_second_row"

    def run(self, dispatcher, tracker, domain):
        second_row = tracker.latest_message['text']
        return [SlotSet("second_row", second_row), FollowupAction("utter_thirdrow")]

class ActionThirdRow(Action):
    def name(self):
        return "action_third_row"

    def run(self, dispatcher, tracker, domain):
        third_row = tracker.latest_message['text']
        return [SlotSet("third_row", third_row), FollowupAction("action_transpose_matrix")]

class ActionTransposeMatrix(Action):
    def name(self):
        return "action_transpose_matrix"

    def run(self, dispatcher, tracker, domain):
        first_row = tracker.get_slot("first_row")
        second_row = tracker.get_slot("second_row")
        third_row = tracker.get_slot("third_row")
        first_row = [int(i) for i in re.findall(r"\b\d+\b", first_row)]
        second_row = [int(i) for i in re.findall(r"\b\d+\b", second_row)]
        third_row = [int(i) for i in re.findall(r"\b\d+\b", third_row)]
        dispatcher.utter_message("This is the transpose of the input matrix")
        dispatcher.utter_message("Row 1 : [{}, {}, {}]".format(first_row[0], second_row[0], third_row[0]))
        dispatcher.utter_message("Row 2 : [{}, {}, {}]".format(first_row[1], second_row[1], third_row[1]))
        dispatcher.utter_message("Row 3 : [{}, {}, {}]".format(first_row[2], second_row[2], third_row[2]))