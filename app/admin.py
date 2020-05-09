from django.contrib import admin

from .models import (CustomToken, CustomUser, Donation, HelpProgram, Message,
                     Organization)

admin.site.register(CustomUser)
admin.site.register(CustomToken)
admin.site.register(Donation)
admin.site.register(HelpProgram)
admin.site.register(Message)
admin.site.register(Organization)
