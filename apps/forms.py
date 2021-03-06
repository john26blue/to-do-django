from django.forms import ModelForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from apps.models import *

class CreateForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['content', 'status', 'marked']

    def __init__(self, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.field_class = 'col-sm-8'
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.add_input(Submit('submit', 'Submit'))

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',]

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.field_class = 'col-sm-8'
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.add_input(Submit('submit', 'Submit'))