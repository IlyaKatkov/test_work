from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """ Менеджер пользовательской модели. """
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        """ Создает и сохраняет пользователя с переданными e-mail, password. """
        if not email:
            raise ValueError('Вы должны указать e-mail адрес.')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        """ Создает и сохраняет пользователя с переданными e-mail, password. """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь статус '
                             'is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь статус '
                             'is_superuser=True.')

        return self.create_user(email, password, **extra_fields)