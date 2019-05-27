from django.urls import path
from . views import Hometemplateview,Categoryview,CategoryUpdate,categoryDelete,Category_status

urlpatterns = [
    path('',Hometemplateview.as_view(),name="home"),
    path('category',Categoryview.as_view(),name="category"),
    path('edit/<int:pk>',CategoryUpdate.as_view(),name="category_update"),
    path('categoryDelete/<int:pk>',categoryDelete.as_view(),name="categoryDelete"),
    path('Category_status/<int:pk>',Category_status.as_view(),name="Category_status")
]