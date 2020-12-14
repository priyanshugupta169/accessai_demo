from django.db import models
from datetime import date

from django.contrib.auth.base_user import BaseUserManager,AbstractBaseUser
# Create your models here.

class MyAccountManager(BaseUserManager):
	"""
	creating a custom user authentication model as we require additional fields.
	"""
	def create_user(self, email, username,phno, city, address, password=None):
		"""
		overriding the function and creating our own function for user creation
		"""
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')
		if not phno:
			raise ValueError('Users must have a contact number')
		if not password:
			raise ValueError('Password cannot be Empty')
		user = self.model(
			email=self.normalize_email(email),
			username=username,
			phno = phno,
			city=city,
			address=address,
			
		)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email,phno, username,city, address, password):
		"""
		overriding the function and creating our own function for superuser creation
		"""
		user = self.create_user(
			email=self.normalize_email(email),
			username=username,
			password=password,
			phno = phno,
			city=city,
			address=address,

		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user
	

class Accounts(AbstractBaseUser):
	"""
	custom model for the user authentication table
	below are the fields listed for the table
	"""
	email 					= models.EmailField(verbose_name="email",max_length=100,unique=True,primary_key=True)
	username 				= models.CharField(max_length=70)
	phno                    = models.CharField(max_length=20)
	city                    = models.CharField(max_length=50)
	address                 = models.CharField(max_length=80)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username','phno','city','address']
	EMAIL_FIELD='email'

	objects = MyAccountManager()

	def __str__(self):
		return self.email