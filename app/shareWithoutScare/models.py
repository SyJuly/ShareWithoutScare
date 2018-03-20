# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Friend(models.Model):
    name = models.CharField(max_length=40)
    birthday = models.DateTimeField()
    title = models.CharField(max_length=60)

    def __str_(self):
        return self.name
