from django.urls import path

from . import views
app_name = 'kategori_apparel'
urlpatterns = [
    path('',views.index, name='index'),
]

