from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from bailfund.models import Personal, Roster, Errors, Bond
#from autos.forms import MakeForm

# Create your views here.

class RosterListView(View) :
    def get(self, request):
        roster = Roster.objects.using('roster_db').all();
        roster_count = Roster.objects.using('bailfund').all().count;
        #al = Auto.objects.all();

        ctx = { 'roster_count': roster_count, 'roster_list': roster };
        return render(request, 'bailfund/roster_list.html', ctx)

class BondListView(View):
    def get(self,request):
        # Get query_name from request
        query_so = request.GET.get('so')
        bonds = Bond.objects.using('roster_db').filter(so=str(query_so));
        personal = Personal.objects.using('roster_db').filter(so=str(query_so)).first();
        roster = Roster.objects.using('roster_db').filter(so=str(query_so)).first();


        bond_count = Bond.objects.using('roster_db').filter(so=str(query_so)).count;


        ctx = { 'bond_count': bond_count, 'bond_list': bonds, 'roster':roster,'personal':personal};
        return render(request, 'bailfund/bond_list.html', ctx)