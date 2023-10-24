from django.db import models

# Create your models here.
# model => python class
# model represents a table in the db
# attributes are the fields in the table

# job posting table
## title, description, company, salary

class JobPosting(models.Model):
    # id - starts at 1 and autoincrements
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    is_Active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} | {self.company} | {self.is_Active}"

# makemigrations (Doesn't affect the db)
## -> creates instructions telling django how the db have changed
# migrate (affects the db)
##  -> applies the above changes to db

# CRUD
# create
# read
# update
# delete

# model manager -> objects
# JobPosting.objects.all() - Selects all the objects in the database
# JobPosting.objects.get(id=1) - can specify id to get which row you want
# JobPosting.objects.filter(title="job title"), JobPosting.objects.filter(company="Rakuten")

