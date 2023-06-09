from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'shop'

urlpatterns = [
    
    path('fill-database/', views.fill_database, name='fill_database'),
    path('', views.ProductsListView.as_view(), name='shop'),
    path('cart_view/',  views.cart_view, name='cart_view'),
    path('add-item-to-cart/<int:pk>', views.add_item_to_cart, name='add_item_to_cart'),
    path('delete_item/<int:pk>', views.CartDeleteItem.as_view(), name='cart_delete_item'),
    path('make-order/', views.make_order, name='make_order'),
    path('cart_pnumber/', views.cart_pnumber, name='cart_pnumber'),

]

