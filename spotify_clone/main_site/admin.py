from django.contrib import admin


from .models import UserModel

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("user_name", "user_email", "user_gender", "is_newsletter")
    
    
admin.site.register(UserModel, UserAdmin)