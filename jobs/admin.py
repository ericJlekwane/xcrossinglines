from django.contrib import admin

# .. models 
from .models import Job, Route


# .. register models 
admin.site.register(Job)
admin.site.register(Route)
