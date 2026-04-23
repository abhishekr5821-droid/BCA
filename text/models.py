from django.db import models


# ✅ YOUR ORIGINAL MODEL (UNCHANGED)
class Timetable(models.Model):
    day = models.CharField(max_length=20)
    period = models.IntegerField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.day} - {self.period} - {self.subject}"


# ✅ MERGED SYLLABUS MODEL (OLD + NEW COMBINED)
class Syllabus(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='syllabus_files/', blank=True, null=True)

    def __str__(self):
        return self.title