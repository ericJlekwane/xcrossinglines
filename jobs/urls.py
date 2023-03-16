from django.urls import path, include


from . import views


urlpatterns = [
        
        # // retrieve all bookings TESTED AND WORKS 
        path("staff/get/", views.JobsGETALLCustomerListAPIVIEW.as_view(), name = "staff-customer-jobs"),
        
        # ... customer request their own bookings 
        path("get/", views.JobsGETCustomerListAPIVIEW.as_view(), name="get-customer-jobs"),
        
        # .. get customer job 
        path("get/<int:pk>/", views.GetJobAPIView.as_view(), name="get-customer-job"),
        
        # ... generate quote 
        path("job/generate-quote/", views.GenerateQuoteAPIVIEW.as_view(), name="generate-quote"),
        
        # ... customer create Job 
        path("job/create/", views.JobCustomerCreateAPIVIEW.as_view(), name="create-customer-job"),
        
        # ... customer update job  
        path("job/update/<int:pk>/", views.JobCustomerUpdateAPIVIEW.as_view(), name="create-customer-job"),

        # ... generate distance apiview 
        path("compute-distance/", views.GenerateDistanceAPIVIEW.as_view(), name="compute-distance")

]
