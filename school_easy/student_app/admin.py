from django.contrib import admin
from .models import *

#admin.site.register(Coures)
@admin.register(Etudiant)
class StudentEtudiant(admin.ModelAdmin):
    list_display = ('matricule', 'nom','genre', 'status', )
    ordering = ('matricule', )
    search_fields = ('matricule', )
    
@admin.register(Personnel)
class StudentPersonnel(admin.ModelAdmin):
    list_display = ('matricule', 'nom','genre', 'grade', )
    ordering = ('matricule', )
    search_fields = ('matricule', )
    
@admin.register(Adresse)
class StudentAdresse(admin.ModelAdmin):
    list_display = ('telephone', 'email','quartier', 'ville', )
    ordering = ('email', )
    search_fields = ('email', )
    
@admin.register(Matiere)
class StudentMatiere(admin.ModelAdmin):
    list_display = ('nom', 'credit','note', 'appreciation', )
    ordering = ('nom', )
    search_fields = ('nom', )
