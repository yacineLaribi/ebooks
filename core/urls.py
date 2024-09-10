from django.urls import path 
from .views import home , signup , login_user , logout_view , soon , termsOfUse

app_name = 'core'

urlpatterns = [
    path('',home,name='index'),

    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'),
    path('logout/',logout_view,name='logout'),
    path('soon/',soon,name='soon'),
    path('terms/',termsOfUse,name='terms'),

]
