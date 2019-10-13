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
* restaurant_search{"email": "yes"}
	-slot{"email": "yes"}
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
* restaurant_search{"email": "no"}
	-slot{"email": "no"}
	-utter_goodbye
