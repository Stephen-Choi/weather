# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from decimal import Decimal
from django.db import models

# Create your models here.
class Weather(models.Model):
	event = models.CharField(max_length=500, default="none")
	location = models.CharField(max_length=500, default="none")
	conditions = models.BooleanField()
	morn_temp = models.DecimalField(max_digits=4, decimal_places=2, default=Decimal('0.00'))
	day_temp =  models.DecimalField(max_digits=4, decimal_places=2, default=Decimal('0.00'))
	night_temp = models.DecimalField(max_digits=4, decimal_places=2, default=Decimal('0.00'))
	date = models.DecimalField(max_digits=12, decimal_places=1, default=Decimal('0.0'))

	def __str__(self):
		return self.event


