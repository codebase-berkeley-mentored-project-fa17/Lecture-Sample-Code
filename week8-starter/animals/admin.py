from django.contrib import admin

# Register your models here.
from.models import Cat, Member, Project

admin.site.register(Cat)
admin.site.register(Member)
admin.site.register(Project)