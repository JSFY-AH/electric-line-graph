from django.db import models


class Line(models.Model):
    name = models.CharField(max_length=200)
    root_x = models.CharField(max_length=200, null=True)
    root_y = models.CharField(max_length=200, null=True)


class Node(models.Model):
    line_id = models.IntegerField(default=0)
    data = models.CharField(max_length=200)
    father_id = models.IntegerField(default=-1)
    node_type = models.IntegerField(default=0)
    X = models.CharField(max_length=200, null=True)
    Y = models.CharField(max_length=200, null=True)
    online = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
# Create your models here.
