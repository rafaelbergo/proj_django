from django.urls import path
from recipes.views import home, contato, sobre


urlpatterns = [
    path('', home),
    path('contato/', contato), # dominio.com/contato/
    path('sobre/', sobre),   # dominio.com/sobre/
]