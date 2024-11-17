class Array :

    def Initialize_Array(self,List1) :
        self.List1 = List1
        self.Length = 0
        for i in self.List1 :
            self.Length += 1


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


# ----------------------------------------------------------------------------------------------------------------------


Example_Array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

obj = Array()

obj.Initialize_Array(Example_Array)

print(obj.Reverse(Example_Array))
# prints [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


# Thank you for Watching ;)
# Developed By Hadi_Molaei