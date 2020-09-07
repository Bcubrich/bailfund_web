from web_ideas.models import Priority,  Difficulty, Status, Ideas
from web_ideas.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView




class IdeaListView(OwnerListView):
    model = Ideas
    # By convention:
    # template_name = "ads/ad_list.html"


class IdeaDetailView(OwnerDetailView):
    model = Ideas


class IdeaCreateView(OwnerCreateView):
    model = Ideas
    fields = ['name', 'priority','difficulty', 'status','description','linkedin_url']


class IdeaUpdateView(OwnerUpdateView):
    model = Ideas
    fields = ['name', 'priority', 'difficulty','status','description','linkedin_url']


class IdeaDeleteView(OwnerDeleteView):
    model = Ideas