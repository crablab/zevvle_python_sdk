import requests

class zevvle():

    def __init__(self, key, url):
        self._url = url
        self._header = {"Authorization": "Bearer {}".format(key)}
    
    def _do_request(self, url, parameters={}):
        if(not url):
            raise Exception("Called without URL")

        r = requests.get(self._url + url, headers=self._header, params=parameters)

        if(r.status_code == 200):
            return r.json()

        raise Exception("Request failed with error {}".format(str(r.status_code)))

    def get_account(self, account_id):
        if(not account_id):
            raise Exception("Missing account_id parameter")
        
        return self._do_request("/accounts/{}".format(account_id))
    
    def get_user(self, user_id):
        if(not user_id):
            raise Exception("Missing user_id parameter")
            
        return self._do_request("/users/{}".format(user_id))

    def get_sim(self, sim_id):
        if(not sim_id):
            raise Exception("Missing sim_id parameter")
            
        return self._do_request("/sim_cards/{}".format(sim_id))

    def list_sim_cards(self):
        return self._do_request("/sim_cards")

    def list_call_records(self, sim_id, type="", limit="", before=None, after=None):
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
        if(not call_record_id):
            raise Exception("Missing call_record_id parameter")
        
        return self._do_request("/call_records/{}".format(call_record_id))

    