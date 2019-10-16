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

## Generated Story -3141530855876654586
* greet
    - utter_greet
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search
    - action_restaurant
    - slot{"location": "pune"}
    - utter_ask_email
* deny
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

## Generated Story 6180926786765231440
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "noida", "price": "medium"}
    - slot{"cuisine": "italian"}
    - slot{"location": "noida"}
    - action_location
	- slot{"Validate_loc": "Tier12"}
    - slot{"location": "delhi"}
    - slot{"price": "medium"}
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_email
* restaurant_search{"email": "akkic2@yahoo.com"}
    - slot{"email": "akkic2@yahoo.com"}
    - utter_email_sent_goodbye
    - export

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

## Generated Story -6022665901933320607
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location
    - slot{"Validate_loc": "Tier12"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
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
* restaurant_search{"email": "naacn@jahsh.com"}
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
* restaurant_search{"email": "aakau@hotmail.com"}
    - slot{"email": "aakau@hotmail.com"}
    - utter_email_sent_goodbye
    - export

