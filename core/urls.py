from django.contrib import admin
from django.urls import path,include
from core import views
from django.contrib.auth import views as auth_view
from core.couriour import views as couriour_views
from core.customer import views as customer_views
from django.conf import settings
from django.conf.urls.static import static
customer_urlpatterns = [
    path('', customer_views.customer,name='home'),
    path('profile',couriour_views.profile_couriour,name='profile'),
    path('payment_method/',couriour_views.payment_method_page,name='payment_method'),
]
couriour_urlpatterns = [
    path('',couriour_views.couriour,name='home'),
    path('profile',couriour_views.profile_couriour,name='profile'),
    path('payment_method/',couriour_views.payment_method_page,name='payment_method'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base,name='base'),
    path('', include('social_django.urls', namespace='social')),
    path('sign_in/',auth_view.LoginView.as_view(template_name='sign_in.html')),
    path('sign_out/',auth_view.LogoutView.as_view(next_page='base')),
    path('sign_up/',views.sign_up,name='sign_up'),
   # path('signin/',views.signin,name='signin'),

    path('test/',views.test),
    path('customer/',include((customer_urlpatterns, 'customer'))),
    path('couriour/',include((couriour_urlpatterns, 'couriour'))),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)