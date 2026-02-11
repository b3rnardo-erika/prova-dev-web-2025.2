from django.contrib import admin
from .models import Produto, Venda, ItemDeVenda

admin.site.register(Produto)
admin.site.register(Venda)
admin.site.register(ItemDeVenda)
