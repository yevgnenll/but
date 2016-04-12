from rest_framework.generics import ListAPIView

from trades.serializers import SellModelsSerializer
from trades.models import Sell


class SellListAPIView(ListAPIView):

    serializer_class = SellModelsSerializer
    queryset = Sell.objects.is_public_true()
