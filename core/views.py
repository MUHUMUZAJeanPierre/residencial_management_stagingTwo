from rest_framework import viewsets
from .models import Building, Room, Resident, MaintenanceRequest, Event, Announcement, User
from .serializers import (
    BuildingSerializer, RoomSerializer, ResidentSerializer,
    MaintenanceRequestSerializer, EventSerializer, AnnouncementSerializer,
    SignupSerializer, LoginSerializer
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema

# ViewSets for the models

@swagger_auto_schema(
    operation_summary="List all buildings",
    operation_description="Retrieve a list of all buildings."
)
class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

    @swagger_auto_schema(
        operation_summary="Create a new building",
        operation_description="Create a new building in the system.",
        request_body=BuildingSerializer,
        responses={status.HTTP_201_CREATED: BuildingSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a building",
        operation_description="Retrieve a specific building by its ID.",
        responses={status.HTTP_200_OK: BuildingSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a building",
        operation_description="Update an existing building.",
        request_body=BuildingSerializer,
        responses={status.HTTP_200_OK: BuildingSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update a building",
        operation_description="Partially update a building.",
        request_body=BuildingSerializer,
        responses={status.HTTP_200_OK: BuildingSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a building",
        operation_description="Delete a specific building by its ID."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
# class BuildingViewSet(viewsets.ModelViewSet):
#     queryset = Building.objects.all()
#     serializer_class = BuildingSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    @swagger_auto_schema(
        operation_summary="List all rooms",
        operation_description="Retrieve a list of all rooms."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new room",
        operation_description="Create a new room in the system.",
        request_body=RoomSerializer,
        responses={status.HTTP_201_CREATED: RoomSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a room",
        operation_description="Retrieve a specific room by its ID.",
        responses={status.HTTP_200_OK: RoomSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a room",
        operation_description="Update an existing room.",
        request_body=RoomSerializer,
        responses={status.HTTP_200_OK: RoomSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update a room",
        operation_description="Partially update a room.",
        request_body=RoomSerializer,
        responses={status.HTTP_200_OK: RoomSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a room",
        operation_description="Delete a specific room by its ID."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

# class RoomViewSet(viewsets.ModelViewSet):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer


class ResidentViewSet(viewsets.ModelViewSet):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer

    @swagger_auto_schema(
        operation_summary="List all residents",
        operation_description="Retrieve a list of all residents."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new resident",
        operation_description="Create a new resident in the system.",
        request_body=ResidentSerializer,
        responses={status.HTTP_201_CREATED: ResidentSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a resident",
        operation_description="Retrieve a specific resident by its ID.",
        responses={status.HTTP_200_OK: ResidentSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a resident",
        operation_description="Update an existing resident.",
        request_body=ResidentSerializer,
        responses={status.HTTP_200_OK: ResidentSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update a resident",
        operation_description="Partially update a resident.",
        request_body=ResidentSerializer,
        responses={status.HTTP_200_OK: ResidentSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a resident",
        operation_description="Delete a specific resident by its ID."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

# class ResidentViewSet(viewsets.ModelViewSet):
#     queryset = Resident.objects.all()
#     serializer_class = ResidentSerializer

class MaintenanceRequestViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer

    @swagger_auto_schema(
        operation_summary="List all maintenance requests",
        operation_description="Retrieve a list of all maintenance requests."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new maintenance request",
        operation_description="Create a new maintenance request in the system.",
        request_body=MaintenanceRequestSerializer,
        responses={status.HTTP_201_CREATED: MaintenanceRequestSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve a maintenance request",
        operation_description="Retrieve a specific maintenance request by its ID.",
        responses={status.HTTP_200_OK: MaintenanceRequestSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update a maintenance request",
        operation_description="Update an existing maintenance request.",
        request_body=MaintenanceRequestSerializer,
        responses={status.HTTP_200_OK: MaintenanceRequestSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update a maintenance request",
        operation_description="Partially update a maintenance request.",
        request_body=MaintenanceRequestSerializer,
        responses={status.HTTP_200_OK: MaintenanceRequestSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete a maintenance request",
        operation_description="Delete a specific maintenance request by its ID."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
# class MaintenanceRequestViewSet(viewsets.ModelViewSet):
#     queryset = MaintenanceRequest.objects.all()
#     serializer_class = MaintenanceRequestSerializer
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @swagger_auto_schema(
        operation_summary="List all events",
        operation_description="Retrieve a list of all events."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new event",
        operation_description="Create a new event in the system.",
        request_body=EventSerializer,
        responses={status.HTTP_201_CREATED: EventSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve an event",
        operation_description="Retrieve a specific event by its ID.",
        responses={status.HTTP_200_OK: EventSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update an event",
        operation_description="Update an existing event.",
        request_body=EventSerializer,
        responses={status.HTTP_200_OK: EventSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update an event",
        operation_description="Partially update an event.",
        request_body=EventSerializer,
        responses={status.HTTP_200_OK: EventSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete an event",
        operation_description="Delete a specific event by its ID."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
# class EventViewSet(viewsets.ModelViewSet):
#     queryset = Event.objects.all()
#     serializer_class = EventSerializer
class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    @swagger_auto_schema(
        operation_summary="List all announcements",
        operation_description="Retrieve a list of all announcements."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Create a new announcement",
        operation_description="Create a new announcement in the system.",
        request_body=AnnouncementSerializer,
        responses={status.HTTP_201_CREATED: AnnouncementSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Retrieve an announcement",
        operation_description="Retrieve a specific announcement by its ID.",
        responses={status.HTTP_200_OK: AnnouncementSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Update an announcement",
        operation_description="Update an existing announcement.",
        request_body=AnnouncementSerializer,
        responses={status.HTTP_200_OK: AnnouncementSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Partial update an announcement",
        operation_description="Partially update an announcement.",
        request_body=AnnouncementSerializer,
        responses={status.HTTP_200_OK: AnnouncementSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Delete an announcement",
        operation_description="Delete a specific announcement by its ID."
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

# class AnnouncementViewSet(viewsets.ModelViewSet):
#     queryset = Announcement.objects.all()
#     serializer_class = AnnouncementSerializer

# User ViewSet for registration and login

from drf_yasg import openapi

class UserViewSet(viewsets.ViewSet):
    @swagger_auto_schema(
        operation_summary='Register users',
        operation_description="Register new users in the system.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD)
            },
            required=['username', 'email', 'password']
        )
    )

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'status': 'user created',
                'user': SignupSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary='Login users',
        operation_description="Log in existing users.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD)
            },
            required=['username', 'password']
        )
    )
    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({
                'status': 'login successful',
                'user': LoginSerializer(user).data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
