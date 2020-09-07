from django.urls import path, reverse_lazy

from . import views

app_name = 'web_ideas'
urlpatterns = [
    path('', views.IdeaListView.as_view()),
    path('web_ideas', views.IdeaListView.as_view(), name='all'),
    path('ideas/<int:pk>', views.IdeaDetailView.as_view(), name='ideas_detail'),
    path('ideas/create',
        views.IdeaCreateView.as_view(success_url=reverse_lazy('web_ideas:all')), name='ideas_create'),
    path('ideas/<int:pk>/update',
        views.IdeaUpdateView.as_view(success_url=reverse_lazy('web_ideas:all')), name='ideas_update'),
    path('ideas/<int:pk>/delete',
        views.IdeaDeleteView.as_view(success_url=reverse_lazy('web_ideas:all')), name='ideas_delete'),
]