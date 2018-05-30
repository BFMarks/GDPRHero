# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from quickstart.models import models

class TaskHistoryAdminModel(admin.ModelAdmin):
    list_display = (“name”,)
    class Meta:
        models.TaskHistory
admin.site.register(models.TaskHistory, TaskHistoryAdminModel)
 