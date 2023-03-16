
# .. 3rd party packages
from rest_framework.serializers import ModelSerializer, SerializerMethodField, ImageField
from rest_framework import serializers
from rest_framework.authentication import get_user_model

#.. models 
from .models import Account, AccountProfile

#... 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# serializers 
class SignupSerializer(ModelSerializer):
    
    #// create meta class 
    class Meta: 
        model= Account
        fields = ('email', 
                'f_name', 
                's_name',
                'm_number', 
                'password', 
                'customer', 
                'driver', 
                'is_staff',)
        extra_kwargs = {'password': {'write_only': True}}
        
    #// create password 
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
# new account serializer 
class AccountSerializer(ModelSerializer):
    
    class Meta: 
        model = Account
        fields = "__all__"
        
        
class AccountUpdateSerializer(ModelSerializer):
    
    class Meta:
        model = Account
        fields = ['f_name', 's_name', 'm_number',]


# ... 
class AccountProfileSerializer(ModelSerializer):
    
    class Meta:
        model = AccountProfile
        fields = "__all__"  
        
#// custom JWT TOKEN SERIALIZER
class SigninTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, account):
        # ...
        token = super().get_token(account)
        _type = type(None)
        # ///
        aProfile = AccountProfile\
                        .objects\
                        .get(account = account)
                        
        #.. retrieve refferal code 
        referal_code = "None"
        if(isinstance(aProfile, AccountProfile)):
            referal_code = aProfile.referal_code
            
                  
        #... check if profile is incomplete 
        profile_complete = False
        if(isinstance(account.f_name, str) 
            and isinstance(account.s_name, str) 
                and isinstance(account.m_number, str)):
            
            # check if they are populated 
            if(len(f"{account.f_name}")>0 
                and len(f"{account.s_name}")>0 
                    and len(f"{account.m_number}") > 0): 
                
                # .. then the profile is complete 
                                
                # .. then the profile is complete 
                print(len(f"{account.f_name}")>0, "length of f_name")
                print(len(f"{account.s_name}")>0, "length of s_name")
                print(len(f"{account.m_number}") > 0,  "length of m_number: ", f"{account.m_number}")
                profile_complete = True 
            else: 
                profile_complete = False 

        #// here we add 
        token["f_name"] = account.f_name
        token["s_name"] = account.s_name
        token["referal_code"] = referal_code
        token["p_incomplete"] = profile_complete
        token["driver"] = account.driver
        token["is_staff"] = account.is_staff
        # token['image'] = aProfile.image.url
    
        return token 
            

    
