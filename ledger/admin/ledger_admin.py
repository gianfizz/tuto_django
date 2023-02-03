from django.contrib import admin
from ledger.models.ledger_model import LedgerModel


@admin.register(LedgerModel)
class LedgerAdmin(admin.ModelAdmin):
    list_display = ("client_id", "ledger_type", "amount")
