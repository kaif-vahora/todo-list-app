from django.db import models

# Create your models here.
class Project(models.Model):
    project_name =models.CharField(max_length=30)
    project_description =models.TextField()
    class Meta:
        db_table = 'project'




