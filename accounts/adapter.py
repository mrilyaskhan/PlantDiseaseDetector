from allauth.account.adapter import DefaultAccountAdapter

class NoMessageAccountAdapter(DefaultAccountAdapter):
    def add_message(self, *args, **kwargs):
        pass
