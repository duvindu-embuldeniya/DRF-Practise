from django.contrib import admin
from . models import Shop, Tag, Product, Buyer, Blog, Review

admin.site.register(Shop)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Buyer)

admin.site.register(Blog)
admin.site.register(Review)