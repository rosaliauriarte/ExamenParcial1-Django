from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
  
   def create_user(self,email,password=None,**extra_fields):
       if not email:
           raise ValueError('Se requiere el email del usuario')
      
       user = self.model(
           full_name = self.full_name,
           avatar = self.avatar
       )
       extra_fields.setdefault('is_superuser', False)
       extra_fields.setdefault('is_staff', True)
       extra_fields.setdefault('is_active', False)
       user.save(using=self.db)
       return user


   def create_superuser(self,email,password=None,**extra_fields):
      
       if not email:
           raise ValueError('El campo email es mandatorio')
      


       extra_fields.setdefault("is_staff", True)
       extra_fields.setdefault("is_superuser", True)
       extra_fields.setdefault("is_active", True)
      
       return self.create_user(email, password, **extra_fields)
