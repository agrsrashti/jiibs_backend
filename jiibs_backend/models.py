from django.db import models

# Create your models here.
class Users(models.Model):
    user_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    password=models.CharField(max_length=255,default="password")
    mobile_no=models.CharField(max_length=11)
    email=models.EmailField()
    dob=models.CharField()
    role=models.CharField(max_length=25)
    property_name=models.CharField(max_length=255,default="")
    property_management_company=models.CharField(max_length=255,default="")

class Buildings(models.Model):
    building_id=models.AutoField(primary_key=True)
    building_name=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    floors=models.BigIntegerField()
    total_units=models.BigIntegerField()
    year_of_built=models.CharField(max_length=255)
    status=models.CharField(max_length=255)
    description=models.TextField()
    neighbourhood_name=models.CharField(max_length=255)
    thumbnail=models.CharField()
    agent_id=models.ForeignKey(Users,on_delete=models.CASCADE)

class Units(models.Model):
    unit_id = models.AutoField(primary_key=True)
    unit_name = models.CharField(max_length=255)
    unit_no = models.CharField(max_length=255)
    unit_size = models.CharField(max_length=255)
    beds = models.PositiveIntegerField()
    baths = models.PositiveIntegerField()
    description = models.TextField()
    photos = models.URLField()  # Assuming photos are URLs, change accordingly
    floor_plan = models.URLField()  # Assuming floor_plan is a URL, change accordingly
    status = models.CharField(max_length=255)
    deals = models.TextField()
    thumbnail = models.URLField(max_length=255)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    building_id = models.ForeignKey(Buildings, on_delete=models.CASCADE)

class Amenities(models.Model):
    amenity_id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    photos = models.URLField()  # Assuming photos are URLs, change accordingly
    building_id = models.ForeignKey(Buildings, on_delete=models.CASCADE)

class Neighbourhood(models.Model):
    neighbourhood_id = models.AutoField(primary_key=True)
    building_id = models.ForeignKey(Buildings, on_delete=models.CASCADE)
    neighbourhood_name = models.CharField(max_length=255)

class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    agent_id = models.ForeignKey(Users, on_delete=models.CASCADE)

class Advertisement(models.Model):
    ad_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    property_name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=11)
    property_management_company = models.CharField(max_length=255)
    agent_id = models.ForeignKey(Users, on_delete=models.CASCADE)

class Messages(models.Model):
    message_id = models.AutoField(primary_key=True)
    sender_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='sender_messages')
    receiver_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='receiver_messages')
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    building_id = models.ForeignKey(Buildings, on_delete=models.CASCADE)

class Media(models.Model):
    media_id = models.AutoField(primary_key=True)
    link = models.URLField()
    linked_id = models.BigIntegerField()
    media_name = models.CharField(max_length=255)
    media_type = models.CharField(max_length=255)