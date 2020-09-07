from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse

def session_monitor(request):
    num_visits= request.session.get('num_visits', 0) +1
    request.session['num_visits'] = num_visits
    if num_visits >4 : del(request.session['num_visits'])
    response=HttpResponse('view count='+str(num_visits))
    response.set_cookie('dj4e_cookie', '532b7cbe', max_age=1000)
    return response