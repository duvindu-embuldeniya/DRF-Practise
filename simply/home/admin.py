from django.contrib import admin
from . models import Shop, Tag, Product, Buyer

admin.site.register(Shop)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Buyer)