from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import re
from threading import Thread

import urllib3
from rasa_sdk import Action
from rasa_sdk.events import SlotSet, Restarted, AllSlotsReset, SessionStarted

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
from pretty_html_table import build_table

urllib3.disable_warnings()

top_10_restaurant_details = []

ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)


def RestaurantSearch(city, cuisine):
    temp = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: cuisine.lower() in x.lower())) & (
        ZomatoData['City'].apply(lambda x: city.lower() in x.lower()))]
    return temp[['Restaurant Name', 'Address', 'Average Cost for two', 'Aggregate rating']]


class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        print("------------------------------------------------------------\n")
        print('location: ', loc)
        cuisine = tracker.get_slot('cuisine')
        print('cuisine: ', cuisine)
        budget = tracker.get_slot('budget')
        print('budget: ', budget)
        if str(budget) == 'low':
            budget_min_price = 0
            budget_max_price = 300
        elif str(budget) == 'mid':
            budget_min_price = 300
            budget_max_price = 700
        else:
            budget_min_price = 700
            budget_max_price = 10000

        if cuisine is not None and loc is not None:
            results = RestaurantSearch(city=loc, cuisine=cuisine)

        results = restaurant_result(results, budget_min_price, budget_max_price)
        print("Search result: ", results[:2])
        restaurant_exist = False
        response = ""
        print(budget_min_price, budget_max_price)

        if results.shape[0] == 0:
            response = "Sorry no results found"
            restaurant_exist = False
            dispatcher.utter_message("---------------------------------------------------------------\n" + response)
            return [SlotSet('restaurant_exist', restaurant_exist)]
        else:
            restaurant_df = restaurant_result(results, budget_min_price, budget_max_price)
            global top_10_restaurant_details
            top_10_restaurant_details = restaurant_df[:10]
            if len(top_10_restaurant_details) > 0:
                restaurant_exist = True
            for restaurant in results.sort_values(by='Aggregate rating', ascending=False).iloc[:5].iterrows():
                restaurant = restaurant[1]
                response = response + F"{restaurant['Restaurant Name']} in {restaurant['Address']} has been rated \
{restaurant['Aggregate rating']} and the average price for two people here is {restaurant['Average Cost for two']}\n"
                response = response + '\n'
            message = F"Showing you top rated restaurants with {cuisine.title()} cuisine in {loc.title()} : \n"
            dispatcher.utter_message(message)
            dispatcher.utter_message("-----------------------------------------------------------------------\n")
            dispatcher.utter_message(response)
            return [SlotSet('location', loc), SlotSet('restaurant_exist', restaurant_exist)]


def restaurant_result(responses, min_value, max_value):
    dataset = responses[
        (responses['Average Cost for two'] > min_value) & (responses['Average Cost for two'] < max_value)]
    dataset = dataset.sort_values(by='Aggregate rating', ascending=False).iloc[:10]
    return dataset


class ActionEmailProvided(Action):
    def name(self):
        return 'action_email_provided'

    def run(self, dispatcher, tracker, domain):
        mail_provided = tracker.get_slot('email_provided')
        print("mail_provided: ", mail_provided)
        if mail_provided == 'Yes':
            return [SlotSet('email_provided', True)]
        elif mail_provided == 'No':
            return [SlotSet('email_provided', False)]


class ActionSendMail(Action):
    def name(self):
        return 'action_send_mail'

    def run(self, dispatcher, tracker, domain):
        mail_id = tracker.get_slot('email')
        loc_mail = tracker.get_slot('location')
        cuisine_mail = tracker.get_slot('cuisine')
        # print('Mail id for action send mail:', mail_id)
        response = build_table(top_10_restaurant_details, 'blue_light')
        thr = Thread(target=sendmail, args=[mail_id, loc_mail, cuisine_mail, response])
        thr.start()
        email_sent = F'\nWe have sent the list of restaurants in {loc_mail.title()} with {cuisine_mail.title()} food on {mail_id}'
        dispatcher.utter_message(email_sent)
        return [SlotSet('email', mail_id)]


class ActionVerifyBudget(Action):

    def name(self):
        return 'action_verify_budget'

    def run(self, dispatcher, tracker, domain):
        error_msg = "Sorry!! price range not supported, Please re-enter."
        try:
            budget = tracker.get_slot('budget')
            if str(budget) == 'low':
                budget_min_price = 0
                budget_max_price = 300
            elif str(budget) == 'mid':
                budget_min_price = 300
                budget_max_price = 700
            else:
                budget_min_price = 700
                budget_max_price = 10000
        except ValueError:
            dispatcher.utter_message(error_msg)
            return [SlotSet('budgetmin', None), SlotSet('budgetmax', None), SlotSet('budget_ok', False)]
        min_dict = [0, 300, 700]
        max_dict = [300, 700]
        if budget_min_price in min_dict and (budget_max_price in max_dict or budget_max_price > 700):
            return [SlotSet('budgetmin', budget_min_price), SlotSet('budgetmax', budget_max_price),
                    SlotSet('budget_ok', True)]
        else:
            dispatcher.utter_message(error_msg)
            return [SlotSet('budgetmin', 0), SlotSet('budgetmax', 10000), SlotSet('budget_ok', False)]


sender_address = 'foodieebotrasa@gmail.com'
sender_pass = '@lHOMOR1'


class ActionValidateLocation(Action):
    TIER_1 = []
    TIER_2 = []

    def __init__(self):
        self.TIER_1 = ['ahmedabad', 'bangalore', 'chennai', 'delhi', 'hyderabad', 'kolkata', 'mumbai', 'pune']
        self.TIER_2 = ['agra', 'ajmer', 'aligarh', 'amravati', 'amritsar', 'asansol', 'aurangabad', 'bareilly', 'bhubaneshwar',
                       'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar', 'bikaner', 'bilaspur', 'bokaro steel city',
                       'chandigarh', 'coimbatore', 'cochin', 'cuttack', 'dehradun', 'dhanbad', 'bhilai', 'durgapur', 'erode', 'faridabad',
                       'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gwalior', 'gurgaon', 'guwahati', 'hamirpur',
                       'hubli–dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi',
                       'jodhpur', 'kakinada', 'kannur', 'kanpur', 'kochi', 'kolhapur', 'kollam', 'kozhikode', 'kurnool',
                       'ludhiana', 'lucknow', 'madurai', 'malappuram', 'mathura', 'goa', 'mangalore', 'meerut', 'moradabad', 'mysore',
                       'nagpur', 'nanded','nashik', 'nellore', 'noida', 'patna', 'pondicherry', 'purulia', 'prayagraj', 'raipur', 'rajkot',
                       'rajahmundry', 'ranchi', 'rourkela', 'salem', 'sangli', 'shimla', 'siliguri', 'solapur',
                       'srinagar', 'surat','thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tiruppur', 'ujjain', 'bijapur', 'vadodara',
                       'varanasi', 'vasai-virar city', 'vijayawada', 'visakhapatnam', 'vellore', 'warangal']
                     # , 'Bhubaneswar', 'New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi',
            #              'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun',
            #              'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore',
            #              'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa',
            #              'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']

    def name(self):
        return "action_validate_location"

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        if loc == "Other_cities":
            dispatcher.utter_template("utter_other_cities", tracker)
            loc = tracker.get_slot('location')
            print('loc inside validate_location:', loc)
            return [SlotSet('location', loc), SlotSet("location_ok", False)]

        if not (self.verify_location(loc)):
            dispatcher.utter_message("Sorry, we do not operate in " + loc.title() + " yet. Please try some other city.")
            print("Sorry, we do not operate in " + loc.title())
            return [SlotSet('location', None), SlotSet("location_ok", False)]
        # elif not (self.verify_operation(loc)):
        #     dispatcher.utter_message("Sorry, the operations in " + loc.title() + " are not currently functional")
        #     print("Sorry, operations are suspended in  " + loc.title())
        #     return [SlotSet('location', loc), SlotSet("location_ok", True)]
        else:
            return [SlotSet('location', loc), SlotSet("location_ok", True)]

    def verify_location(self, loc):
        return loc.lower() in self.TIER_1 or loc.lower() in self.TIER_2

    # def verify_operation(self, loc):
    #     return loc.lower() in self.WeOperate


def sendmail(email, location, cuisine, response):
    # The mail addresses and password
    # print('mail response: ', response)
    receiver_address = email
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Foodie has found some restaurants for you'  # The subject line
    # The body and the attachments for the mail
    mail_body = F'Dear Customer,\nWe have found below restaurants in {location} with {cuisine} food  for you:\n'
    message.attach(MIMEText(mail_body, 'plain'))
    message.attach(MIMEText(response, 'html'))
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    # print('text:', text)
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')
    print("------------------------------------------------------------\n")


class ActionValidateEmail(Action):
    def name(self):
        return 'action_validate_email'

    def run(self, dispatcher, tracker, domain):
        pattern = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        email_check = tracker.get_slot('email')
        print(email_check)
        if email_check is not None:
            if re.search(pattern, email_check):
                print('Valid email')
                return [SlotSet('email_ok', True)]
            else:
                print('Invalid email')
                dispatcher.utter_message("Sorry this is not a valid email. Please check for typing errors")
                return [SlotSet('email', None), SlotSet("email_ok", False)]
        else:
            print('No email')
            dispatcher.utter_message("Sorry I couldn't understand the email address you provided?\
             Could you please provide again")
            return [SlotSet('email', None)]


class ActionRestarted(Action):
    def name(self):
        return 'action_restart'

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]


class ActionSlotReset(Action):
    def name(self):
        return 'action_slot_reset'

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]


class ActionStarted(Action):
    def name(self):
        return 'action_start'

    def run(self, dispatcher, tracker, domain):
        return [SessionStarted()]
