from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Produto(models.Model):
    codigo = models.CharField(max_length=20)
    descricao = models.CharField(max_length=100)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def clean(self):
        if self.valor_unitario <= 0:
            raise ValidationError("Valor unitário deve ser maior que 0")

    def __str__(self):
        return self.descricao

class Venda(models.Model):
    cpf_comprador = models.CharField(max_length=14)
    data = models.DateTimeField()

    def clean(self):
        if len(self.cpf_comprador) != 14:
            raise ValidationError("CPF deve ter 14 caracteres")

        if self.data and self.data > timezone.now():
            raise ValidationError("Data não pode ser futura")

    def total_venda(self):
        return sum(item.total_item() for item in self.itens.all())

    def __str__(self):
        return self.cpf_comprador


class ItemDeVenda(models.Model):
    venda = models.ForeignKey(
        Venda,
        on_delete=models.CASCADE,
        related_name="itens"
    )
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def clean(self):
        if self.quantidade <= 0:
            raise ValidationError("Quantidade deve ser maior que 0")

    def total_item(self):
        return self.quantidade * self.produto.valor_unitario

    def __str__(self):
        return f"{self.produto} x {self.quantidade}"
