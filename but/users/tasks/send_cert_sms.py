from celery import Task

from users.models import PhoneCertificate

from but.utils import SMSSend


class SendCertificateNumber(Task):

    def run(self, cert_id):

        certificate = PhoneCertificate.objects.get(
                id=cert_id,
        )

        send_cert_message = SMSSend()
        send_cert_message.send_sms(
                dest_num=certificate.phone_number,
                msg="인증번호 {cert_number}를 입력해주세요".format(
                    cert_number=certificate.random_number,
                )
        )
