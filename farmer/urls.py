from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'^$', views.FarmerListView.as_view(), name='farmerdata'),
    
]