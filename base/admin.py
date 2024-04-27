from django.contrib import admin
from .models import User
from .models import BattleRoyale,Games,ClashRoyale
# Register your models here.
admin.site.register(User)
admin.site.register(BattleRoyale)
admin.site.register(Games)
admin.site.register(ClashRoyale)