#! /usr/bin/python
# -*- coding: utf-8 -*-

from testtools import TestCase

from .. import Shingling


class ShinglingTest(TestCase):

    def setUp(self):
        super(ShinglingTest, self).setUp()
        self.shingling = Shingling()

    def test_wordShingling(self):
        self.assertEqual(self.shingling.wshingling(u"ഇത് ഒരു നല്ല കാര്യമാണ് ഇത് ഒരു", 2), [[u"ഇത്", u"ഒരു"], [u"ഒരു", u"നല്ല"], [u"നല്ല", u"കാര്യമാണ്"], [u"കാര്യമാണ്", u"ഇത്"]])
