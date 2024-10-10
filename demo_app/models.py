from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class AppVariety(models.Model):
    APP_TYPE_CHOICE = [
        ('CM', 'COMMERCIAL'),
        ('SM', 'SOCIAL'),
        ('ED', 'EDUCATIONAL'),
        ('OT', 'OTHER')
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='apps/')
    date_added =  models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=APP_TYPE_CHOICE)
    description = models.TextField(default='')

    def __str__(self):
        return self.name
    
#One to Many

class AppReview(models.Model):
    app = models.ForeignKey(AppVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.user.username} review for {self.app.name}'

# Many to Many

class AppStore(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    app_varieties = models.ManyToManyField(AppVariety, related_name='app_store')
    
    def __str__(self):
        return self.name
    
# One to One

class AppCertificate(models.Model):
    app = models.OneToOneField(AppVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()
    
    def __str__(self):
        return f'Certificate for {self.name.app}'
    