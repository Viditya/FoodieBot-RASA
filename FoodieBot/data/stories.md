## complete path and email provided
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}  
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget_for_two
* budget{"budget": "low"}
    - action_verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_exist": true}
    - utter_ask_ifmail
* allowornot{"email_provided": true}
    - action_email_provided
    - slot{"email_provided": true}
    - utter_ask_email
* send_email{"email": "viditya.tyagi@gmail.com"}
    - slot{"email": "viditya.tyagi@gmail.com"}
    - action_validate_email
    - slot{"email_ok": true}
    - action_send_mail
* goodbye
    - utter_goodbye
    - action_slot_reset

## complete path and email provided
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "cochin"}
    - action_validate_location
    - slot{"location": "cochin"}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "Kochi"}
    - action_validate_location
    - slot{"location": "Kochi"}
    - slot{"location_ok": true}  
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget_for_two
* budget{"budget": "high"}
    - action_verify_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_exist": true}
    - utter_ask_ifmail
* allowornot{"email_provided": true}
    - action_email_provided
    - slot{"email_provided": true}
    - utter_ask_email
* send_email{"email": "vidi.viditya@gmail.com"}
    - slot{"email": "vidi.viditya@gmail.com"}
    - action_validate_email
    - slot{"email_ok": true}
    - action_send_mail
* goodbye
    - utter_goodbye
    - action_slot_reset

## restaurant not found in given budget
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - action_validate_location
    - slot{"location": "pune"}
    - slot{"location_ok": true}  
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget_for_two
* budget{"budget": "low"}
    - action_verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": false}
    - utter_ask_budget_for_two
* budget{"budget": "mid"}
    - action_verify_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": true}
    - utter_ask_ifmail
* allowornot{"email_provided": true}
    - action_email_provided
    - slot{"email_provided": true}
    - utter_ask_email
* send_email{"email": "viditya.tyagi@gmail.com"}
    - slot{"email": "viditya.tyagi@gmail.com"}
    - action_validate_email
    - slot{"email_ok": true}
    - action_send_mail
* goodbye
    - utter_goodbye 
    - action_slot_reset

## restaurant not found in given budget on second attempt
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - action_validate_location
    - slot{"location": "pune"}
    - slot{"location_ok": true}  
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget_for_two
* budget{"budget": "low"}
    - action_verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": false}
    - utter_ask_budget_for_two
* budget{"budget": "mid"}
    - action_verify_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": false}
       - utter_ask_budget_for_two
* budget{"budget": "high"}
    - action_verify_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "pune"}
    - slot{"restaurant_exist": true}
    - utter_ask_ifmail
* allowornot{"email_provided": true}
    - action_email_provided
    - slot{"email_provided": true}
    - utter_ask_email
* send_email{"email": "viditya.tyagi@gmail.com"}
    - slot{"email": "viditya.tyagi@gmail.com"}
    - action_validate_email
    - slot{"email_ok": true}
    - action_send_mail
* goodbye
    - utter_goodbye
   - action_slot_reset


## restaurant not found with given cuisine
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - action_validate_location
    - slot{"location": "pune"}
    - slot{"location_ok": true}  
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget_for_two
* budget{"budget": "low"}
    - action_verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": false}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - slot{"restaurant_exist": true}
    - utter_ask_ifmail
* allowornot{"email_provided": true}
    - action_email_provided
    - slot{"email_provided": true}
    - utter_ask_email
* send_email{"email": "viditya.tyagi@gmail.com"}
    - slot{"email": "viditya.tyagi@gmail.com"}
    - action_validate_email
    - slot{"email_ok": true}
    - action_send_mail
* goodbye
    - utter_goodbye
   - action_slot_reset

  
## complete path and email not provided
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}  
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget_for_two
* budget{"budget": "low"}
    - action_verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_exist": true}
    - utter_ask_ifmail
* allowornot{"email_provided": false}
    - action_email_provided
    - slot{"email_provided": false}
    - utter_goodbye
    - action_slot_reset
  
## location specified and valid email
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}  
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget_for_two
* budget{"budget": "mid"}
    - action_verify_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_exist": true}
    - utter_ask_ifmail
* affirm
    - utter_ask_email
* send_email{"email": "viditya.tyagi@gmail.com"}
    - slot{"email": "viditya.tyagi@gmail.com"}
    - action_validate_email
    - slot{"email_ok": true}
    - action_send_mail
* goodbye
    - utter_goodbye
    - action_slot_reset  

## location specified not in tier xy and valid email
* greet
    - utter_greet
* restaurant_search{"location": "Haridwar"}
    - slot{"location": "Haridwar"}
    - action_validate_location
    - slot{"location": null}
    - slot{"location_ok": false}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget_for_two
* budget{"budget": "mid"}
    - action_verify_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_exist": true}
    - utter_ask_ifmail
* affirm
    - utter_ask_email
* send_email{"email": "viditya.tyagi@gmail.com"}
    - slot{"email": "viditya.tyagi@gmail.com"}
    - action_validate_email
    - slot{"email_ok": true}
    - action_send_mail
* goodbye
    - utter_goodbye
    - action_slot_reset

## cuisine specified and valid email
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}   
    - utter_ask_budget_for_two
* budget{"budget": "mid"}
    - action_verify_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_exist": true}
    - utter_ask_ifmail
* affirm
    - utter_ask_email
* send_email{"email": "viditya.tyagi@gmail.com"}
    - slot{"email": "viditya.tyagi@gmail.com"}
    - action_validate_email
    - slot{"email_ok": true}
    - action_send_mail
* goodbye
    - utter_goodbye
    - action_slot_reset
  
## location specified and invalid email
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"} 
    - slot{"location_ok": true}  
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget_for_two
* budget{"budget": "mid"}
    - action_verify_budget
    - slot{"budgetmin": 300}
    - slot{"budgetmax": 700}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - utter_ask_ifmail
* affirm
    - utter_ask_email
* send_email{"email": "invalidemail@wrongdomain"}
    - slot{"email": "invalidemail@wrongdomain"}
    - action_validate_email
    - slot{"email_ok": false}
    - slot{"email": null}
    - utter_ask_email
* send_email{"email": "viditya.tyagi@gmail.com"}
    - slot{"email": "viditya.tyagi@gmail.com"}
    - action_validate_email
    - slot{"email_ok": true}
    - action_send_mail
    - utter_goodbye
    - action_slot_reset

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - action_validate_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget_for_two
* budget{"budget": "high"}
    - action_verify_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_exist": true}
    - utter_ask_ifmail
* affirm
    - utter_ask_email
* send_email{"email": "viditya.tyagi@gmail.com"}
    - slot{"email": "viditya.tyagi@gmail.com"}
    - action_validate_email
    - slot{"email_ok": true}
    - action_send_mail
* goodbye
    - utter_goodbye
    - action_slot_reset 

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
- action_validate_location
    - slot{"location": "italy"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget_for_two
* budget{"budget": "high"}
    - action_verify_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "italy"}
    - slot{"restaurant_exist": true}
    - utter_ask_ifmail
* affirm
    - utter_ask_email
* send_email{"email": "viditya.tyagi@gmail.com"}
    - slot{"email": "viditya.tyagi@gmail.com"}
    - action_validate_email
    - slot{"email_ok": true}
    - action_send_mail
* goodbye
    - utter_goodbye
    - action_slot_reset
## complete path 4

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
- action_validate_location
    - slot{"location": "delhi"}
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget_for_two
* budget{"budget": "high"}
    - action_verify_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"restaurant_exist": true}
    - utter_ask_ifmail
* affirm
    - utter_ask_email
* send_email{"email": "viditya.tyagi@gmail.com"}
    - slot{"email": "viditya.tyagi@gmail.com"}
    - action_validate_email
    - slot{"email_ok": true}
    - action_send_mail
* goodbye
    - utter_goodbye
    - action_slot_reset

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Delhi", "budget":"low"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"} 
    - slot{"budget": "low"}
    - action_verify_budget
    - slot{"budgetmin": 700}
    - slot{"budgetmax": 10000}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "low"}
    - action_validate_location
    - slot{"budget_ok": true}  
    - slot{"location_ok": true}
    - slot{"restaurant_exist": true}
    - utter_ask_ifmail
* affirm
    - utter_ask_email
* send_email{"email": "viditya.tyagi@gmail.com"}
    - slot{"email": "viditya.tyagi@gmail.com"}
    - action_validate_email
    - slot{"email": "viditya.tyagi@gmail.com"}
    - slot{"email_ok": true}
    - action_send_mail
* goodbye
    - utter_goodbye
    - action_slot_reset

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - slot{"location_ok": true}
    - slot{"location": "Delhi"}
    - utter_ask_budget_for_two
* budget{"budget": "low"}
    - slot{"budget": "low"}
    - action_verify_budget
    - slot{"budgetmin": 0}
    - slot{"budgetmax": 300}
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"restaurant_exist": true}
    - utter_ask_ifmail
* affirm
    - utter_ask_email
* send_email{"email": "viditya.tyagi@gmail.com"}
    - slot{"email": "viditya.tyagi@gmail.com"}
    - action_validate_email
    - slot{"email": "viditya.tyagi@gmail.com"}
    - slot{"email_ok": true}
    - action_send_mail
* goodbye
    - utter_goodbye
    - action_slot_reset 