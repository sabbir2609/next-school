from django.test import TestCase
from school.models import (
    Subject,
    Class,
    # Section,
    Student,
    # Teacher,
    # SectionSubject,
    # StudentAssign,
    # Attendance,
)

# Create your tests here.


class SubjectTestCase(TestCase):
    def setUp(self):
        Subject.objects.create(title="Math", description="Mathematics")
        Subject.objects.create(title="Science", description="Science")

    def test_subject_title(self):
        math = Subject.objects.get(title="Math")
        science = Subject.objects.get(title="Science")
        self.assertEqual(math.title, "Math")
        self.assertEqual(science.title, "Science")

    def test_subject_description(self):
        math = Subject.objects.get(title="Math")
        science = Subject.objects.get(title="Science")
        self.assertEqual(math.description, "Mathematics")
        self.assertEqual(science.description, "Science")


class ClassTestCase(TestCase):
    def setUp(self):
        Class.objects.create(title="Class 1", description="Class 1")
        Class.objects.create(title="Class 2", description="Class 2")

    def test_class_title(self):
        cls1 = Class.objects.get(title="Class 1")
        cls2 = Class.objects.get(title="Class 2")
        self.assertEqual(cls1.title, "Class 1")
        self.assertEqual(cls2.title, "Class 2")

    def test_class_description(self):
        cls1 = Class.objects.get(description="Class 1")
        cls2 = Class.objects.get(description="Class 2")
        self.assertEqual(cls1.description, "Class 1")
        self.assertEqual(cls2.description, "Class 2")


class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(
            student_id="1",
            name_en="Sagar",
            name_bn="সাগর",
            birth_certificate_no="12394839843948394",
            image="",
        )

    def test_student_id(self):
        student = Student.objects.get(student_id="1")
        self.assertEqual(student.student_id, "1")

    def url_get_at_current_location(self):
        response = self.client.get("students/")
        self.assertEqual(response.status_code, 200)
