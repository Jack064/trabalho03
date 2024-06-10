from django.shortcuts import redirect, render
from .models import Servico

# Create your views here.

def home(request):
    servicos = Servico.objects.all()
    return render(request, "index.html", {"servicos":servicos})

def cadastro(request):
    return render(request, "cadastro.html")

def salvar(request):
    vcodigo = request.POST.get("codigo")
    vdescricao = request.POST.get("descricao")
    vdata = request.POST.get("data")
    vsolicitante = request.POST.get("solicitante")
    vcontato = request.POST.get("contato")
    Servico.objects.create(codigo = vcodigo, descricao = vdescricao, data = vdata, solicitante = vsolicitante, contato = vcontato)
    servicos = Servico.objects.all()
    return redirect(home)
    
def editar(request, id):
    servico = Servico.objects.get(id = id)
    return render(request,"update.html",{"servico":servico})

def update(request, id):
    vcodigo = request.POST.get("codigo")
    vdescricao = request.POST.get("descricao")
    vdata = request.POST.get("data")
    vsolicitante = request.POST.get("solicitante")
    vcontato = request.POST.get("contato")
    servico = Servico.objects.get(id = id)
    servico.codigo = vcodigo
    servico.descricao = vdescricao
    servico.data = vdata
    servico.solicitante = vsolicitante
    servico.contato = vcontato
    servico.save()
    return redirect(home)

def apagar(request, id):
    servico = Servico.objects.get(id = id)
    servico.delete()
    return redirect(home)
