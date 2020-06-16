from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from .models import Investor
from django.contrib.auth.decorators import login_required

# Create your views here.
# view for all the farmers #
@method_decorator(login_required, name='dispatch')
class InvestorListView(ListView):
    model = Investor
    context_object_name = 'investors'
    template_name = 'investor/investordata.html'
    ordering = 'name'