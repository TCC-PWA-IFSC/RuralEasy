from django.contrib import admin

from .models import ProdutorRural
from .models import PropriedadeRural
from .models import Lote
from .models import Raca
from .models import Animal
from .models import Veterinario
from .models import ProdSanitario
from .models import Venda
from .models import ComprarAnimal
from .models import Ocorrencias
from .models import Inseminacao
from .models import Movimentacao
from .models import Suplementacao
admin.site.register(ProdutorRural)
admin.site.register(PropriedadeRural)
admin.site.register(Lote)
admin.site.register(Raca)
admin.site.register(Animal)
admin.site.register(Veterinario)
admin.site.register(ProdSanitario)
admin.site.register(Venda)
admin.site.register(ComprarAnimal)
admin.site.register(Ocorrencias)
admin.site.register(Inseminacao)
admin.site.register(Movimentacao)
admin.site.register(Suplementacao)