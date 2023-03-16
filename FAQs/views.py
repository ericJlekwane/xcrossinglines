from rest_framework import generics 
from rest_framework.permissions import AllowAny, IsAuthenticated
# .. import model 
from .models import FAQ

# ... serializers 
from .serializers import FAQsSerializer

# //views 
class FAQsGetListAPIVIEW(generics.ListAPIView):
    
    # ...  
    queryset = FAQ.objects\
                .all()\
                .order_by("-created_at")
    serializer_class = FAQsSerializer
    permission_classes = [AllowAny,]
