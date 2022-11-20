from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, TemplateView

import stripe

from items.models import Item


stripe.api_key = settings.STRIPE_SECRET_KEY


class CancelView(TemplateView):
    template_name = 'items/cancel.html'


class SuccessView(TemplateView):
    template_name = 'items/success.html'


class ItemPageView(DetailView):
    model = Item
    template_name = 'items/item_detail.html'

    def get_context_data(self, **kwargs):
        item_id = self.kwargs['pk']
        item = get_object_or_404(Item, id=item_id)
        context = super().get_context_data(**kwargs)
        context.update({
            "item": item,
        })
        return context


def create_checkout_session(*args, **kwargs):
    item_id = kwargs['pk']
    item = Item.objects.get(id=item_id)
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': item.price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/cancel',
    )
    return redirect(session.url, code=303)
