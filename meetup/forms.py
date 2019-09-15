from django.forms import PasswordInput,forms,CharField,EmailField,ChoiceField,Textarea
from meetup.models import Register_user
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from bootstrap_datepicker_plus import DatePickerInput

class RegisterForm(forms.Form):
    first_name=CharField(label='First Name',max_length=100)
    last_name=CharField(label='Last Name',max_length=100)
    email=EmailField()
    ch=[("0","select"),("CSE","Computer Science"),("ECE","Electronics")]
    choice=ChoiceField(choices=ch,label="Branch",help_text="optional",required=False)
    ch2=[("0","select"),("1","first"),("2","second"),("3","third"),("4","fourth"),("3501","Graduated")]
    curr_year=ChoiceField(choices=ch2,label="Current Year")
    adm_no=CharField(label='Admission No',max_length=8,help_text="enter your id/roll_no")
    #work_exp=CharField(max_length=1000,widget=Textarea)
    #contact_no=CharField(max_length=10,help_text="we would love to approach you")

    def clean_email(self):
        email=self.cleaned_data['email']
        if Register_user.objects.filter(email=email).exists():
            raise ValidationError(_("The given email already exists"))
        return email

    def clean_choice(self):
        ch=self.cleaned_data['choice']
        if (ch=="0"):
            ch="none"
        return ch

    def clean_adm_no(self):
        rno=self.cleaned_data['adm_no']
        if Register_user.objects.filter(roll_no=rno).exists():
            raise ValidationError(_(" the given id is already registered"))
        return rno
