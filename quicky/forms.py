from allauth.account.forms import SignupForm
from .models import Referral


class MyCustomSignupForm(SignupForm):
	def save(self, request):


		fName = request.POST['first_name']
		lName = request.POST['last_name']
		user = super(MyCustomSignupForm, self).save(request)
		user.first_name = fName
		user.last_name = lName
		user.save()   # this updates the value of previous save
		ref_id = request.POST.get('ref', None)

		if ref_id == "":
			ref_id = None
		else:
			if Referral.objects.filter(refer_id=ref_id).exists():
				ref_model = Referral.objects.get(refer_id=ref_id)
				ref_model.user.save()
				ref_model.save()
			else:
				ref_id = None
		
		new_ref_model = Referral.objects.create(user=user, referred_from=ref_id,)
		new_ref_model.save()

		return user
