#!/usr/bin/env python3

# Для каждого регулярного выражения, которое требуется написать,
# указана строка, в которой нужно найти подстроку, а следом
# после стрелки (--->) указана сама искомая подстрока

# bab ---> a
# bcb ---> c
# bxb ---> x
REGEXP_1 = '[^b]'

# ooooAAAooooo ---> AAA
# asdfasdAAAAfasdf ---> AAAA
# AAAAAAfasdf ---> AAAAAA
# iiiiiA ----> A
REGEXP_2 = '[A]{1,6}'

# There is <html> tag ---> <html>
# color can be used as <font color='red'> ---> <font color='red'>
# There is x <> 10 and something was wrong with < or > brace. ---> < or >
REGEXP_3 = '[<].{1,30}[>]'

# C@n Y0u f1nd CaPoAira? ---> CaPoAira
# s0 Wh@t i5 CamelStyle? ---> CamelStyle
# Any simple word should match. ---> Any
# I like regular expressions ---> like
REGEXP_4 = ''

# all those that were numbered of the camps throughout their hosts were 603550. ---> 603550
# What is the meaning of life, the universe and everything? *42* Douglas Adams ---> 42
# Clive Staples Lewis was born in Belfast, Ireland, on 29 November 1898. ----> 29
REGEXP_5 = '\d+'

# New York: W. H. Freeman, pp. 347-353, 1991. ---> Freeman
# set out to travel much faster than light ---> travel
# Arise ye, and depart; for this is not your rest... ---> depart
REGEXP_6 = '\w(reeman|ravel|epart)}'

# I know that cat can catch a mouse! ---> cat can catch a mouse
# But this mouse is faster than the cat. ---> mouse is faster than the cat
# Mouse Mickey is not a simple mouse. Tom is a dummy cat. ---> mouse. Tom is a dummy cat
REGEXP_7 = '[m]{1}[.]{0,40}[t]{1}'

# his phone number was 892512366482. ---> 892512366482
# I called +7 999 648-99-86 ans it was right. ---> +7 999 648-99-86
# Some 52221 numbers should not hide phone numbers such as 8 915 747-68-99 ---> 8 915 747-68-99
REGEXP_8 = '[+]?\b[+79684321][0-9]{0,15}[-]?\s?[+79684321]?[0-9]{0,15}[-]?\s?[+79684321]?[0-9]{0,15}[-]?\s?[+79684321]?[0-9]{0,15}[-]?\s?[+79684321]?[0-9]{0,15}'
