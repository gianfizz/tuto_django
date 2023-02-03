import uuid
from django.db import models


class AccountType(models.Choices):
    COMMON = "COMMON"
    SPECIAL = "SPECIAL"


class AccountModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    client_id = models.CharField(max_length=11)
    account_type = models.CharField(
        max_length=12, choices=AccountType.choices, default=AccountType.COMMON
    )
    amount = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.client_id}"

    class Meta:
        unique_together = ("client_id", "account_type")
        