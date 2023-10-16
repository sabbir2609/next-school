# homepage/tests.py
from django.test import TestCase
from .models import Notice, GovernanceBody
from django.db import models


class NoticeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        Notice.objects.create(
            title="Test Notice",
            slug="test-notice",
            description="This is a test notice description.",
            attachment="notices/test.pdf",
            date="2023-10-05",
        )

    def test_title_label(self):
        notice = Notice.objects.get(id=1)
        field_label = notice._meta.get_field("title").verbose_name
        self.assertEqual(field_label, "title")

    def test_date_is_datefield(self):
        notice = Notice.objects.get(id=1)
        field = notice._meta.get_field("date")
        self.assertIsInstance(field, models.DateField)


class GovernanceBodyModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        GovernanceBody.objects.create(
            name="Test Body",
            description="This is a test governance body description.",
            speech_text="This is a test governance body speech text.",
            speech_file="governance_bodies/test.mp3",
            image="governance_bodies/test.png",
        )

    def test_name_label(self):
        body = GovernanceBody.objects.get(id=1)
        field_label = body._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")
