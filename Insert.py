class Array :

    def Initialize_Array(self,List1) :
        self.List1 = List1
        self.Length = 0
        for i in self.List1 :
            self.Length += 1


    def Insert1(self,Index,Value) :
        if Index <= self.Length :
            self.List2 = self.List1 + [None]
            self.List2[Index] = Value
            for i in range(Index+1,self.Length+1) :
                self.List2[i] = self.List1[i-1]
            return self.List2
        else :
            print("Index out of range (Index Must between 0 and", self.Length - 1)


    def Insert2(self,Index,Value) :
        if Index <= self.Length :
            self.List7 = [0] * (self.Length+1)
            for i in range (Index) :
                self.List7[i] = self.List1[i]
            self.List7[Index] = Value
            for j in range (Index,self.Length) :
                self.List7[j+1] = self.List1[j]
            return self.List7
        else :
            print("Index out of range (Index Must between 0 and", self.Length - 1)



# ----------------------------------------------------------------------------------------------------------------------


Example_Array = [1,2,3,4,5,6,7,8,9,10]

obj = Array()

obj.Initialize_Array(Example_Array)

print(obj.Insert1(4,20))
# prints [1, 2, 3, 4, 20, 5, 6, 7, 8, 9, 10]

print(obj.Insert2(8,50))
# prints [1, 2, 3, 4, 5, 6, 7, 8, 50, 9, 10]


#Thank you for Watching ;)
#Developed By Hadi_Molaei
