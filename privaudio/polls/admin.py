from django.contrib import admin

# Register your models here.
#from .models import User
from .models import Message

#admin.site.register(User)
admin.site.register(Message)

from .models import Audio
admin.site.register(Audio)

from .models import Video
admin.site.register(Video)