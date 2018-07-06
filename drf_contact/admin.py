from django.contrib import admin
from .models import ContactDetail


class MyModelAdmin(admin.ModelAdmin):

    def get_readonly_fields(self, request, obj=None):
        """
        Makes created_by & create_date readonly when editing.
        :param request: HttpResponse
        :param obj: Model's Object
        :return: tuple
        """
        if not obj:
            return ()
        return 'created_by', 'create_date'


admin.site.register(ContactDetail, MyModelAdmin)
