"""currency_t standard enumeration type, originally defined in resource file
set standard 00:00:00:00:00:00:00:00-0."""


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


class currency_t(base.Enumeration):
    """currency_t standard enumeration."""

    # Invalid Value.
    CU_NUL = -1

    # Argentine Peso.
    CU_ARGENTINA_PESO = 0

    # Australian Dollar.
    CU_AUSTRALIA_DOLLAR = 1

    # Austrian Schilling.
    CU_AUSTRIA_SCHILLING = 2

    # Bahraini Dinar.
    CU_BAHRAIN_DINAR = 3

    # Belgian Franc.
    CU_BELGIUM_FRANC = 4

    # Brazilian Cruzeiro Real.
    CU_BRAZIL_CRUZEIRO_REAL = 5

    # British Pound.
    CU_BRITAIN_POUND = 6

    # Canadian Dollar.
    CU_CANADA_DOLLAR = 7

    # Czechoslovakian Koruna.
    CU_CZECH_KORUNA = 8

    # Chilean Peso.
    CU_CHILE_PESO = 9

    # Chinese Renminbi Yuan.
    CU_CHINA_RENMINBI = 10

    # Colombian Peso.
    CU_COLOMBIA_PESO = 11

    # Danish Krone.
    CU_DENMARK_KRONE = 12

    # Ecuadorian Sucre.
    CU_ECUADOR_SUCRE = 13

    # European Euro.
    CU_EUROPEAN_CURRENCY_UNIT = 14

    # Finnish Markka.
    CU_FINLAND_MARKKA = 15

    # French Franc.
    CU_FRANCE_FRANC = 16

    # German Mark.
    CU_GERMANY_MARK = 17

    # Greek Drachma.
    CU_GREECE_DRACHMA = 18

    # Hong Kong Dollar.
    CU_HONG_KONG_DOLLAR = 19

    # Hungarian Forint.
    CU_HUNGARY_FORINT = 20

    # Indian Rupee.
    CU_INDIA_RUPEE = 21

    # Indonesian Rupiah.
    CU_INDONESIA_RUPIAH = 22

    # Irish Punt.
    CU_IRELAND_PUNT = 23

    # Israeli Shekel.
    CU_ISRAEL_SHEKEL = 24

    # Italian Lira.
    CU_ITALY_LIRA = 25

    # Japanese Yen.
    CU_JAPAN_YEN = 26

    # Jordanian Dinar.
    CU_JORDAN_DINAR = 27

    # Kuwaiti Dinar.
    CU_KUWAIT_DINAR = 28

    # Lebanese Pound.
    CU_LEBANON_POUND = 29

    # Malaysian Ringgit.
    CU_MALAYSIA_RINGGIT = 30

    # Maltese Lira.
    CU_MALTA_LIRA = 31

    # Mexican New Peso.
    CU_MEXICO_PESO = 32

    # Netherlands Guilder.
    CU_NETHERLANDS_GUILDER = 33

    # New Zealand Dollar.
    CU_NEW_ZEALAND_DOLLAR = 34

    # Norwegian Krone.
    CU_NORWAY_KRONE = 35

    # Pakistani Rupee.
    CU_PAKISTAN_RUPEE = 36

    # Peruvian New Sol.
    CU_PERU_NEW_SOL = 37

    # Philippine Peso.
    CU_PHILIPPINES_PESO = 38

    # Polish Zloty.
    CU_POLAND_ZLOTY = 39

    # Portuguese Escudo.
    CU_PORTUGAL_ESCUDO = 40

    # Saudi Arabian Riyal.
    CU_SAUDI_ARABIA_RIYAL = 41

    # Singaporean Dollar.
    CU_SINGAPORE_DOLLAR = 42

    # Slavic Koruna.
    CU_SLOVAK_KORUNA = 43

    # South African Rand.
    CU_SOUTH_AFRICA_RAND = 44

    # South Korean Won.
    CU_SOUTH_KOREA_WON = 45

    # Spanish Peseta.
    CU_SPAIN_PESETA = 46

    # international governmental exchange.
    CU_SPECIAL_DRAWING_RIGHTS = 47

    # Swedish Krona.
    CU_SWEDEN_KRONA = 48

    # Swiss Franc.
    CU_SWITZERLAND_FRANC = 49

    # Taiwanese Dollar.
    CU_TAIWAN_DOLLAR = 50

    # Thai Baht.
    CU_THAILAND_BAHT = 51

    # Turkish Lira.
    CU_TURKEY_LIRA = 52

    # United Arab Emirates Dirham.
    CU_UNITED_ARAB_DIRHAM = 53

    # United States Dollar.
    CU_UNITED_STATES_DOLLAR = 54

    # Uruguayan New Peso.
    CU_URUGUAY_NEW_PESO = 55

    # Venezuelan Bolivar.
    CU_VENEZUELA_BOLIVAR = 56

    def __init__(self):
        super().__init__(
            key=9,
            scope=0,
            prefix='CU_'
        )
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = currency_t()
    pass
