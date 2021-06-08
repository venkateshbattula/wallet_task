from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'users', views.UsersViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('addwalletdetails/<int:id>', views.addWalletForm, name='addwalletdetails'),
    path('changewalletstatus/<int:id>', views.disablewallet, name='changewalletstatus'),
    path('getwalletdetails/<int:id>', views.showwalletdetails, name='getwalletdetails'),
    path('addmoneytowallet/<int:id>', views.addmoneytowallet, name='addmoneytowallet')
]