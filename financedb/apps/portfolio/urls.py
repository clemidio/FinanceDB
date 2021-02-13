from django.urls import include, path
from . import views as v

app_name = 'portfolio'


# entrada_patterns = [
#     path('', v.EstoqueEntradaList.as_view(), name='estoque_entrada_list'),
#     path('add/', v.estoque_entrada_add, name='estoque_entrada_add'),
# ]

# saida_patterns = [
#     path('', v.EstoqueSaidaList.as_view(), name='estoque_saida_list'),
#     path('add/', v.estoque_saida_add, name='estoque_saida_add'),
# ]

urlpatterns = [

    path('list', v.list_portfolio, name='url_list_portfolio'),
    # path('<int:pk>/', v.EstoqueDetail.as_view(), name='estoque_detail'),
    # path('entrada/', include(entrada_patterns)),
    # path('saida/', include(saida_patterns)),
]
