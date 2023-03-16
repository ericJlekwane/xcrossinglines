from django.db.models.signals import post_save, pre_delete, pre_save 
from django.dispatch import receiver

# ... import models 
from .models import Job, Route

# .. utils 
from .g_quote import GenerateQuote

 
# ... is executed at the end
#  .. of the save method
@receiver(post_save, sender = Job)
def updated_job(sender, instance = None, created = False, **kwargs):

    if(created):
        print("NEW RECORD WAS CREATED")


#  .. executed at the beginning
#  .. of the save method
@receiver(pre_save, sender = Job)
def before_saved(sender, instance, *args, **kwargs):
    
    # ... check correct instance
    if(isinstance(instance, Job)):
        
        # .. compute distance 
        dStance = float("%.0f"%instance.distance)
    
        # .. generate instance 
        gQuoteClass = GenerateQuote(
                        distance = dStance,
                        floors = instance.floors,
                        helpers = instance.helpers,
                        vSize = instance.vehicle_size,
                        job_date = instance.job_date)
    
        # .. generated quote 
        quote, dPeak = gQuoteClass.base_discounts

        # .. set 
        instance.quote = float("%.0f"%quote) 
        instance.distance = float("%.0f"%dStance)
        instance.middle_month_discount = float("%.0f"%dPeak) 


