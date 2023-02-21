from django.db import models

class Personne(models.Model):
    Genre = (
    ('M', ('masculin')),
    ('F', ('feminin')),
    ('Autre', ('autre')),
)
    nom = models.CharField(max_length=200)
    naissance = models.DateTimeField('date de naisssance')
    genre = models.CharField(max_length=32, choices=Genre)
    nationalite = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="photo",blank=True)
    def __str__(self):
        return self.nom

class Adresse(models.Model):
    telephone = models.CharField(max_length=20,blank=True,unique=True)
    email = models.CharField(max_length=250,unique=True)
    quartier = models.CharField(max_length=150)
    ville = models.CharField(max_length=150)
    def __str__(self):
        return self.email

class Matiere(models.Model):
    nom=models.CharField(max_length=150)
    credit=models.FloatField(max_length=15,blank=True)
    note= models.FloatField(max_length=15,blank=True)
    appreciation=models.CharField(max_length=150,blank=True)
    def __str__(self):
        return self.nom

class Etudiant(Personne):
    Status = (
    ('Nouveau', ('nouveau')),
    ('Ancien', ('ancien')),
)
    Niveau = (
    ('L1', ('licence 1')),
    ('L2', ('licence 2')),
    ('L3', ('licence 3')),
)
    Regime = (
    ('RN', ('normal')),('RS', ('spécial')),
)
    matricule = models.CharField(max_length=20,unique=True)
    filiere = models.CharField(max_length=50)
    status = models.CharField(max_length=32, choices=Status)
    niveau = models.CharField(max_length=32, choices=Niveau)
    regime = models.CharField(max_length=15, choices=Regime)
    adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
    matiere = models.ManyToManyField(Matiere)
    def __str__(self):
        return self.matricule

class Personnel(Personne):
    matricule = models.CharField(max_length=20,unique=True)
    grade=models.CharField(max_length=50)
    poste=models.CharField(max_length=50)
    type_poste=models.CharField(max_length=50)
    adresse = models.ForeignKey(Adresse, on_delete=models.CASCADE)
    matiere = models.ManyToManyField(Matiere)
    def __str__(self):
        return self.matricule