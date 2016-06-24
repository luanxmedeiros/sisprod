from django.conf.urls import patterns,include,url
from appprod.views import *
urlpatterns=[url(r'^$',home,name='home'),
             url(r'^materias/$',listarmateria,name='materias'),
             url(r'^prestadores/$', listarprestadores, name='prestadores')

]