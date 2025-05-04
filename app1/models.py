from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
class PricingPlan(models.Model):
    PLAN_CHOICES = [
        ('basic', 'Basic'),
        ('standard', 'Standard'),
        ('premium', 'Premium'),
    ]
    
    name = models.CharField(max_length=50, choices=PLAN_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    blogs_per_month = models.CharField(max_length=100)
    can_turn_subscribers = models.BooleanField(default=False)
    can_add_paywalls = models.BooleanField(default=False)
    can_setup_schedules = models.BooleanField(default=False)

    def __str__(self):
        return self.name.capitalize()