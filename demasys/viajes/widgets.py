# coding: utf-8
from django.forms.widgets import ClearableFileInput, CheckboxInput
from django.utils.safestring import mark_safe
from django.utils.html import format_html, conditional_escape
from django.utils.encoding import force_text

class MetronicFileInput(ClearableFileInput):
    
    template_with_initial = """
                            <div class="fileinput fileinput-new" data-provides="fileinput">
                                <span class="btn default btn-file">
                                    <span class="fileinput-new">
                                    Seleccionar </span>
                                    <span class="fileinput-exists">
                                    Cambiar </span>
                                    %(input)s
                                </span>
                                <span class="fileinput-filename">
                                </span>
                                &nbsp; <a href="#" class="close fileinput-exists" data-dismiss="fileinput">
                                </a>
                            </div>
                            <p>%(initial_text)s: %(initial)s </p>                                                    
                            """
                            
    url_markup_template = '<a href="{0}" class="btn blue" target="_blank"><i class="fa fa-file-o"></i></a>'
    
    def render(self, name, value, attrs=None):
        substitutions = {
            'initial_text': self.initial_text,
            'input_text': self.input_text,
            'clear_template': '',
            'clear_checkbox_label': self.clear_checkbox_label,
        }
        template = """
                    <div class="fileinput fileinput-new" data-provides="fileinput">
                        <span class="btn default btn-file">
                            <span class="fileinput-new">
                            Seleccionar </span>
                            <span class="fileinput-exists">
                            Cambiar </span>
                            %(input)s
                        </span>
                        <span class="fileinput-filename">
                        </span>
                        &nbsp; <a href="#" class="close fileinput-exists" data-dismiss="fileinput">
                        </a>
                    </div>
                    """
        substitutions['input'] = super(ClearableFileInput, self).render(name, value, attrs)

        if value and hasattr(value, "url"):
            template = self.template_with_initial
            substitutions['initial'] = format_html(self.url_markup_template,
                                                   value.url)
            if not self.is_required:
                checkbox_name = self.clear_checkbox_name(name)
                checkbox_id = self.clear_checkbox_id(checkbox_name)
                substitutions['clear_checkbox_name'] = conditional_escape(checkbox_name)
                substitutions['clear_checkbox_id'] = conditional_escape(checkbox_id)
                substitutions['clear'] = CheckboxInput().render(checkbox_name, False, attrs={'id': checkbox_id})
                substitutions['clear_template'] = self.template_with_clear % substitutions

        return mark_safe(template % substitutions)
