from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Party, Clown
from .forms import PartyForm, ClownForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def party_list(request):
    parties = Party.objects.all()
    form = PartyForm()
    return render(request,'party_list.html', {'parties':parties, 'form':form})

def party_detail(request, pk):
    party = Party.objects.get(pk=pk)
    form = PartyForm()
    return render(request, 'party_detail.html' , {'party' : party, 'form':form})

class PartyCreate(CreateView):
    model = Party
    fields = ["title","location","description"]
    success_url = reverse_lazy("party_list")

class PartyDelete(DeleteView):
    model = Party
    success_url = reverse_lazy("party_list")


class PartyUpdate(UpdateView):
    model = Party
    fields = ["title","location","description"]
    success_url = reverse_lazy("party_list")
