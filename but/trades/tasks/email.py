from celery import Task

from trades.models import Contact

from but.utils import Mailgun


class SendEmailBuyerToSeller(Task):

    def run(self, contact_id):

        contact = Contact.objects.get(
            id=contact_id,
        )

        mailgun = Mailgun()
        respose = mailgun.send_simple_email(contact)
