#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Batinfo
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

import os
import logging
import json

logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.CRITICAL)

class battery(object):
    """
    Battery stats
    """

    def __init__(self, path="/sys/class/power_supply", name="BAT0"):
        self.path = os.path.join(path, name)
        self.name = name
        self.__update__()          

    def __str__(self):
        self.__update__()
        if 'capacity' in repr(self):
            return str(self.capacity)
        else:
            return ""

    def __repr__(self):
        self.__update__()
        return json.dumps(self, default=lambda o: o.__dict__)

    def __getattr__(self, stat):
        """
        Catch message if attribute did not exist
        """
        log.error("Attribute %s did not exist" % stat)
        return ""

    def __get_stat__(self, stat):
        """
        Read stat from the Linux kernel
        """
        try:
            with open(os.path.join(self.path, stat), 'r') as f:
                return f.read().strip()
        except Exception:
            log.error("Can not read file %s" % stat)
            return ""

    def __update__(self):
        """
        Update the stats
        """
        # Get all file in the battery system folder
        stats = [f for f in os.listdir(self.path)
                 if os.path.isfile(os.path.join(self.path, f))]
        for stat in stats:
            #~ print("%s = %s" % (stat, self.__get_stat__(stat)))
            value = self.__get_stat__(stat)
            try:
                # Try to convert to integer
                value = int(value)
            except ValueError:
                # Not possible, not a problem
                pass
            setattr(self, stat, value)
        if ('capacity' not in stats and 'charge_full' in stats
        and 'charge_now' in stats) :
            value = self.charge_now*100/self.charge_full
            setattr(self, 'capacity', value)


class batteries(object):
    """
    Class to retreive stats of all the batteries
    List of battery (class)
    """

    def __init__(self, bat_root_path="/sys/class/power_supply"):
        # Root path for batteries stats
        self.bat_root_path = bat_root_path
        # Update stat
        self.update()

    def update(self):
        # Init the batteries stat list
        self.stat = []
        # and update it...
        # Find all the batteries in the bat_root_path folder
        # It's a battery if the file "type" exist
        # and contain "Battery"
        for dirname in os.listdir(self.bat_root_path):
            type_file = os.path.join(self.bat_root_path, dirname, "type")
            if (os.path.isfile(type_file)):
                try:
                    with open(type_file, 'r') as f:
                        is_bat = (f.read().strip() == "Battery")
                except Exception:
                    log.error("Can not read file %s" % type_file)
                if (is_bat):
                    # It is a battery, let's add it to the list
                    # print("Add the battery %s to the list" % dirname)
                    self.stat.append(battery(self.bat_root_path, dirname))

    def __len__(self):
        return len(self.stat)
