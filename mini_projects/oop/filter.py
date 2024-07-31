languages = [('C', 1972), ('C++', 1985), ('Java', 1995), ('JavaScript', 1995), ('PHP', 1994), ('Python', 1991)]

def date(lang):
    return lang[1] > 1990

print(list(filter(date,languages)))
#start with j
languages = [('C', 1972), ('C++', 1985), ('Java', 1995), ('JavaScript', 1995), ('PHP', 1994), ('Python', 1991)]
def find(iterable, text):
    def finder(Lang):
        for i in Lang:
            if str(i).startswith(text):
                return True
            return False
    return list(filter(finder, iterable))

results = find(languages, 'J')

print(results)