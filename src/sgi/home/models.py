# -*-coding:utf-8 -*-

from mongoengine import *

__all__ = [
    'Cliente'
]


class Cliente(Document):
    nome = StringField(required=True)
    sobrenome = StringField(required=True)