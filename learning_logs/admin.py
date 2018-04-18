from django.contrib import admin
from learning_logs.models import Topic, Entry, Comment
# Register your models here.
class TopicAdmin(admin.ModelAdmin):
    list_display = ('text', 'owner')

class EntryAdmin(admin.ModelAdmin):
    list_display = ('topic', 'entrytitle', 'text', 'owner')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('entry', 'text', 'owner')

admin.site.register(Topic, TopicAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Comment, CommentAdmin)

'''
class TopicAdmin(admin.ModelAdmin):
    list_display = ('text', 'owner')

class EntryAdmin(admin.ModelAdmin):
    list_display = ('topic', 'entrytitle', 'text', 'owner')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('entry', 'text', 'owner')

xadmin.site.register(Topic, TopicAdmin)
xadmin.site.register(Entry, EntryAdmin)
xadmin.site.register(Comment, CommentAdmin)
'''