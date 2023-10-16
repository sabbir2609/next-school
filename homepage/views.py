# import json
# import os
# from django.shortcuts import render
# from django.views.generic import TemplateView


# class HomePageView(TemplateView):
#     template_name = "home/homepage.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         # using temporary data for dev purpose
#         json_file_path = os.path.join(os.path.dirname(__file__), "data/data.json")
#         with open(json_file_path, "r") as json_file:
#             data = json.load(json_file)

#         context["dropdowns"] = data["dropdowns"]
#         context["notices"] = data["notices"]
#         context["img_data"] = data["images"]
#         context["useful_links"] = data["useful_links"]
#         context["whatsHappening"] = data["whatsHappening"]
#         context["star_student"] = data["star_student"]
#         context["data"] = [i for i in range(1, 20)]
#         return context


from django.views.generic import TemplateView
from .models import (
    DropdownNavigation,
    Notice,
    GovernanceBody,
    Contact,
    UsefulLink,
    ImageGallery,
    Stat,
    WhatsHappening,
    CoCurricular,
    BrightStudent,
)


class HomePageView(TemplateView):
    template_name = "home/homepage.html"  # Adjust the template path as needed

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch data from your models and pass it to the template
        context["dropdowns"] = DropdownNavigation.objects.all()
        context["notices"] = Notice.objects.all()
        context["governance_bodies"] = GovernanceBody.objects.all()
        context["contacts"] = Contact.objects.all()
        context["useful_links"] = UsefulLink.objects.all()
        context["image_galleries"] = ImageGallery.objects.all()
        context["stats"] = Stat.objects.all()
        context["whats_happening"] = WhatsHappening.objects.all()
        context["co_curricular"] = CoCurricular.objects.all()
        context["bright_students"] = BrightStudent.objects.all()

        return context
