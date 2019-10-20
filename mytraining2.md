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

