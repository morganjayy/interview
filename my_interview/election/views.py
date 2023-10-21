from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from election.models import PollingUnit, LocalGovtResult
from election.forms import NewPollingUnit

def polling_result(request):
  """
  This view display the result from a selected polling unit under a local government.
  """
  results = PollingUnit.objects.all().values()
  template = loader.get_template('polling_result.html')
  context = {
    'results': results,
  }
  return HttpResponse(template.render(context, request))

def lga_result(request):
  """
  This view shows all Local Government in the state and the total vote accumulated by each party from 
  all polling units.
  """
  results = LocalGovtResult.objects.all().values()
  template = loader.get_template('lga_result.html')
  context = {
    'results': results,
  }
  return HttpResponse(template.render(context, request))

def lga_details(request, id):
  """
  This view displays a page to displays results from selected local government 
  """
  results = LocalGovtResult.objects.get(id=id)
  template = loader.get_template('lga_detail.html')
  context = {
    'results': results,
  }
  return HttpResponse(template.render(context, request))

def home_page(request):
  """
  This view displays a form that new polling unit results can be entered. 
  """
  context = {}
  context ['form'] = NewPollingUnit()
  return render(request, "home.html", context)

# Create your views here.
