import re
txt= "The rain in Germany"
x = re.search("^The.*Germany$", txt)
if x:
    print("YES!, We have a match")
else:
    print("No Match!")