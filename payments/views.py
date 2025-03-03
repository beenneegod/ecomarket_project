from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    return render(request, 'checkout.html', { 'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY })

def create_checkout_session(request):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'pln',
                'product_data': {
                    'name': 'Zakupy w EcoMarket',
                },
                'unit_amount': 5000,  # сумма в грошах (50.00 PLN)
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/payments/success/'),
        cancel_url=request.build_absolute_uri('/payments/cancel/'),
    )
    return JsonResponse({'id': session.id})

def payment_success(request):
    return render(request, 'success.html')

def payment_cancel(request):
    return render(request, 'cancel.html')