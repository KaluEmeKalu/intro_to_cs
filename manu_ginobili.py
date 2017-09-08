# -*- coding: utf-8 -*-

"""
What are Python Data Types?
    A data type defines how the variable is stored and the rules governing how the data can be manipulated.

Four Major Categories of Data Types
    1) Booleans - Boolean
    2) Sequences - String, Tuple, List
    3) Mappings - Dictionary
    4) Numeric - Integer, Float

1) Int
    age = 20
2) Float
    gpa = 3.333
3) String
    name = "Kalu"
4) List
    favorite_foods = ["Nigerian food", "Chinese food", "Pizza"]
5) Tuple
    triangle_sides = ("Side A", "Side B", "Side C")
6) Boolean
    isPublished = True
7) Dict
    profile = {'name': 'Kalu', 'age': 20, 'job': 'banker', 'salary': 400,000}



"""

# String
name = "Manu Ginobili"

# Boolean
isGOAT = True

# Int
number = 23

# float
career_pts_per_36 = 19.1

#tuple, immutable, cannot be changed
draft = ('1999 Draft', "San Antonio Spurs", "2nd round", "28th pick", '57th overall')

# list - mutable, can be changed
awards = ["2x All-Star", "4x NBA Champion", "2x All-NBA", "2002-03 All-Rookie"]

#dict
name_translations = {"Spanish": "Emanuel Ginóbili", "Chinese": "马努·吉诺比利", 
                     "Japanese": "エマニュエル・ジノビリ", "Korean": "마누 지노빌리",
                     "Persian": "مانو جینوبلی آمار"}


text = "\n\nIn Chinese he is called " + name_translations["Chinese"] + '. '
text += "In Korean, " + name_translations['Korean'] + ', '
text += "and in English he is called " + name + '. '
text += "But his mother named him the one and only "
text += name_translations['Spanish']
text += ". Wearing the number " + str(number) + " he was drafted in "

print(text)
