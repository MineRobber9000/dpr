def hashCode(s):
	bs = s.encode("utf-8")
	hash = 0
	for i in range(len(bs)):
		hash = (31*hash+bs[i])&0xFFFFFFFF
	return ((hash+0x80000000)&0xFFFFFFFF)-0x80000000

if __name__=="__main__": print(hashCode(input("> ")))
