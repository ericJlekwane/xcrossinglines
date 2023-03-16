from django.db import models
from rest_framework.authentication import get_user_model
from django.utils.translation import gettext_lazy as _

# ... testimonanials 
class Testimonial(models.Model):
    
    # .. stop skipping 
    id = models.AutoField(primary_key=True)
    
        # .. personel 
    customer = models.ForeignKey(get_user_model(), 
                                on_delete=models.CASCADE,
                                related_name=_("testimonials_customer"), 
                                null=True)
    
    testimonial = models.TextField(default= 'awesome service', 
                                   max_length = 1000, 
                                   null = True, 
                                   blank = True)
    
    # ... customer feed back 
    service_rating = models.IntegerField(default = 0, blank = True)
    
    # .. date fields 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # overide the string method 
    def __str__(self):
        return 'Testimonial: {0}'.format(self.id)