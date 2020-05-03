from pet import *  
from petpriority import *


dog1 = Dog("Romeo", "labrador", 2)
dog2 = Dog("Juliet", "labrador", 5)
dog3 =  Dog("Ashley", "Golden retreiver", 7)

cat1 =  Cat("Daisy", "Bobtail", 3)
cat2 =  Cat("Bily", "American Shorhair", 4)
cat3 =  Cat("Tom", "Abyssinian", 1)
cat4 =  Cat("Aron", "Bengal", 6)

array = [cat4, dog1, cat2, dog2, cat1, cat3, dog3]
size = len(array)
PQ = Sorting(array, size)
CatsNDogs = PQ.sort_temp()
print([items.name for items in CatsNDogs])
print([items.type for items in CatsNDogs])
print([items.age for items in CatsNDogs])





