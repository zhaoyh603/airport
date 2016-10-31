#!/usr/bin/env python
# coding=utf-8

from flask import Blueprint
codemaker = Blueprint('codemaker', __name__)


from . import modelgen
