from django.urls import path
from . import views


urlpatterns = [
    # Home page and others
    path('', views.home, name='rock-home'),
    path('about/', views.about, name='rock-about'),

    # Seller
    path('seller/', views.seller, name='rock-seller'),
    path('createorder/', views.createProduct, name='seller-create-order'),
    path('updateorder/<str:pk>/', views.updateProduct, name='updateorder'),
    path('deleteorder/<str:pk>/', views.deleteProduct, name='deleteorder'),

    # User CRUD for Cart
    path('cart/', views.cart, name='rock-cart'),
    path('checkout/', views.checkout, name='rock-checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),


]