from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse

from trades.models import Comment, Sell


class CommentAttachView(CreateView):

    model = Comment

    slug_field = "hash_id"

    fields = [
            'content',
    ]

    def form_valid(self, form):

        slug = self.kwargs.get('slug')
        sell = Sell.objects.get(hash_id=slug)

        form.instance.sell = sell
        form.instance.user = self.request.user

        return super(CommentAttachView, self).form_valid(form)

    def get_success_url(self, **kwargs):

        slug = self.kwargs.get('slug')

        return reverse('goods_detail', kwargs={
                'slug': slug,
            },
        )
