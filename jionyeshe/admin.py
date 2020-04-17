from django.contrib import admin
from .models import Project, Category, Screenshot, Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.



class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'
    fk_name = 'user'


class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    # list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    # list_filter = ('is_staff', 'is_superuser', 'is_active')


admin.site.unregister(User)  # Unregister user to add new inline ProfileInline
admin.site.register(User, UserAdmin)  # Register User with this inline profile

class ScreenshotInline(admin.StackedInline):
    model = Screenshot
    extra = 2


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'duration',
                    'client_name', 'project_url')
    list_filter = ("client_name",)
    search_fields = ['title', 'client_name']
    prepopulated_fields = {'client_name': ('title',)}
    inlines = [ScreenshotInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
