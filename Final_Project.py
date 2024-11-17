class Array :

    def Initialize_Array(self , List1) :
        self.List1 = List1
        self.Length = 0
        for i in self.List1 :
            self.Length += 1


    def Insert1(self , Index , Value) :
        if Index <= self.Length :
            self.List2 = self.List1 + [None]
            self.List2[Index] = Value
            for i in range(Index+1,self.Length+1) :
                self.List2[i] = self.List1[i-1]
            return self.List2
        else :
            print("Index out of range (Index Must between 0 and", self.Length - 1)


    def Insert2(self , Index , Value) :
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


    def Delete_By_Value(self , value) :
        self.List3 = [0] * (self.Length-1)
        for i in range (self.Length-1) :
            self.List3[i] = self.List1[i]
        for j in range (self.Length) :
            if self.List1[j] == value :
                for k in range (j,self.Length-1) :
                    self.List3[k] = self.List1[k+1]
                return j


    def Delete_By_Index(self , Index) :
        self.List4 = [0] * (self.Length-1)
        for i in range (self.Length-1) :
            self.List4[i] = self.List1[i]
        for i  in range (self.Length-1) :
            if i == Index :
                for j in range (i,self.Length-1) :
                    self.List4[j] = self.List1[j+1]
        return self.List4



    def Display(self) :
        return self.List1



    def Append(self , Value) :
        self.List5 = [0] * (self.Length+1)
        for i in range (self.Length) :
            self.List5[i] = self.List1[i]
        self.List5[self.Length] = Value
        return self.List5



    def Reverse (self,arr1) :
        Count = 0
        for i in arr1 :
            Count += 1
        arr2 = [0] * Count
        j = Count - 1
        for i in range (Count) :
            arr2[i] = arr1[j]
            j -= 1
        return arr2



    def Search_by_Value(self,Value) :
        for i in range (self.Length) :
            if self.List1[i] == Value :
                return i



# ----------------------------------------------------------------------------------------------------------------------


Example_Array = [1,2,3,4,5,6,7,8,9,10]

obj = Array ()

obj.Initialize_Array (Example_Array)

# print(obj.Insert1(4,20))
# prints [1, 2, 3, 4, 20, 5, 6, 7, 8, 9, 10]

# print(obj.Insert2(8,50))
# prints [1, 2, 3, 4, 5, 6, 7, 8, 50, 9, 10]

# print(obj.Delete_By_Value(7))
# prints 6

# print(obj.Delete_By_Index(9))
# prints [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(obj.Display(Example_Array))
# prints [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(obj.Append(900))
# prints [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 900]

# print(obj.Reverse(Example_Array))
# prints [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# print(obj.Search_by_Value(3))
# prints 2


# Thank you for Watching ;)
# Developed By Hadi_Molaei





