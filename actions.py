from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json


class Searchforlocation(Action):
    def name(self):
        return 'action_location'

    def run(self, dispatcher, tracker, domain):
        locn = tracker.get_slot('location')
        dispatcher.utter_message("------------------------------\n"+locn)
        FromTier12 = ['pune','delhi','mumbai','noida']
        FromTier3 = ['bhutan','gurgaon']
        if locn.lower() in FromTier12:
            responses = "Tier12"
            dispatcher.utter_message("---------------It is in Tier12---------------\n")    
            return [SlotSet('Validate_loc',responses),SlotSet('location',locn)]
        elif locn.lower() in FromTier3:
            responses = "NotWorking"
            dispatcher.utter_message("---------------It is in Tier3---------------\n")
            return [SlotSet('Validate_loc',responses),SlotSet('location',None)]
        else:
            response = "OutOfRange"
            dispatcher.utter_message("---------------It is Out of range---------------\n")
            return [SlotSet('Validate_loc',responses),SlotSet('location',None)]
        
        

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'

	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"5200b060757d691783e5c806775b36bd"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
        #price = tracker.get_slot('price')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'mexican':73,'American':1,'chinese':25,'italian':55,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				response=response+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " has been rated ---" + restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n\n"

		dispatcher.utter_message("------------------------------\n"+response)
		return [SlotSet('location',loc)]
