from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from django.core.exceptions import ValidationError

from ledger.models.ledger_model import LedgerModel, LedgerType
from ledger.models.account_model import AccountModel
from django_q.tasks import async_task

@receiver(pre_save, sender=LedgerModel)
def ledger_model_pre_save(sender, instance: LedgerModel, **kwargs):
    
    if instance.ledger_type == LedgerType.IN.value:
        if instance.amount < 0:
            raise ValidationError('Invalid Amount')

    if instance.ledger_type == LedgerType.OUT.value:
        if (instance.client_id.amount - instance.amount) < 0:
            raise ValidationError('Invalid Amount')

def update_account_balance(created ,instance: LedgerModel)->None:
    if created:
        if instance.ledger_type == LedgerType.IN.value:
            instance.client_id.amount += instance.amount
        if instance.ledger_type == LedgerType.OUT.value:
            instance.client_id.amount -= instance.amount
        instance.client_id.save()

@receiver(post_save, sender=LedgerModel)
def ledger_model_post_save(sender, instance: LedgerModel, created, **kwargs):
    async_task(update_account_balance, created, instance)