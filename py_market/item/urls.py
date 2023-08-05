from django.urls import path
from . import views



app_name = 'item'

urlpatterns = [
    path('<int:item_id>', views.details, name='details')

]