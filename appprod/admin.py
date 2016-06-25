from django.contrib import admin

# Register your models here.

from django.contrib import admin
from appprod.models import Cargo
from appprod.models import Prestador
from appprod.models import UnidadeMedida
from appprod.models import ProcessoProducao
from appprod.models import MateriaPrima
from appprod.models import EtapaProducao
from appprod.models import MateriaEtapa

admin.site.register(Cargo)
admin.site.register(Prestador)
admin.site.register(UnidadeMedida)
admin.site.register(ProcessoProducao)
admin.site.register(MateriaPrima)
admin.site.register(EtapaProducao)
admin.site.register(MateriaEtapa)
