from django.contrib import admin
from django.db import models
from .models import (
    Notice,
    GovernanceBody,
    Contact,
    UsefulLink,
    ImageGallery,
    Stat,
    WhatsHappening,
    CoCurricular,
    BrightStudent,
    DropdownNavigation,
    DropdownNavigationItem,
)
from tinymce.widgets import TinyMCE


class DropdownNavigationItemInline(admin.TabularInline):
    model = DropdownNavigationItem
    extra = 1

    prepopulated_fields = {
        "slug": ("name",),
    }


@admin.register(DropdownNavigation)
class DropdownNavigationAdmin(admin.ModelAdmin):
    inlines = [DropdownNavigationItemInline]


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    formfield_overrides = {models.TextField: {"widget": TinyMCE()}}

    list_display = ("title", "date")

    ordering = ("-date",)


@admin.register(GovernanceBody)
class GovernanceBodyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(UsefulLink)
class UsefulLinkAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(ImageGallery)
class ImageGalleryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    pass


@admin.register(WhatsHappening)
class WhatsHappeningAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(CoCurricular)
class CoCurricularAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(BrightStudent)
class BrightStudentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
