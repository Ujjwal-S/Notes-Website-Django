from allauth.account.signals import email_confirmed
from django.dispatch import receiver
from .models import Referral

@receiver(email_confirmed)
def email_confirmed_(request, email_address, **kwargs):
    user = email_address.user
    user.email_verified = True
    

    from_user_id = Referral.objects.get(user=user).referred_from 

    if from_user_id == None:
        pass
    else:
        from_user = Referral.objects.get(refer_id=from_user_id)

        from_user.referred_count += 1
        from_user.save()   
        from_user.user.points += 10
        from_user.user.save()

    user.save()