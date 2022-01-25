from django.urls import path
from .views import admin_page, customer_page, staff_page, my_customers, my_team_member, my_projects, project_profile, new_bill_of_material, new_measurement_chart, new_other_issues, edit_bill_of_material, delete_bill_of_material, edit_measurement_chart, delete_measurement_chart, edit_other_issues, delete_other_issues, project_overview, time_and_action_page, add_style_data, edit_po_summary, delete_po_summary, edit_style_data, delete_style_data
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin_page', admin_page, name='admin_page'),
    path('', customer_page, name='customer_page'),
    path('team_member_page', staff_page, name='team_member_page'),
    path('my_customers', my_customers, name='my_customers'),
    path('my_customers/<str:pk>/time_and_action_page',
         time_and_action_page, name='time_and_action_page'),
    path('my_customers/<str:pk>/add_style_data',
         add_style_data, name='add_style_data'),
    path('my_customers/<str:pk>/edit_po_summary/<str:id>',
         edit_po_summary, name='edit_po_summary'),
    path('my_customers/<str:pk>/delete_po_summary/<str:id>',
         delete_po_summary, name='delete_po_summary'),
    path('my_customers/<str:pk>/edit_style_data/<str:id>',
         edit_style_data, name='edit_style_data'),
    path('my_customers/<str:pk>/delete_style_data/<str:id>',
         delete_style_data, name='delete_style_data'),
    path('my_team', my_team_member, name='my_team'),
    path('my_projects', my_projects, name='my_projects'),
    path('project_profile/<str:pk>/', project_profile, name='project_profile'),
    path('project_profile/<str:pk>/project_overview',
         project_overview, name='project_overview'),
    path('project_profile/<str:pk>/new_bill_material',
         new_bill_of_material, name='new_bill_material'),
    path('project_profile/<str:pk>/new_measurement_chart',
         new_measurement_chart, name='new_measurement_chart'),
    path('project_profile/<str:pk>/other_issues',
         new_other_issues, name='other_issues'),
    path('project_profile/<str:pk>/edit_bill_material/<str:id>/',
         edit_bill_of_material, name='edit_bill_material'),
    path('project_profile/<str:pk>/delete_bill_material/<str:id>/',
         delete_bill_of_material, name='delete_bill_material'),
    path('project_profile/<str:pk>/edit_measurement_chart/<str:id>/',
         edit_measurement_chart, name='edit_measurement_chart'),
    path('project_profile/<str:pk>/delete_measurement_chart/<str:id>/',
         delete_measurement_chart, name='delete_measurement_chart'),
    path('project_profile/<str:pk>/edit_other_issue/<str:id>/',
         edit_other_issues, name='edit_other_issue'),
    path('project_profile/<str:pk>/delete_other_issue/<str:id>/',
         delete_other_issues, name='delete_other_issue'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
