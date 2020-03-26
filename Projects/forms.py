from django import forms
from .models import Projects

class ProjectsFrom(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ["project_name","project_content","project_image"]
       