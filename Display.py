class Array :

    def Initialize_Array(self,List1) :
        self.List1 = List1
        self.Length = 0
        for i in self.List1 :
            self.Length += 1


    def Display(self,List1) :
        return self.List1



# ----------------------------------------------------------------------------------------------------------------------

Example_Array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

obj = Array()

obj.Initialize_Array(Example_Array)

print(obj.Display(Example_Array))
# prints [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Thank you for Watching ;)
# Developed By Hadi_Molaei