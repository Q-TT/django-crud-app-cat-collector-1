from django.contrib import admin
from .models import Cat, Feeding, Toy

# Register your models here.
admin.site.register(Cat)
# Register the new Feeding model
admin.site.register(Feeding)

admin.site.register(Toy)

