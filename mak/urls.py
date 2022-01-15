from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from mak.views import home_page



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('', include('product.urls', namespace='products')),
    path('', include('salesman_profile.urls', namespace='salesman_profile')),
    path('', include('customer_profile.urls', namespace='customer_profile')),
    path('', include('comment.urls', namespace='comments')),

]
if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)