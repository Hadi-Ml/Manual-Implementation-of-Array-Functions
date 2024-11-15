class Array :
    def Initialize_Array(self , List1) :
        self.List1 = List1
        self.Length = 0
        for i in self.List1 :
            self.Length += 1

    def Insert(self , Index , Value) :
        if Index <= self.Length :
            self.List2 = self.List1.copy() + [None]
            self.List2[Index-1] = Value
            for i in range(Index,self.Length+1) :
                self.List2[i] = self.List1[i-1]
            return self.List2
        else :
            print("Index out of range (Index Must between 0 and", self.Length - 1)



Example_Array = [1,2,3,4,5,6,7,8,9,10]

obj = Array ()

obj.Initialize_Array (Example_Array)

# print(obj.Insert(4,20))

print(obj.Delete_By_Value(10))





