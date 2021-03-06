from django.contrib.auth.models import BaseUserManager
from django.db.models import Q

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user