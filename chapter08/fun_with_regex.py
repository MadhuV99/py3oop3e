# fun_with_regex.py
import re
pattern_search = [
# ('hello world', '^hello world$'),
# ('hello worl', '^hello world$'),
# ('hello world', 'hel.o world'),
# ('helpo world', 'hel.o world'),
# ('hel o world', 'hel.o world'),
# ('helo world', 'hel.o world'),

# ('hello world', 'hel[lp]o world'),
# ('helpo world', 'hel[lp]o world'),
# ('helPo world', 'hel[lp]o world'),

# ('hello   world', 'hello [a-z] world'),
# ('hello b world', 'hello [a-z] world'),
# ('hello B world', 'hello [a-zA-Z] world'),
# ('hello 2 world', 'hello [a-zA-Z0-9] world'),

# ('0.05', '0\.[0-9][0-9]'),
# ('005', '0\.[0-9][0-9]'),
# ('0,05', '0\.[0-9][0-9]'),

# ('(abc]', '\(abc\]'),
# (' 1a', '\s\d\w'),
# ('\t5n', '\s\d\w'),
# ('5n', '\s\d\w'),
# (' 1aword', '\s\d\w'),

# ('hello', 'hel*o'),
# ('heo', 'hel*o'),
# ('hellllllo', 'hel*o'),

# ('A string.', '[A-Z][a-z]* [a-z]*\.'),
# ('No .', '[A-Z][a-z]* [a-z]*\.'),
# ('', '[a-z]*.*'),

# ('0.4', '\d+\.\d+'),
# ('1.002', '\d+\.\d+'),
# ('1.', '\d+\.\d+'),
# ('1%', '\d+\.\d+'),
# ('99%', '\d+\.\d+'),
# ('999%', '\d+\.\d+'),

('Eat.', '[A-Z][a-z]*( [a-z]+)*\.$'),
('Eat more good food.', '[A-Z][a-z]*( [a-z]+)*\.$'),
('A good meal.', '[A-Z][a-z]*( [a-z]+)*\.$'),

]
for search_string, pattern in pattern_search:
    # search_string = "hello world"
    # pattern = "hello world"
    match = re.match(pattern, search_string)
    if match:
        # print("regex matches") 
        template = "'{}' matches pattern '{}'"
    else:
        template = "'{}' does not match pattern '{}'"
    print(template.format(search_string, pattern)) 