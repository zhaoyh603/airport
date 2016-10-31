#!/usr/bin/env python
# coding=utf-8
import codecs
import sys
import sqlacodegen
from sqlalchemy import MetaData

from sqlacodegen.codegen import (CodeGenerator, ModelClass)


class ModelGen(CodeGenerator):
    """生成model代码
    views:是否包含视图
    outfile:生成文件路径
    tables:包含的表，用,分隔。
    """

    def render(self):
        """

        :rtype: text
        """
        txt = self.header + '\n'

        # Render the collected imports
        txt += self.collector.render() + '\n\n'

        if any(isinstance(model, ModelClass) for model in self.models):
            txt += 'from app import db'
        else:
            txt += 'metadata = MetaData()'

        # Render the model tables and classes
        for model in self.models:
            txt += '\n\n\n' + model.render().rstrip('\n')

        if self.footer:
            txt += self.footer
        return txt.replace("Base", "db.Model")

