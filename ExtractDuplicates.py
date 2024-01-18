
# prints duplicates in list a

from collections import Counter

a = [1, 5, 1, 2, 3, 5, 'azi', 'azi', 'a']


print([element for element, count in Counter(a).items() if count > 1])
    