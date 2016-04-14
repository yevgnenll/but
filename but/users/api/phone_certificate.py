from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import PhoneCertificate, User

from users.utils import six_digit_number


class CertificateUserPhone(APIView):

    def post(self, request):

        phone_number = request.POST.get('phone_number')
        send_number = phone_number.replace('.', '').replace('-', '').replace(' ', '')

        random_int = six_digit_number()

        cert = PhoneCertificate.objects.create(
                user=request.user,
                phone_number=send_number,
                random_number=random_int,
        )

        result = {
                'status': '200',
                'certificate': cert.id,
        }

        return Response(result)


class CheckCertificatePhone(APIView):

    def post(self, request):

        cert_number = request.POST.get('cert_number')
        certification = PhoneCertificate.objects.filter(
                user=request.user
        )

        check = certification.last()
        # from IPython import embed; embed()
        result = {}

        if cert_number == check.random_number:
            user = User.objects.get(
                    username=request.user.username,
            )
            user.phone_number = check.phone_number
            user.is_phone_certificate = True
            user.save()
            result['status'] = '200'
        else:
            result['status'] = '403'

        return Response(result)
