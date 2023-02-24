from django import forms
from django.forms import ModelForm
from .models import Etudiant

class EtudiantForm(forms.ModelForm):
	class Meta:
		model = Etudiant
		fields = ( 'nom', 'naissance', 'genre', 'nationnalite',  'filiere',  'matricule', 'niveau', 'status', 'adresse', 'Matiere', 'photo',)

		labels = {
			'matricule': 'Matricule', 
			'nom': 'Nom et Prenom',     
			#'filiere': '',  
			'genre': 'Selectionner le genre ', 
			'nationnalite': 'Nationnalité',
			'filiere': 'Filière', 
			'niveau': 'Selectionner le niveau',
			'status': 'Selectionner le status',
			'adresse': 'Selectionner l\'adresse', 
			'Matiere': 'Selectionner les matières',  
			'photo': 'Selectionner une photo',  
		}

		widgets = {
			'matricule': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir le matricule',}), 
			'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom et Prenom',}), 
			'naissance': forms.TextInput(attrs={'class': 'form-control','type':'datetime-local'}),
			'genre': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Genre',}), 
			'nationnalite': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nationnalité',}), 
			'filiere': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrer la filière',}),
			'niveau': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Niveau',}), 
			'status': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Status',}),   
			#'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description',}), 
			'adresse': forms.Select(attrs={'class': 'form-select', 'placeholder': 'adresse',}),
			'Matiere': forms.SelectMultiple(attrs={'class': 'form-select', 'placeholder': 'Choisir les matières',}), 
			#'photo': forms.FileField()
		}
