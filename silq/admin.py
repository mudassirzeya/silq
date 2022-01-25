from django.contrib import admin
from .models import Project, Bill_Of_Materials, Measurement_Chart, Other_Issue, Po_Summary, Style_Data

# Register your models here.
admin.site.register(Project)
admin.site.register(Bill_Of_Materials)
admin.site.register(Measurement_Chart)
admin.site.register(Other_Issue)
admin.site.register(Po_Summary)
admin.site.register(Style_Data)
