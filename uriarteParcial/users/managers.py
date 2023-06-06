from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):

   def create_superuser(self,email,password=None,**extra_fields):
      
       if not email:
           raise ValueError('El campo email es mandatorio')

       extra_fields.setdefault("is_staff", True)
       extra_fields.setdefault("is_superuser", True)
       extra_fields.setdefault("is_active", True)
      
       return self.createuser(email, password, **extra_fields)