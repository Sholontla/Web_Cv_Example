from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, permission_required

from inv.models import Categoria, SubCategoria, Marca, \
    UnidadMedida


from .forms import UMForm

from bases.views import SinPrivilegios

class UMView(SinPrivilegios, generic.ListView):
    model = UnidadMedida
    template_name = "data_migrations/migration_list.html"
    context_object_name = "obj"
    permission_required="inv.um_list"
def migration_excel(request):

    if request.method == 'POST':
    	uploaded_file = request.FILES['document']
    	print(uploaded_file)
