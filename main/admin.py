from django.contrib import admin

from .models import (Skill, Project, BlockOfSkill, Picture, Message, Profile,
                     Link, SkillDescription)


class LinkAdmin(admin.StackedInline):
    model = Link
    extra = 0

class SkillDescriptionlAdmin(admin.StackedInline):
    model = SkillDescription
    extra = 0

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    inlines = [
        LinkAdmin,
        SkillDescriptionlAdmin
    ]


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

admin.site.register(Link)
admin.site.register(SkillDescription)
