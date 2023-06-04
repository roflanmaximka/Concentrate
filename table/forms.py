from django import forms
from .models import Record
from django.forms import ModelForm


class AddRecordForm(forms.ModelForm): # Класс формы для и отображения формы и добавления в БД
    employee_name = forms.CharField(required=True, widget=forms.widgets.TextInput
        (attrs={"placeholder": "Логин работника", "class": "form-control"}), label="")
    raw_material_name = forms.CharField(required=True, widget=forms.widgets.TextInput
        (attrs={"placeholder": "Наименование сырья", "class": "form-control"}), label="")
    iron_concentration = forms.CharField(required=True, widget=forms.widgets.TextInput
        (attrs={"placeholder": "Содержание железа", "class": "form-control"}), label="")
    silicon_concentration = forms.CharField(required=True, widget=forms.widgets.TextInput
        (attrs={"placeholder": "Содержание кремния", "class": "form-control"}), label="")
    aluminum_concentration = forms.CharField(required=True, widget=forms.widgets.TextInput
        (attrs={"placeholder": "Содержание алюминия", "class": "form-control"}), label="")
    calcium_concentration = forms.CharField(required=True, widget=forms.widgets.TextInput
        (attrs={"placeholder": "Содержание кальция", "class": "form-control"}), label="")
    sulfur_concentration = forms.CharField(required=True, widget=forms.widgets.TextInput
        (attrs={"placeholder": "Содержание серы", "class": "form-control"}), label="")

    class Meta: #Сериализатор
        model = Record #От какой модели наследуемся
        fields = '__all__' #Здесь указываем либо fields для отображения тех полей, которые на нужны,
                           #либо except для отображения все полей за исключением тех, которые мы укажем
