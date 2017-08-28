#!/usr/bin/env python
# encoding: utf-8

class Read() :
    def __init__(self,num) :
        self.num = int(num)
        self.sumup = 0

    def sum_up(self) :
        x = self.num
        n = 0
        while x >= 10:
            n = x-int(x/10)*10+n
            x = int(x/10)
        print ("%d%s:%d"%(self.num,"的总和是",n+x))

    def print_it(self) :
        L = ['ling','yi','er','san','si','wu','liu','qi','ba','jiu']
        x = self.num
        n = 0
        while x >= 10 :
            n = x - int(x/10)*10+n
            x = int(x/10)
        s = n+x
        if s >= 100 :
            a = s%10
            b = int ((s%100-s%10)/10)
            c = int (s/100)   
            print ("%d%s:%s%s%s"%(s,"的拼音是",L[c],L[b],L[a]))
        elif s >= 10 :
            a = s%10
            b = int(s/10)
            print ("%d%s:%s%s"%(s,"的拼音是",L[b],L[a]))
        else :
            print ("%d%s:%s"%(s,"的拼音是",L[s]))

    def change(self) :
        q = self.num
        n = 0
        while q >= 10 :
            n = q - int(q/10)*10+n
            q = int (q/10)
        x = q+n
        a = int(x/pow(7,3))
        x = x - a*pow(7,3)
        b = int(x/pow(7,2))
        x = x - b*pow(7,2)
        c = int(x/7)
        x = x - c*7        
        s = a*1000+b*100+c*10+x
        print ("%d%s:%d"%(q+n,"的7进制数是",s))
if __name__ == '__main__' :
    number = Read(input("输入一个尽可能长的数字\n"))
    number.sum_up()
    number.print_it()
    number.change()