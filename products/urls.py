from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),

    # /products/12/
    path('<int:product_id>/', views.detail, name='detail')
]
