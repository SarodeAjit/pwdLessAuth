from django.urls import path

from . import views
from django.conf import settings 
from django.conf.urls.static import static 

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('success/', views.success, name='success'),

]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
print (urlpatterns[0])
print (urlpatterns[1])