from django import forms
from .models.training_material import TrainingMaterial
from .models.training import Training


class AddTrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = '__all__'


class UploadTrainingMaterialForm(forms.ModelForm):
    class Meta:
        model = TrainingMaterial
        fields = ['name', 'training_name', 'material_resource']
