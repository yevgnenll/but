from django.views.generic import View
from trades.models import Sell


class GoodsSellBase(View):

    model = Sell
