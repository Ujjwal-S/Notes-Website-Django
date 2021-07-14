from allauth.account.adapter import DefaultAccountAdapter



class CustomAccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        next_url = '/'
        email_conf_url = super(CustomAccountAdapter, self).get_email_confirmation_url(request, emailconfirmation)
        if next_url:
            return '%s?next=%s' % (email_conf_url, next_url)
        else:
            return email_conf_url

    def get_email_confirmation_redirect_url(self, request):
        next_url = '/'
        if next_url:
            return next_url
        else:
            return super(CustomAccountAdapter, self).get_email_confirmation_redirect_url(request)