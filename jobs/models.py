from django.db import models
from rest_framework.authentication import get_user_model
from django.utils.translation import gettext_lazy as _


# .. create route model 
class Route(models.Model):

    # stop skipping 
    id = models.AutoField(primary_key=True)
    
    # ... route details 
    route_name = models.CharField(default = '', max_length = 400, null=True, blank=True)
    lat =  models.DecimalField(max_digits=35, decimal_places=30, null=True, blank=True)
    lng =  models.DecimalField(max_digits=35, decimal_places=30, null=True, blank=True)
    
    # date fields 
    created_at = models.DateTimeField(auto_now_add= True)
      
    
    
# .. create Job Model 
class Job(models.Model):
    
    # set 
    VSIZECHOICES = [(1.0, 1.0), (1.5, 1.5)]
    FLOORSCHOICES = [(f, f) for f in range(11)]
    HELPERCHOICES = [(h + 1, h + 1) for h in range(3)]
    
    
    # .. stop skipping 
    id = models.AutoField(primary_key=True)
    
    # .. personel 
    customer = models.ForeignKey(get_user_model(), 
                                on_delete=models.CASCADE,
                                related_name=_("customer_identity"), 
                                null=True)
    
    driver = models.ForeignKey(get_user_model(), 
                            on_delete=models.CASCADE,
                            related_name=_("driver_identity"),
                            null=True,
                            blank=True)
    
    # ... additional information 
    helpers = models.IntegerField(default = 1,
                                  choices=HELPERCHOICES, 
                                  null = True, 
                                  blank = True)
    floors = models.IntegerField(default = 0, 
                                 choices=FLOORSCHOICES,
                                 null = True, 
                                 blank = True)
    vehicle_size = models.FloatField(default = 1.0, 
                                     choices=VSIZECHOICES,
                                     null = True, 
                                     blank = True)
    payment_option = models.CharField(default = 'CASH', max_length = 50, null=True, blank=True)
    driver_note = models.TextField(default= 'No note left', max_length = 1000, null = True, blank = True)

    # ... customer feed back 
    service_rating = models.IntegerField(default = 0, blank = True)
    
    # ... referal code for discount 
    referal_code = models.CharField(max_length=150, null=True, blank=True, default="") 
    referal_discount = models.FloatField(default = 0.0, 
                                            null = True, blank = True)

    # ... job money 
    quote = models.FloatField(default = 0.0, null = True, blank = True)
    middle_month_discount = models.FloatField(default = 0.0, null = True, blank = True)
    distance = models.FloatField(default = 0.0, null = True, blank = True)
    
    # ... 
    routes = models.ManyToManyField(Route, blank = True)
    
    # ... booleans 
    job_completed = models.BooleanField(default=False, null = False, blank=False)
    job_canceled = models.BooleanField(default=False, null = False, blank=False)
    
    # .. date fields 
    job_date = models.DateField(null = True)
    job_time = models.TimeField(null = True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    # overide the string method 
    def __str__(self):
        return 'JOB INVOICE: {0}'.format(self.id)
      

