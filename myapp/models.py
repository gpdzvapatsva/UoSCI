from django.db import models

"""
myapp.models
------------
Model definitions for the myapp application.

Models:
- Students: represents a student record with first name, surname,
  numeric student identifier and enrolled course.

Notes:
- See the generated migration for the initial schema:
  [myapp/migrations/0001_initial.py](myapp/migrations/0001_initial.py)
"""

class Students(models.Model):
    """
    A single student record.

    Fields
    - firstname: given name (max 20 chars)
    - surname: family name (max 20 chars)
    - student_id: integer student identifier (as stored in the DB)
    - course: name of the enrolled course (max 20 chars)

    Usage:
        students = Students.objects.all()
        for s in students:
            print(s.get_full_name())
    """
    firstname = models.CharField("first name", max_length=20, help_text="Student's given name")
    surname = models.CharField("surname", max_length=20, help_text="Student's family name")
    student_id = models.IntegerField("student id", help_text="Numeric identifier assigned to the student")
    course = models.CharField("course", max_length=20, help_text="Enrolled course name")

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['surname', 'firstname']

    def __str__(self) -> str:
        """
        Human-readable representation used throughout Django admin and templates.
        """
        return f"Student #{self.id} — {self.firstname} {self.surname} (SID: {self.student_id}) — {self.course}"

    def get_full_name(self) -> str:
        """Return the student's full name as 'Firstname Surname'."""
        return f"{self.firstname} {self.surname}"