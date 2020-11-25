from django.db import models
from datetime import datetime, date
from django import forms
# Inside your app's models.py file
from django.db import models

# Our custom manager!
# No methods in our new manager should ever receive the whole request object as an argument! 
# (just parts, like request.POST)
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "please fill the title field at least 2 char"
        else:
            for s in Show.objects.all():
               if postData['title'] == s.title:
                    errors["title"] = "please type another title"


        if len(postData['network']) < 3:
            errors["network"] = "please fill the network field at least 3 char"

        if len(postData['date']) < 1:
            errors["date"] = "please choose the date  past"
        else: 
            x = postData['date'].split("-")
            if  int(x[0]) > 2019:
                errors["date"] = "the date should be in the past"
        if len(postData['desc']) < 1:
            pass
        else:
            if len(postData['desc']) < 11:
            
                errors["desc"] = "please fill the description field at least 10 characters"


        # if len(postData['desc']) < 11:
        #     errors["desc"] = "please the description field"

        return errors


class DateInput (forms.DateInput):
    input_type = 'date'

class Show  (models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    relasDate = models.DateField()
    desc = models.CharField(max_length=255) 
    objects = BlogManager()


