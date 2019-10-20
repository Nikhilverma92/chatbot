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

