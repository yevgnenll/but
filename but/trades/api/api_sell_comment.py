from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from trades.serializers import CommentModelSerializer
from trades.models import Comment, Sell


class CommentAPIView(RetrieveAPIView):

    serializer_class = CommentModelSerializer
    lookup_field = 'sell.hash_id'
    queryset = Sell.objects.all()
