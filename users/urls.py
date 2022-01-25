from django.urls import path
from .views import loginuser, admin_registration, logoutuser, add_new_staff, add_new_customer
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login', loginuser, name='login'),
    path('admin_signup/', admin_registration, name='admin_signup'),
    path('add_new_staff/', add_new_staff, name='add_new_staff'),
    path('add_new_customer/', add_new_customer, name='add_new_customer'),
    path('logout/', logoutuser, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
