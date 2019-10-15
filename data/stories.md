## Generated Story by hand 1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_location
	- slot{"Validate_loc": "Tier12"}
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
	- action_location
	- slot{"Validate_loc": "NotWorking"}
	- slot{"location": null}
    - utter_not_operate
* restaurant_search{"location": "delhi"}
	- slot{"location": "delhi"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
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



## Generated Story -8972014242190157214
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_location
	- slot{"Validate_loc": "OutOfRange"}
	- slot{"location": null}
	- utter_not_operate
* restaurant_search{"location": "mumbai"}
	- slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "High"}
	- slot{"price": "High"}
    - action_restaurant
	- slot{"location": "mumbai"}
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
* restaurant_search{"cuisine": "indian"}
	- slot{"cuisine": "indian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_location
	- slot{"Validate_loc": "Tier12"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"price": "Low"}
	- slot{"price": "Low"}
	- action_restaurant
	- slot{"location": "delhi"}
	- utter_ask_email
* affirm
	- utter_ask_for_email_address
* restaurant_search{"email": "email@gmail.com"}
	- slot{"email": "email@gmail.com"}
	- utter_email_sent_goodbye
	
	
## Generated Story -by hand
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian"}
	- slot{"cuisine": "Italian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_location
	- slot{"Validate_loc": "OutOfRange"}
    - slot{"location": null}
	- utter_not_operate
* restaurant_search{"location": "mumbai"}
	- slot{"location": "mumbai"}
    - utter_ask_price
* restaurant_search{"price": "Low"}
	- slot{"price": "Low"}
	- action_restaurant
	- slot{"location": "delhi"}
	- utter_ask_email
* affirm
	- utter_ask_for_email_address
* restaurant_search{"email": "email@gmail.com"}
	- slot{"email": "email@gmail.com"}
	- utter_email_sent_goodbye
