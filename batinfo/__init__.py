#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# BatInfo
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

__appname__ = "batinfo"
__version__ = "0.1.8"
__author__ = "Nicolas Hennion <nicolas@nicolargo.com>"
__licence__ = "LGPL"

__all__ = ['batteries', 'battery']

from battery import battery, batteries
