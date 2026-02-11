from django.shortcuts import render

from django.views import View
from django.shortcuts import render, get_object_or_404
from .models import Venda


class IndexView(View):

    def get(self, request):
        lista = Venda.objects.all().order_by("-data")

        return render(request, "venda/index.html", {
            "lista": lista,
            "pesquisa": False
        })

    def post(self, request):
        termo = request.POST.get("cpf", "")

        lista = Venda.objects.filter(
            cpf_comprador__icontains=termo
        ).order_by("-data")

        return render(request, "venda/index.html", {
            "lista": lista,
            "pesquisa": True,
            "termo": termo
        })


class VendaView(View):

    def get(self, request, pk):
        venda = get_object_or_404(Venda, pk=pk)

        return render(request, "venda/cupom.html", {
            "venda": venda,
            "itens": venda.itens.all(),
            "total": venda.total_venda()
        })
