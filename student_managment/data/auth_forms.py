from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):  #Meta is an inner class in Django forms and models.
        model = User # we need our form to still behave like UserCreationForm but point to our Custom_User model instead of the default auth.User.
        fields = ('username', 'email', 'password1', 'password2')
