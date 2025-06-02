from django.contrib import admin
from .models import AboutSection,ImageSlider,TeamMember,\
  ContactMessage,HomeSection, Servico, Depoimento

admin.site.register(AboutSection)
admin.site.register(ImageSlider)
admin.site.register(TeamMember)
admin.site.register(ContactMessage)
admin.site.register(HomeSection)
admin.site.register(Servico)
admin.site.register(Depoimento)