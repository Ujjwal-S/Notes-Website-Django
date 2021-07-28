from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.fields import EmailField
from notes.models import Note
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import secrets, string
import uuid 


class User(AbstractUser):
    profile_photo = models.ImageField(upload_to="profile_images", default="default_profile.jpg")
    points = models.IntegerField(default=0)


def generate_refer_id():
    res = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(10))
    return res


class Referral(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    refer_id = models.CharField(max_length=50, editable=False, null=True, default=generate_refer_id)
    referred_count = models.IntegerField(default=0)
    referred_from = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.user} (Ref id. {self.refer_id} ) -> referred from -> {self.referred_from}"


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)  #TODO time zone sahi kar dena razorpay se pahle
    complete = models.BooleanField(default=False)
    recipt = models.UUIDField(primary_key=False, default=uuid.uuid4)
    r_order_id = models.CharField(max_length=200, null=True) #TODO yeh null ko hata do

    def __str__(self):
        return f"{str(self.id)} | {self.customer}"

    @property
    def get_cart_total(self):   # total paise
        orderitems = self.orderitem_set.all()                  # saare orderItem lo
        total = sum([item.note_name.price for item in orderitems])   # unn pe loop laga ke har ek orderitem pe .get_total laga do toh total mil jaayega   - .get_total attribute hai jo orderitem mai defiened hai
        return total

class OrderItem(models.Model):
    note_name = models.ForeignKey(Note, on_delete=models.CASCADE, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order.customer.username} || {self.note_name}"


class Subscriber(models.Model):
    email = models.EmailField(max_length=254)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


# """ Whenever ANY model is deleted, if it has a file field on it, delete the associated file too """
@receiver(post_delete)
def delete_files_when_row_deleted_from_db(sender, instance, **kwargs):
    for field in sender._meta.concrete_fields:
        if isinstance(field,models.FileField):
            instance_file_field = getattr(instance,field.name)
            delete_file_if_unused(sender,instance,field,instance_file_field)


# """ Delete the file if something else get uploaded in its place """
@receiver(pre_save)
def delete_files_when_file_changed(sender,instance, **kwargs):
    # Don't run on initial save
    if not instance.pk:
        return
    for field in sender._meta.concrete_fields:
        if isinstance(field,models.FileField):
            #its got a file field. Let's see if it changed
            try:
                instance_in_db = sender.objects.get(pk=instance.pk)
            except sender.DoesNotExist:
                # We are probably in a transaction and the PK is just temporary
                # Don't worry about deleting attachments if they aren't actually saved yet.
                return
            instance_in_db_file_field = getattr(instance_in_db,field.name)
            instance_file_field = getattr(instance,field.name)
            if instance_in_db_file_field.name != instance_file_field.name:
                delete_file_if_unused(sender,instance,field,instance_in_db_file_field)


# """ Only delete the file if no other instances of that model are using it """    
def delete_file_if_unused(model,instance,field,instance_file_field):
    dynamic_field = {}
    dynamic_field[field.name] = instance_file_field.name
    other_refs_exist = model.objects.filter(**dynamic_field).exclude(pk=instance.pk).exists()
    if not other_refs_exist:
        instance_file_field.delete(False)