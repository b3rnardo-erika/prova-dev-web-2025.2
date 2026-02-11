from .models import Venda

class VendaService:

    @staticmethod
    def obter_venda_com_total(venda_id):
        venda = Venda.objects.get(pk=venda_id)

        itens = venda.itens.all()

        total = 0
        for item in itens:
            total += item.total_item()

        return {
            "venda": venda,
            "itens": itens,
            "total": total
        }