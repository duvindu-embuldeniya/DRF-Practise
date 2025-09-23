from . serializers import ProductSerializer, BlogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from home.models import Product, Blog, Review
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)
    

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_product(request,pk):
    try:
        product = Product.objects.get(pk=pk)
        print(request.user)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        print(request.user)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


# @api_view(['GET'])
# def blogs(request):
#     if request.method == 'GET':
#         blogs = Blog.objects.all()
#         serializer = BlogSerializer(blogs, many = True)
#         return Response(serializer.data)



# @api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
# def get_blog(request,pk):
#     try:
#         blog = Blog.objects.get(pk=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         user = request.user
#         data = request.data

#         review,created = Review.objects.get_or_create(
#             reviewer = user,
#             blog = blog
#         )

#         review.type = data['type']
#         review.save()
        
#         blog.get_total

#         serializer = BlogSerializer(blog)
#         return Response(serializer.data)
    

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def blogs(request):
    if request.method == 'GET':
        objects = Blog.objects.all()
        serializer = BlogSerializer(objects, many = True)
        return Response(serializer.data)
    
        
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def get_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogSerializer(blog, many = False)
        return Response(serializer.data)
    
    if request.method == 'POST':
        user = request.user
        data = request.data

        review,created = Review.objects.get_or_create(
            reviewer = user,
            blog = blog
        )

        review.type = data['type']
        review.save()

        blog.get_total

        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    
