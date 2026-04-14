from django.contrib import admin
from .models import Artworks
from .models import Contact
from .models import Purchase
from .models import Gallery


admin.site.register(Artworks)
admin.site.register(Contact)
admin.site.register(Purchase)
admin.site.register(Gallery)
