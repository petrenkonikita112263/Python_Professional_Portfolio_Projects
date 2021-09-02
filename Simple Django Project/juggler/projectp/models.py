from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Project(models.Model):
    name = models.CharField(max_length=80, help_text="The title of the project.")
    description = models.TextField(help_text="Project description.")
    progress = models.IntegerField(help_text="The progress bar value",
                                   default=0, validators=[MaxValueValidator(100)])
    members = models.IntegerField(help_text="The number of people is working on thr project",
                                  default=0, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=30, help_text="The task title for the project.")
    info = models.TextField(null=True, help_text="Additional info about the task.")
    created_date = models.DateField(auto_now_add=True, verbose_name="The date the task was created.")
    status = models.BooleanField(default=False, verbose_name="The task is finished or not.")
    closed_date = models.DateField(verbose_name="The date the task was completed.")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
