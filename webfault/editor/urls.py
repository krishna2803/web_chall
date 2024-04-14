from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_html, name='render_html'),
    path('flag/', views.get_flag, name='get_flag'),
]
