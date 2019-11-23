from django.urls import path
from .views import (
    Itemsdetailsview,
    Inventorydetails,
    PostCreateView,
    itemupdateview,
    ItemDeleteView,
    temporary,
)

urlpatterns = [
    #  path('',Inventorydetails.as_view(),name='inventory-details'),
     path('',temporary.as_view(),name='inventory-details'),
    path('additem',PostCreateView.as_view(),name='Addnew-item'),

    path('item/<int:pk>/', Itemsdetailsview.as_view(template_name='inventory/hh.html'), name='item-detail'),
    path('item/<int:pk>/update', itemupdateview.as_view(), name='item-update'),
    path('item/<int:pk>/delete', ItemDeleteView.as_view(), name='item-delete'),
 
]
