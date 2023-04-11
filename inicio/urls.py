from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.mi_vista, name='inicio'),
    path('crear-remera/', views.crear_remera, name='crear_remera'),
]