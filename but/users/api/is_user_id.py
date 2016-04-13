from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import User


class UserCheckAPIView(APIView):

    def get(self, request, slug):

        user = User.objects.filter(
                username=slug,
        )

        result = {}
        if user:
            result['status'] = '403'
        else:
            result['status'] = '200'

        return Response(result)
