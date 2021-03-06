from django.urls import path

from . import views
from django.urls import path, re_path
from django.views.generic import TemplateView

# ルーティング情報を列挙する
urlpatterns = [
  path('iftag', views.iftag, name='iftag'),
  path('yesno', views.yesno, name='yesno'),
  path('firstof', views.firstof, name='firstof'),
  path('forloop', views.forloop, name='forloop'),
  path('forempty', views.forempty, name='forempty'),
  path('fortag', views.fortag, name='fortag'),
  path('ifchanged', views.ifchanged, name='ifchanged'),
  path('regroup', views.regroup, name='regroup'),
  path('cycle', views.cycle, name='cycle'),
  path('escape', views.escape, name='escape'),
  path('temptag', views.temptag, name='temptag'),
  path('verbatim', views.verbatim, name='verbatim'),
]
