from django.contrib import admin
from grow_map.models import Person

LIST_PER_PAGE = 50


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ('person_name',)
    list_display = (
        'person_name',
    )
    empty_value_display = 'empty'
    ordering = ('person_name',)
    list_per_page = LIST_PER_PAGE
