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

## Generated Story 3626286338579491285
* greet
    - utter_greet
* restaurant_search{"location": "noida", "cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "noida"}
    - action_location
    - slot{"Validate_loc": "Tier12"}
    - slot{"location": "noida"}
    - utter_ask_price
* restaurant_search
    - action_restaurant
    - utter_ask_email
* affirm{"email": "akku@hot.com"}
    - slot{"email": "akku@hot.com"}
    - utter_email_sent_goodbye
    - export

## Generated Story 4242221443357119545
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_location
    - slot{"Validate_loc": "Tier12"}
    - slot{"location": "noida"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_restaurant
    - utter_ask_email
* deny
    - utter_goodbye
    - export

## Generated Story -1515086700419213281
* restaurant_search
    - utter_ask_location
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_location
    - utter_not_operate
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese", "price": "low"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "low"}
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_email
* affirm{"email": "abhi@akkucd.in"}
    - slot{"email": "abhi@akkucd.in"}
    - utter_email_sent_goodbye
    - export

## Generated Story -5565455898140904
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location
    - slot{"Validate_loc": "Tier12"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"price": "high", "cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - slot{"price": "high"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email
* restaurant_search
    - utter_goodbye
    - export

## Generated Story 4244965692782336665
* restaurant_search{"cuisine": "italian", "location": "noida", "price": "medium"}
    - slot{"cuisine": "italian"}
    - slot{"location": "noida"}
    - slot{"price": "medium"}
    - action_location
    - slot{"Validate_loc": "Tier12"}
    - slot{"location": "noida"}
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_email
* affirm{"email": "aakash@ana.co.in"}
    - slot{"email": "aakash@ana.co.in"}
    - utter_email_sent_goodbye
    - export

## Generated Story 6388358495573164532
* restaurant_search{"price": "high", "cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "high"}
    - utter_ask_location
* restaurant_search{"location": "bhutan"}
    - slot{"location": "bhutan"}
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

## Generated Story -8486241683112340721
* greet
    - utter_greet
* restaurant_search{"location": "mumbai", "cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "mumbai"}
    - action_location
    - slot{"Validate_loc": "Tier12"}
    - slot{"location": "mumbai"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_email
* affirm
    - utter_ask_for_email_address
* restaurant_search{"email": "akku@gmail.com"}
    - slot{"email": "akku@gmail.com"}
    - action_email_sent
    - slot{"email": "Done"}
    - utter_email_sent_goodbye
    - export

## Generated Story 2895263103598800775
* restaurant_search{"price": "high", "cuisine": "mexican", "location": "bangalore"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "bangalore"}
    - slot{"price": "high"}
    - action_location
    - slot{"Validate_loc": "Tier12"}
    - slot{"location": "bangalore"}
    - action_restaurant
    - slot{"location": "bangalore"}
    - utter_ask_email
* restaurant_search{"email": "aakashkumar5066@gmail.com"}
    - slot{"email": "aakashkumar5066@gmail.com"}
    - action_email_sent
    - slot{"email": "Done"}
    - utter_email_sent_goodbye
* goodbye
    - utter_goodbye
    - export

## Generated Story 2996396983500242163
* restaurant_search{"cuisine": "chinese", "location": "goa"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "goa"}
    - action_location
    - slot{"Validate_loc": "Tier12"}
    - slot{"location": "goa"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_restaurant
    - slot{"location": "goa"}
    - utter_ask_email
* affirm{"email": "aakashkumar5066@gmail.com"}
    - slot{"email": "aakashkumar5066@gmail.com"}
    - action_email_sent
    - slot{"email": "Done"}
    - utter_email_sent_goodbye
* affirm
    - export

## Generated Story 7554649148997635311
* restaurant_search{"price": "medium", "cuisine": "chinese", "location": "bhutan"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "bhutan"}
    - slot{"price": "medium"}
    - action_location
    - slot{"Validate_loc": "NotWorking"}
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "ajmer"}
    - slot{"location": "ajmer"}
    - action_restaurant
    - slot{"location": "ajmer"}
    - utter_ask_email
* affirm{"email": "aakashkumar5066@gmail.com"}
    - slot{"email": "aakashkumar5066@gmail.com"}
    - action_email_sent
    - slot{"email": "Done"}
    - utter_email_sent_goodbye
    - export

## Generated Story -109749491927304653
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_location
    - slot{"Validate_loc": "Tier12"}
    - slot{"location": "delhi"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email
* deny
    - utter_goodbye
    - export

## Generated Story 7598967177083905818
* restaurant_search{"location": "bhutan", "cuisine": "mexican", "price": "high"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "bhutan"}
    - slot{"price": "high"}
    - action_location
    - slot{"Validate_loc": "NotWorking"}
    - slot{"location": null}
    - utter_ask_location
* restaurant_search{"location": "noida"}
    - slot{"location": "noida"}
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_email
* deny
    - utter_goodbye
    - export

## Generated Story -2761258070489457386
* restaurant_search{"location": "lgnsh"}
    - slot{"location": "lgnsh"}
    - action_location
    - slot{"Validate_loc": "OutOfRange"}
    - slot{"location": null}
    - utter_not_operate
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian", "price": "high"}
    - slot{"cuisine": "south indian"}
    - slot{"price": "high"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email
* affirm{"email": "aakashkumar5066@gmail.com"}
    - slot{"email": "aakashkumar5066@gmail.com"}
    - action_email_send
    - utter_email_sent_goodbye
    - export

## Generated Story 7536719899963834054
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* affirm{"location": "ajsnd"}
    - slot{"location": "ajsnd"}
    - action_location
    - slot{"Validate_loc": "OutOfRange"}
    - slot{"location": null}
    - utter_not_operate
* restaurant_search{"location": "noida", "price": "high"}
    - slot{"location": "noida"}
    - slot{"price": "high"}
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_email
* affirm
    - utter_ask_for_email_address
* affirm{"email": "aakashkumar5066@gmail.com"}
    - slot{"email": "aakashkumar5066@gmail.com"}
    - action_email_send
    - slot{"email": "Done"}
    - utter_email_sent_goodbye
    - export

