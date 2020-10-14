from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request,
                       "There's nothing in your shopping basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Hc6RJCM38ctaxuamPwSiRWXRaZdcUO0lkMBtah39LWPAWeZ5miVTI5AFZ6HKoKxramtCHnNbWN65KpnsG8zwhHq00PNDuqE0S',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)
