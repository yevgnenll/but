from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import PhoneCertificate

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
