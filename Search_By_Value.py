class Array :

    def Initialize_Array(self,List1) :
        self.List1 = List1
        self.Length = 0
        for i in self.List1 :
            self.Length += 1


    def Search_by_Value(self,Value) :
        for i in range (self.Length) :
            if self.List1[i] == Value :
                return i



# ----------------------------------------------------------------------------------------------------------------------


Example_Array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

obj = Array()

obj.Initialize_Array(Example_Array)

print(obj.Search_by_Value(3))
# prints 2


# Thank you for Watching ;)
# Developed By Hadi_Molaei