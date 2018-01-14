def find(Numbers,target):
	'''先排序，先用双重循环得到两个数字的组合，另外两个数字，一个从前往后，一个从后向前，遍历得到'''
	L=[]
	length = len(Numbers)
	Numbers.sort()
	for i in range(0,length):
		#遇见相同数直接跳过
		if i != 0 and Numbers[i] == Numbers[i-1]:
			continue
		for j in range(i+1,length):
			if j != i+1 and Numbers[j] == Numbers[j-1]:
				continue
			m = j+1
			n = length-1
			while m<n:
				counter = Numbers[i]+Numbers[j]+Numbers[m]+Numbers[n]
				if m != j+1 and Numbers[m] == Numbers[m-1]:
					m = m+1
				elif n != length-1 and Numbers[n] == Numbers[n+1]:
					n=n-1
				elif counter == target:
					s=[Numbers[i],Numbers[j],Numbers[m],Numbers[n]]
					m=m+1
					n=n-1
					if s not in L:
						L.append(s)
				elif counter > target:
					n=n-1
				elif counter < target:
					m=m+1
	return L

if __name__ == "__main__" :
	L=[1,2,3,4,2]
	print(find(L,10))