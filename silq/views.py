from django.shortcuts import redirect, render
from silq.models import Bill_Of_Materials, Measurement_Chart, Other_Issue, Po_Summary, Project, Style_Data
from .forms import Bill_Of_Material_Form, Measurement_Chart_Form, Other_Issue_Form, PO_Summary_Form, Project_Form, Style_Data_Form
from users.models import UserProfile
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def admin_page(request):
    project = Project.objects.all()
    total_project = project.count()
    client = UserProfile.objects.filter(user_type='customer')
    total_client = client.count()
    issue_bill_material = Bill_Of_Materials.objects.filter(issue_code=1)
    issue_measurement = Measurement_Chart.objects.filter(issue_code2=1)
    issue_other = Other_Issue.objects.filter(issue_code3=1)
    total_issues = int(issue_bill_material.count()) + \
        int(issue_measurement.count()) + int(issue_other.count())

    context = {'total_project': total_project,
               'total_client': total_client, 'total_issues': total_issues}
    return render(request, 'admin_page.html', context)


@login_required(login_url='login')
def staff_page(request):
    context = {}
    return render(request, 'staff_page.html', context)


@login_required(login_url='login')
def customer_page(request):
    userProfile = UserProfile.objects.get(user=request.user)
    usertype = userProfile.user_type
    if usertype == 'admin':
        return redirect('admin_page')
    elif usertype == 'customer':
        return redirect('customer_page')
    elif usertype == 'staff':
        return redirect('team_member_page')
    context = {}
    return render(request, 'customer_page.html', context)


@login_required(login_url='login')
def my_customers(request):
    # userprofile = UserProfile.objects.get(user=request.user)
    customers = UserProfile.objects.filter(user_type='customer')
    context = {'customers': customers}
    return render(request, 'all_customer_page.html', context)


@login_required(login_url='login')
def my_team_member(request):
    # userprofile = UserProfile.objects.get(user=request.user)
    team_member = UserProfile.objects.filter(user_type='staff')
    context = {'team_member': team_member}
    return render(request, 'team_members.html', context)


@login_required(login_url='login')
def my_projects(request):
    projects = Project.objects.all()
    customers = UserProfile.objects.filter(user_type='customer')
    if request.method == 'POST':
        project_name = request.POST.get('name')
        customer_id = request.POST.get('customer')
        note = request.POST.get('note')
        customer = UserProfile.objects.get(id=int(customer_id))
        Project.objects.create(
            customer=customer,
            project_name=project_name,
            project_note=note,
        )
        return redirect('my_projects')
    context = {'customers': customers, "projects": projects}
    return render(request, 'all_projects.html', context)


@login_required(login_url='login')
def project_profile(request, pk):
    project = Project.objects.get(id=pk)
    bill_of_material_data = Bill_Of_Materials.objects.filter(project=project)
    measurement_chart_data = Measurement_Chart.objects.filter(project=project)
    other_issue_data = Other_Issue.objects.filter(project=project)
    project_form = Project_Form(instance=project)
    bill_of_material = Bill_Of_Material_Form()
    measurement_chart = Measurement_Chart_Form()
    other_issue = Other_Issue_Form()
    context = {
        'project_form': project_form,
        'bill_of_material': bill_of_material,
        'measurement_chart': measurement_chart,
        'other_issue': other_issue,
        'project': project,
        'bill_of_material_data': bill_of_material_data,
        'measurement_chart_data': measurement_chart_data,
        'other_issue_data': other_issue_data,
    }
    return render(request, 'project_profile.html', context)


@login_required(login_url='login')
def new_bill_of_material(request, pk):
    project = Project.objects.get(id=pk)
    form = Bill_Of_Material_Form()
    if request.method == 'POST':
        form = Bill_Of_Material_Form(request.POST)
        if form.is_valid():
            new_bill = form.save(commit=False)
            new_bill.project = project
            new_bill.save()
            return redirect('project_profile', pk=pk)
    context = {'form': form}
    return render(request, 'project_profile.html', context)


@login_required(login_url='login')
def new_measurement_chart(request, pk):
    project = Project.objects.get(id=pk)
    form = Measurement_Chart_Form()
    if request.method == 'POST':
        form = Measurement_Chart_Form(request.POST)
        if form.is_valid():
            new_bill = form.save(commit=False)
            new_bill.project = project
            new_bill.save()
            return redirect('project_profile', pk=pk)
    context = {'form': form}
    return render(request, 'project_profile.html', context)


@login_required(login_url='login')
def new_other_issues(request, pk):
    project = Project.objects.get(id=pk)
    form = Other_Issue_Form()
    if request.method == 'POST':
        form = Other_Issue_Form(request.POST)
        if form.is_valid():
            new_bill = form.save(commit=False)
            new_bill.project = project
            new_bill.save()
            return redirect('project_profile', pk=pk)
    context = {'form': form}
    return render(request, 'project_profile.html', context)


@login_required(login_url='login')
def edit_bill_of_material(request, pk, id):
    project = Project.objects.get(id=pk)
    bill_material = Bill_Of_Materials.objects.get(id=id)
    form = Bill_Of_Material_Form(instance=bill_material)
    if request.method == 'POST':
        form = Bill_Of_Material_Form(request.POST, instance=bill_material)
        if form.is_valid():
            new_bill = form.save(commit=False)
            new_bill.project = project
            new_bill.save()
            return redirect('project_profile', pk=pk)
    context = {'form': form, 'project': project,
               'bill_material': bill_material}
    return render(request, 'edit_bill_of_materials.html', context)


@login_required(login_url='login')
def delete_bill_of_material(request, pk, id):
    project = Project.objects.get(id=pk)
    bill_material = Bill_Of_Materials.objects.get(id=id)
    form = Bill_Of_Material_Form(instance=bill_material)
    if request.method == 'POST':
        bill_material.delete()
        return redirect('project_profile', pk=pk)
    context = {'form': form, 'project': project,
               'bill_material': bill_material}
    return render(request, 'edit_bill_of_materials.html', context)


@login_required(login_url='login')
def edit_measurement_chart(request, pk, id):
    project = Project.objects.get(id=pk)
    measurement_chart = Measurement_Chart.objects.get(id=id)
    form = Measurement_Chart_Form(instance=measurement_chart)
    if request.method == 'POST':
        form = Measurement_Chart_Form(request.POST, instance=measurement_chart)
        if form.is_valid():
            new_bill = form.save(commit=False)
            new_bill.project = project
            new_bill.save()
            return redirect('project_profile', pk=pk)
    context = {'form': form, 'project': project,
               'measurement_chart': measurement_chart}
    return render(request, 'edit_measurement_chart.html', context)


@login_required(login_url='login')
def delete_measurement_chart(request, pk, id):
    project = Project.objects.get(id=pk)
    measurement_chart = Measurement_Chart.objects.get(id=id)
    form = Measurement_Chart_Form(instance=measurement_chart)
    if request.method == 'POST':
        measurement_chart.delete()
        return redirect('project_profile', pk=pk)
    context = {'form': form, 'project': project,
               'measurement_chart': measurement_chart}
    return render(request, 'edit_measurement_chart.html', context)


@login_required(login_url='login')
def edit_other_issues(request, pk, id):
    project = Project.objects.get(id=pk)
    other_issues = Other_Issue.objects.get(id=id)
    form = Other_Issue_Form(instance=other_issues)
    if request.method == 'POST':
        form = Other_Issue_Form(request.POST, instance=other_issues)
        if form.is_valid():
            new_bill = form.save(commit=False)
            new_bill.project = project
            new_bill.save()
            return redirect('project_profile', pk=pk)
    context = {'form': form, 'project': project,
               'other_issues': other_issues}
    return render(request, 'edit_other_issue.html', context)


@login_required(login_url='login')
def delete_other_issues(request, pk, id):
    project = Project.objects.get(id=pk)
    other_issues = Other_Issue.objects.get(id=id)
    form = Other_Issue_Form(instance=other_issues)
    if request.method == 'POST':
        other_issues.delete()
        return redirect('project_profile', pk=pk)
    context = {'form': form, 'project': project,
               'other_issues': other_issues}
    return render(request, 'edit_other_issue.html', context)


@login_required(login_url='login')
def project_overview(request, pk):
    project = Project.objects.get(id=pk)
    project_form = Project_Form(instance=project)
    if request.method == 'POST':
        project_form = Project_Form(request.POST, instance=project)
        if project_form.is_valid():
            project_form.save()
            # edit_project.customer = project.customer
            # edit_project.project_name = project.project_name
            # edit_project.save()
            return redirect('project_profile', pk=pk)
    context = {'project': project, 'project_form': project_form}
    return render(request, 'project_profile.html', context)


@login_required(login_url='login')
def time_and_action_page(request, pk):
    customer = UserProfile.objects.get(id=pk)
    po_summary_data = Po_Summary.objects.filter(customer=customer)
    # po_dropdown = po_summary_data.distinct('project_name')
    style_data = Style_Data.objects.filter(customer=customer)
    po_summary_form = PO_Summary_Form()
    style_data_form = Style_Data_Form()
    # style_data_form.fields['po_name'].queryset = Po_Summary.objects.filter(
    #     customer=customer)
    if request.method == 'POST':
        po_summary_form = PO_Summary_Form(request.POST)
        if po_summary_form.is_valid():
            po_form = po_summary_form.save(commit=False)
            po_form.customer = customer
            po_form.save()
            return redirect('time_and_action_page', pk=pk)
    context = {'po_summary_form': po_summary_form,
               'style_data_form': style_data_form,
               'po_summary_data': po_summary_data,
               'customer': customer,
               'style_data': style_data,
               }
    return render(request, 'time_and_action.html', context)


@login_required(login_url='login')
def add_style_data(request, pk):
    customer = UserProfile.objects.get(id=pk)
    style_data = Style_Data.objects.filter(customer=customer)
    style_data_form = Style_Data_Form()
    if request.method == 'POST':
        po_name = request.POST.get('po_select')
        print("po", po_name)
        style_data_form = Style_Data_Form(request.POST)
        if style_data_form.is_valid():
            style_form = style_data_form.save(commit=False)
            style_form.customer = customer
            style_form.po_name = po_name
            style_form.save()
            return redirect('time_and_action_page', pk=pk)
    context = {'style_data': style_data,
               'style_data_form': style_data_form,
               'customer': customer
               }
    return render(request, 'time_and_action.html', context)


@login_required(login_url='login')
def edit_po_summary(request, pk, id):
    customer = UserProfile.objects.get(id=pk)
    po_summary = Po_Summary.objects.get(id=id)
    form = PO_Summary_Form(instance=po_summary)
    if request.method == 'POST':
        form = PO_Summary_Form(request.POST, instance=po_summary)
        if form.is_valid():
            new_bill = form.save(commit=False)
            new_bill.customer = customer
            new_bill.save()
            return redirect('time_and_action_page', pk=pk)
    context = {'form': form, 'customer': customer,
               'po_summary': po_summary}
    return render(request, 'edit_po_summary.html', context)


@login_required(login_url='login')
def delete_po_summary(request, pk, id):
    # customer = UserProfile.objects.get(id=pk)
    po_summary = Po_Summary.objects.get(id=id)
    form = PO_Summary_Form(instance=po_summary)
    if request.method == 'POST':
        po_summary.delete()
        return redirect('time_and_action_page', pk=pk)
    context = {'form': form}
    return render(request, 'edit_po_summary.html', context)


@login_required(login_url='login')
def edit_style_data(request, pk, id):
    customer = UserProfile.objects.get(id=pk)
    style_data = Style_Data.objects.get(id=id)
    po_summary_data = Po_Summary.objects.filter(customer=customer)
    style_data_form = Style_Data_Form(instance=style_data)
    style_data_form.fields['po_name'].queryset = Po_Summary.objects.filter(
        customer=customer)
    if request.method == 'POST':
        po_name = request.POST.get('po_select')
        style_data_form = Style_Data_Form(request.POST, instance=style_data)
        if style_data_form.is_valid():
            new_style = style_data_form.save(commit=False)
            new_style.customer = customer
            new_style.po_name = po_name
            new_style.save()
            return redirect('time_and_action_page', pk=pk)
    context = {'style_data_form': style_data_form, 'customer': customer,
               'style_data': style_data,
               "po_summary_data": po_summary_data}
    return render(request, 'edit_style_data.html', context)


@login_required(login_url='login')
def delete_style_data(request, pk, id):
    # customer = UserProfile.objects.get(id=pk)
    style_data = Style_Data.objects.get(id=id)
    style_data_form = Style_Data_Form(instance=style_data)
    if request.method == 'POST':
        style_data.delete()
        return redirect('time_and_action_page', pk=pk)
    context = {'style_data_form': style_data_form}
    return render(request, 'edit_style_data.html', context)
