from celery import Task
from users.models import User


class PhoneNumberCertificateTask(Task):

    def run(self, user_instance):
        pass
