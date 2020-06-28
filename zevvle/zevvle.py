import requests

class zevvle():

    def __init__(self, key, url="https://api.zevvle.com"):
        """
        Initializes the SDK.
        
        :param key: Your Zevvle API key. 
        :param url optional: The Zevvle API URL. 
        """
        if(not key):
            raise Exception("Missing API key.")
        
        self._url = url
        self._header = {"Authorization": "Bearer {}".format(key)}
    
    def _do_request(self, url, parameters={}):
        """
        Makes a request. 

        :param url: The full URL of the request.
        :param parameters optional: Dict of parameters for the request.

        :returns: JSON response. 
        """
        if(not url):
            raise Exception("Called without URL")

        r = requests.get(self._url + url, headers=self._header, params=parameters)

        if(r.status_code == 200):
            return r.json()

        raise Exception("Request failed with error {}".format(str(r.status_code)))

    def get_account(self, account_id):
        """
        Looks up Zevvle account.
        
        :param account_id: ID of the Zevvle account to look up.
        :returns: Zevvle account details. 
        """
        if(not account_id):
            raise Exception("Missing account_id parameter")
        
        return self._do_request("/accounts/{}".format(account_id))
    
    def get_user(self, user_id):
        """
        Looks up Zevvle user.
        
        :param user_id: ID of the Zevvle user to look up.
        :returns: Zevvle user details. 
        """
        if(not user_id):
            raise Exception("Missing user_id parameter")
            
        return self._do_request("/users/{}".format(user_id))

    def get_sim(self, sim_id):
        """
        Looks up Zevvle SIM card.
        
        :param sim_id: ID of the Zevvle SIM card to look up.
        :returns: Zevvle SIM card details. 
        """
        if(not sim_id):
            raise Exception("Missing sim_id parameter")
            
        return self._do_request("/sim_cards/{}".format(sim_id))

    def list_sim_cards(self):
        """
        Lists all SIM cards linked to the Zevvle API key.
        
        :returns: SIM cards for the API key in use. 
        """
        return self._do_request("/sim_cards")

    def list_call_records(self, sim_id, type="", limit="", before=None, after=None):
        """
        Lists call records for a given Zevvle SIM ID, according to filtering. 
        
        :param sim_id: ID of the Zevvle SIM card to get records for.
        :param type optional: Call record type (data, voice, sms, mms) to filter on.
        :param limit optional: How many records to limit the results to. 
        :param before: Limit results to records before a given datetime. 
        :param after: Limit results to records after a given datetime. 
        :returns: Call records for the given query. 
        """
        parameters = {}

        if(not sim_id):
            raise Exception("Missing sim_id parameter")
        else:
            parameters["sim_card_id"] = sim_id

        if(type and type not in ["data", "voice", "sms", "mms"]):
            raise Exception("Invalid call record type (data, voice, sms, mms) only")
        elif(type):
            # Valid type supplied
            parameters["type"] = type
        
        if(limit):
            parameters["limit"] = limit

        if(before):
            parameters['before'] = before
        
        if(after):
            parameters['after'] = after
        
        return self._do_request("/call_records/", parameters)
     
    def get_call_record(self, call_record_id): 
        """
        Looks up Zevvle call record.
        
        :param call_record_id: ID of the Zevvle call record to look up.
        :returns: Zevvle call record details. 
        """
        if(not call_record_id):
            raise Exception("Missing call_record_id parameter")
        
        return self._do_request("/call_records/{}".format(call_record_id))

    