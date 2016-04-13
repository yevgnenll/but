from rest_framework.generics import ListAPIView

from trades.serializers import SellDetailModelSerializer, CommentModelSerializer
from trades.models import Comment, Sell


class CommentAPIView(ListAPIView):

    serializer_class = CommentModelSerializer

    def get_queryset(self):

        queryset = Sell.objects.get(
                pk=self.kwargs.get('pk')
        )

        return queryset.comment_set.all()
