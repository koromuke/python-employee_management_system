from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'employee_management_system/employee_list.html'
