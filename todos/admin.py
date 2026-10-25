from django.contrib import admin

# Register your models here.
from .models import Todo, Person


admin.site.register(Person)


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'deadline', 'done')
    search_fields = ('title' ,)
    list_filter = ('priority','deadline')