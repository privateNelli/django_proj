from django.urls import path
from . import views

urlpatterns = {
    path('index', views.index, name='index'),
    path('alumnos_list', views.crud, name='alumnos_list'),
    path('crud', views.crud, name='crud'),
    path('alumnosAdd', views.alumnosAdd, name='alumnosAdd'),

}