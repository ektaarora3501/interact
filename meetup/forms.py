from django.forms import PasswordInput,forms,CharField,EmailField,ChoiceField,Textarea
from meetup.models import RegisMentor
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from bootstrap_datepicker_plus import DatePickerInput

class RegisMentorForm(forms.Form):
    first_name=CharField(max_length=100)
    last_name=CharField(max_length=100)
    email=EmailField()
    ch=[("0","select"),("IT","IT"),("Civil","Civil"),("Mech","Mechanical")]
    choice=ChoiceField(choices=ch,label="field of specialization",help_text="optional",required=False)
    ch2=[("0","select"),("2018","2018"),("2017","2017"),("2016","2016"),("2015","2015"),("2014","2014"),("2013","2013"),("2012","2012")]
    grad_year=ChoiceField(choices=ch2,label="graduation year")
    Batch_id=CharField(max_length=8,help_text="enter your id/roll_no")
    work_exp=CharField(max_length=1000,widget=Textarea)
    contact_no=CharField(max_length=10,help_text="we would love to approach you")
    
    def clean_email(self):
        email=self.cleaned_data['email']
        if RegisMentor.objects.filter(email=email).exists():
            raise ValidationError(_("The given email already exists"))
        return email

    def clean_choice(self):
        ch=self.cleaned_data['choice']
        if (ch=="0"):
            ch="none"
        return ch

    def clean_Batch_id(self):
        rno=self.cleaned_data['Batch_id']
        if RegisMentor.objects.filter(Batch_id=rno).exists():
            raise ValidationError(_(" the given id is already registered"))
        return rno
