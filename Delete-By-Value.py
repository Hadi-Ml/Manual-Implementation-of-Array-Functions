class Array :

    def Initialize_Array(self,List1) :
        self.List1 = List1
        self.Length = 0
        for i in self.List1 :
            self.Length += 1

    def Delete_By_Value(self,value) :
        self.List3 = [0] * (self.Length-1)
        for i in range (self.Length-1) :
            self.List3[i] = self.List1[i]
        for j in range (self.Length) :
            if self.List1[j] == value :
                for k in range (j,self.Length-1) :
                    self.List3[k] = self.List1[k+1]
                return j



# ----------------------------------------------------------------------------------------------------------------------


Example_Array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

obj = Array()

obj.Initialize_Array(Example_Array)

print(obj.Delete_By_Value(7))
# prints 6


# Thank you for Watching ;)
# Developed By Hadi_Molaei