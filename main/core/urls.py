
# from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
# from 

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include("invenotry.urls")),
    path('inventory/', include("invenotry.urls")),
    path('send/', include("send.urls")),


]
