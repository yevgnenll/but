from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import User


class UserCheckAPIView(APIView):

    def post(self, request):

        username = request.POST.get('username')

        user = User.objects.filter(
                username=username,
        ) or None

        result = {}
        if user:
            result['status'] = '200' 
        else:
            result['status'] = '403'

        return Response(result)

    def get(self, request, slug):

        user = User.objects.filter(
                username=slug,
        ) or None

        result = {}
        if user:
            result['status'] = '200' 
        else:
            result['status'] = '403'

        return Response(result)
