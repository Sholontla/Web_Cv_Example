from django.urls import path
from .views import UMView, migration_excel
from . import views

#from data_migrations.core import views
''', UMNew, UMEdit, um_inactivar'''

urlpatterns = [

    path('um_viwes/',UMView.as_view(), name="migration"),
  	path('migration_excel/', views.migration_excel, name='migration_list'),

] 

''' path('um/new',UMNew.as_view(), name="um_new"),
    path('um/edit/<int:pk>',UMEdit.as_view(), name="um_edit"),
    path('um/inactivar/<int:id>',um_inactivar, name="um_inactivar"),'''

    