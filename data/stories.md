## Generated Story by hand 1
* greet
    - utter_greet
	
## Generated Story by hand 1
* restaurant_search
    - utter_ask_location

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
	- action_email_sent
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
	- action_email_sent
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
	- action_email_sent
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
	- action_email_sent
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
	- action_email_sent
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
	- action_email_sent
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
	- action_email_sent
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
	- action_email_sent
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
	- action_email_sent
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
	- action_email_sent
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
	- action_email_sent
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
	- action_email_sent
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
* deny
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
	- action_email_sent
    - utter_email_sent_goodbye
    - export

## Generated Story hand
* restaurant_search{"cuisine": "italian", "location": "noida", "price": "medium"}
    - slot{"cuisine": "italian"}
    - slot{"location": "noida"}
    - slot{"price": "medium"}
    - action_location
	- slot{"Validate_loc": "NotWorking"}
	- slot{"location": null}
    - utter_not_operate
* restaurant_search{"location": "delhi"}
	- slot{"location": "delhi"}
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_email
* affirm{"email": "aakash@ana.co.in"}
    - slot{"email": "aakash@ana.co.in"}
	- action_email_sent
    - utter_email_sent_goodbye
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
* deny
    - utter_goodbye
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

## Generated Story -1105737737719149275
* greet{"location": "hola"}
    - slot{"location": "hola"}
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "pune"}
    - slot{"cuisine": "american"}
    - slot{"location": "pune"}
    - action_location
    - slot{"Validate_loc": "Tier12"}
    - slot{"location": "pune"}
    - utter_ask_price
* restaurant_search{"price": "300"}
    - slot{"price": "300"}
    - action_restaurant
    - slot{"location": "pune"}
    - utter_ask_email
* affirm{"email": "nvvermanikhil@gmail.com"}
    - slot{"email": "nvvermanikhil@gmail.com"}
    - utter_ask_for_email_address
* goodbye
* goodbye
    - utter_goodbye
    - export

## Generated Story -2776683821362502146
* greet
    - utter_greet
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - action_location
    - slot{"Validate_loc": "Tier12"}
    - slot{"location": "hyderabad"}
    - utter_ask_price
* restaurant_search{"price": "700"}
    - slot{"price": "700"}
    - action_restaurant
    - slot{"location": "hyderabad"}
    - utter_ask_email
* affirm{"email": "aakashkumar@gmail.com"}
    - slot{"email": "aakashkumar@gmail.com"}
    - utter_ask_for_email_address
* goodbye
    - utter_goodbye
    - utter_goodbye
    - export
    
## Generated Story -8090831796301103683
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "chennai"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "chennai"}
    - action_location
    - slot{"Validate_loc": "Tier12"}
    - slot{"location": "chennai"}
    - utter_ask_price
* restaurant_search{"low": "300", "price": "700"}
    - slot{"price": "700"}
    - action_restaurant
    - slot{"location": "chennai"}
    - utter_ask_email
* affirm{"location": "nik@gmail.com"}
    - slot{"location": "nik@gmail.com"}
    - utter_ask_for_email_address
* goodbye
    - utter_goodbye
    - export
