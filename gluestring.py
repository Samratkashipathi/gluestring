import re
def glue_it(templateString, dictionaryToMatch):
    pattern = re.compile('\{\{([^}$]*)\}\}')
    number_of_patterns_found = len(pattern.findall(templateString))
     
    for i in range(number_of_patterns_found):
        val = pattern.search(templateString).groups()[0]
        if val in dictionaryToMatch:
            templateString = templateString.replace('{{'+val+'}}',dictionaryToMatch[val])
        else:
            templateString = templateString.replace('{{'+val+'}}',dictionaryToMatch['default'])            
    return templateString