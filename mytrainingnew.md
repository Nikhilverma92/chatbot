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

