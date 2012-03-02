# -*-coding:utf-8 -*-

from mongoengine import *

__all__ = [
    'Cliente',
    'Imovel'
]


class Cliente(Document):
    nome = StringField(required=True)
    sobrenome = StringField(required=True)


class Imovel(Document):
    nome = StringField(required=True)
    endereco = StringField(required=True)
    aluguel = DecimalField(required=False)
    proprietario = ReferenceField('Cliente', required=True)
    inquilino = ReferenceField('Cliente', required=False)