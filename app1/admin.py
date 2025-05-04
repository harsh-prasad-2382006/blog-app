from django.contrib import admin
from .models import Post,PricingPlan
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [i.name for i in Post._meta.fields]

@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = [i.name for i in PricingPlan._meta.fields]