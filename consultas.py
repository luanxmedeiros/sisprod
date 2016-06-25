from appprod.models import *

from appprod.models import *

'''
for processo in ProcessoProducao.objects.all():
        prestadores = []
        for prest in Prestador.objects.get(id=processo.id).nome:
                prestadores.append(prest)
        print("Processo:",processo.descricao.__str__(), prestadores)
'''
tudo = []
for prest in Prestador.objects.all():
    tudotemp = {"Prestador":"","Processo_Etapa":[]}
    procetap = []
    #, "Matéria Prima":[]
    tudotemp["Prestador"] = prest.nome.__str__()
    for proco in ProcessoProducao.objects.filter(prestador=prest):
        procetap.append("Processo: "+proco.descricao.__str__()+". Etapas: ")
        for etap in EtapaProducao.objects.filter(processo_producao=proco):
            procetap.append(etap.descricao.__str__())
        #for p in ProcessoProducao.objects.filter(prestador=proco.prestador):

    tudotemp["Processo_Etapa"] = procetap
     #lista.append(prestador.nome)
    #print("Prestador: ",prest.nome, "Processos: ",processoss, "Etapas: ",etapas)

    #print('Processo: ',processo.descricao,  '\nPrestadores: ', lista)
    tudo.append(tudotemp)
    tudotemp = {"Prestador":"","Processo_Etapa":[]}
    procetap = []
for x in tudo:
    print (x,"\n")


'''
for processo in ProcessoProducao.objects.all():
<<<<<<< Updated upstream
        print("Processo:", processo.descricao.__str__())

'''
