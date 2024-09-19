from django.db import models

# Custom User model
class User(models.Model):
    email = models.CharField(max_length=80, unique=True)
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Building(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name


class Room(models.Model):
    BUILDING_TYPES = [
        ('single', 'Single'),
        ('double', 'Double'),
    ]
    number = models.CharField(max_length=10)
    building = models.ForeignKey(Building, related_name='rooms', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=BUILDING_TYPES)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.number} - {self.building.name}'


class Resident(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='residents', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.room.number}'


class MaintenanceRequest(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    issue = models.TextField()
    location = models.ForeignKey(Room, on_delete=models.CASCADE)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.issue} - {self.priority}'


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.ForeignKey(Building, related_name='events', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Announcement(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
