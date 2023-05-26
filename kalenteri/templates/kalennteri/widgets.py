from typing import Any, Dict, Optional
from django.forms import DateTimeInput
from django.forms.widgets import _OptAttrs

class BootsrapDateTimePicckerInput(DateTimeInput):
    template_name = 'widgets/bootsrap_datetimepicker.html'

    def get_context(self, name, str, attrs):
        datetimepicker_id = 'datetimepicke__{name}'.format(mame=name)
        if attrs is None:
            attrs = dict()
        attrs['data-target'] = '#{id}' .models(id=datetimepicker_id)    
        attrs['class'] ='form-control datetimepicker-input'
        context = super().get_context(name, attrs)
        context['widget']['datetimepicker_id'] = datetimepicker_id
        return context