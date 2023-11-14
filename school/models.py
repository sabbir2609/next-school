import datetime

from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Subject(models.Model):
    title = models.CharField(max_length=255, help_text="Subject Name", unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Subjects"


class Class(models.Model):
    class ClassChoices(models.TextChoices):
        CLASS_6 = "6", _("Class 6")
        CLASS_7 = "7", _("Class 7")
        CLASS_8 = "8", _("Class 8")
        CLASS_9 = "9", _("Class 9")
        CLASS_10 = "10", _("Class 10")

    title = models.CharField(
        max_length=8, choices=ClassChoices.choices, primary_key=True
    )
    slug = models.SlugField(unique=True, blank=True, null=True)
    teacher = models.ForeignKey(
        "Teacher",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Class Teacher",
    )
    description = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        help_text="eg: Class 6, total 120 students, 4 sections, 30 students in each section",
        default="",
    )

    def __str__(self):
        return f"Class {self.title}"

    class Meta:
        verbose_name_plural = "Classes"
        ordering = ("title",)


class Section(models.Model):
    SECTION_CHOICES_CLASS_6_7_8 = [
        ("A", "Section A"),
        ("B", "Section B"),
        ("C", "Section C"),
    ]

    SECTION_CHOICES_CLASS_9_10 = [
        ("Sc", "Science"),
        ("Co", "Commerce"),
        ("Ar", "Arts"),
    ]

    class_name = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        help_text="Class",
        verbose_name="Class",
    )

    name = models.CharField(
        max_length=2,
        verbose_name="Section",
        choices=SECTION_CHOICES_CLASS_6_7_8 + SECTION_CHOICES_CLASS_9_10,
    )
    description = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Section Description, e.g. Section A of Class 6, total 30 students ",
    )

    teacher = models.ForeignKey(
        "Teacher",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Section Teacher",
    )
    seat = models.PositiveIntegerField(default=45)
    subjects = models.ManyToManyField(Subject, through="SectionSubject")

    def clean(self):
        # Check your validation conditions and raise ValidationError if needed
        if self.name in ("Ar", "Co", "Sc") and self.class_name.title not in ("9", "10"):
            raise ValidationError(f"'{self.get_name_display()}' can only be applied to classes 'Nine' and 'Ten'")

        if self.name in ("A", "B", "C") and self.class_name.title in ("9", "10"):
            raise ValidationError(f"'{self.get_name_display()}' can only be applied to classes 'Six', 'Seven', and 'Eight'")

    def save(self, *args, **kwargs):
        # Run full clean to trigger the custom clean method
        self.full_clean()

        # Proceed with the normal save process
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.class_name} - Section {self.name}"

    class Meta:
        verbose_name_plural = "Sections"
        unique_together = ("name", "class_name")


class Guardian(models.Model):
    FATHER = "Father"
    MOTHER = "Mother"
    OTHER = "Guardian"

    RELATION_CHOICES = [
        (FATHER, "Father"),
        (MOTHER, "Mother"),
        (OTHER, "Guardian"),
    ]

    name_en = models.CharField(max_length=50)
    name_bn = models.CharField(max_length=50, null=True, blank=True)
    nid = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to="guardian", blank=True, null=True)
    relation = models.CharField(max_length=8, choices=RELATION_CHOICES, default=OTHER)

    def __str__(self):
        return f"{self.name_en}"


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

    guardian = models.OneToOneField(
        Guardian,
        on_delete=models.CASCADE,
        related_name="guardian",
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name_plural = "Students"
        unique_together = ("student_id", "birth_certificate_no")
        ordering = ("-created_at",)


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
    photo = models.ImageField(
        upload_to="teacher_photo",
        null=True,
        blank=True,
        help_text="Recommended: Upload 1:1 ratio image",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name_plural = "Teachers"
        unique_together = ("teacher_id", "nid")
        ordering = ("-created_at",)


class SectionSubject(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    period = models.IntegerField(
        unique=True, default=0, validators=[MaxValueValidator(10), MinValueValidator(0)]
    )
    time = models.TimeField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["period"]
        unique_together = ("teacher", "section", "period")

    def __str__(self):
        return f"{self.section} - {self.subject.title} - {self.teacher.name_en}"


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
    student = models.ForeignKey(
        StudentAssign,
        on_delete=models.CASCADE,
        related_name="attendance_student",
    )
    date = models.DateField(default=datetime.date.today)
    status = models.BooleanField(default=False)

    def clean(self):
            # Check if the day of the week is not Friday (where Monday is 0 and Sunday is 6)
            if self.date.weekday() == 4:
                raise ValidationError({'date': ["Attendance record cannot be created on Fridays."]})

    def save(self, *args, **kwargs):
        self.clean()  # Call the clean method before saving
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["date"]
        unique_together = ("student", "date")

    def __str__(self):
        return f"{self.student} - {self.date} ({self.status})"


# Exam model
class Exam(models.Model):
    EXAM_CHOICES = (
        ("Half Yearly", "Half Yearly"),
        ("Year Final", "Year Final"),
        ("Pretest", "Pretest"),
        ("Test", "Test"),
    )

    exam_type = models.CharField(max_length=20, choices=EXAM_CHOICES)
    year = models.CharField(max_length=4)
    date = models.DateField(default=datetime.date.today)

    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.exam_type} - {self.year}"


class ExamSubject(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.class_name} - {self.subject}"


class ExamAssign(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject = models.ForeignKey(ExamSubject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.PROTECT, null=True, blank=True
    )
    question_paper = models.FileField(upload_to="question_paper", null=True, blank=True)

    full_mark = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    pass_mark = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    exam_time = models.TimeField(null=True, blank=True, help_text="Exam Time")

    class Meta:
        ordering = ["exam", "subject"]
        unique_together = ("exam", "subject")

    def __str__(self):
        return f"{self.exam} || {self.subject}"


class StudentResult(models.Model):
    exam_assign = models.ForeignKey(
        ExamAssign, on_delete=models.CASCADE, help_text="Exam Assign"
    )
    student_assign = models.ForeignKey(
        StudentAssign, on_delete=models.CASCADE, help_text="Student Assign"
    )

    # obtained marks
    mcq_mark = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    written_mark = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    practical_mark = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(100), MinValueValidator(0)]
    )

    def clean(self):
        if (
            self.mcq_mark + self.written_mark + self.practical_mark
            > self.exam_assign.full_mark
        ):
            raise ValidationError("Total marks can't be greater than full marks")

    class Meta:
        unique_together = ("exam_assign", "student_assign")

    def __str__(self):
        return f"{self.exam_assign} || {self.student_assign}"
