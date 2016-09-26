from django import forms
from models import state, hmo_list, patient

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length = 20)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class PatientForm(forms.Form):
    attributes = {'class' : 'form-control'}
    surname = forms.CharField(max_length=15, required= True, widget= forms.TextInput(attrs= attributes))
    firstname = forms.CharField(max_length= 15, required= True, widget= forms.TextInput(attrs= attributes))
    othername = forms.CharField(max_length= 15, required= True, widget= forms.TextInput(attrs= attributes))
    cardNo = forms.CharField(max_length=15, required=True, widget= forms.TextInput(attrs= attributes))
    gender = forms.ChoiceField(choices= (("M", "Male"), ("F", "Female")), initial= "M", widget= forms.Select(attrs=attributes))
    mobileNo = forms.CharField(required=True, widget= forms.TextInput(attrs= attributes))
    address = forms.CharField(required= True, widget= forms.TextInput(attrs= attributes))
    origin = forms.ModelChoiceField(required=True, widget=forms.Select(attrs=attributes), queryset= state.objects.order_by("state_name"), empty_label="Select a State")
    hmo = forms.ModelChoiceField(required=True, widget=forms.Select(attrs=attributes), queryset= hmo_list.objects.order_by("name"), empty_label= "Select an HMO")

    def __init__ (self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(PatientForm, self).__init__(*args, **kwargs)

    def __str__(self):
        data = self.cleaned_data
        return ("%s %s with card number: %s has been created" % (data['surname'], data['firstname'], data['cardNo']))


    def save (self):
        data = self.cleaned_data
        new_patient = patient(surname = data['surname'], firstname = data['firstname'], othernames = data['othername'],                              card_no = data['cardNo'], gender = data['gender'], phone_number = data['mobileNo'],                                  address = data['address'], hmo = data['hmo'], added_by = self.user,
                              origin = data['origin'])
        new_patient.save()


