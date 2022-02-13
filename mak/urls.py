from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mak.views import home_page
from azbankgateways.urls import az_bank_gateways_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


admin.autodiscover()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    # path('header', header, name='header'),
    path('', include('product.urls', namespace='products')),
    path('', include('salesman_profile.urls', namespace='salesman_profile')),
    path('', include('customer_profile.urls', namespace='customer_profile')),
    path('', include('comment.urls', namespace='comments')),
    path('', include('cart.urls', namespace='cart')),
    path('', include('payment.urls', namespace='payment')),
    path('bankgateways/', az_bank_gateways_urls()),
    path('', include('cart.urls', namespace='carts')),
    path('api-auth/', include('rest_framework.urls')),
]
if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)