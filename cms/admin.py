from django.contrib import admin
from django.contrib.auth.models import Group
from cms.models import Contact

############## customizing existing bore admin panel view in Contact table ################
########### all the names inside list_display and list_editable must match models field name #############


class ContactCustomization(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'info', 'gender', 'image', 'date_added')
    # list_editable = ('name',)
    list_display_links = ('name',) # list_display_links item cannot be in list_editable
    list_editable = ('gender',) # here comma has a massive role if tuple has only one item
    list_per_page = 10 # pagination process
    search_fields = ('name', 'email', 'phone', 'info', 'gender') # added search field to admin panel
    list_filter = ('gender', 'date_added')


# Register your models here.

admin.site.register(Contact, ContactCustomization)


############# unregister from admin panel ################

admin.site.unregister(Group)
# admin.site.unregister(User)

