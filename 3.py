def decompose(n):
	L = []
	while True:
		i = n % 10
		L.append(i)
		n=int(n/10)
		if n==0:
		    break
	return L
def merge(L):
	sum=0
	for i,value in enumerate(L):
		sum+=value*10**i
	return sum

def find(L,k):
	counter=0
	i=len(L)
	if i==1:
		if L[0]>=k:
			return 1
	else:
		counter += 10**(i-1)+(L[-1])*10**(i-2)*(i-1)
		if L[-1]<k or k == 0 :
			counter -=10**(i-1)
		if L[-1]==k:
			counter-=10**(i-1)
			#print(counter)
			L2=L[0:len(L)-1]
			counter+=merge(L2)+1
			#print(counter)
		flag=False
		for j in range(-2,-len(L)-1,-1):
			if L[j]!=0:
				flag=True
				break
		if not flag:
			j=j-1
		L1=L[0:len(L)+j+1]
		if len(L1)==0:
			return counter
	return counter+find(L1,k)

def find_k(n,k):
	'''比如说n=404，此函数求解100到404中k出现的次数'''
	counter=0
	L=decompose(n)
	i=len(L)
	if n==1:
		if L[-1]>=k:
			return 1
	else:
		#比如说n=404，此处求解100到400，k出现的次数
		counter += 10**(i-1)+(L[-1]-1)*10**(i-2)*(i-1)
		if L[-1]<k or k == 0 :
			counter -=10**(i-1)
		if L[-1]==k:
			counter-=10**(i-1)
			L2=L[0:len(L)-1]
			counter+=merge(L2)+1
		#比如说n=404，后续将求解400到404，k出现的次数
		flag=False
		for j in range(-2,-len(L)-1,-1):
			if L[j]!=0:
				flag=True
				break
		if not flag:
			j=j-1
		L1=L[0:len(L)+j+1]
		if len(L1)==0:
			return counter
		#print('A',counter)
		#print('B',find(L1,k))
		return counter+find(L1,k)

def count(n,k):
	s=str(n)
	k1=str(k)
	counter=0
	#统计从长度为1到长度为len(n)-1的数字中k出现的次数
	#比如说n=404，改循环求解0，到99中k出现的次数
	for i in range(1,len(s)):
		counter += 10**(i-1)+9*10**(i-2)*(i-1)#满足此公式
		if k == 0 and i !=1:
			counter -=10**(i-1)
			
	counter=int(counter+find_k(n,k))
	return counter

def find_k_version1(n,k):
	k=str(k)
	counter=0
	for i in range(0,n+1):
		i=str(i)
		for j in i:
			if j == k:
				counter+=1
	return counter
if __name__ == '__main__':
	print(count(9999,9))


#a better way
'''
#除开五的倍数之外的奇数和末尾不是0的数相乘，不产生零位，故剔除
#剩下的数，利用分配率，寻找能产生末尾0的组合，将10提出，继续，直至无零位产生

def number_of_last_zeros(n):
	L=[]
	for i in range(1,n+1):
		L.append(i)
	k=count_zeros(L)
	return k


def count_zeros(L):
	if len(L)==0:
		return 0
	k=0#用来表示当前末尾0的个数
	L1=[]
	#剔除非5的倍数的奇数
	for i in L:
		if i %10 ==0:
			x,t=find_zeros(i)
			k=k+x
			if t%2 !=1 or t % 5==0:
				L1.append(t)
		elif i%2 !=1 or i % 5==0:
			L1.append(i)
	#如果全部剔除，返回k
	if len(L1)==0:
		return k
	else:
		#初始化标志列表，如果两位数相乘末尾为0，则该轮不可用
		is_used=[0 for i in range(0,len(L1))]
	is_countinue=False
	L2=[]
	for i in range(0,len(L1)-1):
		for j in range(i+1,len(L1)):
			if is_used[i] ==1 or is_used[j] ==1:
				continue
			c=L1[i]*L1[j]
			if c%10==0:
				is_countinue=True
				is_used[i],is_used[j]=1,1
				x,t=find_zeros(c)
				k=k+x
				if t %2 !=1 or t % 5==0:
					L2.append(t)
	for i in range(0,len(L1)):
		if is_used[i]==0 :
			L2.append(L1[i])
	if not is_countinue:
		return k
	else:
		return k+count_zeros(L2)

def find_zeros(n):
	#对10的倍数操作，返回幂次和余数
	k=0
	while True:
		if n%10 != 0:
			return k,n 
		k=k+1
		n=n/10
if __name__=='__main__':
	L=[1,2,3,4]
	L1=L[]
	print(L1)
	#print(count_zeros(L))
	#print(L[]) 
'''