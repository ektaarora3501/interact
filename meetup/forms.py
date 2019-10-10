from django.forms import PasswordInput,forms,CharField,EmailField,ChoiceField,Textarea,ImageField
from meetup.models import Register_user
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
#from bootstrap_datepicker_plus import DatePickerInput
#import bcrypt
#from hashing import *

class RegisterForm(forms.Form):
    first_name=CharField(label='First Name',max_length=100)
    last_name=CharField(label='Last Name',max_length=100)
    email=EmailField()
    ch=[("0","select"),("CSE","Computer Science"),("ECE","Electronics")]
    choice=ChoiceField(choices=ch,label="Branch",help_text="optional",required=False)
    ch2=[("0","select"),("1","first"),("2","second"),("3","third"),("4","fourth"),("3501","Graduated")]
    curr_year=ChoiceField(choices=ch2,label="Current Year")
    adm_no=CharField(label='Admission No',max_length=8,help_text="enter your id/roll_no")
    password=CharField(max_length=12,widget=PasswordInput,help_text="Set up password to peek in !!")
    cnf_pass=CharField(max_length=12,widget=PasswordInput,help_text="Reconfirm  your password")

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

    def clean_cnf_pass(self):
        passw=self.cleaned_data['password']
        cnf=self.cleaned_data['cnf_pass']
        if(len(passw)<8):
            raise ValidationError(_("Password must be atleast 8 characaters long"))
        if(cnf!=passw):
            raise ValidationError(_("Please reconfirm your password"))
            return cnf
        return passw

class LoginForm(forms.Form):
    adm_no=CharField(label='Admission No',max_length=8)
    password=CharField(label='Secret code to enter ',max_length=12,widget=PasswordInput,help_text="Enter your password")
    def clean_password(self):
        adm=self.cleaned_data['adm_no']
        if Register_user.objects.filter(roll_no=adm).exists():
            print(adm)
        else:
            raise ValidationError(_("Hey buddy seems like you are not registered"))
            return adm
        us=Register_user.objects.get(roll_no=adm)
        print(us.branch)
        p=self.cleaned_data['password']
        a=verify_password(us.password,p)
        if(a is False ):
            raise ValidationError(_("Incorrect Password"))
        return a



class UpdateForm(forms.Form):
    email=EmailField()
    github_link=CharField(max_length=100,help_text='enter your github id')
    ch=[(None,"select"),("python","Python"),("C++","C++"),("django","Django"),("Node","Nodejs"),("React","React.js"),("java","Java"),("Android","Android"),("Flutter","Flutter"),("Competitive-coding","Competitive coding"),("ML","Machine learning")]
    skill1=ChoiceField(choices=ch,label="Technical Skill 1",help_text="optional",required=False)
    skill2=ChoiceField(choices=ch,label="Technical Skill 2",help_text="optional",required=False)
    skill3=ChoiceField(choices=ch,label="Technical  Skill 3",help_text="optional",required=False)
    skill4=ChoiceField(choices=ch,label="Technical  Skill 4",help_text="optional",required=False)
    ch2=[(None,"select"),("Joyfest","Joyfest"),("Cinephelia","Cinephalia"),("Convex","Convex"),("Kirdaar","Kirdaar"),("Raag","Raag"),("Malang","Malang")]
    ntech1=ChoiceField(choices=ch2,label="Member of..",help_text="Non tech",required=False)
    ntech2=ChoiceField(choices=ch2,label="Member of..",help_text="Non tech",required=False)
    ntech3=ChoiceField(choices=ch2,label="Member of..",help_text="Non tech",required=False)
    ntech4=ChoiceField(choices=ch2,label="Member of..",help_text="Non tech",required=False)
    summmary=CharField(widget=Textarea,label="something to show offf !!",help_text="Short Description about yourself")
