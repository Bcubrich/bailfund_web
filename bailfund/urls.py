from django.urls import path, reverse_lazy

from . import views

app_name = 'bailfund'
urlpatterns = [
    path('', views.RosterListView.as_view()),
    path('bailfund', views.RosterListView.as_view(), name='all'),
    path('bond_list', views.BondListView.as_view()),

]


#urlpatterns = [
#    path('', views.RosterListView.as_view()),
#    path('bailfund', views.RosterListView.as_view(), name='all'),
#    path('bond_list', views.BondListView.as_view()),

#]