from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField()
    
    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        if name and len(name) < 5:
            raise forms.ValidationError('Name','Name should be more than 5 characters')
        
        email = cleaned_data.get('email')
        if email and not email.endswith('@gmail.com'):
            raise forms.ValidationError('Email', 'Email must end with @gmail.com')
        
        
        password = cleaned_data.get('password')
        if password and len(password) < 8:
                raise forms.ValidationError('Password must be at least 8 characters long')
        if not any(char.isdigit() for char in password):
                raise forms.ValidationError('Password must contain at least one digit')
        if not any(char.isalpha() for char in password):
                raise forms.ValidationError('Password must contain at least one letter')
