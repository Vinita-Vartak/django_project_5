from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class NewUserForm(UserCreationForm):
# 	email = forms.EmailField(required=True)

# 	class Meta:
# 		model = User
# 		fields = ("username", "email", "password1", "password2")

	# def save(self, commit=True):
	# 	user = super(NewUserForm, self).save(commit=False)
	# 	user.email = self.cleaned_data['email']
	# 	if commit:
	# 		user.save()
	# 	return user
 
# if in the form we want more details then
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required= True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)    

    class Meta:
        model = User
        fields = ("username","first_name","last_name","email", "password1", "password2")
        
    def save(self, commit =True):
        user = super(NewUserForm, self).save(commit=False)   # commit-false no enetry in database
        print(user.__dict__)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        # user.is_staff = True 
        if commit:   # when commit is true ,it will get stored in database
            user.save()
        return user

	