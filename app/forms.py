from django import forms

from app.models import Mascota

TOPIC_CHOICES = (
    ('general', 'General enquiry'),
    ('bug', 'Bug report'),
    ('suggestion', 'Suggestion'),
)


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = (
            'nombre_mascota',
            'edad_mascota',
            'persona_id',
            'tipo_mascota'
        )
