from django.urls import path
from . views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('products/', get_products, name = 'products'),
    path('product/<int:pk>/', get_product, name = 'product'),

    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('blog/<int:pk>/', get_blog, name = 'blog')
]

