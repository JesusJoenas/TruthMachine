from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from .models import Feedback

# Form for handling user registration
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

# Form for capturing user profile preferences
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['preferred_categories']

# Form for collecting user feedback on articles
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['rating', 'comment']
