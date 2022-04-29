from django.db import models

# Create your models here.


class UserModel(models.Model):
    user_email = models.EmailField(verbose_name="e-mail")
    user_name = models.CharField(verbose_name="Имя",max_length=20)
    user_password = models.CharField(verbose_name="Пароль", max_length=60)
    user_birthdate = models.DateField(verbose_name="Дата рождения")
    user_gender = models.CharField(max_length=20, verbose_name="Пол", 
                                   choices=[(1, "Мужчина"), (2, "Женщина"), (3, "Другой")])
    is_newsletter = models.BooleanField(verbose_name="Статус рассылки", default=False)
    
    class Meta:
        verbose_name_plural = "Users"