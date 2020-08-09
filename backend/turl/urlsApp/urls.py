from django.urls import path

from . import views

urlpatterns = [
    path('<int:path_id>', views.get, name='redirect'),
    path('', views.post, name='add'),
]
