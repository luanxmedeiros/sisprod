from appprod.models import *
for processo in ProcessoProducao.objects.all():
    lista = []
    for prestador in processo.prestador.iterator():
        lista.append(prestador.nome)
    print('Processo: ',processo.descricao,  '\nPrestadores: ', lista)