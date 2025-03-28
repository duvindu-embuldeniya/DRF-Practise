from . models import Project, Review, Tag
from django import forms
from django import forms

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'source_link', 'tags', 'featured_image']
    

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        # self.fields['title'].widget.attrs.update(
        #     {'class':'input', 'placeholder':'xxx'})
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
