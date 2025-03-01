from django.urls import path
from .views import CashMachineAPIView

urlpatterns = [
    path("cash_machine/", CashMachineAPIView.as_view(), name="cash_machine"),
]
