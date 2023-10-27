from django import forms
from stacktry.models import Lesson, ParticipationCount
from django.core.files.uploadedfile import InMemoryUploadedFile
from ads.humanize import naturalsize



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



class ParticipationCountForm(forms.Form):
    class Meta:
        model = ParticipationCount
        fields = ['jiu_jitsu_count', 'grappling_count', 'kick_boxing_count', 'yoga_count']
