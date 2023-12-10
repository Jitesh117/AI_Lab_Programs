import language_check


# Mention the language keyword
tool = language_check.LanguageTool('en-US')
i = 0

# Path of file which needs to be checked
with open(r'transcript1.txt', 'r') as fin:
			
	for line in fin:
		matches = tool.check(line)
		i = i + len(matches)	
		pass

# prints total mistakes which are found
# from the document
print("No. of mistakes found in document is ", i)
print()

# prints mistake one by one
for mistake in matches:
	print(mistake)
	print()
