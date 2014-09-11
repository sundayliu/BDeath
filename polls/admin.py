from django.contrib import admin

# Register your models here.
from polls.models import Poll
from polls.models import Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
    
class PollAdmin(admin.ModelAdmin):
    #fields = ['pub_date','question']
    fieldsets = [
                 (None,{'fields':['question']}),
                 ('Date information',{'fields':['pub_date']})
                 ]
    list_display = ('question','pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    inlines = [ChoiceInline]
admin.site.register(Poll,PollAdmin)