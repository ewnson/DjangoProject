from django.db import models

class Contacts(models.Model):
    # name of contact
    name = models.CharField(max_length=255, null=False)
    # number of contact
    number = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.name, self.number)

class BaseModel(models.Model):

    class Meta:
        abstract = True  # specify this model as an Abstract Model
        app_label = 'quickstart'