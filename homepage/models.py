from django.db import models
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager


class DropdownNavigation(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class DropdownNavigationItem(models.Model):
    dropdown = models.ForeignKey(
        DropdownNavigation, on_delete=models.CASCADE, related_name="items"
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(DropdownNavigationItem, self).save(*args, **kwargs)


class Notice(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True)
    date = models.DateField()
    description = RichTextUploadingField()
    attachment = models.FileField(
        upload_to="notices/",
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "docx", "doc"])],
        blank=True,
        null=True,
        help_text="Upload Your Notice PDF or Docs",
    )
    tags = TaggableManager(blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Notice, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Notices"
        ordering = ["-date"]


class GovernanceBody(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200, default="Member")
    slug = models.SlugField()
    image = models.ImageField(upload_to="governance_bodies/")
    description = models.TextField(null=True, blank=True)

    speech_text = models.TextField(null=True, blank=True)
    speech_file = models.FileField(
        upload_to="governance_bodies/",
        validators=[FileExtensionValidator(allowed_extensions=["pdf", "docx", "doc"])],
        blank=True,
        null=True,
        help_text="Upload Speech PDF or Docs",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Governance Bodies"


class Contact(models.Model):
    address = models.TextField()
    map = models.TextField(
        help_text="<b style='color: red'> Copy and Paste google map's <em> iframe </em> tag here </b>"
    )

    def __str__(self):
        return self.address


class PhoneNumber(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.number


class EmailAddress(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.email


class UsefulLink(models.Model):
    site = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.site

    class Meta:
        verbose_name_plural = "Useful Links"


class ImageGallery(models.Model):
    image = models.ImageField(upload_to="image_gallery/")
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Image Gallery"


class Stat(models.Model):
    title = models.CharField(max_length=200)
    count = models.IntegerField()
    icon = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="<em> Add font-awesome icon tag </em>",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Stats"


class WhatsHappening(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to="whats_happening/")
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "What's Happening"


class CoCurricular(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()

    def __str__(self):
        return f"Co-Curricular: {self.title}"

    class Meta:
        verbose_name_plural = "Co-Curricular"


class BrightStudent(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to="bright_students/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Bright Students"
