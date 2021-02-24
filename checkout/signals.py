# Used the code from the Code Institute Project - Boutique Ado -
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


# receiver decorator telling we're receiving post save signals from the order line item model
@receiver(post_save, sender=OrderLineItem)
# function handle signals from the post_save event
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()

# receiver decorator telling we're receiving post delete signals from the order line item model
@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()