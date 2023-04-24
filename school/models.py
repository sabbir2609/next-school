from django.db import models


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
        help_text="eg: 'Class 6, total 120 students, 4 sections, 30 students in each section'"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Classes"


class Section(models.Model):
    SECTION_CHOICES = (
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("Sc", "Science"),
        ("Co", "Commerce"),
        ("Ar", "Arts"),
    )
    title = models.CharField(max_length=2, choices=SECTION_CHOICES, primary_key=True)
    description = models.TextField(
        help_text="Section Description, e.g. 'Section A of Class 6, total 30 students'"
    )
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Sections"
        unique_together = ("title", "class_name")


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

    # student info
    name_bn = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=True, blank=True
    )
    religion = models.CharField(
        max_length=1, choices=RELIGION_CHOICES, null=True, blank=True
    )
    blood_group = models.CharField(
        max_length=3, choices=BLOOD_GROUP_CHOICES, null=True, blank=True
    )
    student_id = models.CharField(max_length=7, null=False, blank=True)
    birth_certificate_no = models.CharField(max_length=17, null=False, blank=True)

    # student contact info
    mobile_no = models.CharField(max_length=11, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    # father's info
    fathers_name_bn = models.CharField(max_length=255, null=True, blank=True)
    fathers_name_en = models.CharField(max_length=255, null=True, blank=True)
    fathers_nid = models.CharField(max_length=17, null=True, blank=True)
    fathers_occupation = models.CharField(max_length=255, null=True, blank=True)
    fathers_mobile_no = models.CharField(max_length=11, null=True, blank=True)

    # mother's info
    mothers_name_bn = models.CharField(max_length=255, null=True, blank=True)
    mothers_name_en = models.CharField(max_length=255, null=True, blank=True)
    mothers_nid = models.CharField(max_length=17, null=True, blank=True)
    mothers_occupation = models.CharField(max_length=255, null=True, blank=True)
    mothers_mobile_no = models.CharField(max_length=11, null=True, blank=True)

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

    # teacher info
    name_bn = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    dob = models.DateField(auto_now_add=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, null=True, blank=True
    )
    religion = models.CharField(
        max_length=1, choices=RELIGION_CHOICES, null=True, blank=True
    )
    blood_group = models.CharField(
        max_length=3, choices=BLOOD_GROUP_CHOICES, null=True, blank=True
    )

    teacher_id = models.CharField(max_length=7, null=False, blank=True)
    nid = models.CharField(max_length=17, null=False, blank=True)

    # teacher contact info
    mobile_no = models.CharField(max_length=11, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    # address
    present_address = models.TextField(null=True, blank=True)
    permanent_address = models.TextField(null=True, blank=True)

    # school info
    joining_date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to="teacher_photo", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_en

    class Meta:
        verbose_name_plural = "Teachers"
        unique_together = ("teacher_id", "nid")


class Subject(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Subjects"


class TeacherAssign(models.Model):
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="teacher"
    )
    subject = models.ManyToManyField(Subject, related_name="subject")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.teacher} - {self.subject} "

    class Meta:
        verbose_name_plural = "Teacher Assign"


class StudentAssign(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="student"
    )
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name="section"
    )
    class_roll = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return f"{self.student} - {self.section}"

    class Meta:
        verbose_name_plural = "Student Assign"
        unique_together = ("student", "section", "class_roll")


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} - {self.date}"

    class Meta:
        verbose_name_plural = "Attendances"


class Exam(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Exams"


class ExamAssign(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="exam")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    teacher = models.ManyToManyField(Teacher, related_name="exam_teacher")

    status = models.BooleanField(default=False)

    def __str__(self):
        return f" {self.exam} - {self.subject} - {self.section} "

    class Meta:
        verbose_name_plural = "Exam Assign"


class ExamAttendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} - {self.exam} - {self.date}"

    class Meta:
        verbose_name_plural = "Exam Attendances"


class ExamResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.PositiveSmallIntegerField()

    def __str__(self):
        return f" {self.student} - {self.exam} - {self.subject} "

    class Meta:
        verbose_name_plural = "Exam Results"
