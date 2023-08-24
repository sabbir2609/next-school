import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Subject(models.Model):
    title = models.CharField(max_length=255, help_text="Subject Name")
    description = models.TextField(
        null=True, blank=True, help_text="Subject Description",
        default=""
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Subjects"


class Class(models.Model):
    CLASS_CHOICES = (
        ("6", "Six"),
        ("7", "Seven"),
        ("8", "Eight"),
        ("9", "Nine"),
        ("10", "Ten"),
    )
    title = models.CharField(max_length=2, choices=CLASS_CHOICES, primary_key=True)
    class_teacher = models.ForeignKey(
        "Teacher", on_delete=models.SET_NULL, null=True, blank=True
    )
    description = models.TextField(
        null=True, blank=True,
        help_text="eg: 'Class 6, total 120 students, 4 sections, 30 students in each section'", default=""
    )

    def __str__(self):
        return f"Class {self.title}"

    class Meta:
        verbose_name_plural = "Classes"


class Section(models.Model):
    SECTION_CHOICES = (
        ("A", "Section A"),
        ("B", "Section B"),
        ("C", "Section C"),
        ("Sc", "Science"),
        ("Co", "Commerce"),
        ("Ar", "Arts"),
    )
    name = models.CharField(
        max_length=2, choices=SECTION_CHOICES, verbose_name="Section"
    )
    description = models.TextField(
        null=True, blank=True,
        help_text="Section Description, e.g. 'Section A of Class 6, total 30 students'"
    )
    class_name = models.ForeignKey(
        Class, on_delete=models.CASCADE, help_text="Class", verbose_name="Class"
    )
    section_teacher = models.OneToOneField(
        "Teacher",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Section Teacher",
    )
    seat = models.PositiveIntegerField(default=0)
    subjects = models.ManyToManyField(Subject, through="SectionSubject")

    def __str__(self):
        return f"{self.class_name} - Section {self.name}"

    class Meta:
        verbose_name_plural = "Sections"
        unique_together = ("name", "class_name")


class Student(models.Model):
    BLOOD_GROUP_CHOICES = (
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("O+", "O+"),
        ("O-", "O-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
    )

    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )

    RELIGION_CHOICES = (
        ("M", "Muslim"),
        ("H", "Hindu"),
        ("C", "Christian"),
        ("B", "Buddhist"),
        ("O", "Others"),
    )
    student_id = models.CharField(
        max_length=9,
        primary_key=True,
        unique=True,
        null=False,
        blank=False,
        verbose_name="Student ID",
        help_text="Student ID, e.g. 20190001",
    )
    # student info
    name_en = models.CharField(
        max_length=255,
        verbose_name="Name (EN)",
        help_text="Student's full name in English",
    )
    name_bn = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Name (BN)",
        help_text="Student's name in Bangla",
    )
    date_of_birth = models.DateField(
        verbose_name="Date of Birth", null=True, blank=True
    )
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=True, blank=True
    )
    religion = models.CharField(
        max_length=1, choices=RELIGION_CHOICES, null=True, blank=True
    )
    blood_group = models.CharField(
        max_length=3,
        choices=BLOOD_GROUP_CHOICES,
        verbose_name="Blood Group",
        null=True,
        blank=True,
    )
    birth_certificate_no = models.CharField(
        max_length=17,
        verbose_name="Birth Certificate Number",
        unique=True,
        null=False,
        blank=True,
    )

    # student contact info
    phone = models.CharField(
        max_length=11, verbose_name="Phone Number", null=True, blank=True
    )
    email = models.EmailField(null=True, blank=True)

    # father's info
    fathers_name_en = models.CharField(
        max_length=255, verbose_name="Father's Name (EN)", null=True, blank=True
    )
    fathers_name_bn = models.CharField(
        max_length=255, verbose_name="Father's Name (EN)", null=True, blank=True
    )
    fathers_nid = models.CharField(
        max_length=17, unique=True, verbose_name="Father's NID", null=True, blank=True
    )
    fathers_occupation = models.CharField(max_length=255, null=True, blank=True)
    fathers_phone = models.CharField(max_length=11, null=True, blank=True)

    # mother's info
    mothers_name_en = models.CharField(
        max_length=255, verbose_name="Mother's Name (EN)", null=True, blank=True
    )
    mothers_name_bn = models.CharField(
        max_length=255, verbose_name="Mother's Name (BN)", null=True, blank=True
    )
    mothers_nid = models.CharField(
        max_length=17, verbose_name="Mother's NID", unique=True, null=True, blank=True
    )
    mothers_occupation = models.CharField(max_length=255, null=True, blank=True)
    mothers_phone = models.CharField(max_length=11, null=True, blank=True)

    # address
    present_address = models.TextField(null=True, blank=True)
    permanent_address = models.TextField(null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)

    # school info
    admission_date = models.DateField(null=True, blank=True)
    admission_class = models.ForeignKey(
        Class, on_delete=models.PROTECT, null=True, blank=True
    )
    image = models.ImageField(upload_to="student_photo", null=True, blank=True)

    # other info
    comment = models.TextField(
        help_text="eg: any record about that student", null=True, blank=True
    )

    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name_plural = "Students"
        unique_together = ("student_id", "birth_certificate_no")


class Teacher(models.Model):
    BLOOD_GROUP_CHOICES = (
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("O+", "O+"),
        ("O-", "O-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
    )

    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )

    RELIGION_CHOICES = (
        ("M", "Muslim"),
        ("H", "Hindu"),
        ("C", "Christian"),
        ("B", "Buddhist"),
        ("O", "Others"),
    )

    teacher_id = models.CharField(
        max_length=9,
        primary_key=True,
        unique=True,
        verbose_name="Teacher ID",
        null=False,
        blank=False,
        help_text="Teacher ID, e.g. 20190001",
    )

    # teacher info
    name_en = models.CharField(max_length=255)
    name_bn = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=True, blank=True
    )
    religion = models.CharField(
        max_length=1, choices=RELIGION_CHOICES, null=True, blank=True
    )
    blood_group = models.CharField(
        max_length=3, choices=BLOOD_GROUP_CHOICES, null=True, blank=True
    )

    nid = models.CharField(max_length=17, null=False, blank=True)

    # teacher contact info
    phone = models.CharField(max_length=11, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    # address
    present_address = models.TextField(null=True, blank=True)
    permanent_address = models.TextField(null=True, blank=True)

    # school info
    joining_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to="teacher_photo", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name_plural = "Teachers"
        unique_together = ("teacher_id", "nid")


class SectionSubject(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    period = models.IntegerField(
        default=0, validators=[MaxValueValidator(10), MinValueValidator(0)]
    )
    time = models.TimeField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["period"]
        unique_together = ("teachers", "section", "period")

    def __str__(self):
        return f"{self.section} - {self.subject.title} - {self.teachers.name_en}"


# student assign to section and class roll model
class StudentAssign(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name="student_assign",
    )
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name="section"
    )
    class_roll = models.CharField(max_length=3, null=True, blank=True)

    class Meta:
        unique_together = ("section", "class_roll")

    def __str__(self):
        return f"{self.student} - {self.section} ({self.class_roll})"

# student attendance model
class Attendance(models.Model):
    student_assign = models.ForeignKey(
        StudentAssign, on_delete=models.CASCADE, related_name="student_attendance",
    )
    date = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date"]

    unique_together = ("student", "date")

    def __str__(self):
        return f"{self.student} - {self.date} ({self.status})"

"""
Exam Model
for handling exam related data
"""
    
class Exam(models.Model):
    EXAM_CHOICES = (
        ("Half Yearly", "Half Yearly"),
        ("Final", "Final"),
        ("Test", "Test"),
        ("Pre-Test", "Pre-Test")
    )

    exam_title = models.CharField(max_length=255, choices=EXAM_CHOICES)
    exam_date = models.DateField(null=True, blank=True)
    exam_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.exam_title

class ExamAssign(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    subject = models.ForeignKey(SectionSubject, on_delete=models.CASCADE)
    question_paper = models.FileField(upload_to="question_paper", null=True, blank=True)
    full_mark = models.IntegerField(
        default=0, validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    pass_mark = models.IntegerField(
        default=0, validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    exam_date = models.DateField(null=True, blank=True)
    exam_time = models.TimeField(null=True, blank=True)

    class Meta:
        unique_together = ("exam", "section", "subject")

    def __str__(self):
        return f"{self.exam} - {self.section} - {self.subject}"

class Result(models.Model):
    student_assign = models.ForeignKey(StudentAssign, on_delete=models.CASCADE)
    exam_assign = models.ForeignKey(ExamAssign, on_delete=models.CASCADE)