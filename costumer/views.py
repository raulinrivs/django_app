from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Costumer

from .forms import CostumerForm

@login_required
def costumer_create_view(request):
	form = CostumerForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect("../list")
	context = {
		'form': form
	}
	return render(request, "costumer/costumer_create.html", context)

def costumer_list_view(request):
	queryset = Costumer.objects.all()
	
	context = {
		'object_list': queryset
	}
	return render(request, "costumer/costumer_list.html", context)

def costumer_detail_view(request, id):
	obj = get_object_or_404(Costumer, id=id)
	context = {
		"object": obj
	}
	return render(request, "costumer/costumer_detail.html", context)

@login_required
def costumer_update_view(request, id):
	obj = get_object_or_404(Costumer, id=id)
	form = CostumerForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	context = {
		'form': form
	}
	return render(request, "costumer/costumer_create.html", context)
	
@login_required
def costumer_delete_view(request, id):
	obj = get_object_or_404(Costumer, id=id)
	if request.method == "POST":
		obj.delete()
		return redirect('../list')
	context = {
		"object" : obj
	}
	return render (request, "costumer/costumer_delete.html", context)