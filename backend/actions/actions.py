from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# class ActionProvideLesson(Action):

#     def name(self) -> Text:
#         return "action_provide_lesson"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         language = tracker.get_slot("language")
#         lesson_type = tracker.get_slot("lesson_type")
#         difficulty_level = tracker.get_slot("difficulty_level")

#         if language and lesson_type and difficulty_level:
#             lesson = f"Here's a {difficulty_level} {lesson_type} lesson in {language}."
#         else:
#             lesson = "I need more information to provide a lesson."

#         dispatcher.utter_message(text=lesson)
#         return []

class ActionProvideLesson(Action):

    def name(self) -> Text:
        return "action_provide_lesson"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        language = tracker.get_slot('language')
        lesson_type = tracker.get_slot('lesson_type')
        difficulty_level = tracker.get_slot('difficulty_level')
        
        if language and lesson_type and difficulty_level:
            response = f"Here's a {difficulty_level} {lesson_type} lesson in {language}."
        else:
            response = "I need more information to provide a lesson."
        
        dispatcher.utter_message(text=response)
        
        return []


class ActionGenerateQuiz(Action):

    def name(self) -> Text:
        return "action_generate_quiz"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        language = tracker.get_slot("language")
        lesson_type = tracker.get_slot("lesson_type")
        difficulty_level = tracker.get_slot("difficulty_level")

        if language and lesson_type and difficulty_level:
            quiz = f"Here's a {difficulty_level} {lesson_type} quiz in {language}."
        else:
            quiz = "I need more information to generate a quiz."

        dispatcher.utter_message(text=quiz)
        return []

class ActionPracticeConversation(Action):

    def name(self) -> Text:
        return "action_practice_conversation"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        language = tracker.get_slot("language")
        conversation = f"Let's practice a conversation in {language}."

        dispatcher.utter_message(text=conversation)
        return []

