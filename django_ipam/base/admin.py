from ipaddress import IPv4Network, IPv6Network, ip_address

import swapper
from django.contrib.admin import ModelAdmin
from django.http import HttpResponse
from openwisp_utils.admin import TimeReadonlyAdminMixin

Subnet = swapper.load_model("django_ipam", "Subnet")
IpAddress = swapper.load_model("django_ipam", "IpAddress")


class AbstractSubnetAdmin(TimeReadonlyAdminMixin, ModelAdmin):
    change_form_template = "admin/django-ipam/change_form.html"

    def change_view(self, request, object_id, form_url="", extra_context=None):
        instance = Subnet.objects.get(pk=object_id)
        if type(instance.subnet) == IPv4Network:
            total = [host for host in instance.subnet.hosts()]
            used = len(list(instance.ipaddress_set.all()))
            used_ip = [ip_address(ip.ip_address) for ip in instance.ipaddress_set.all()]
            available = len(total) - used
            labels = ['Used', 'Available']
            values = [used, available]
            extra_context = {'labels': labels,
                             'values': values,
                             'total': total,
                             'subnet': instance,
                             'used_ip': used_ip}
        elif type(instance.subnet) == IPv6Network:
            used_ip = [ip for ip in instance.ipaddress_set.all()]
            extra_context = {'used_ip': used_ip}

        return super(AbstractSubnetAdmin, self).change_view(request, object_id, form_url, extra_context)

    class Media:
        js = ('django-ipam/js/custom.js',)
        css = {'all': ('django-ipam/css/admin.css',)}


class AbstractIpAddressAdmin(TimeReadonlyAdminMixin, ModelAdmin):
    def response_add(self, request, obj, post_url_continue='../%s/'):
        '''
            Custom reponse to dismiss an add form popup for IP address.
        '''
        resp = super(AbstractIpAddressAdmin, self).response_add(request, obj, post_url_continue)
        if request.POST.get("_popup"):
            return HttpResponse('''
               <script type="text/javascript">
                  opener.dismissAddAnotherPopup(window);
               </script>''')
        return resp
