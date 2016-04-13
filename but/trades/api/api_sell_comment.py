from rest_framework.generics import RetrieveAPIView

from trades.serializers import SellDetailModelSerializer, CommentModelSerializer
from trades.models import Comment, Sell


class CommentAPIView(RetrieveAPIView):

    serializer_class = CommentModelSerializer

    def get_queryset(self):

        queryset = Sell.objects.get(
                pk=self.kwargs.get('pk')
        )

        return queryset
