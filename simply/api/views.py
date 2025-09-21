from . serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from home.models import Product


@api_view(['GET'])
def get_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)
    

@api_view(['GET'])
def get_product(requets,pk):
    try:
        product = Product.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if requets.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)