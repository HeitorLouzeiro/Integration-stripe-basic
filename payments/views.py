import stripe
from django.conf import settings
# Create your views here.
from django.shortcuts import redirect, render


def home(request):
    template_name = 'payments/pages/home.html'
    stripe.api_key = settings.STRIPE_SECRET_KEY
    return render(request, template_name)


def charge(request):
    if request.method == 'POST':
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1MCqakASQv92CGV2YGc5bOYM',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://localhost:8000',
            cancel_url='http://localhost:8000',
        )
        return redirect(checkout_session.url, code=303)
