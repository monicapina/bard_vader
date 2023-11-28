import requests
from bardapi.constants import SESSION_HEADERS
from bardapi import Bard

class BardInterface:
    def __init__(self, token_1PSID=None, token_1PSIDTS=None):
        #Check that tokens are provided before starting session
        if token_1PSIDTS is None or token_1PSID is None:
            print('ERROR! Please provide token values from your browser cookie server')
            raise ValueError
        else:
            self.token_1PSID = token_1PSID
            self.token_1PSIDTS = token_1PSIDTS
        
        # Create auxiliary variables
        self.preprompt = ""
        self.last_question = ""
        self.last_answer = ""

        # Create session object
        self.session = requests.Session()
        # Set session headers from Bard API
        self.session.headers = SESSION_HEADERS
        # Set cookies from browser
        self.session.cookies.set("__Secure-1PSID", self.token_1PSID)
        self.session.cookies.set("__Secure-1PSIDTS", self.token_1PSIDTS)

        # Create Bard object for the created session
        self.bard = Bard(token=self.token_1PSID, session=self.session)
    
    def set_preprompt(self, prompt):
        '''
        Convenience class to set a pre-prompt to any question you might ask.
        This preprompt will be added at the start of the question, and aims to
        be a modifier for the answer obtained from bard
        '''
        self.preprompt = prompt
    
    def clear_preprompt(self):
        '''
        Clears any provided preprompt
        '''
        self.preprompt = ""
    
    def ask(self, question=None, add_preprompt=True):
        '''
        Ask question to Bard and return answer
        '''
        if question is None:
            print('ERROR! Please provide a question')
            raise ValueError
        elif type(question) is not str:
            print('ERROR! Question must be a string')
            raise ValueError
        
        if add_preprompt:
            self.last_question = self.preprompt + ':' + question
        else:
            self.last_question = question
        
        self.last_answer = self.bard.get_answer(self.last_question)['content']

        return self.last_answer
    

    def get_last_answer(self):
        return self.last_answer
    
    def get_last_question(self):
        return self.last_question
    
    def get_preprompt(self):
        return self.preprompt

        