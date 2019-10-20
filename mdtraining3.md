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

