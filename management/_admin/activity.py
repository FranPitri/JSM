from django.contrib import admin

from management.models import Activity, Turn


class TurnInline(admin.StackedInline):
    model = Turn
    extra = 1


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    inlines = [TurnInline]
    list_filter = ('start_date',)
    search_fields = ('title',)
    list_display = ('title', 'start_date', 'end_date', 'number_of_students')

    def get_queryset(self, request):
        qs = super(ActivityAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return request.user.activities.all()
        return qs
