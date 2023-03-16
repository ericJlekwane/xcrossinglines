from django.contrib import admin

# ... register 
from .models import FAQ


# ... 
admin.site.register(FAQ)