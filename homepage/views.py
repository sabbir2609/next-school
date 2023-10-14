import json
import os
from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home/homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # using temporary data for dev purpose
        json_file_path = os.path.join(os.path.dirname(__file__), "data/data.json")
        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)

        context["dropdowns"] = data["dropdowns"]
        context["notices"] = data["notices"]
        context["img_data"] = data["images"]
        context["useful_links"] = data["useful_links"]
        context["whatsHappening"] = data["whatsHappening"]
        context["star_student"] = data["star_student"]
        context["data"] = [i for i in range(1, 20)]
        return context
