from django.contrib import admin
from django.urls import include, path
from movies import views as movies_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('', include('movies.urls'), name='index'),
    path('registration/', movies_views.registration, name='registration'),
]