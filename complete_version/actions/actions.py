# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from googletrans import Translator

import pandas as pd
import numpy as np
import os

translator = Translator(service_urls=['translate.googleapis.com'])


class ActionLanguageSearch(Action):

    def name(self) -> Text:
        return "action_lang_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data_path = os.path.join("data", "cldf-datasets-wals-014143f", "cldf", "languages.csv")
        wals_data = pd.read_csv(data_path)
        entities = list(tracker.get_latest_entity_values("language"))

        print(entities)
        if len(entities) >= 0 :
            query_lang = entities.pop()
            query_lang = translator.translate(query_lang,dest ='en').text
            query_lang = query_lang.lower().capitalize()
            print(query_lang)
            
            out_row = wals_data[wals_data["Name"] == query_lang].to_dict("records")

            if len(out_row) > 0:
                out_row = out_row[0]
                out_text = "భాష %s కుటుంబానికి చెందినది %s\n జాతితో %s\n మరియు ISO కోడ్ ఉంది %s" % (translator.translate(out_row["Name"],dest='te').text,translator.translate(out_row["Family"],dest='te').text,translator.translate(out_row["Genus"],dest='te').text, out_row["ISO_codes"])
                dispatcher.utter_message(text = out_text)
            else:
                dispatcher.utter_message(text = "క్షమించండి! భాష కోసం మాకు రికార్డులు లేవు %s" % translator.translate(query_lang,dest='te').text)

        return []
class ActionFamilySearch(Action):

    def name(self) -> Text:
        return "action_fam_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data_path = os.path.join("data", "cldf-datasets-wals-014143f", "cldf", "languages.csv")
        wals_data = pd.read_csv(data_path)
        entities = list(tracker.get_latest_entity_values("language"))

        print(entities)
        if len(entities) >= 0 :
            query_lang = entities.pop()
            query_lang = translator.translate(query_lang,dest ='en').text
            query_lang = query_lang.lower().capitalize()
            print(query_lang)
            
            out_row = wals_data[wals_data["Name"] == query_lang].to_dict("records")

            if len(out_row) > 0:
                out_row = out_row[0]
                out_text = "ఈ భాష యొక్క కుటుంబం %s" % (translator.translate(out_row["Family"],dest='te').text)
                dispatcher.utter_message(text = out_text)
            else:
                dispatcher.utter_message(text = "క్షమించండి! భాష కోసం మాకు రికార్డులు లేవు %s" % translator.translate(query_lang,dest='te').text)

        return []
class ActionISOSearch(Action):

    def name(self) -> Text:
        return "action_iso_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data_path = os.path.join("data", "cldf-datasets-wals-014143f", "cldf", "languages.csv")
        wals_data = pd.read_csv(data_path)
        entities = list(tracker.get_latest_entity_values("language"))

        print(entities)
        if len(entities) >= 0 :
            query_lang = entities.pop()
            query_lang = translator.translate(query_lang,dest ='en').text
            query_lang = query_lang.lower().capitalize()
            print(query_lang)
            
            out_row = wals_data[wals_data["Name"] == query_lang].to_dict("records")

            if len(out_row) > 0:
                out_row = out_row[0] 
                print(out_row)
                out_text = "ISO కోడ్ %s" % out_row["ISO_codes"]
                dispatcher.utter_message(text = out_text)
            else:
                dispatcher.utter_message(text = "క్షమించండి! భాష కోసం మాకు రికార్డులు లేవు %s" % translator.translate(query_lang,dest='te').text)

        return []
class ActionFamilyLanguagesSearch(Action):

    def name(self) -> Text:
        return "action_famlang_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data_path = os.path.join("data", "cldf-datasets-wals-014143f", "cldf", "languages.csv")
        wals_data = pd.read_csv(data_path)
        entities = list(tracker.get_latest_entity_values("language"))

        print(entities)
        if len(entities) >= 0 :
            query_lang = entities.pop()
            query_lang = translator.translate(query_lang,dest ='en').text
            query_lang = query_lang.lower().capitalize()
            print(query_lang)
            
            out_row = family_lang = list(wals_data.loc[np.where(wals_data['Family'] == (wals_data[wals_data['Name']==query_lang]['Family'].values[0]))]['Name'].values[:10])

        

            if len(out_row) > 0:
                out_text = "ఈ కుటుంబంలోని కొన్ని ఇతర భాషలు %s" % (out_row)
                dispatcher.utter_message(text = out_text)
            else:
                dispatcher.utter_message(text = "క్షమించండి! భాష కోసం మాకు రికార్డులు లేవు %s" % translator.translate(query_lang,dest='te').text)

        return []
