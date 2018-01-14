#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#date:2017-5-31
def aplusb(a, b):
    if b == 0:
        return a
    if a == 0:
        return b
    #直到进位为0
    while b!=0:
        carry = (a&b)<<1 #求进位
        a = a ^ b#忽略进位求和
        b = carry#加上进位
    return a
def tong(A):
    x=max(A)
    count={}
    for i in range(0,x+1):
        count[i]=0
        for i in A:
            count[i]+=1
    sum=0
    L={}
    for i in range(0,x+1):
        L[i]=0
    for i in range(0,x+1):
        if i==0:
            L[i]=0
        else:
            sum=sum+count[i-1]
            L[i]=sum
    for i in A:
        print(L[i])
