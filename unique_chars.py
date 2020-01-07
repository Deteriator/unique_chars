def unique_char(st): 
	if st == "": 
		return False
  #make sure it doesn't go over range
	if len(st) > 256: 
		return False

	# set all codes for characters
	char_set = [False] * 128

	# check if it exits in charset
	# in char_set 
	for i in range(0, len(st)): 
		st = st.lower()
		# Find ASCII value and check if it 
		# exists in set. 
		val = ord(st[i]) 
		if char_set[val]: 
			return False

		char_set[val] = True

	return True
# tests

print(unique_char('abcd')) #True
print(unique_char('aab')) #False
print(unique_char("Aa")) # False
print(unique_char("")) #False

