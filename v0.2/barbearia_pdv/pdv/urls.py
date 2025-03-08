from django.urls import path
from django.contrib import admin
from .views import (register_view, logout_view, login_view, dashboard, clientes_view,
criar_cliente, servicos_view, criar_servico, agendamentos_view, criar_agendamento, relatorios_view  )

urlpatterns = [
    path('', login_view, name='login'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('clientes/', clientes_view, name='clientes'),
    path('clientes/criar/', criar_cliente, name='criar_cliente'),
    path('servicos/', servicos_view, name='servicos'),
    path('servicos/criar/', criar_servico, name='criar_servico'),
    path('agendamentos/', agendamentos_view, name='agendamentos'),
    path('agendamentos/criar/', criar_agendamento, name='criar_agendamento'),
    path('relatorio/', relatorios_view, name='relatorios')
]
