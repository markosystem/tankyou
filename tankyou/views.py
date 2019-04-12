from django.shortcuts import render
from .models import Lancamento


def viewInicio(request):
    return render(request, 'tankyou/inicio.html')


def viewSobrec(request):
    return render(request, 'tankyou/sobre.html')


def viewLancamentos(request):
    lancamentos = Lancamento.objects.filter(km_final__isnull=False).all()
    return render(request, 'tankyou/lancamentos.html', {'lancamentos': lancamentos})
