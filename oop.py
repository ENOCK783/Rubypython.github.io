class Fruits:
    #constructor
    def __init__(self, price,shape,name):
        self.price = price
        self.shape = shape
        self.name = name
    def display(self):
        print(f"my favorite fruit is {self.name} and its {self.shape} in shape and cost is {self.price}  shillings")

   # create instance of a class(object)

myobj=Fruits(10,"oval","apple")
myobj.display()