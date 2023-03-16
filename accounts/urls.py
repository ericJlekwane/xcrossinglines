from django.urls import path, include, re_path

# .. views 
from . import views


# .. return view 
urlpatterns = [
    
    # .. signup create C
    path("signup/", views.AccountCreateAPIVIEW.as_view(), name="signup-view"),
    
    # ... read R
    path("get/", views.AccountGetAPIVIEW.as_view(), name="account-get-view"),
    
    # ... update U
    path("update/", views.AccountUpdateAPIVIEW.as_view(), name = "update-view"),
    
    # .. delete view D
    path("delete/", views.DeleteAccountAPIVIEW.as_view(), name="delete-view"),
    
    #... SIGNIN
    path("signin/", views.SignInTokenObtainPairView.as_view(), name="signin-view"),
    path("signin/google/", views.GoogleRegisterLoginAPIView.as_view(), name="google-signin-view"),
    # path("signin/google", views.register_by_access_token, name="google-sigin-view"),
    #... signout 
    path("signout/blacklist/", views.SignOutAPIVIEW.as_view(), name="signout-view"),
    
    # //testing password reset 
    path('password/reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    
]