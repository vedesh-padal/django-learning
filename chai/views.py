from django.shortcuts import render, get_object_or_404
from .models import ChaiVariety, Store
from .forms import ChaiVarietyForm

def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, 'chai/all_chai.html', {'chais': chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(ChaiVariety, pk=chai_id)
    return render(request, 'chai/chai_detail.html', {'chai': chai})

def contact(request):
  return render(request, 'chai/contact.html')

def about(request):
  # return HttpResponse("I am a student")
  return render(request, 'chai/about.html')

def chai_store_view(request):
  stores = None
  if request.method == 'POST':

    # 2 cases of form:
    # - we want to render the form ( default - rendering )
    # - user sent to the server after filling [ post ]

    form = ChaiVarietyForm(request.POST)
    if form.is_valid():
      chai_variety = form.cleaned_data['chai_variety']
      stores = Store.objects.filter(chai_varieties=chai_variety)

  else:
    form = ChaiVarietyForm()  # creating the form and sending to user [ 1 ]


  return render(request, 'chai/chai_stores.html', { 'stores': stores, 'form': form })

