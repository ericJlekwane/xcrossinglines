from rest_framework.serializers import ModelSerializer, SerializerMethodField, ImageField
from rest_framework import serializers

# ... models 
from rest_framework.authentication import get_user_model
from .models import Route, Job
from accounts.models import AccountProfile, Account

# ... external serializers 
from accounts.serializers import AccountProfileSerializer, AccountSerializer

# .. serializers 
class JobsGetCustomerSerializer(ModelSerializer):
    
    # .. customer 
    customer = serializers.SerializerMethodField(read_only = True)
    driver = serializers.SerializerMethodField(read_only = True)
    routes = serializers.SerializerMethodField(read_only = True)

    # meta 
    class Meta: 
        model = Job
        # fields = "__all__"
        fields = [
            "id",
            "customer",
            "driver",
            "job_canceled",
            "job_completed",
            "helpers",
            "floors",
            "referal_discount",
            "vehicle_size",
            "payment_option",
            "driver_note",
            "service_rating",
            "quote",
            "middle_month_discount",
            "distance",
            "routes",
            "job_date",
            "job_time",
            "created_at",
            "updated_at",
        ]
        
    # ... we need to get full customer profile 
    def get_customer(self, obj):
        
        # payload = {}
        
        # # get request 
        # request = self.context.get("request") or None
        
        # check booking instance 
        if(isinstance(obj.customer, get_user_model())):
            
            # ... lets find the profile 
            aProfile = AccountProfile\
                        .objects.get(
                        account = obj.customer)
            
            # ... seralize this 
            sAccountProfile = AccountProfileSerializer(aProfile, many = False)
            sAccount = AccountSerializer(obj.customer, many = False)
            
            # // 
            sAccountJson = sAccount.data
            sAccountJson["account-profile"] = sAccountProfile.data
            
            #//
            return sAccountJson 
        
        return None
    
    # ... we need to get full customer profile 
    def get_driver(self, obj):

        # check booking instance 
        if(isinstance(obj.driver, get_user_model())):
            
            # ... lets find the profile 
            aProfile = AccountProfile\
                        .objects.get(
                        account = obj.customer)
            
            # ... seralize this 
            sAccountProfile = AccountProfileSerializer(aProfile, many = False)
            sAccount = AccountSerializer(obj.customer, many = False)
            
            # // 
            sAccountJson = sAccount.data
            sAccountJson["account-profile"] = sAccountProfile.data
            
            #//
            return sAccountJson 
        
        return None
    
    # get routes 
    def get_routes(self, obj):
        
        # ---simplified version
        return [{"lat": a.lat, 
                    "lng": a.lng, 
                        "route_name": a.route_name} 
                            for a in obj.routes.all()]
        

# ... create Serializer 
class JobCreateSerializer(ModelSerializer):
    
    class Meta: 
        model = Job
        fields = (
            "customer",
            "helpers",
            "floors",
            "vehicle_size",
            "payment_option",
            "driver_note",
            "quote",
            "referal_code",
            "referal_discount",
            "middle_month_discount",
            "distance",
            "job_canceled",
            "job_date",
            "job_time",
     
        )
        

class GenenerateQuoteSerializer(ModelSerializer):
    pass
        
        
# ... Update Serializer 
class JobUpdateSerializer(ModelSerializer):
    
    class Meta: 
        model = Job
        fields = (
            "customer",
            "helpers",
            "floors",
            "vehicle_size",
            "payment_option",
            "driver_note",
            "quote",
            "middle_month_discount",
            "distance",
            "job_canceled",
            "job_date",
            "job_time",
     
        )