from django.contrib import admin

# Register your models here.
from .models import Poem

admin.site.register(Poem)