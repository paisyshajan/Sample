
from django import forms
from .models import Person, Branch

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')












# from django import forms
#
# from . models import Person
#
# class PersonForm(forms.ModelForm):
#     class Meta:
#         model=Person
#         fields="__all__"
#         # fields=['name','dob','age','email','address','gender','phone','state','district','branch','account','materials']