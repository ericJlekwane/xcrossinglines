from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.authentication import get_user_model

# app imports 
from .managers import AccountManager

#// account 
class Account(AbstractBaseUser, PermissionsMixin):
    
    #// unique customer id
    id = models.AutoField(primary_key=True)
    
    #// fields 
    email = models.EmailField(_('email address'), unique = True)
    f_name = models.CharField(max_length=150, null = True, default="") #// first name 
    s_name = models.CharField(max_length=150, null = True, default="") #// last name 
    m_number = models.CharField(max_length=50, null= True, blank= True, default="")
    
    #// date time fields 
    d_joined = models.DateTimeField(default=timezone.now)
    d_updated = models.DateTimeField(auto_now=True)
    
    #// boolean fields 
    is_active = models.BooleanField(default=True)
    verified = models.BooleanField(default=True)
    did_accept_ts_cs = models.BooleanField(default=True)
    
    #// determine whos registering 
    is_staff = models.BooleanField(default=False)
    customer = models.BooleanField(default=False)
    driver = models.BooleanField(default=False)
    
    
    #... set upfields 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["f_name", "s_name", "m_number"]
    
    #... override managers
    objects = AccountManager()
    
    #//set 
    def __str__(self):
        return f"{self.f_name} {self.s_name}, pk = {self.id}"

#// account profile
class AccountProfile(models.Model):
    
    #// unique customer id
    id = models.AutoField(primary_key=True, unique=True)
    
    #... refferal code 
    referal_code = models.CharField(max_length=150, unique=True) 
    
    #// 
    account = models.OneToOneField(get_user_model(),
                                    on_delete=models.CASCADE,
                                                        null=True)
    
    id_number = models.PositiveBigIntegerField(null=True, blank=True)
    
    
    use_crossing_lines_for = models.CharField(max_length=150,null = True, 
                                                blank=True, default='private')
    
 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    #//set 
    def __str__(self):
        return f"{self.account.f_name} {self.account.s_name}, pk = {self.account.id}"
