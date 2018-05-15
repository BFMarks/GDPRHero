from django.contrib import admin

# Register your models here.
from .models import Snippet
from .models import Profile
from .models import InboundEmail

admin.site.register(Snippet),
admin.site.register(Profile),
admin.site.register(InboundEmail)
