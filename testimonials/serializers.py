from rest_framework.serializers import ModelSerializer, SerializerMethodField, ImageField
from rest_framework import serializers
from rest_framework.authentication import get_user_model

# ... import model 
from .models import Testimonial

# ... foreign serializers 
from accounts.serializers import AccountSerializer


# serializer 
class TestimonialSerializer(ModelSerializer):
    
    # .. get full customer profile 
    customer = serializers.SerializerMethodField(read_only = True)
    
    # ... 
    class Meta: 
        model = Testimonial
        fields = [
            "id",
            "customer",
            "testimonial",
            "service_rating",
            "created_at",
            "updated_at",
        ]
        
        # ... we need to get full customer profile 
    def get_customer(self, obj):
        
        # check booking instance 
        if(isinstance(obj.customer, get_user_model())):
            # .. convert this to string 
            serializeAccount = AccountSerializer(obj.customer, many= False)
            #//
            return serializeAccount.data 
        
        return None