from django.contrib import admin

from ledger.models.account_model import AccountModel

# Register your models here.


@admin.register(AccountModel)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("client_id", "account_type", "amount")
