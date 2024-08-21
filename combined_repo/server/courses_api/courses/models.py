from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    course_code = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return f"{self.course_code} - {self.title}"

class CourseInstance(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    year = models.IntegerField()
    semester = models.IntegerField()

    class Meta:
        unique_together = ('course', 'year', 'semester')

    def __str__(self):
        return f"{self.course.title} ({self.year} - Semester {self.semester})"