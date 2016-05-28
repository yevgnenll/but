from django.views.generic import TemplateView

from django.shortcuts import redirect


class HomeView(TemplateView):

    def get(self, request):

        return redirect('goods_list')
