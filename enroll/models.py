from django.db import models


# Create your models here.


class First(models.Model):
    choices = (
        ('1', 'Formal (Public Sector)'),
        ('2', 'Informal (Private Sector)'),
    )
    plan_type = models.CharField(max_length=30, blank=False, null=False, choices=choices)

    def __str__(self):
        return self.plan_type


class Terms(models.Model):
    term = models.BooleanField()


class Enroll(models.Model):
    choices = (
        ('1', 'Grace Hospital'),
        ('2', 'Gifted Hospice'),
        ('3', 'Tranquil Hospital'),
    )
    mda_type = models.CharField(max_length=30, blank=True, null=True, choices=choices)
    employment_number = models.CharField(max_length=50, blank=True, null=True)
    nin = models.CharField(max_length=50, blank=True, null=True)


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Lga(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Town(models.Model):
    lga = models.ForeignKey(Lga, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Registration(models.Model):
    sex = (
        ('1', 'Male'),
        ('2', 'Female'),
        ('3', 'Rather not say'),
    )
    group = (
        ('1', 'A'),
        ('2', 'B'),
        ('3', 'AB'),
        ('4', 'O'),
    )
    kin = (
        ('1', 'Cousin'),
        ('2', 'Nephew'),
        ('3', 'other')
    )
    plan = (
        ('1', 'Public Sector Plan'),
        ('2', 'Public Sector Plan')
    )
    school = (
        ('1', 'University of Ibadan College of Medicine'),
        ('2', 'Obafemi Awolowo University'),
        ('3', 'Ahmadu Bello University Faculty of Medicine'),
        ('4', 'University of Lagos College of Medicine'),
        ('5', 'Lagos State University College of Medicine'),
        ('6', 'Nsukka Faculty of Medical Sciences'),
        ('7', 'University of Ilorin College of Health Sciences'),
        ('8', 'Delta State University'),
        ('9', ' Niger Delta University College of Health Sciences'),
        ('10', 'Imo State University Faculty of Medicine'),
    )
    genotypes = (
        ('1', 'AA'),
        ('2', 'AO'),
        ('3', 'BB'),
        ('4', 'BO'),
        ('5', 'AB'),
        ('6', 'OO')
    )
    religions = (
        ('1', 'Christian'),
        ('2', 'Muslim'),
        ('3', 'other')
    )
    status = (
        ('1', 'Single'),
        ('2', 'Married')
    )
    dependants = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )
    hcp_lga = (
        ('1', 'Ajeromi-Ifelodun'),
        ('2', 'Abuja Municipal Area Council	'),
        ('3', 'Aguata'),
        ('4', 'Awgu'),
    )
    hcp = (
        ('1', 'Sancta Maria Specialist & Mat.'),
        ('2', 'Abia State University Teaching Hospital'),
        ('3', 'Federal Medical Centre, Umuahia'),
        ('4', 'Life Care Clinics Ltd'),
    )
    spouse_sex = (
        ('1', 'Male'),
        ('2', 'Female'),
        ('3', 'Rather not say'),
    )
    spouse_group = (
        ('1', 'A'),
        ('2', 'B'),
        ('3', 'AB'),
        ('4', 'O'),
    )
    diabetic = (
        ('1', 'type 1'),
        ('2', 'type 2'),
        ('3', 'Gestational'),
        ('4', 'None'),
    )
    hyper = (
        ('1', 'Primary'),
        ('2', 'Secondary'),
        ('3', 'None'),
    )
    sickle = (
        ('1', 'Sickle Cell Anemia (SS)'),
        ('2', 'Sickle Hemoglobin-C Disease (SC)'),
        ('3', 'Sickle Beta-Plus Thalassemia'),
        ('4', 'Sickle Beta-Zero Thalassemia'),
        ('5', 'None'),
    )
    cancer_type = (
        ('1', 'Carcinoma'),
        ('2', 'Sarcoma'),
        ('3', 'Leukemia'),
        ('4', 'Lymphoma'),
        ('5', 'None'),
    )
    kidneys = (
        ('1', 'Kidney Stones'),
        ('2', 'Chronic Kidney Disease'),
        ('3', 'Urinary tract infections'),
        ('4', 'Glomerulonephritis'),
        ('5', 'None'),
    )
    name = models.CharField(max_length=150, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=30, blank=True, null=True, choices=sex)
    mobile_number = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    date_of_birth = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    blood_group = models.CharField(max_length=30, blank=True, null=True, choices=group)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True)
    lga = models.ForeignKey(Lga, on_delete=models.SET_NULL, blank=True, null=True)
    town = models.ForeignKey(Town, on_delete=models.SET_NULL, blank=True, null=True)
    next_of_kin = models.CharField(max_length=50, blank=True, null=True)
    next_of_kin_address = models.CharField(max_length=50, blank=True, null=True)
    next_of_kin_phone_no = models.CharField(max_length=50, blank=True, null=True)
    relationship_with_kin = models.CharField(max_length=50, blank=True, null=True, choices=kin)
    choose_plan = models.CharField(max_length=50, blank=True, null=True, choices=plan)
    school_name = models.CharField(max_length=50, blank=True, null=True, choices=school)
    genotype = models.CharField(max_length=30, blank=True, null=True, choices=genotypes)
    religion = models.CharField(max_length=50, blank=True, null=True, choices=religions)
    marital_status = models.CharField(max_length=50, blank=True, null=True, choices=status)
    no_of_dependants = models.CharField(max_length=50, blank=True, null=True, choices=dependants)
    preferred_primary_hcp_lga = models.CharField(max_length=50, blank=True, null=True, choices=hcp_lga)
    preferred_primary_hcp = models.CharField(max_length=50, blank=True, null=True, choices=hcp)
    date_of_employment = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    spouse_name = models.CharField(max_length=50, blank=True, null=True)
    spouse_dob = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    spouse_sex = models.CharField(max_length=50, blank=True, null=True, choices=spouse_sex)
    spouse_blood_group = models.CharField(max_length=50, blank=True, null=True, choices=spouse_group)
    spouse_image = models.ImageField(upload_to='images', null=True, blank=True)
    child_name = models.CharField(max_length=50, blank=True, null=True)
    child_dob = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    child_gender = models.CharField(max_length=50, blank=True, null=True, choices=sex)
    child_blood_group = models.CharField(max_length=50, blank=True, null=True, choices=group)
    child_image = models.ImageField(upload_to='images', null=True, blank=True)
    principal_category = models.CharField(max_length=50, blank=True, null=True, choices=kin)
    diabetes = models.CharField(max_length=50, blank=True, null=True, choices=diabetic)
    hypertension = models.CharField(max_length=50, blank=True, null=True, choices=hyper)
    sickle_cell = models.CharField(max_length=50, blank=True, null=True, choices=sickle)
    cancer = models.CharField(max_length=50, blank=True, null=True, choices=cancer_type)
    kidney_issue = models.CharField(max_length=50, blank=True, null=True, choices=kidneys)

    def __str__(self):
        return str(self.surname)


class Capture(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)


class Informal(models.Model):
    new_choices = (
        ('1', 'Domain Hospital'),
        ('2', 'Western Hospice'),
        ('3', 'Daniel Hospital'),
    )
    mda_name = models.CharField(max_length=30, blank=True, null=True, choices=new_choices)
    employment_id = models.CharField(max_length=50, blank=True, null=True)
    nim = models.CharField(max_length=50, blank=True, null=True)