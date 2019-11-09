#Class Animal wich is also a node of the list
class Animal:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = newdata
        
    def set_next(self, new_next):
        self.next = new_next

    def get_animalID(self):
        return self.animalID

class LinkedList():
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()

        return count

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_animalID() > item.get_animalID():
                stop = True
            else:
                previous = current
                current = current.get_next()
        
        temp = item
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

            if previous == None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())

    def getLastItem(self):
        return self.head



class PetAnimal(Animal): 
    #constructor of class pet
    def __init__(self, animalID = "", typeOfAnimal = "", vaccinated = "", dateOfArrival = "", dateOfDeparture = "", destination = "", destinationAddress = "", breed = "", neutered = "", microchipNumber = ""):
        self.animalID = animalID
        self.typeOfAnimal = typeOfAnimal
        self.vaccinated = vaccinated
        self.dateOfArrival = dateOfArrival
        self.dateOfDeparture = dateOfDeparture
        self.destination = destination
        self.destinationAddress = destinationAddress
        self.breed = breed
        self.neutered = neutered
        self.microchipNumber = microchipNumber

class WildAnimal(Animal):
    #constructor of class pet
    def __init__(self, animalID = "", typeOfAnimal = "", reasonOfAdmission = "", vaccinated = "", dateOfArrival = "", dateOfDeparture = "", destination = "", destinationAddress = ""):
        self.animalID = animalID
        self.typeOfAnimal = typeOfAnimal
        self.reasonOfAdmission = reasonOfAdmission
        self.vaccinated = vaccinated
        self.dateOfArrival = dateOfArrival
        self.dateOfDeparture = dateOfDeparture
        self.destination = destination
        self.destinationAddress = destinationAddress
