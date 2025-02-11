from django.urls import path
from . import views # Import everything from views to connect routes to view functions

urlpatterns = [
    # Routes will be added here
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for cats index
    path('cats/', views.cat_index, name='cat-index'),
    path('cats/<int:cat_id>/', views.cat_detail, name='cat-detail'),
    # new route used to create a cat
    path('cats/create/', views.CatCreate.as_view(), name='cat-create'),
    # update and delete cat
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cat-update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cat-delete'),
    #eeding route
    path(
        'cats/<int:cat_id>/add-feeding/', 
        views.add_feeding, 
        name='add-feeding'
    ),
]
