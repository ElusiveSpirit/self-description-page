from django.contrib import admin

from .models import Skill, Project, BlockOfSkill, Picture



from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import ugettext_lazy as _


class PictureAdmin(admin.StackedInline):
    model = Picture
    extra = 3

class BlockOfSkillAdmin(admin.StackedInline):
    model = BlockOfSkill
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        PictureAdmin,
        BlockOfSkillAdmin
    ]

admin.site.register(Skill)
admin.site.register(BlockOfSkill)
admin.site.register(Picture)
