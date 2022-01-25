from dataclasses import field
from django.forms import ModelForm
from .models import Bill_Of_Materials, Measurement_Chart, Other_Issue, Project, Po_Summary, Style_Data


class Project_Form(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class Bill_Of_Material_Form(ModelForm):
    class Meta:
        model = Bill_Of_Materials
        fields = '__all__'


class Measurement_Chart_Form(ModelForm):
    class Meta:
        model = Measurement_Chart
        fields = '__all__'


class Other_Issue_Form(ModelForm):
    class Meta:
        model = Other_Issue
        fields = '__all__'


class PO_Summary_Form(ModelForm):
    class Meta:
        model = Po_Summary
        fields = '__all__'


class Style_Data_Form(ModelForm):
    class Meta:
        model = Style_Data
        fields = '__all__'

    # def __init__(self, client=None, args, *kwargs):
    #     super(Style_Data_Form, self).__init__(*args, **kwargs)
        # to remove default dash from dropdown
        # self.fields['team'].empty_label = None

        # if client:
        #     self.fields['team'].queryset = Team.objects.filter(
        #         client=client)
