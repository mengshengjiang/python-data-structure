from stack import Stack


def matches(open, close):
	opens = "([{"
	closes = ")]}"
	return opens.index(open) == closes.index(close)

	
def parChecker(symbolString):
	s = Stack()
	index = 0
	balanced = True
	while index < len(symbolString):
		symbol = symbolString[index]
		if symbol in '([{':
			s.push(symbol)
		elif symbol in '}])':
			if s.isEmpty():
				balanced = False
			else:
				top = s.pop()
				if not matches(top,symbol):
					balanced = False

		index += 1


	if s.isEmpty() and balanced:
		return True
	else:
		return False



print(parChecker('((([)))'))
print(parChecker('()[]{}'))
