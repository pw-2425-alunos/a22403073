from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length=200)
    ano = models.IntegerField()
    semestre = models.IntegerField()
    docentes = models.CharField(max_length=300)
    link_moodle = models.URLField()
    link_ulusofona = models.URLField()

    def __str__(self):
        return f"{self.nome} ({self.ano}/{self.semestre})"


class Tecnologia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    logo = models.ImageField(upload_to='tecnologias_logos/')

    def __str__(self):
        return self.nome


class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    link_github = models.URLField(blank=True, null=True)
    link_demo = models.URLField(blank=True, null=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    tecnologias = models.ManyToManyField(Tecnologia)

    def __str__(self):
        return self.titulo


class ImagemProjeto(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(upload_to='projetos_imagens/')
    descricao = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Imagem de {self.projeto.titulo}"


class Conceito(models.Model):
    projeto = models.OneToOneField(Projeto, on_delete=models.CASCADE)
    conceitos_aplicados = models.TextField()
    desafios_tecnicos = models.TextField()

    def __str__(self):
        return f"Conceitos de {self.projeto.titulo}"


class Visitante(models.Model):
    session_key = models.CharField(max_length=40, unique=True) #unique serve para que a mesma sessao apenas seja contada 1 vez
    data_visita = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.session_key

#ESTUDAR

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    disciplina = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='prof_pic',blank=True, null=True)

    def __str__(self):
        return self.nome

class Interesse(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    projetos = models.ManyToManyField(Projeto, blank=True)
    disciplinas = models.ManyToManyField(Disciplina, blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, blank=True)

    def __str__(self):
        return self.nome









