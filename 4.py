def find_ugly_number(n):
	counter=0
	ugly_number=[1]#store the disorted ugly number
	ugly_number_sorted=[]
	factor=(2,3,5)
	i=0
	#新的丑数由之前最小的丑数乘上2,3,5得到，不断更新之前的丑数 
	while counter<n:
		min_value=min(ugly_number)#优先队列
		ugly_number.remove(min_value)
		ugly_number_sorted.append(min_value)
		counter+=1
		for j in factor:
			c=j*min_value
			if c not in ugly_number:
				ugly_number.append(c)
		i=i+1
	return ugly_number_sorted[n-1]
if __name__=='__main__':
	print(find_ugly_number(9))