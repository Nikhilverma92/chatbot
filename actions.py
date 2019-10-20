from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import zomatopy
import json
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Searchforlocation(Action):
    def name(self):
        return 'action_location'

    def run(self, dispatcher, tracker, domain):
        locn = tracker.get_slot('location')
        dispatcher.utter_message("------------------------------\n"+locn)
        FromTier12 = ['bangalore', 'chennai', 'delhi', 'hyderabad', 'kolkata', 'mumbai', 'ahmedabad', 'pune', 'agra', 'ajmer', 'aligarh', 'amravati', 'amritsar', 'asansol', 'aurangabad', 'bareilly', 'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bilaspur', 'bokaro steel city', 'chandigarh', 'coimbatore nagpur', 'cuttack', 'dehradun', 'dhanbad', 'bhilai', 'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gwalior', 'gurgaon', 'guwahati', 'hubli–dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kakinada', 'kannur', 'kanpur', 'kochi', 'kottayam', 'kolhapur', 'kollam', 'kota', 'kozhikode', 'kurnool', 'ludhiana', 'lucknow', 'madurai', 'malappuram', 'mathura', 'goa', 'mangalore', 'meerut', 'moradabad', 'mysore', 'nanded', 'nashik', 'nellore', 'noida', 'palakkad', 'patna', 'pondicherry', 'purulia allahabad', 'raipur', 'rajkot', 'rajahmundry', 'ranchi', 'rourkela', 'salem', 'sangli', 'siliguri', 'solapur', 'srinagar', 'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tirupati', 'tirunelveli', 'tiruppur', 'tiruvannamalai', 'ujjain', 'bijapur', 'vadodara', 'varanasi', 'vasai-virar city', 'vijayawada', 'vellore', 'warangal', 'surat', 'visakhapatnam']
        FromTier3 = ['bhutan','Mexico']
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
        price = tracker.get_slot('price')
        location_detail=zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        cuisines_dict={'mexican':73,'American':1,'chinese':25,'italian':55,'north indian':50,'south indian':85}
        results=zomato.restaurant_search_all("", lat, lon, str(cuisines_dict.get(cuisine)),100)
        d = json.loads(results)
        response=""
        output_data=""
        restaurant_data={}
        if d['results_found'] == 0:
            output_data= "No Restaurants were found for the given input."
        else:
            """
            for restaurant in d['restaurants']:
                #response=response+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " has been rated ---" + restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n\n"
               
                restaurant_data['Name']=restaurant['restaurant']['name'];
                restaurant_data['Location']=restaurant['restaurant']['location']['address'];
                restaurant_data['Rating']=restaurant['restaurant']['user_rating']['aggregate_rating'];
                restaurant_data['CFT']=restaurant['restaurant']['average_cost_for_two'];
            """   
            response = pd.DataFrame({"Name":restaurant['restaurant']['name'],"Location":restaurant['restaurant']['location']['address'],"Rating":restaurant['restaurant']['user_rating']['aggregate_rating'],"CFT":restaurant['restaurant']['average_cost_for_two']} for restaurant in d['restaurants'])

            if price.lower() == "low":
                response = response[response['CFT']<=300];
            elif price.lower() == "medium":
                response = response[(response['CFT']>300) & (response['CFT']<=700)]
            else:
                response = response[response['CFT']>700]

            response = response.sort_values(by=["CFT"],ascending =False)

            response=response.head(5);
            #dispatcher.utter_message("---------------------------------------------\n"response)
                        
            for a in response.index:
                output_data= output_data + str(response["Name"][a]) + " in " + str(response["Location"][a]) + " has been rated -- " + str(response["Rating"][a]) +" CFT is --  "+ str(response["CFT"][a]) + "\n"

            dispatcher.utter_message("------------------------------\n"+output_data)
        return [SlotSet('location',loc)]

	
class SendMailToReceiver(Action):
	def name(self):
			return 'action_email'
		
	def run(self, dispatcher, tracker, domain):
		#email_received = tracker.get_slot ('email')
		#restaurants10 = restaurants.head(10)
		# creates SMTP session 
		mail_content = 'Hello, This is a simple mail.'
		#The mail addresses and password
		sender_address = 'restaurantfoodiesearch@gmail.com'
		sender_pass = 'qwerty@123'
		receiver_address = 'akkic2@gmail.com'
		#Setup the MIME
		message = MIMEMultipart()
		message['From'] = sender_address
		message['To'] = receiver_address
		message['Subject'] = 'A test mail sent by Python. It has not an attachment.'   #The subject line
		#The body and the attachments for the mail
		message.attach(MIMEText(mail_content, 'plain'))
		#Create SMTP session for sending the mail
		session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
		session.starttls() #enable security
		session.login(sender_address, sender_pass) #login with mail_id and password
		text = message.as_string()
		session.sendmail(sender_address, receiver_address, text)
		session.quit()
		
        dispatcher.utter_message("-----------------Mail Sent-----------------\n")
        

