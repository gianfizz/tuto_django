import uuid
from django.db import models
from ledger.models.account_model import AccountModel
from django.core.exceptions import ValidationError

class LedgerType(models.Choices):
    IN = "IN"
    OUT = "OUT"


class LedgerModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    client_id = models.ForeignKey(AccountModel, on_delete=models.DO_NOTHING)
    ledger_type = models.CharField(max_length=12, choices=LedgerType.choices)
    amount = models.FloatField(default=0.0) #sumar un validador solo positivos
    description = models.TextField(default="No description", blank=True)

    def __str__(self):
        return f"{self.client_id}, type: {self.ledger_type}, amount: {self.amount}"

    def clean(self):
        pass
        #raise ValidationError('Item already booked for those dates')    