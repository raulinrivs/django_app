from django.urls import path
from .views import (costumer_create_view, 
costumer_list_view, 
costumer_detail_view, 
costumer_update_view,
costumer_delete_view)


urlpatterns = [
	#path(url/, function.on.wiews, name="callable_on_htmls")
    path('create/', costumer_create_view, name='costumer-create'),
    path('list/', costumer_list_view, name='costumer-list'),
    path('<int:id>', costumer_detail_view, name='costumer-detail'),
    path('<int:id>/delete', costumer_delete_view, name='costumer-delete'),
    path('update/<int:id>/', costumer_update_view, name='costumer-update')
]
