def commonCharacters(a, b):
	chars = {}
	result = ""

	for letter in b:
		chars[letter] = True

	for letterInA in a:
		if letterInA in chars:
			result += letterInA

	return result

print(commonCharacters("asdf", "ad"))