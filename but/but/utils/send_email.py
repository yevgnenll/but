import requests
import os


class Mailgun:

    mailgun_domain = os.environ.get('MAILGUN_DOMAIN')
    auth_api = os.environ.get('MAILGUN_SECRET_KEY')

    def get_sender(self, instance):

        result_str = "{username} <{sender_mail}>".format(
            username=instance.send.username,
            sender_mail=instance.send.email,
        )

        return result_str

    def get_accept(self, instance):
        result_list = []
        result_list.append(instance.accept.email)
        return result_list

    def send_simple_email(self, instance):
        print(self.mailgun_domain)
        response = requests.post(
            self.mailgun_domain,
            auth=('api', self.auth_api),
            data={
                'from': self.get_sender(instance),
                'to': self.get_accept(instance),
                'subject': instance.message_title,
                'text': instance.message_text,
            },
        )

        return response

    def numerous_email_send(self, instance, accepts):

        response = requests.post(
            self.mailgun_domain,
            auth=('api', self.auth_api),
            data={
                'from': self.get_sender(instance),
                'to': accepts,
                'subject': instance.message_title,
                'text': instance.message_text,
            }
        )

        return response
