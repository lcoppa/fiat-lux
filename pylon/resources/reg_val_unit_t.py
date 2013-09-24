"""reg_val_unit_t standard enumeration type, originally defined in resource
file set standard 00:00:00:00:00:00:00:00-0."""


# Copyright (C) 2013 Echelon Corporation.  All Rights Reserved.

# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software" to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

# This file is generated from device resource files using an automated
# database to source code conversion process.  Grammar and punctuation within
# the embedded documentation may not be correct, as this data is gathered and
# combined from several sources.  The machine-generated code may not meet
# compliance with PEP-8 and PEP-257 recommendations at all times.
# Generated at 12-Sep-2013 11:27.

from pylon.resources import base
from pylon.resources.standard import standard


class reg_val_unit_t(base.Enumeration):
    """reg_val_unit_t standard enumeration."""

    # invalid unit of measure (INVALID).
    RVU_NUL = -1

    # no units specified ( ).
    RVU_NONE = 0

    # Watts (W).
    RVU_W = 1

    # kiloWatts (kW).
    RVU_KW = 2

    # megaWatts (MW).
    RVU_MW = 3

    # gigaWatts (GW).
    RVU_GW = 4

    # Volt-Amperes reactive (var).
    RVU_VAR = 5

    # kilo-Volt-Amperes reactive (kvar).
    RVU_KVAR = 6

    # mega-Volt-Amperes reactive (Mvar).
    RVU_MVAR = 7

    # giga-Volt-Amperes reactive (Gvar).
    RVU_GVAR = 8

    # Watt-hour (Wh).
    RVU_WH = 9

    # kiloWatt-hour (kWh).
    RVU_KWH = 10

    # megaWatt-hour (MWh).
    RVU_MWH = 11

    # gigaWatt-hour (GWh).
    RVU_GWH = 12

    # Volt-Amperes reactive -hour (varh).
    RVU_VARH = 13

    # kilo-Volt-Amperes reactive -hour (kvarh).
    RVU_KVARH = 14

    # mega-Volt-Amperes reactive -hour (Mvarh).
    RVU_MVARH = 15

    # giga-Volt-Amperes reactive -hour (Gvarh).
    RVU_GVARH = 16

    # Volts (V).
    RVU_V = 17

    # Amps (A).
    RVU_A = 18

    # (cosf).
    RVU_COSF = 19

    # cubic metres (m^3)(cu.m).
    RVU_M3 = 20

    # litres (l).
    RVU_L = 21

    # millilitres (ml).
    RVU_ML = 22

    # U.S.  Gallons (USG).
    RVU_USGAL = 23

    # giga-Joules (GJ).
    RVU_GJ = 24

    # mega-Joules (MJ).
    RVU_MJ = 25

    # megacalories (Mcal).
    RVU_MCAL = 26

    # kilocalories (kcal) / Calories (Cal).
    RVU_KCAL = 27

    # mega-British thermal units (mBtu).
    RVU_MBTU = 28

    # kilo-British thermal units (kBtu).
    RVU_KBTU = 29

    # mega-Joules per hour (MJ/h).
    RVU_MJH = 30

    # millilitres per second (ml/s).
    RVU_MLS = 31

    # litres per second (l/s).
    RVU_LS = 32

    # cubic-metres per second (m^3/s) (cu.m/s).
    RVU_M3S = 33

    # (C).
    RVU_C = 34

    # litres per hour (l/h).
    RVU_LH = 35

    # Volt-Amperes (VA).
    RVU_VA = 36

    # kiloVolt-Amperes (kVA).
    RVU_KVA = 37

    # megaVolt-Amperes (MVA).
    RVU_MVA = 38

    # gigaVolt-Amperes (GVA).
    RVU_GVA = 39

    # Volt-Ampere hours (VAh).
    RVU_VAH = 40

    # kiloVolt-Ampere hours (kVAh).
    RVU_KVAH = 41

    # megaVolt-Ampere hours (MVAh).
    RVU_MVAH = 42

    # giga-Volt-Ampere hours (GVAh).
    RVU_GVAH = 43

    def __init__(self):
        super().__init__(
            key=30,
            scope=0,
            prefix='RVU_'
        )
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = reg_val_unit_t()
    pass
