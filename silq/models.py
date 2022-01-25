from django.db import models
# from django.contrib.auth.models import User
from users.models import UserProfile

# Create your models here.


class Project(models.Model):
    STYLEITEM = (
        ('Polo', 'Polo'),
        ('Hoodie', 'Hoodie'),
        ('Shorts', 'Shorts'),
        ('Pants', 'Pants'),
        ('Shirts', 'Shirts'),
        ('T-Shirts', 'T-Shirts'),
        ('Trouser', 'Trouser'),
        ('Bag', 'Bag'),
        ('Joggers', 'Joggers'),
        ('Sweat-Shirt', 'Sweat-Shirt'),
        ('Boxers', 'Boxers'),
        ('UnderWear', 'UnderWear'),
    )
    customer = models.ForeignKey(
        UserProfile, null=True, blank=True, on_delete=models.CASCADE
    )
    project_name = models.CharField(max_length=200, null=True, blank=True)
    project_note = models.CharField(max_length=300, null=True, blank=True)
    date = models.DateField(blank=True, null=True)
    version = models.CharField(max_length=300, null=True, blank=True)
    style = models.CharField(max_length=300, null=True,
                             blank=True, choices=STYLEITEM)
    project_description = models.CharField(
        max_length=300, null=True, blank=True)
    style_hash = models.CharField(max_length=300, null=True, blank=True)
    image_link = models.CharField(max_length=300, null=True, blank=True)
    pdf_link = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return str(self.customer)


class Bill_Of_Materials(models.Model):
    STYLEITEM = (
        ('Fabric', 'Fabric'),
        ('Thread', 'Thread'),
        ('Button', 'Button'),
        ('Interfacing', 'Interfacing'),
        ('Nect Tape', 'Nect Tape'),
        ('Zipper', 'Zipper'),
        ('Jaquard Label', 'Jaquard Label'),
        ('Bottom Tape', 'Bottom Tape'),
        ('Embroidery', 'Embroidery'),
        ('Buckle', 'Buckle'),
        ('Aglets', 'Aglets'),
        ('Heel', 'Heel'),
        ('Toplift', 'Toplift'),
        ('Foam Padding', 'Foam Padding'),
        ('Socks', 'Socks'),
        ('Elastic', 'Elastic'),
    )
    CRITICALITY = (
        ('Critical', 'Critical'),
        ('Minor', 'Minor'),
        ('Major', 'Major'),
    )
    project = models.ForeignKey(
        Project, null=True, blank=True, on_delete=models.CASCADE)
    item = models.CharField(max_length=500, null=True, blank=True)
    item_style = models.CharField(
        max_length=500, null=True, blank=True, choices=STYLEITEM)
    description = models.CharField(max_length=500, null=True, blank=True)
    color = models.CharField(max_length=500, null=True, blank=True)
    item_content = models.CharField(max_length=500, null=True, blank=True)
    placement = models.CharField(max_length=500, null=True, blank=True)
    size = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.CharField(max_length=500, null=True, blank=True)
    supplier = models.CharField(max_length=500, null=True, blank=True)
    comments = models.CharField(max_length=500, null=True, blank=True)
    pricing_estimate = models.CharField(max_length=200, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    issue_code = models.CharField(max_length=500, null=True, blank=True)
    issue_description = models.CharField(max_length=500, null=True, blank=True)
    criticality = models.CharField(
        max_length=500, null=True, blank=True, choices=CRITICALITY)
    silq_comment = models.CharField(max_length=500, null=True, blank=True)
    option_1 = models.CharField(max_length=500, null=True, blank=True)
    option_2 = models.CharField(max_length=500, null=True, blank=True)
    option_3 = models.CharField(max_length=500, null=True, blank=True)
    customer_response = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)


class Measurement_Chart(models.Model):
    CRITICALITY = (
        ('Critical', 'Critical'),
        ('Minor', 'Minor'),
        ('Major', 'Major'),
    )
    project = models.ForeignKey(
        Project, null=True, blank=True, on_delete=models.CASCADE)
    item2 = models.CharField(max_length=500, null=True, blank=True)
    pom = models.CharField(max_length=500, null=True, blank=True)
    description2 = models.CharField(max_length=500, null=True, blank=True)
    xtra_small = models.CharField(max_length=500, null=True, blank=True)
    small = models.CharField(max_length=500, null=True, blank=True)
    medium = models.CharField(max_length=500, null=True, blank=True)
    large = models.CharField(max_length=500, null=True, blank=True)
    xtra_large = models.CharField(max_length=500, null=True, blank=True)
    xtra_large2 = models.CharField(max_length=500, null=True, blank=True)
    xtra_large3 = models.CharField(max_length=500, null=True, blank=True)
    tol_plus = models.CharField(max_length=500, null=True, blank=True)
    tol_minus = models.CharField(max_length=500, null=True, blank=True)
    comments2 = models.CharField(max_length=500, null=True, blank=True)
    issue_code2 = models.CharField(max_length=500, null=True, blank=True)
    issue_description2 = models.CharField(
        max_length=500, null=True, blank=True)
    criticality2 = models.CharField(
        max_length=500, null=True, blank=True, choices=CRITICALITY)
    silq_comment2 = models.CharField(max_length=500, null=True, blank=True)
    option_1_2 = models.CharField(max_length=500, null=True, blank=True)
    option_2_2 = models.CharField(max_length=500, null=True, blank=True)
    option_3_2 = models.CharField(max_length=500, null=True, blank=True)
    customer_response2 = models.CharField(
        max_length=500, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)


class Other_Issue(models.Model):
    CRITICALITY = (
        ('Critical', 'Critical'),
        ('Minor', 'Minor'),
        ('Major', 'Major'),
    )
    SECTION = (
        ('Construction', 'Construction'),
        ('Stitching', 'Stitching'),
    )
    project = models.ForeignKey(
        Project, null=True, blank=True, on_delete=models.CASCADE)
    section = models.CharField(
        max_length=500, null=True, blank=True, choices=SECTION)
    item3 = models.CharField(max_length=500, null=True, blank=True)
    issue_code3 = models.CharField(max_length=500, null=True, blank=True)
    issue_description3 = models.CharField(
        max_length=500, null=True, blank=True)
    criticality3 = models.CharField(
        max_length=500, null=True, blank=True, choices=CRITICALITY)
    silq_comments3 = models.CharField(max_length=500, null=True, blank=True)
    option_1_3 = models.CharField(max_length=500, null=True, blank=True)
    option_2_3 = models.CharField(max_length=500, null=True, blank=True)
    option_3_3 = models.CharField(max_length=500, null=True, blank=True)
    customer_response_3 = models.CharField(
        max_length=500, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)


class Po_Summary(models.Model):
    PROJECT_TYPE = (
        ('Sampling', 'Sampling'),
        ('Production Management', 'Production Management'),
        ('The Works', 'The Works'),
        ('Tech Pack Bundle', 'Tech Pack Bundle'),
    )
    STATUS = (
        ('Complete', 'Complete'),
        ('In Progress', 'In Progress'),
        ('Not Started', 'Not Started'),
    )
    customer = models.ForeignKey(
        UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    project_type = models.CharField(
        max_length=500, null=True, blank=True, choices=PROJECT_TYPE)
    project_name = models.CharField(max_length=200, blank=True, null=True)
    customer_po_number = models.CharField(
        max_length=200, blank=True, null=True)
    total_po_value = models.CharField(max_length=200, blank=True, null=True)
    project_recieved_date = models.DateField(
        max_length=200, blank=True, null=True)
    project_estimated_delivery_date = models.DateField(
        max_length=200, blank=True, null=True)
    project_actual_delivery_date = models.DateField(
        max_length=200, blank=True, null=True)
    status = models.CharField(
        max_length=200, blank=True, null=True, choices=STATUS)


class Style_Data(models.Model):
    SAMPLE_SELECT = (
        ('Fit Sample', 'Fit Sample'),
        ('Lab Dip', 'Lab Dip'),
        ('Pre-Production', 'Pre-Production'),
        ('Swatch', 'Swatch'),
        ('Print Strike-O', 'Print Strike-O'),
        ('Sewing Trim', 'Sewing Trim'),
        ('Packaging', 'Packaging'),
        ('Top Sample', 'Top Sample'),
        ('Size Set', 'Size Set'),
        ('Fit Sample', 'Fit Sample'),
        ('Photo Sample', 'Photo Sample'),
    )
    STATUS_VENDOR = (
        ('RECEIVED', 'RECEIVED'),
        ('PENDING', 'PENDING'),
        ('NOT REQUIRED', 'NOT REQUIRED'),
    )
    SILQ_APPROVAL = (
        ('APPROVED', 'APPROVED'),
        ('PENDING', 'PENDING'),
        ('REJECTED', 'REJECTED'),
    )
    CUSTOMER_APPROVAL = (
        ('APPROVED', 'APPROVED'),
        ('PENDING', 'PENDING'),
        ('REJECTED', 'REJECTED'),
        ('NOT REQUIRED', 'NOT REQUIRED'),
        ('LOCAL APPROVAL', 'LOCAL APPROVAL'),
    )
    customer = models.ForeignKey(
        UserProfile, null=True, blank=True, on_delete=models.CASCADE)
    po_name = models.CharField(max_length=200, blank=True, null=True)
    style_name = models.CharField(max_length=200, blank=True, null=True)
    style_hash = models.CharField(max_length=200, blank=True, null=True)
    customer_style_item_description = models.CharField(
        max_length=200, blank=True, null=True)
    color = models.CharField(max_length=200, blank=True, null=True)
    sample = models.CharField(
        max_length=200, blank=True, null=True, choices=SAMPLE_SELECT)
    sample_comment = models.CharField(max_length=200, blank=True, null=True)
    sample_quantity = models.CharField(max_length=200, blank=True, null=True)
    assigned_inspector = models.CharField(
        max_length=200, blank=True, null=True)
    status_from_vendor = models.CharField(
        max_length=200, blank=True, null=True, choices=STATUS_VENDOR)
    date_recieved_from_vendor = models.DateField(
        max_length=200, blank=True, null=True)
    silq_approval_status = models.CharField(
        max_length=200, blank=True, null=True, choices=SILQ_APPROVAL)
    silq_comment = models.CharField(max_length=200, blank=True, null=True)
    date_sent_to_customer = models.DateField(
        max_length=200, blank=True, null=True)
    courier_number = models.CharField(max_length=200, blank=True, null=True)
    approval_status_from_customer = models.CharField(
        max_length=200, blank=True, null=True, choices=CUSTOMER_APPROVAL)
    date_approved_by_customer = models.DateField(
        max_length=200, blank=True, null=True)
    comment_from_customer = models.CharField(
        max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        if self.po_name:
            return str(self.po_name)
        else:
            return self.customer
