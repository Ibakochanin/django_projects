from django import forms
from stacktry.models import Lesson, ParticipationCount
from django.core.files.uploadedfile import InMemoryUploadedFile
from ads.humanize import naturalsize
from accounts.models import CustomUser


# Create the form class.

class UserPreferencesForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)

    # Call this 'picture' so it gets copied from the form to the in-memory model
    # It will not be the "bytes", it will be the "InMemoryUploadedFile"
    # because we need to pull out things like content_type
    profile_picture = forms.FileField(required=False, label='File to Upload <= '+max_upload_limit_text)
    upload_field_name = 'profile_picture'


    colors = ['white', 'blue', 'purple', 'brown', 'black']
    martial_arts_fields = {}
    for color in colors:
        martial_arts_fields[color + '_jiu_jitsu_count'] = forms.IntegerField(
            label=f'{color.capitalize()} Jiu Jitsu Count', initial=0
        )
    class Meta:
        model = CustomUser
        fields = ['belt', 'stripes', 'member_type', 'gym_choice', 'profile_picture']  # Include 'stripes' field in the form
        widgets = {
            'belt': forms.Select(attrs={'class': 'form-control col-3'}),
            'stripes': forms.Select(attrs={'class': 'form-control col-3'}),  # Add stripes field widget
            'member_type': forms.Select(attrs={'class': 'form-control col-3'}),
            'gym_choice': forms.Select(attrs={'class': 'form-control col-3'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        user = cleaned_data.get('profile_picture')
        if user is None:
            return
        if len(user) > self.max_upload_limit:
            self.add_error('profile_picture', "File must be < "+self.max_upload_limit_text+" bytes")

    def save(self, commit=True):
        instance = super(UserPreferencesForm, self).save(commit=False)

        # We only need to adjust picture if it is a freshly uploaded file
        f = instance.profile_picture   # Make a copy
        if isinstance(f, InMemoryUploadedFile):  # Extract data from the form to the model
            bytearr = f.read()
            instance.content_type = f.content_type
            instance.profile_picture = bytearr  # Overwrite with the actual image data

        if commit:
            instance.save()

        return instance

class ParticipationCountForm(forms.ModelForm):
    class Meta:
        model = ParticipationCount
        fields = ['user', 'white_jiu_jitsu_count', 'blue_jiu_jitsu_count', 'purple_jiu_jitsu_count', 'brown_jiu_jitsu_count', 'black_jiu_jitsu_count']
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'white_jiu_jitsu_count': forms.TextInput(attrs={'class': 'form-control col-2'}),
            'blue_jiu_jitsu_count': forms.TextInput(attrs={'class': 'form-control col-2'}),
            'purple_jiu_jitsu_count': forms.TextInput(attrs={'class': 'form-control col-2'}),
            'brown_jiu_jitsu_count': forms.TextInput(attrs={'class': 'form-control col-2'}),
            'black_jiu_jitsu_count': forms.TextInput(attrs={'class': 'form-control col-2'}),
        }

    def init(self, args, **kwargs):
        instance = kwargs.pop('instance', None)
        super().init(args, **kwargs)
        self.instance = instance
        if instance:
            self.fields['user'].initial = instance.user



# Create the form class.

class CreateForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)

    # Call this 'picture' so it gets copied from the form to the in-memory model
    # It will not be the "bytes", it will be the "InMemoryUploadedFile"
    # because we need to pull out things like content_type
    picture = forms.FileField(required=False, label='File to Upload <= '+max_upload_limit_text)
    upload_field_name = 'picture'



    # Hint: this will need to be changed for use in the ads application :)
    class Meta:
        model = Lesson
        fields = ['title', 'text', 'picture', 'day', 'spot', 'time', 'category', 'color', 'school']  # Picture is manual

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'day': forms.Select(attrs={'class': 'form-control'}),
            'spot': forms.Select(attrs={'class': 'form-control'}),
            'time': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'color': forms.Select(attrs={'class': 'form-control'}),
            'school': forms.Select(attrs={'class': 'form-control'}),
        }

    # Validate the size of the picture
    def clean(self):
        cleaned_data = super().clean()
        lesson = cleaned_data.get('picture')
        if lesson is None:
            return
        if len(lesson) > self.max_upload_limit:
            self.add_error('picture', "File must be < "+self.max_upload_limit_text+" bytes")

    def clean_text(self):
       text = self.cleaned_data.get('text')
       paragraphs = ['<p>{}</p>'.format(line) for line in text.splitlines()]
       cleaned_text = ''.join(paragraphs)
       return cleaned_text


    # Convert uploaded File object to a picture
    def save(self, commit=True):
        instance = super(CreateForm, self).save(commit=False)

        # We only need to adjust picture if it is a freshly uploaded file
        f = instance.picture   # Make a copy
        if isinstance(f, InMemoryUploadedFile):  # Extract data from the form to the model
            bytearr = f.read()
            instance.content_type = f.content_type
            instance.picture = bytearr  # Overwrite with the actual image data

        if commit:
            instance.save()

        return instance



