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
* restaurant_search{"price": "300"}
	-slot{"price": "300"}
	-action_restaurant
	-utter_ask_email
* affirm
	-utter_ask_for_email_address
* restaurant_search{"email": "email@gmail.com"}
	-slot{"email": "email@gmail.com"}
	-utter_email_sent_goodbye
	
	
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
* restaurant_search{"price": "300"}
	-slot{"price": "300"}
	-action_restaurant
	-utter_ask_email
* deny
	-utter_goodbye



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
* restaurant_search
    - action_restaurant
    - utter_ask_email
* affirm
    - utter_ask_for_email_address
* restaurant_search
    - utter_email_sent_goodbye
    - export


## Generated Story -7089415360611904251
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "indian"}
    - slot{"cuisine": "indian"}
    - utter_ask_price
* restaurant_search
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email
* affirm
    - utter_ask_for_email_address
* restaurant_search
    - utter_email_sent_goodbye
    - export

## Generated Story -1116213696233533874
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "pune"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "pune"}
    - utter_ask_price
* restaurant_search
    - action_restaurant
    - slot{"location": "pune"}
    - utter_ask_email
* restaurant_search
    - utter_ask_for_email_address
* restaurant_search
    - utter_email_sent_goodbye
    - export
