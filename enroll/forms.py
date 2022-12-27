from django import forms
from django.forms import ModelForm
from .models import *

choices = (
    ('1', 'Formal (Public Sector)'),
    ('2', 'Informal (Private Sector)'),
)


class PlanForm(forms.Form):
    plan_type = forms.ChoiceField(choices=choices)


class CheckBox(forms.ModelForm):
    term = models.BooleanField()

    class Meta:
        model = Terms
        fields = '__all__'

    def clean(self):
        # data from the form is fetched using super function
        super(CheckBox, self).clean()

        # extract the term field
        term = self.cleaned_data.get('term')

        # conditions
        if not term:
            self._errors['term'] = self.error_class([
                'You must agree to the terms and Conditions'])
        return self.cleaned_data


class EnrolForm(forms.ModelForm):
    class Meta:
        model = Enroll
        fields = '__all__'

    def clean(self):

        # data from the form is fetched using super function
        super(EnrolForm, self).clean()

        # extract the term field
        mda_type = self.cleaned_data.get('mda_type')
        employment_number = self.cleaned_data.get('employment_number')
        nin = self.cleaned_data.get('nin')

        # conditions
        if not mda_type:
            self._errors['mda_type'] = self.error_class([
                'You must choose an MDA Type'])
        if not employment_number:
            self._errors['employment_number'] = self.error_class(['This field is compulsory'])
        if not nin:
            self._errors['nin'] = self.error_class(['This field is compulsory'])
        return self.cleaned_data


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Registration
        exclude = ('name',)
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['state'].queryset = State.objects.none()
        if 'country' in self.data:
            try:
                country_idm = int(self.data.get('country'))
                self.fields['state'].queryset = State.objects.filter(country_id=country_idm).order_by('name')
            except(ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['state'].queryset = self.instance.country.state_set.order_by('name')

        self.fields['lga'].queryset = Lga.objects.none()
        if 'state' in self.data:
            try:
                state_idm = int(self.data.get('state'))
                self.fields['lga'].queryset = Lga.objects.filter(state_id=state_idm).order_by('name')
            except(ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['lga'].queryset = self.instance.state.lga_set.order_by('name')

        self.fields['town'].queryset = Town.objects.none()
        if 'lga' in self.data:
            try:
                lga_idm = int(self.data.get('lga'))
                self.fields['town'].queryset = Town.objects.filter(lga_id=lga_idm).order_by('name')
            except(ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['town'].queryset = self.instance.lga.town_set.order_by('name')

    def clean(self):

        # data from the form is fetched using super function
        super(RegisterForm, self).clean()

        # extract the term field
        title = self.cleaned_data.get('title')
        surname = self.cleaned_data.get('surname')
        first_name = self.cleaned_data.get('first_name')
        middle_name = self.cleaned_data.get('middle_name')
        gender = self.cleaned_data.get('gender')
        mobile_number = self.cleaned_data.get('mobile_number')
        email = self.cleaned_data.get('email')
        date_of_birth = self.cleaned_data.get('date_of_birth')
        address = self.cleaned_data.get('address')
        blood_group = self.cleaned_data.get('blood_group')
        next_of_kin = self.cleaned_data.get('next_of_kin')
        next_of_kin_address = self.cleaned_data.get('next_of_kin_address')
        next_of_kin_phone_no = self.cleaned_data.get('next_of_kin_phone_no')
        relationship_with_kin = self.cleaned_data.get('relationship_with_kin')
        choose_plan = self.cleaned_data.get('choose_plan')
        school_name = self.cleaned_data.get('school_name')
        genotype = self.cleaned_data.get('genotype')
        religion = self.cleaned_data.get('religion')
        marital_status = self.cleaned_data.get('marital_status')
        no_of_dependants = self.cleaned_data.get('no_of_dependants')
        preferred_primary_hcp_lga = self.cleaned_data.get('preferred_primary_hcp_lga')
        preferred_primary_hcp = self.cleaned_data.get('preferred_primary_hcp')
        date_of_employment = self.cleaned_data.get('date_of_employment')
        spouse_name = self.cleaned_data.get('spouse_name')
        spouse_dob = self.cleaned_data.get('spouse_dob')
        spouse_sex = self.cleaned_data.get('spouse_sex')
        spouse_blood_group = self.cleaned_data.get('spouse_blood_group')
        child_name = self.cleaned_data.get('child_name')
        child_dob = self.cleaned_data.get('child_dob')
        child_gender = self.cleaned_data.get('child_gender')
        child_blood_group = self.cleaned_data.get('child_blood_group')
        principal_category = self.cleaned_data.get('principal_category')
        diabetes = self.cleaned_data.get('diabetes')
        hypertension = self.cleaned_data.get('hypertension')
        sickle_cell = self.cleaned_data.get('sickle_cell')
        cancer = self.cleaned_data.get('cancer')
        kidney_issue = self.cleaned_data.get('kidney_issue')

        # conditions
        if not title:
            self._errors['title'] = self.error_class([
                'This field is compulsory'])
        if not surname:
            self._errors['surname'] = self.error_class(['This field is compulsory'])
        if not first_name:
            self._errors['first_name'] = self.error_class(['This field is compulsory'])
        if not middle_name:
            self._errors['middle_name'] = self.error_class([
                'This field is compulsory'])
        if not gender:
            self._errors['gender'] = self.error_class(['This field is compulsory'])
        if not mobile_number:
            self._errors['mobile_number'] = self.error_class(['This field is compulsory'])
        if not email:
            self._errors['email'] = self.error_class([
                'This field is compulsory'])
        if not date_of_birth:
            self._errors['date_of_birth'] = self.error_class(['This field is compulsory'])
        if not address:
            self._errors['address'] = self.error_class(['This field is compulsory'])
        if not blood_group:
            self._errors['blood_group'] = self.error_class([
                'This field is compulsory'])
        if not next_of_kin:
            self._errors['next_of_kin'] = self.error_class(['This field is compulsory'])
        if not next_of_kin_address:
            self._errors['next_of_kin_address'] = self.error_class([
                'This field is compulsory'])
        if not next_of_kin_phone_no:
            self._errors['next_of_kin_phone_no'] = self.error_class(['This field is compulsory'])
        if not relationship_with_kin:
            self._errors['relationship_with_kin'] = self.error_class(['This field is compulsory'])
        if not choose_plan:
            self._errors['choose_plan'] = self.error_class([
                'This field is compulsory'])
        if not school_name:
            self._errors['school_name'] = self.error_class(['This field is compulsory'])
        if not genotype:
            self._errors['genotype'] = self.error_class(['This field is compulsory'])
        if not religion:
            self._errors['religion'] = self.error_class([
                'This field is compulsory'])
        if not marital_status:
            self._errors['marital_status'] = self.error_class(['This field is compulsory'])
        if not no_of_dependants:
            self._errors['no_of_dependants'] = self.error_class(['This field is compulsory'])
        if not preferred_primary_hcp_lga:
            self._errors['preferred_primary_hcp_lga'] = self.error_class([
                'This field is compulsory'])
        if not preferred_primary_hcp:
            self._errors['preferred_primary_hcp'] = self.error_class(['This field is compulsory'])
        if not date_of_employment:
            self._errors['date_of_employment'] = self.error_class(['This field is compulsory'])
        if not spouse_name:
            self._errors['spouse_name'] = self.error_class([
                'This field is compulsory'])
        if not spouse_dob:
            self._errors['spouse_dob'] = self.error_class(['This field is compulsory'])
        if not spouse_sex:
            self._errors['spouse_sex'] = self.error_class(['This field is compulsory'])
        if not spouse_blood_group:
            self._errors['spouse_blood_group'] = self.error_class([
                'This field is compulsory'])
        if not child_name:
            self._errors['child_name'] = self.error_class(['This field is compulsory'])
        if not child_dob:
            self._errors['child_dob'] = self.error_class([
                'This field is compulsory'])
        if not child_gender:
            self._errors['child_gender'] = self.error_class(['This field is compulsory'])
        if not child_blood_group:
            self._errors['child_blood_group'] = self.error_class(['This field is compulsory'])
        if not principal_category:
            self._errors['principal_category'] = self.error_class(['This field is compulsory'])
        if not diabetes:
            self._errors['diabetes'] = self.error_class(['This field is compulsory'])
        if not hypertension:
            self._errors['hypertension'] = self.error_class([
                'This field is compulsory'])
        if not sickle_cell:
            self._errors['sickle_cell'] = self.error_class(['This field is compulsory'])
        if not cancer:
            self._errors['cancer'] = self.error_class(['This field is compulsory'])
        if not kidney_issue:
            self._errors['kidney_issue'] = self.error_class([
                'This field is compulsory'])
        return self.cleaned_data


class CaptureForm(forms.ModelForm):
    class Meta:
        model = Capture
        fields = '__all__'

    def clean(self):

        # data from the form is fetched using super function
        super(CaptureForm, self).clean()

        # extract the term field
        capture = self.cleaned_data.get('name')

        # conditions
        if not capture:
            self._errors['name'] = self.error_class([
                'This field is compulsory'])


class InFormalForm(forms.ModelForm):
    class Meta:
        model = Informal
        fields = '__all__'

    def clean(self):

        # data from the form is fetched using super function
        super(InFormalForm, self).clean()

        # extract the term field
        mda_type = self.cleaned_data.get('mda_name')
        employment_number = self.cleaned_data.get('employment_id')
        nin = self.cleaned_data.get('nim')

        # conditions
        if not mda_type:
            self._errors['mda_name'] = self.error_class([
                'You must choose an MDA Type'])
        if not employment_number:
            self._errors['employment_id'] = self.error_class(['This field is compulsory'])
        if not nin:
            self._errors['nim'] = self.error_class(['This field is compulsory'])
        return self.cleaned_data

