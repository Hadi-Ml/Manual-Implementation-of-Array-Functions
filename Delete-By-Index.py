class Array :

    def Initialize_Array(self,List1) :
        self.List1 = List1
        self.Length = 0
        for i in self.List1 :
            self.Length += 1


    def Delete_By_Index(self , Index) :
        self.List4 = [0] * (self.Length-1)
        for i in range (self.Length-1) :
            self.List4[i] = self.List1[i]
        for i  in range (self.Length-1) :
            if i == Index :
                for j in range (i,self.Length-1) :
                    self.List4[j] = self.List1[j+1]
        return self.List4


# ----------------------------------------------------------------------------------------------------------------------

Example_Array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

obj = Array()

obj.Initialize_Array(Example_Array)

print(obj.Delete_By_Index(9))
# prints [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Thank you for Watching ;)
# Developed By Hadi_Molaei