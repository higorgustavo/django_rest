from ..models import Vaga
from .tecnologia_service import get_tecnologia_id
from django.http import Http404


def listar_vagas():
    vagas = Vaga.objects.all()
    return vagas


def cadastrar_vaga(vaga):
    vaga_bd = Vaga.objects.create(
        titulo=vaga.titulo,
        descricao=vaga.descricao,
        salario=vaga.salario,
        local=vaga.local,
        quantidade=vaga.quantidade,
        contato=vaga.contato,
        tipo_contrato=vaga.tipo_contrato,
    )
    vaga_bd.save()
    for i in vaga.tecnologias:
        tecnologia = get_tecnologia_id(i.id)
        vaga_bd.tecnologias.add(tecnologia)
    return vaga_bd


def get_vaga_id(id):
    try:
        return Vaga.objects.get(id=id)
    except Vaga.DoesNotExist:
        raise Http404


def editar_vaga(vaga_antiga, vaga_nova):
    vaga_antiga.titulo = vaga_nova.titulo
    vaga_antiga.descricao = vaga_nova.descricao
    vaga_antiga.salario = vaga_nova.salario
    vaga_antiga.local = vaga_nova.local
    vaga_antiga.quantidade = vaga_nova.quantidade
    vaga_antiga.contato = vaga_nova.contato
    vaga_antiga.tipo_contrato = vaga_nova.tipo_contrato
    vaga_antiga.tecnologias.set(vaga_nova.tecnologias)
    vaga_antiga.save(force_update=True)


def remover_vaga(vaga):
    vaga.delete()