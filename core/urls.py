# from django.urls import path
# from .views import SignupView, LoginView

# urlpatterns = [
#     path('signup/', SignupView.as_view(), name='signup'),
#     # path('login/', LoginView.as_view(), name='login'),
#     path('login/', LoginView.as_view(), name='login'),
# ]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BuildingViewSet, RoomViewSet, ResidentViewSet,
    MaintenanceRequestViewSet, EventViewSet, AnnouncementViewSet,
    UserViewSet
)

# Create a router and register viewsets
router = DefaultRouter()

# Register model viewsets
router.register(r'buildings', BuildingViewSet, basename='building')
router.register(r'rooms', RoomViewSet, basename='room')
router.register(r'residents', ResidentViewSet, basename='resident')
router.register(r'maintenance-requests', MaintenanceRequestViewSet, basename='maintenance_request')
router.register(r'events', EventViewSet, basename='event')
router.register(r'announcements', AnnouncementViewSet, basename='announcement')

# The UserViewSet doesn't need a basename since we handle custom actions
# Register user routes for registration and login
user_actions = UserViewSet.as_view({
    'post': 'register'
})
login_action = UserViewSet.as_view({
    'post': 'login'
})

# Define URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Automatically generated routes for ModelViewSets
    path('register/', user_actions, name='register'),  # Register URL
    path('login/', login_action, name='login'),        # Login URL
]
