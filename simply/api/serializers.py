from home.models import Shop, Tag, Product, Buyer
from rest_framework import serializers

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    shop = ShopSerializer(many=False)
    tags = TagSerializer(many=True)
    buyers = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'
    
    def get_buyers(self,object):
        buyers = object.buyer_set.all()
        serializer = BuyerSerializer(buyers, many = True)
        return serializer.data
    
