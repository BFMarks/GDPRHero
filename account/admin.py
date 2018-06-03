from django.contrib import admin

# Register your models here.
from .models import Apps
from .models import DataProcessors


admin.site.register(Apps),
admin.site.register(DataProcessors),
