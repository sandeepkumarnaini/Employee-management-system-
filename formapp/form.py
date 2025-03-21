from django import forms
from django.core.exceptions import ValidationError
from dbapp.models import Department,Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
def iseven(val):
    if val%2!=0:
        raise ValidationError('it is not even')
class Addition(forms.Form):
    v1=forms.IntegerField(help_text='marks',initial=10)
    v2=forms.IntegerField(validators=['iseven'])
    dob=forms.DateField(widget=forms.SelectDateWidget)
    def clean_v1(self):
        v1=int(self.cleaned_data['v1'])
        if v1<0:
            raise ValidationError('negative values are not aloowed')
        return v1
    def clean_v2(self):
        v2=int(self.cleaned_data['v2'])
        if v2<100:
            raise ValidationError('value should not be greater than 100')
        return v2
    
'''class Insertform(forms.Form):
    eno=forms.IntegerField(required=True)
    ename=forms.CharField(max_length=20)
    esal=forms.IntegerField()
    department=forms.ModelChoiceField(queryset=Department.objects.all())'''

class Insertform(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'

class userform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2','email']