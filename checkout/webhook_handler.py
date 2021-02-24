# Used the code from the Code Institute Project - Boutique Ado -

from django.http import HttpResponse


# Need a webhook handler to prevent getting a payment from a customer, but no order in our database, because the customer
# accidentily closes the window browser window after the payment is confirmed.
class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)