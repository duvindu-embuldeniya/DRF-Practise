from . serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from home.models import Product
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_products(request):
    if request.method == 'GET':
        print(request.user)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)
    

@api_view(['GET'])
def get_product(requet,pk):
    try:
        product = Product.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if requet.method == 'GET':
        print(requet.user)
        serializer = ProductSerializer(product)
        return Response(serializer.data)