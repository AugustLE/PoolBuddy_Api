from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
	def create_user(self, email, full_name, password=None, **extra_fields):
		if not email:
			raise ValueError('Users must have an email address')

		if not full_name:
			raise ValueError('Users must have a name')

		user = self.model(
			email=self.normalize_email(email), **extra_fields
		)

		user.set_password(password)
		user.full_name = full_name
		user.save(using=self._db)
		return user

	def create_superuser(self, email, full_name, password):

		user = self.create_user(
			email,
			full_name,
			password=password
		)
		user.is_admin = True
		user.save(using=self._db)
		return user


class CustomUser(AbstractBaseUser):
	email = models.EmailField(
		verbose_name='email address',
		max_length=255,
		unique=True,
	)
	full_name = models.CharField(verbose_name='full name', max_length=50)
	date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)

	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	objects = CustomUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['full_name']

	def get_full_name(self):
		return self.full_name

	def get_email(self):
		return self.email

	def get_short_name(self):
		# The user is identified by their email address
		return self.email

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.is_admin







