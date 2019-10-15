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
* affirm{"email": "email@gmail.com"}
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
* affirm{"email": "email@gmail.com"}
	- slot{"email": "email@gmail.com"}
    - utter_email_sent_goodbye
    - export

	
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
* deny
	-utter_goodbye
	-export

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
* affirm{"email": "email@gmail.com"}
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
* affirm{"email": "email@gmail.com"}
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
* affirm{"email": "email@gmail.com"}
	- slot{"email": "email@gmail.com"}
	- utter_email_sent_goodbye


## Generated Story -661710345259266116
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "gurgaon"}
    - slot{"location": "gurgaon"}
    - action_location
    - slot{"Validate_loc": "NotWorking"}
    - slot{"location": null}
    - utter_not_operate
* restaurant_search{"location": "delhi"}
    - slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"location": "medium"}
    - slot{"location": "medium"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email
* deny
    - utter_goodbye
    - export


## Generated Story 6180926786765231440
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "price": "medium", "location": "noida"}
    - slot{"cuisine": "italian"}
    - slot{"price": "medium"}
    - slot{"location": "noida"}
    - action_location
	- slot{"Validate_loc": "Tier12"}
    - slot{"location": "noida"}
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_email
* affirm{"email": "akkic2@yahoo.com"}
    - slot{"email": "akkic2@yahoo.com"}
    - utter_email_sent_goodbye
    - export


## Generated Story -hand
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "price": "medium", "location": "noida"}
    - slot{"cuisine": "italian"}
	- slot{"price": "medium"}
    - slot{"location": "noida"}
    - action_location
	- slot{"Validate_loc": "OutOfRange"}
	- slot{"location": null}
    - utter_not_operate
* restaurant_search{"location": "delhi"}
	- slot{"location": "delhi"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email
* affirm{"email": "akkic2@yahoo.com"}
    - slot{"email": "akkic2@yahoo.com"}
    - utter_email_sent_goodbye
    - export

## Generated Story -hand
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "price": "medium", "location": "noida"}
    - slot{"cuisine": "italian"}
	- slot{"price": "medium"}
    - slot{"location": "noida"}
    - action_location
	- slot{"Validate_loc": "NotWorking"}
	- slot{"location": null}
    - utter_not_operate
* restaurant_search{"location": "delhi"}
	- slot{"location": "delhi"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email
* deny
    - utter_goodbye
    - export


## Generated Story -6022665901933320607
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location
    - slot{"Validate_loc": "Tier12"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email
* affirm
    - utter_ask_for_email_address
* affirm{"email": "naacn@jahsh.com"}
    - slot{"email": "naacn@jahsh.com"}
    - utter_email_sent_goodbye
    - export
	
## Generated Story -hand
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location
    - slot{"Validate_loc": "Tier12"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email
* deny
    - utter_goodbye
    - export
	
## Generated Story -hand
* greet
    - utter_greet
* restaurant_search{"location": "gurgaon"}
    - slot{"location": "gurgaon"}
    - action_location
	- slot{"Validate_loc": "NotWorking"}
	- slot{"location": null}
    - utter_not_operate
* restaurant_search{"location": "delhi"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email
* deny
    - utter_goodbye
    - export
	
## Generated Story -hand
* greet
    - utter_greet
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
	- utter_ask_location
* restaurant_search{"location": "gurgaon"}
    - slot{"location": "gurgaon"}
    - action_location
	- slot{"Validate_loc": "OutOfRange"}
	- slot{"location": null}
    - utter_not_operate
* restaurant_search{"location": "delhi"}
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email
* deny
    - utter_goodbye
    - export
	
## Generated Story -hand
* greet
    - utter_greet
* restaurant_search{"price": "high","cuisine": "italian"}
    - slot{"price": "high"}
	- slot{"cuisine": "italian"}
	- utter_ask_location
* restaurant_search{"location": "gurgaon"}
    - slot{"location": "gurgaon"}
    - action_location
	- slot{"Validate_loc": "OutOfRange"}
	- slot{"location": null}
    - utter_not_operate
* restaurant_search{"location": "delhi"}
	- slot{"location": "delhi"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email
* affirm{"email": "naacn@jahsh.com"}
    - slot{"email": "naacn@jahsh.com"}
    - utter_email_sent_goodbye
    - export
	
## Generated Story 8596675483252403529
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "pune"}
    - slot{"cuisine": "italian"}
    - slot{"location": "pune"}
    - action_location
    - slot{"Validate_loc": "Tier12"}
    - slot{"location": "pune"}
    - utter_ask_price
* restaurant_search{"location": "medium"}
    - slot{"location": "medium"}
    - action_restaurant
    - utter_ask_email
* affirm{"email": "aakau@hotmail.com"}
    - slot{"email": "aakau@hotmail.com"}
    - utter_email_sent_goodbye
    - export