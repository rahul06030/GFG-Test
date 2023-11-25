from django.db import models
import hashlib
from django.contrib.auth.models import AbstractUser




class Customer(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True,  null=True)
    contact_no = models.CharField(max_length=15, blank=True, null=True)
    username = models.EmailField(unique=True)
    customer_id = models.AutoField(primary_key=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_disabled = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    additional_data = models.JSONField(null=True, blank=True)
    password = models.CharField(max_length=128, default="")
    token = models.CharField(max_length=250,null="",blank="", default="")
    groups = models.ManyToManyField(
        to='auth.Group',
        related_name='customer_groups',  
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        to='auth.Permission',
        related_name='customer_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return f"{self.username}"
    def set_password(self, raw_password):
        self.password = hashlib.md5(raw_password.encode()).hexdigest()

    def check_password(self, raw_password):
        return self.password == hashlib.md5(raw_password.encode()).hexdigest()
    