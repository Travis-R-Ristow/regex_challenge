import re

def get_matching_words(regex):
    results = []
    words = [
        "baby",
        "baseball",
        "denver",
        "facetious",
        "issue",
        "mattress",
        "obsessive",
        "paranoia",
        "rabble",
        "union",
        "volleyball",
    ]
    for word in words:
        if re.search(regex, word):
            results.append(word)

    return results

my_expression = r"."
print 'all'
print get_matching_words(my_expression)
print '-'*100
one = r'ss'
print 'one'
print get_matching_words(one)
print '-'*100
two = r'b\wb'
print 'two'
print get_matching_words(two)
print '-'*100
three = r'b\w+b'
print 'three'
print get_matching_words(three)
print '-'*100
four = r'b\w*b'
print 'four'
print get_matching_words(four)
print '-'*100
five = r'b\w?b'
print 'five'
print get_matching_words(five)
print '-'*100
six = r'a\w*e\w*i\w*o\w*u'
print 'six'
print get_matching_words(six)
print '-'*100
seven = r'[aeiou]{2}$'
print 'seven'
print get_matching_words(seven)
print '-'*100
eight = r'^[regulaxpsion]*$'
print 'eight'
print get_matching_words(eight)
print '-'*100
nine = r'^[^regx]*$'
print 'nine'
print get_matching_words(nine)
print '-'*100
ten = r'l{2}\w*l{2}'
print 'ten'
print get_matching_words(ten)
print '-'*100