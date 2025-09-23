from home.models import Shop, Tag, Product, Buyer, Blog, Review
from rest_framework import serializers
from django.contrib.auth.models import User

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
        serializer = BuyerSerializer(buyers, many=True)
        return serializer.data






# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username','email']


# class BlogSerializer(serializers.ModelSerializer):
#     writer = UserSerializer(many=False)
#     reviews = serializers.SerializerMethodField()

#     class Meta:
#         model = Blog
#         fields = '__all__'
    
#     def get_reviews(self,object):
#         reviews = object.review_set.all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return serializer.data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    writer = UserSerializer(many = False)
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'
    
    def get_reviews(self, object):
        reviews = object.review_set.all()
        serializer = ReviewSerializer(reviews, many = True)
        return serializer.data