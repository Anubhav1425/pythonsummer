def cigar_party(n,w):
	if w ==True:
		if n>40:
			return True
		else:
			return False
	elif w ==False:
		if n<60 and n>40:
			return True
		else:	
			return False
