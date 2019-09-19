from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import re
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
import random
import yagmail
import pickle

tokenizer = Tokenizer()

#Load Model Weights
model = load_model('QA_weights_v5_1.hd5')
with open('tokenizer.pickle', 'rb') as handle:
    loaded_tokenizer = pickle.load(handle)

regex = re.compile('[?]') 

#Load Model Weights
model = load_model('QA_weights_v5.hd5')
revert_back = ['Oops !\n Looks like I don\'t have the answer to that. Helpdesk has been notified, you will receive a response shortly via email.',
                       'Umm this is embarrassing ! I don\'t know the answer to that. Helpdesk will get back to you soon via email.', 
                       'Your query has been sent to the Helpdesk, you will be responded shortly via email.',
                       'Helpdesk has been notified of the query. Response is on its way via email!',
                       'I have sent your query to the Helpdesk. Response will be delivered shortly via email!',
                       'Your query has been recorded. You will receive a response from the Helpdesk in no time via email!',
                       'Your query has been sent to the Helpdesk. Response is awaited via email.']

ask_again = ['Umm ... I don\'t have an answer to that. Can you rephrase your question ?',
             'I didn\'t understand your query, can you please be more specific ?',
             'I\'m still learning, surely I will respond to this one day.\n Till then I can respond to your query regarding academic fees, hostel fees, eligibility and placements']
            
def classify_msg(msg):
    try:  
        if(regex.search(msg) != None): 
            return 1

        else:
            msg = [msg]
            stage_1 = [x.lower() for x in msg]
            stage_2 = [re.sub(r'[^a-z ]','',x) for x in stage_1]
            stage_3 = loaded_tokenizer.texts_to_sequences(stage_2)
            stage_4 = pad_sequences(stage_3, padding='post', maxlen=200)
            result = model.predict(stage_4)
            
            if result[0][0] >= 0.5:
                return 1
            
            else:
                return 0  
    
    except:        
        return 0

def send_email(query_text):
    try:
        mail_body = 'Hello Admin,\nPlease respond to this query: \n'+query_text+'\n\nRegards,\nJASPER'
        mail_subject = 'Requesting Response to Query'
        yagmail.SMTP('droid7developer@gmail.com').send('rjtmehta99@gmail.com', mail_subject, mail_body)
    
    except:
        pass
    
class ActionHelloWorld(Action):

    def name(self):
        return "action_hello_world"

    def run(self, dispatcher, tracker, domain):
        last_msg = re.sub(r'\\','',str(tracker.latest_message['text']))
        if classify_msg(last_msg) == 1:
            send_email(last_msg)
            dispatcher.utter_message(str(random.choice(revert_back)))
                        
        else:
            dispatcher.utter_message(str(random.choice(ask_again)))
            
        #dispatcher.utter_message("Hello World!"+last_msg)

        return []
