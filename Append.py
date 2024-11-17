class Array :

    def Initialize_Array(self,List1) :
        self.List1 = List1
        self.Length = 0
        for i in self.List1 :
            self.Length += 1


    def Append(self , Value) :
        self.List5 = [0] * (self.Length+1)
        for i in range (self.Length) :
            self.List5[i] = self.List1[i]
        self.List5[self.Length] = Value
        return self.List5


# ----------------------------------------------------------------------------------------------------------------------


Example_Array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

obj = Array()

obj.Initialize_Array(Example_Array)

print(obj.Append(900))
# prints [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 900]


# Thank you for Watching ;)
# Developed By Hadi_Molaei