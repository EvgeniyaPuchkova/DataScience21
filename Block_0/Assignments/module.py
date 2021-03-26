class ListKeeper:                               #class, which stores named lists
    def __init__(self):                         #initialization with the list named example
        self.items = {}
        self.items["example"] = [1,2,3,4,5]

    def show(self):                             #returns all list names
        return self.items.keys()

    def add(self, name, list_data):             #adds a new list
        self.items[name] = list_data
        print ("New list added!")

    def delete(self, name):                     #deletes list
        if name in self.items:
            del self.items[name]
            print ("List deleted!")
        return "List could not be deleted, please double check"

    def sort(self, name):                       #returns the sorted list name
        if name in self.items:
            self.items[name].sort()
            return self.items[name]
        return "Error, the list does not exist"

    def append(self, name, list_data):          #appends list to name
        self.items[name].append(list_data)
        print ("Done!")

    def test(self, name):                       #returns the data of the list name as a test
        if name in self.items:
            return self.items[name]
        return "Error, the list does not exist"