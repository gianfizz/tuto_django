from django.apps import AppConfig


class LedgerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ledger"

    def ready(self) -> None:
        from ledger.models import account_model, ledger_model
        from ledger.admin import account_admin, ledger_admin
        from ledger.signals import ledger_signal

        return super().ready()
