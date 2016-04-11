from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from trades.models import Buy


class OrderCompleteView(LoginRequiredMixin, UpdateView):

    model = Buy

    fields = [
            'address',
            'is_complete',
    ]

    slug_field = 'hash_id'

    def form_valid(self, form):

        form.instance.sell.sold_count += form.instance.count
        form.instance.sell.stock -= form.instance.count

        return super(OrderCompleteView, self).form_valid(form)

    def get_success_url(self, **kwargs):

        return reverse('profile', kwargs={
                'slug': self.request.user.username
                }
        )
