## complete path and email provided
* greet: Hi
    - utter_greet
* restaurant_search: Looking to eat 
    - utter_ask_location
* restaurant_search: delhi
    - action_validate_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}  
    - utter_ask_cuisine
* restaurant_search: chinese
    - slot{"cuisine": "chinese"}
    - utter_ask_budget_for_two
* budget: low
    - action_verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_exist": true}
    - utter_ask_ifmail
* allowornot: Yes
    - action_email_provided
    - slot{"email_provided": true}
    - utter_ask_email
* send_email: viditya.tyagi@gmail.com
    - slot{"email": "viditya.tyagi@gmail.com"}
    - action_validate_email
    - slot{"email_ok": true}
    - action_send_mail
* goodbye:bye
    - utter_goodbye
    - action_slot_reset

## complete path and email provided
* greet: hey
    - utter_greet
* restaurant_search: show me some restaurants
    - utter_ask_location
* restaurant_search: cochin
    - action_validate_location
    - slot{"location": "cochin"}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search: Kochi
    - action_validate_location
    - slot{"location": "Kochi"}
    - slot{"location_ok": true}  
    - utter_ask_cuisine
* restaurant_search:mexican
    - slot{"cuisine": "mexican"}
    - utter_ask_budget_for_two
* budget: high
    - action_verify_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_exist": true}
    - utter_ask_ifmail
* allowornot:Yes
    - action_email_provided
    - slot{"email_provided": true}
    - utter_ask_email
* send_email: vidi.viditya@gmail.com
    - slot{"email": "vidi.viditya@gmail.com"}
    - action_validate_email
    - slot{"email_ok": true}
    - action_send_mail
* goodbye: bye
    - utter_goodbye
    - action_slot_reset
  