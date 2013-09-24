"""days_of_month_t standard enumeration type, originally defined in resource
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


class days_of_month_t(base.Enumeration):
    """days_of_month_t standard enumeration."""

    # Invalid value.
    DM_NUL = -1

    # Every day of month.
    DM_EVERY_DAY = 0

    # First day of month.
    DM_DAY_1 = 1

    # Second day of month.
    DM_DAY_2 = 2

    # Third day of month.
    DM_DAY_3 = 3

    # Fourth day of month.
    DM_DAY_4 = 4

    # Fifth day of month.
    DM_DAY_5 = 5

    # Sixth day of month.
    DM_DAY_6 = 6

    # Seventh day of month.
    DM_DAY_7 = 7

    # Eighth day of month.
    DM_DAY_8 = 8

    # Ninth day of month.
    DM_DAY_9 = 9

    # Tenth day of month.
    DM_DAY_10 = 10

    # Eleventh day of month.
    DM_DAY_11 = 11

    # Twelfth day of month.
    DM_DAY_12 = 12

    # Thirteenth day of month.
    DM_DAY_13 = 13

    # Fourteenth day of month.
    DM_DAY_14 = 14

    # Fifteenth day of month.
    DM_DAY_15 = 15

    # Sixteenth day of month.
    DM_DAY_16 = 16

    # Seventeeth day of month.
    DM_DAY_17 = 17

    # Eighteenth day of month.
    DM_DAY_18 = 18

    # Nineteenth day of month.
    DM_DAY_19 = 19

    # Twentieth day of month.
    DM_DAY_20 = 20

    # Twenty-first day of month.
    DM_DAY_21 = 21

    # Twenty-second day of month.
    DM_DAY_22 = 22

    # Twenty-third day of month.
    DM_DAY_23 = 23

    # Twenty-fourth day of month.
    DM_DAY_24 = 24

    # Twenty-fifth day of month.
    DM_DAY_25 = 25

    # Twenty-sixth day of month.
    DM_DAY_26 = 26

    # Twenty-seventh day of month.
    DM_DAY_27 = 27

    # Twenty-eighth day of month.
    DM_DAY_28 = 28

    # Twenty-ninth day of month.
    DM_DAY_29 = 29

    # Thirtieth day of month.
    DM_DAY_30 = 30

    # Thirty-first day of month.
    DM_DAY_31 = 31

    # Last day of month.
    DM_LAST_DAY_OF_MONTH = 32

    # Second to last day of month.
    DM_LAST_SECOND_DAY = 33

    # Third to last day of month.
    DM_LAST_THIRD_DAY = 34

    # Fourth to last day of month.
    DM_LAST_4TH_DAY = 35

    # Fifth to last day of month.
    DM_LAST_5TH_DAY = 36

    # Sixth to last day of month.
    DM_LAST_6TH_DAY = 37

    # Seventh to last day of month.
    DM_LAST_7TH_DAY = 38

    # Eighth to last day of month.
    DM_LAST_8TH_DAY = 39

    # Ninth to last day of month.
    DM_LAST_9TH_DAY = 40

    # Tenth to last day of month.
    DM_LAST_10TH_DAY = 41

    # Eleventh to last day of month.
    DM_LAST_11TH_DAY = 42

    # Twelfth to last day of month.
    DM_LAST_12TH_DAY = 43

    # Thirteenth to last day of month.
    DM_LAST_13TH_DAY = 44

    # Fourteenth to last day of month.
    DM_LAST_14TH_DAY = 45

    # Fifteenth to last day of month.
    DM_LAST_15TH_DAY = 46

    # Sixteenth to last day of month.
    DM_LAST_16TH_DAY = 47

    # Seventeeth to last day of month.
    DM_LAST_17TH_DAY = 48

    # Eighteenth to last day of month.
    DM_LAST_18TH_DAY = 49

    # Nineteenth to last day of month.
    DM_LAST_19TH_DAY = 50

    # Twentieth to last day of month.
    DM_LAST_20TH_DAY = 51

    # Twenty-first to last day of month.
    DM_LAST_21ST_DAY = 52

    # Twenty-second to last day of month.
    DM_LAST_22ND_DAY = 53

    # Twenty-third to last day of month.
    DM_LAST_23RD_DAY = 54

    # Twenty-fourth to last day of month.
    DM_LAST_24TH_DAY = 55

    # Twenty-fifth to last day of month.
    DM_LAST_25TH_DAY = 56

    # Twenty-sixth to last day of month.
    DM_LAST_26TH_DAY = 57

    # Twenty-seventh to last day of month.
    DM_LAST_27TH_DAY = 58

    # Twenty-eighth to last day of month.
    DM_LAST_28TH_DAY = 59

    # Twenty-ninth to last day of month.
    DM_LAST_29TH_DAY = 60

    # Thirtieth to last day of month.
    DM_LAST_30TH_DAY = 61

    # First Sunday of month.
    DM_FIRST_SUN = 62

    # First Monday of month.
    DM_FIRST_MON = 63

    # First Tuesday of month.
    DM_FIRST_TUE = 64

    # First Wednesday of month.
    DM_FIRST_WED = 65

    # First Thursday of month.
    DM_FIRST_THU = 66

    # First Friday of month.
    DM_FIRST_FRI = 67

    # First Saturday of month.
    DM_FIRST_SAT = 68

    # Second Sunday of month.
    DM_SECOND_SUN = 69

    # Second Monday of month.
    DM_SECOND_MON = 70

    # Second Tuesday of month.
    DM_SECOND_TUE = 71

    # Second Wednesday of month.
    DM_SECOND_WED = 72

    # Second Thursday of month.
    DM_SECOND_THU = 73

    # Second Friday of month.
    DM_SECOND_FRI = 74

    # Second Saturday of month.
    DM_SECOND_SAT = 75

    # Third Sunnday of month.
    DM_THIRD_SUN = 76

    # Third Monday of month.
    DM_THIRD_MON = 77

    # Third Tuesday of month.
    DM_THIRD_TUE = 78

    # Third Wednesday of month.
    DM_THIRD_WED = 79

    # Third Thursday of month.
    DM_THIRD_THU = 80

    # Third Friday of month.
    DM_THIRD_FRI = 81

    # Third Saturday of month.
    DM_THIRD_SAT = 82

    # Fourth Sunday of month.
    DM_FOURTH_SUN = 83

    # Fourth Monday of month.
    DM_FOURTH_MON = 84

    # Fourth Tuesday of month.
    DM_FOURTH_TUE = 85

    # Fourth Wednesday of month.
    DM_FOURTH_WED = 86

    # Fourth Thursday of month.
    DM_FOURTH_THU = 87

    # Fourth Friday of month.
    DM_FOURTH_FRI = 88

    # Fourth Saturday of month.
    DM_FOURTH_SAT = 89

    # Fifth Sunday of month.
    DM_FIFTH_SUN = 90

    # Fifth Monday of month.
    DM_FIFTH_MON = 91

    # Fifth Tuesday of month.
    DM_FIFTH_TUE = 92

    # Fifth Wednesday of month.
    DM_FIFTH_WED = 93

    # Fifth Thursday of month.
    DM_FIFTH_THU = 94

    # Fifth Friday of month.
    DM_FIFTH_FRI = 95

    # Fifth Saturday of month.
    DM_FIFTH_SAT = 96

    # Last Sunday of month.
    DM_LAST_SUN = 97

    # Last Monday of month.
    DM_LAST_MON = 98

    # Last Tuesday of month.
    DM_LAST_TUE = 99

    # Last Wednesday of month.
    DM_LAST_WED = 100

    # Last Thursday of month.
    DM_LAST_THU = 101

    # Last Friday of month.
    DM_LAST_FRI = 102

    # Last Saturday of month.
    DM_LAST_SAT = 103

    # Every Sunday of the month.
    DM_EVERY_SUN = 104

    # Every Monday of the month.
    DM_EVERY_MON = 105

    # Every Tuesday of the month.
    DM_EVERY_TUE = 106

    # Every Wednesday of the month.
    DM_EVERY_WED = 107

    # Every Thursday of the month.
    DM_EVERY_THU = 108

    # Every Friday of the month.
    DM_EVERY_FRI = 109

    # Every Saturday of the month.
    DM_EVERY_SAT = 110

    # Every second day (i.e.  every other day) of the date.
    DM_EVERY_SECOND_DAY = 111

    # Every third day of the date interval.
    DM_EVERY_THIRD_DAY = 112

    # Every fourth day of the date interval.
    DM_EVERY_FOURTH_DAY = 113

    # Every fifth day of the date interval.
    DM_EVERY_FIFTH_DAY = 114

    # Every sixth day of the date interval.
    DM_EVERY_SIXTH_DAY = 115

    # Every weekday (Monday - Friday).
    DM_EVERY_WEEKDAY = 116

    # Every weekend day (Saturday - Sunday).
    DM_EVERY_WEEKEND_DAY = 117

    def __init__(self):
        super().__init__(
            key=54,
            scope=0,
            prefix='DM_'
        )
        self._definition = standard.add(self)


if __name__ == '__main__':
    # unit test code.
    item = days_of_month_t()
    pass
