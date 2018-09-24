"""project2 URL Configuration"""


from django.urls import path,include
from django.contrib import admin














urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('shop.urls'), name='shop'),
    path('cart/', include('cart.urls'), name='cart'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)