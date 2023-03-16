from multiprocessing.sharedctypes import Value
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


#// manager 
class AccountManager(BaseUserManager):
    
    user_in_migrations = True
    
    def create_user(self, email, f_name, 
                        s_name, password, 
                                        **other_fields):
        
        #//create check email
        if not email:
            raise TypeError(_('Please provide a valid email address'))
        
  
        #save
        email = self.normalize_email(str(email).lower())
        account = self.model(email = str(email).lower(),
                             f_name = str(f_name).capitalize(),         
                             s_name = str(s_name).capitalize(), 
                             **other_fields)
        
        #set the customer password 
        account.set_password(password)
        account.save(using = self._db)
        
     
        #//return account 
        return account
    
    #//create super user 
    def create_superuser(self, email, f_name,
                                s_name, password, 
                                            **other_fields):
        
        #// set default 
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('verified', True)
        
        #// raise exception if error found  
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to staff = true')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to superuser = true')
        if other_fields.get('is_active') is not True:
            raise ValueError('active must be assigned to active = true')
        if other_fields.get('verified') is not True:
            raise ValueError('verified must be set to verified = true')
        
        
        # create user 
        account = self.create_user(email, f_name, 
                                        s_name, password,
                                                **other_fields)
        
        #// return 
        return account
        