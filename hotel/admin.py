from django.contrib import admin

# Register your models here.
from .models import RNac
from .models import Rac
from .models import Dac

admin.site.register(RNac)
admin.site.register(Rac)
admin.site.register(Dac)
