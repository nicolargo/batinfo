#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# BatInfo test suite
# A simple Python lib to retreive battery information
#
# Copyright (C) 2013 Nicolargo <nicolas@nicolargo.com>
#
# BatInfo is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BatInfo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from batinfo import Batteries
import unittest


class TestBatInfo(unittest.TestCase):

    def setUp(self):
        self.bat = Batteries(bat_root_path="./test")

    def test_BatInfo_get(self):
        self.assertTrue(len(self.bat) == 2)

    def test_BatInfo_name_default(self):
        # print("Battery name: %s" % self.bat.stat().name)
        self.assertTrue(type(self.bat.stat[0].name) == str)
        self.assertTrue(self.bat.stat[0].name == "battery")

    def test_BatInfo_capacity(self):
        # print("Battery capacity: %s" % self.bat.stat().capacity)
        self.assertTrue(type(self.bat.stat[0].capacity) == int)
        self.assertTrue(self.bat.stat[0].capacity == 53)

    def test_BatInfo_charge_now(self):
        # print("Battery 2 charge_now: %s" % self.bat.stat().charge_now)
        self.assertTrue(type(self.bat.stat[1].charge_now) == int)
        self.assertTrue(self.bat.stat[1].charge_now == 1972000)

if __name__ == '__main__':
    unittest.main()
