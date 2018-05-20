from django.contrib.admin import ModelAdmin


# WIP
class AbstractSubnetAdmin(ModelAdmin):
    change_form_template = "admin/django-ipam/change_form.html"

    def change_view(self, request, object_id, form_url="", extra_context=None):
        labels = ['Oxygen', 'Hydrogen', 'Carbon_Dioxide', 'Nitrogen']
        values = [4500, 2500, 1053, 500]
        extra_context = {}
        extra_context['labels'] = labels
        extra_context['values'] = values
        return super(AbstractSubnetAdmin, self).change_view(request, object_id, form_url, extra_context)


class AbstractIPAddressAdmin(ModelAdmin):
    pass
