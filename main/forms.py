from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

from django.forms import ModelForm, Select, TextInput, Textarea, URLInput

from main.models import Experience, Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "technologies",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "technologies": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "technologies": TextInput(
                attrs={
                    "placeholder": "Django, Python, HTML, CSS",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "https://github.com/yohanalouisa/myportofolio",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000"
                }
            ),
        }
    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama proyek tidak boleh hanya berisi tag HTML.")
        return title

    def clean_technologies(self):
        return strip_tags(self.cleaned_data["technologies"]).strip()

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
        ]

        labels = {
            "title": "Judul Experience",
            "description": "Deskripsi",
            "category": "Kategori",
            "thumbnail": "URL Thumbnail",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Data Science Intern",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Describe your experience",
                    "rows": 3,
                }
            ),
            "category": Select(),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://github.com/yohanalouisa/myportofolio",
                }
            ),
        }
    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama experience tidak boleh hanya berisi tag HTML.")
        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()