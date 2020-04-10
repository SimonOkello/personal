from django.contrib import admin
from .models import Project, Category, Screenshot

# Register your models here.


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