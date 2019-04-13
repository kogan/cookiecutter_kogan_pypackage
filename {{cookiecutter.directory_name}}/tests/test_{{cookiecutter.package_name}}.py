# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.test import TestCase

from {{cookiecutter.package_name}} import __version__


class {{cookiecutter.package_name|title}}TestCase(TestCase):
    def test_version(self):
        self.assertEqual(__version__, "0.1.0")
