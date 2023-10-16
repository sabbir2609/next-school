from django.db import models
from django.utils.text import slugify


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
    slug = models.SlugField()
    description = models.TextField()
    attachment = models.FileField(upload_to="notices/")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Notices"


class GovernanceBody(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()
    speech_text = models.TextField()
    speech_file = models.FileField(upload_to="governance_bodies/")
    image = models.ImageField(upload_to="governance_bodies/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Governance Bodies"


class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return f"Contact: {self.email}"

    class Meta:
        verbose_name_plural = "Contacts"


class UsefulLink(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return f"Useful Link: {self.title}"

    class Meta:
        verbose_name_plural = "Useful Links"


class ImageGallery(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    images = models.ImageField(upload_to="image_gallery/")
    description = models.TextField()

    def __str__(self):
        return f"Image Gallery: {self.title}"

    class Meta:
        verbose_name_plural = "Image Gallery"


class Stat(models.Model):
    title = models.CharField(max_length=200)
    count = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"Stat: {self.title}"

    class Meta:
        verbose_name_plural = "Stats"


class WhatsHappening(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to="whats_happening/")
    url = models.URLField()

    def __str__(self):
        return f"What's Happening: {self.title}"

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
        return f"Bright Student: {self.name}"

    class Meta:
        verbose_name_plural = "Bright Students"
