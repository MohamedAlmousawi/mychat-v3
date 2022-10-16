from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
	user= models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
	bio = models.CharField(max_length=100,null=True,blank=True)
	image= models.ImageField(upload_to='images/profile',null=True,blank=True)

	def __str__(self):
		return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
