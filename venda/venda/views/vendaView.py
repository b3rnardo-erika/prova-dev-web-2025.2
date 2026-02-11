from django.views import View
from django.shortcuts import render
from .services.VendaService import VendaService

class VendaView(View):

    def get(self, request, pk):

        dados = VendaService.obter_venda_com_total(pk)

        return render(request, "venda/cupom.html", dados)
