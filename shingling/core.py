#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
# Shingling
#===============================================================================
# Copyright 2011 Hrishikesh K B <hrishi.kb@gmail.com>
# http://www.smc.org.in
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
from silpa_common import *
import indicngram


class Shingling:
    """
    The shingling class. Instantiate to get access to the  methods.
    """
    def wshingling(self, text, window_size=4):
        """
        :param text: Text to be split into shingles.
        :type text: str.
        :param window_size: the window size for splitting the shingles.
        :type: int.
        :returns: text split into shingles.
                """
        window_size = int(window_size)
        s = indicngram.getInstance()
        ngrams = s.wordNgram(text, window_size)
        size = len(ngrams)
        shingling = []
        for x in ngrams:
            if x not in shingling:
                shingling.append(x)
        return shingling

    def get_module_name(self):
        """
        returns the module name
        """
        return "Shingling Library"

    def get_info(self):
        """
        returns more info on the module.
        """
        return "Shingling Library for English and Indian languages"


def getInstance():
    return Shingling()
