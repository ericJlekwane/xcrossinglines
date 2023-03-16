
# third party
from django.conf import settings as _set
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
import uuid

        
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse

from django_rest_passwordreset.signals import reset_password_token_created

# .. models 
from .models import AccountProfile
from referals.models import Referal

# create signal  _set.AUTH_USER_MODEL
@receiver(post_save, sender = _set.AUTH_USER_MODEL)
def create_auth_token(sender, instance = None, created = False, **kwargs):
    
    # create token when user registers 
    if created:
        #Token.objects.create(user = instance)
        # we need to create user profile 
        try:
            #//generate uuid 
            referal_code = "{0}-{1}XCL"\
                    .format(str(uuid.uuid4())[:8], instance.id)\
                    .lower()
            
            #// create Account Profile
            AccountProfile\
                .objects\
                .create(account = instance,  
                        referal_code = referal_code)
                
            #// create Refferal Column
            Referal\
                .objects\
                .create(account = instance, 
                        referal_code = referal_code)
            
            #....
        except Exception as e:
            raise ValueError(e)
        
    


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    
    value = "{}?token={}".format(
            instance.request.build_absolute_uri(reverse('password_reset:reset-password-confirm')),
            reset_password_token.key)
    
    print("CHECK THE URL OUT = ", value)
    # send an e-mail to the user
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.f_name,
        'email': reset_password_token.user.email,
        'reset_password_url': "{}?token={}".format(
            instance.request.build_absolute_uri(reverse('password_reset:reset-password-confirm')),
            reset_password_token.key)
    }

    print("THIS IS THE CONTEXT: ", context)
    # # render email text
    # email_html_message = render_to_string('email/user_reset_password.html', context)
    # email_plaintext_message = render_to_string('email/user_reset_password.txt', context)

    # msg = EmailMultiAlternatives(
    #     # title:
    #     "Password Reset for {title}".format(title="Some website title"),
    #     # message:
    #     email_plaintext_message,
    #     # from:
    #     "noreply@somehost.local",
    #     # to:
    #     [reset_password_token.user.email]
    # )
    # msg.attach_alternative(email_html_message, "text/html")
    # msg.send()

