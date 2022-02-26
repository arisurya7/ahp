from django.urls import path
from weighting import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rfm/', views.rfm, name='rfm'),
    path('lrfm/', views.lrfm, name='lrfm'),
]