from django.db import models


class Class(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Classes"


class Section(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f" {self.name} - {self.class_name} "

    class Meta:
        verbose_name_plural = "Sections"
        unique_together = ("name", "class_name")


class Parent(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Student(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Students"


class Teacher(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Teachers"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Subjects"


class TeacherAssign(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return f" {self.teacher} - {self.subject} "

    class Meta:
        verbose_name_plural = "Teacher Assign"


class StudentAssign(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.student} - {self.section} "

    class Meta:
        verbose_name_plural = "Student Assign"
        unique_together = ("student", "section")


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f" {self.student} - {self.date} "

    class Meta:
        verbose_name_plural = "Attendances"


class Exam(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Exams"


class ExamAssign(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return f" {self.exam} - {self.subject} - {self.section} "

    class Meta:
        verbose_name_plural = "Exam Assign"


class ExamResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.PositiveSmallIntegerField()

    def __str__(self):
        return f" {self.student} - {self.exam} - {self.subject} "

    class Meta:
        verbose_name_plural = "Exam Results"
