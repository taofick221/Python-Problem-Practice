# Search the string to see if it starts with "The" and ends with "Spain"

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)



# Print a list of all matches

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


# Return an empty list if no match was found

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)