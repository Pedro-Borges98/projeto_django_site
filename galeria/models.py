from django.db import models

# essa classe se torna um model pq representa uma tabela no banco de dados
class Fotografia(models.Model):
    nome      = models.CharField(max_length = 100, null = False, blank = False)
    legenda   = models.CharField(max_length = 150, null = False, blank = False)
    descricao = models.TextField(null = False, blank = False)
    foto      = models.CharField(max_length = 100,null = False, blank = False)

    # modelo que retorna o nome da fotografia em si para o front
    def __str__(self):
        return f"Fotografia [nome={self.nome}]"