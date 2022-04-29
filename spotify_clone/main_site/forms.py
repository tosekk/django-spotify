from django import forms
from django.core.validators import MinLengthValidator


DATE_INPUT_FORMATS = ['%d.%m.%Y']


class SignUpForm(forms.Form):
    user_email = forms.EmailField(label="Ваш адрес электронной почты")
    confirm_email = forms.EmailField(label="Подтвердите адрес электронной почты")
    user_password = forms.CharField(widget=forms.PasswordInput(),
                                    validators=[MinLengthValidator(8)],
                                    label="Придумайте пароль")
    user_name = forms.CharField(max_length=20, label="Ваше имя")
    user_birthdate = forms.DateField(label="Ваша дата рождения", 
                                     input_formats=DATE_INPUT_FORMATS)
    user_gender = forms.ChoiceField(
        choices=[(1, "Мужчина"), (2, "Женщина"), (3, "Другой")],
        widget=forms.RadioSelect)
    is_newsletter = forms.BooleanField(required=False, 
                                       label="Я соглашаюсь получать рассылку на почту")