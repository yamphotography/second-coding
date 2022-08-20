from email.message import Message
from django.contrib import admin
from .models import Profile, Skill , Message


admin.site.register(Skill)
admin.site.register(Profile)
admin.site.register(Message)



