from django.contrib import admin
from .models import Projects,Comment

admin.site.register(Comment)

@admin.register(Projects)

class ProjectsAdmin(admin.ModelAdmin):
# Register your models here.
    
    list_display = ["project_name","project_created_date"]

    list_display_links=["project_name","project_created_date"]
    
    search_fields=["project_name"]

    list_filter=["project_created_date"]

    class Meta:
        model = Projects