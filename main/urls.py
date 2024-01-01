from django.contrib import admin
from django.urls import path, include

'''

This is the starting point of the application 

--> Django will match the urls and render the functions/templates accordingly

'''

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('wineApp.urls')),
]
