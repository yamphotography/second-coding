
from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static


def weddings(request):
    return HttpResponse(' Weddings Gallary')

def wedding(request,pk):
   return HttpResponse(' Wedding Gallary' + ' ' + str(pk))




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weddings.urls')),
    path('users/', include('users.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




