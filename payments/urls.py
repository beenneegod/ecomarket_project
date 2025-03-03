from django.urls import path
from .views import checkout, create_checkout_session, payment_success, payment_cancel

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('create-checkout-session/', create_checkout_session, name='create_checkout_session'),
    path('success/', payment_success, name='payment_success'),
    path('cancel/', payment_cancel, name='payment_cancel'),
]