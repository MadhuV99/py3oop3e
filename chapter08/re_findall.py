# re_findall.py
import re

print(re.findall('a.', 'abacadefagah'))
print(re.findall('a(.)', 'abacadefagah'))
print(re.findall('(a)(.)', 'abacadefagah'))
print(re.findall('((a)(.))', 'abacadefagah'))
