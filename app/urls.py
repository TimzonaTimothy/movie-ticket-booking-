from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('search/',views.search,name='search'),
    path('buy/<int:pk>/',views.buy,name='buy'),
    path('pdf/',views.pdf,name='pdf'),
    path('payments/', views.payments, name='payments'),
    path('order_complete/',views.order_complete, name='order_complete'),
]