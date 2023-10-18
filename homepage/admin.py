from django.contrib import admin
from django.db import models
from ckeditor.widgets import CKEditorWidget

from homepage.forms import ContactForm
from .models import (
    EmailAddress,
    Notice,
    GovernanceBody,
    Contact,
    PhoneNumber,
    UsefulLink,
    ImageGallery,
    Stat,
    WhatsHappening,
    CoCurricular,
    BrightStudent,
    DropdownNavigation,
    DropdownNavigationItem,
)


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
    formfield_overrides = {models.TextField: {"widget": CKEditorWidget}}

    list_display = ("title", "date")

    ordering = ("-date",)


@admin.register(GovernanceBody)
class GovernanceBodyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    list_display = ("name", "designation")


class PhoneNumberInline(admin.TabularInline):
    model = PhoneNumber
    extra = 1


class EmailAddressInline(admin.TabularInline):
    model = EmailAddress
    extra = 1


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    form = ContactForm
    inlines = [PhoneNumberInline, EmailAddressInline]

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


@admin.register(UsefulLink)
class UsefulLinkAdmin(admin.ModelAdmin):
    list_display = (
        "site",
        "url",
    )


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
