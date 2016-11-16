BatInfo
=======

A simple Python module to retrieve battery information on Linux-based operating system.
No ACPI or external software is needed.
Only the Linux kernel and its `/sys/class/power_supply` folder.

A simple example says more than thousand words:

    In [1]: import batinfo
    In [2]: bat = batinfo.Batteries()
    In [3]: bat
    Out[3]: <batinfo.Battery.Batteries at 0x31c87d0>
    In [4]: bat.stat
    Out[4]: [{"status": "Full", "capacity": 50, "name": "CMB1", "uevent": "POWER_SUPPLY_NAME=CMB1\nPOWER_SUPPLY_STATUS=Full\nPOWER_SUPPLY_PRESENT=1\nPOWER_SUPPLY_TECHNOLOGY=Li-ion\nPOWER_SUPPLY_CYCLE_COUNT=0\nPOWER_SUPPLY_VOLTAGE_MIN_DESIGN=10800000\nPOWER_SUPPLY_VOLTAGE_NOW=12496000\nPOWER_SUPPLY_CURRENT_NOW=0\nPOWER_SUPPLY_CHARGE_FULL_DESIGN=5800000\nPOWER_SUPPLY_CHARGE_FULL=5800000\nPOWER_SUPPLY_CHARGE_NOW=3900000\nPOWER_SUPPLY_CAPACITY=100\nPOWER_SUPPLY_MODEL_NAME=CP293550-01\nPOWER_SUPPLY_MANUFACTURER=Fujitsu\nPOWER_SUPPLY_SERIAL_NUMBER=01A-Z100320001158Z", "alarm": 0, "charge_full": 5800000, "voltage_now": 12496000, "serial_number": "01A-Z100320001158Z", "cycle_count": 0, "current_now": 0, "charge_now": 3900000, "voltage_min_design": 10800000, "path": "/sys/class/power_supply/CMB1", "technology": "Li-ion", "manufacturer": "Fujitsu", "type": "Battery", "model_name": "CP293550-01", "present": 1, "charge_full_design": 5800000}]
    In [6]: bat.stat[0]
    Out[6]: {"status": "Full", "capacity": 100, "name": "CMB1", "uevent": "POWER_SUPPLY_NAME=CMB1\nPOWER_SUPPLY_STATUS=Full\nPOWER_SUPPLY_PRESENT=1\nPOWER_SUPPLY_TECHNOLOGY=Li-ion\nPOWER_SUPPLY_CYCLE_COUNT=0\nPOWER_SUPPLY_VOLTAGE_MIN_DESIGN=10800000\nPOWER_SUPPLY_VOLTAGE_NOW=12496000\nPOWER_SUPPLY_CURRENT_NOW=0\nPOWER_SUPPLY_CHARGE_FULL_DESIGN=5800000\nPOWER_SUPPLY_CHARGE_FULL=5800000\nPOWER_SUPPLY_CHARGE_NOW=3900000\nPOWER_SUPPLY_CAPACITY=100\nPOWER_SUPPLY_MODEL_NAME=CP293550-01\nPOWER_SUPPLY_MANUFACTURER=Fujitsu\nPOWER_SUPPLY_SERIAL_NUMBER=01A-Z100320001158Z", "alarm": 0, "charge_full": 5800000, "voltage_now": 12496000, "serial_number": "01A-Z100320001158Z", "cycle_count": 0, "current_now": 0, "charge_now": 3900000, "voltage_min_design": 10800000, "path": "/sys/class/power_supply/CMB1", "technology": "Li-ion", "manufacturer": "Fujitsu", "type": "Battery", "model_name": "CP293550-01", "present": 1, "charge_full_design": 5800000}
    In [7]: bat.stat[0].capacity
    Out[7]: 50
    In [8]: print bat.stat[0]
    100
    In [9]: bat.stat[0].manufacturer
    Out[9]: 'Fujitsu'
    In [9]: bat.stat[0].technology
    Out[9]: 'Li-ion'
    In [11]: bat.stat[0].charge_full
    Out[11]: 5800000
    In [12]: bat.stat[0].charge_now
    Out[12]: 3900000
    In [12]: bat.update()
    > Refresh the stats

Have fun...
