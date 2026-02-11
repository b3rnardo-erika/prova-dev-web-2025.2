from django.urls import path
from . import views

app_name = "venda"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("venda/<int:pk>/", views.VendaView.as_view(), name="venda"),
]
