import requests

from django.conf import settings


class SMSSend():

    def __init__(self):
        self.client_id = settings.API_CLIENT
        self.key = settings.API_KEY
        self.api_version ="1"
        self.msg_type = "sms"

        self.api_url = "http://api.openapi.io/ppurio/"+ \
                    "{api_version}/message/{msg_type}/{client_id}/".format(
                    api_version=self.api_version,
                    msg_type=self.msg_type,
                    client_id=self.client_id,
                    )

        self.header = {
            "x-waple-authorization": self.key,
        }
         

    def send_sms(self, dest_num, msg):

        res = requests.post(
                self.api_url,  
                data = {
                    'dest_phone' : dest_num,
                    'msg_body': msg,
                    'send_phone' : '01095716689',
                },
                headers= self.header)
        
        return res
