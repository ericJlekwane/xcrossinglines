from django.db import models
from rest_framework_simplejwt.authentication import get_user_model


# create referals model 
class Referal(models.Model):
    
    #... unique id 
    id = models.AutoField(primary_key=True)
    account = models.OneToOneField(get_user_model(),
                                    on_delete=models.CASCADE,
                                                        null=True)
    
    #.. referal code and potential refferal discount 
    referal_code = models.CharField(max_length=150, unique=True) 
    referal_discount = models.FloatField(default = 0.0, 
                                            null = True, blank = True)
    
    # .. date fields 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    #.. override the string function 
    def __str__(self):
        return f"{self.account.f_name}-({self.referal_code})"

    
    