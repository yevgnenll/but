from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import User


class UserEmailAPIView(APIView):

    def post(self, request):

        email = request.POST.get('email')
        # from IPython import embed; embed()

        user = User.objects.filter(
                email=email,
        )

        result = {}

        if user:
            result['status'] = '403'
        else:
            result['status'] = '200'

        return Response(result)
