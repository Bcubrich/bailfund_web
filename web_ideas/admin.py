from django.contrib import admin

from web_ideas.models import Priority,  Difficulty, Status, Ideas

admin.site.register(Priority)
admin.site.register(Difficulty)
admin.site.register(Status)
admin.site.register(Ideas)
