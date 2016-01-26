from django.contrib import admin


from models.movie import movietop
from models.movie import moviedetail
from models.movie import moviehot


admin.site.register(movietop)
admin.site.register(moviedetail)
admin.site.register(moviehot)
# Register your models here.
