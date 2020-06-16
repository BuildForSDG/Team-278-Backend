from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from .models import Farmer
from django.contrib.auth.decorators import login_required

# Create your views here.
# view for all the farmers #
@method_decorator(login_required, name='dispatch')
class FarmerListView(ListView):
    model = Farmer
    context_object_name = 'farmers'
    template_name = 'farmer/farmerdata.html'
    ordering = 'name'