from django.db import models

# Note Model, represents one Note
class Note(models.Model):
    # title of Note should be up to 20 characters long
    title = models.CharField(max_length=20)
    # content of Note should be up to 250 characters long
    content = models.CharField(max_length=250)
