from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from trades.serializers import CommentModelSerializer
from trades.models import Sell

from django.contrib.auth.mixins import LoginRequiredMixin


class CommentAttachAPIView(LoginRequiredMixin, APIView):

    def post(self, request, *args, **kwargs):

        sell = Sell.objects.get(
            hash_id=kwargs.get('slug'),
        )

        comment = sell.comment_set.create(
            content=request.POST.get('content'),
            user=request.user,
        )

        commnet_serializer = CommentModelSerializer(comment)

        if CommentModelSerializer(data=commnet_serializer.data):
            return Response(commnet_serializer.data, status=status.HTTP_201_CREATED)
        return Response(commnet_serializer.error, status=status.HTTP_400_BAD_REQUEST)
