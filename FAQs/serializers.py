from rest_framework.serializers import ModelSerializer

# .. models 
from .models import FAQ


# //serializer 
class FAQsSerializer(ModelSerializer):

    # .. 
    class Meta: 
        model = FAQ
        fields = "__all__"