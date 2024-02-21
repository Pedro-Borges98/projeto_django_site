from django.db import models
from datetime import datetime

# essa classe se torna um model pq representa uma tabela no banco de dados
class Fotografia(models.Model):

    # modo de criar categorias as respostas
    OPCOES_CATEGORIA = [
        ("NEBULOSA","Nebulosa"),
        ("ESTRELA","Estrela"),
        ("GALAXIA","Galaxia"),
        ("PLANETA","Planeta"),
    ]

    nome      = models.CharField(max_length = 100, null = False, blank = False)
    legenda   = models.CharField(max_length = 150, null = False, blank = False)
    categoria = models.CharField(max_length = 100, choices = OPCOES_CATEGORIA, default="")
    descricao = models.TextField(null = False, blank = False)
    foto      = models.CharField(max_length = 100,null = False, blank = False)
    publicada = models.BooleanField(default = False)
    data_fotografia = models.DateTimeField(default = datetime.now, blank = False)

    # modelo que retorna o nome da fotografia em si para o front
    def __str__(self):
        return f"Fotografia [nome={self.nome}]"