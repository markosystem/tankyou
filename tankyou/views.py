from django.shortcuts import render


def viewInicio(request):
    return render(request, 'tankyou/inicio.html')


def viewSobrec(request):
    return render(request, 'tankyou/sobre.html')


def viewLancamentos(request):
    return render(request, 'admin/lancamentos.html')
