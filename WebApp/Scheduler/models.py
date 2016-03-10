from __future__ import unicode_literals

from django.db import models

class ScheduleObject(models.Model):
	start_time = models.IntegerField(default=0)
	end_time = models.IntegerField(default=0)