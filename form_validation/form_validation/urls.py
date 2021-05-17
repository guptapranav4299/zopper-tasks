from django.urls import path
from .views import get_user_details,create_user_serializer_view


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('users/', create_user_serializer_view),
    path('users/<int:pk>', get_user_details)
]