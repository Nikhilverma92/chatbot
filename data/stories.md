## Generated Story by hand 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Low"}
	- slot{"price": "Low"}
	- action_restaurant
	- utter_ask_email
* affirm
	- utter_ask_for_email_address
* restaurant_search{"email": "email@gmail.com"}
	- slot{"email": "email@gmail.com"}
	- utter_email_sent_goodbye
	
	
## Generated Story by hand 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "High"}
	- slot{"price": "High"}
	- action_restaurant
	- utter_ask_email
* deny
	- utter_goodbye



## Generated Story -8972014242190157214
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "High"}
	- slot{"price": "High"}
    - action_restaurant
    - utter_ask_email
* affirm
    - utter_ask_for_email_address
* restaurant_search{"email": "email@gmail.com"}
	- slot{"email": "email@gmail.com"}
    - utter_email_sent_goodbye
    - export


## Generated Story -by hand
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Medium"}
	- slot{"price": "Medium"}
    - action_restaurant
    - utter_ask_email
* deny
	-utter_goodbye

## Generated Story -7089415360611904251
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "indian"}
    - slot{"cuisine": "indian"}
    - utter_ask_price
* restaurant_search{"price": "High"}
	- slot{"price": "High"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email
* affirm
    - utter_ask_for_email_address
* restaurant_search{"email": "email@gmail.com"}
	- slot{"email": "email@gmail.com"}
    - utter_email_sent_goodbye
    - export

## Generated Story -1116213696233533874
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "pune"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "pune"}
    - utter_ask_price
* restaurant_search{"price": "Low"}
	- slot{"price": "Low"}
    - action_restaurant
    - slot{"location": "pune"}
    - utter_ask_email
* affirm
    - utter_ask_for_email_address
* restaurant_search{"email": "email@gmail.com"}
	- slot{"email": "email@gmail.com"}
    - utter_email_sent_goodbye
    - export


## Generated Story -by hand
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "pune"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "pune"}
    - utter_ask_price
* restaurant_search{"price": "Low"}
	- slot{"price": "Low"}
    - action_restaurant
    - slot{"location": "pune"}
    - utter_ask_email
* deny
	-utter_goodbye
	

## Generated Story -3141530855876654586
* greet
    - utter_greet
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "Medium"}
	- slot{"price": "Medium"}
    - action_restaurant
    - slot{"location": "pune"}
    - utter_ask_email
* deny
    - utter_goodbye
    - export
	
## Generated Story 490474450504330774
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_restaurant
    - slot{"location": "mexican"}
    - utter_ask_email
* affirm
    - utter_ask_for_email_address
* restaurant_search{"email": "aakash@gmail.com"}
    - utter_email_sent_goodbye
    - export
