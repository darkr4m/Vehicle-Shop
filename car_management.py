class CarManager:
    """
    Attributes:
        CLASS: 
            all_cars - List/dictionary that stores all car instances created
            total_cars - integer that keeps track of the total number of cars

        INSTANCE:
            _id - integer - uninque
                should never be repeated and only rise with each car instance
            _make - string
            _model - string
            _year - integer
            _mileage - integer
            _services - list that stores services done to the car

        GETTERS AND SETTERS
            Validate inputs
            Title case make and model
            unique id

        Terminal application:
            Add a car
            View all cars
            view total number of cars
            see one cars details
            service a car
            update mileage
            quit

        Methods:
            __str__ -
                Make:
                Model:
                Year:
                Mileage:
                Services:

        run the manager
            switch
            choice - input
    """
    all_cars = {}
    total_cars = 0

    def __init__(self, id, make, model, year):
        self._id = id
        self._make = make
        self._model = model
        self._year = year
        self._mileage = 0
        self._services = []

        # Sets the key to the id of this car, and assigns the value to the entire object - adds it to the all_cars dict.
        CarManager.all_cars[self._id] = self
        # increments the total number of cars by one
        CarManager.total_cars += 1

    # GETTERS AND SETTERS

    @property
    def id(self):
        return self._id
    
    @property
    def make(self):
        return self._make
    @make.setter
    def make(self, make):
        self._make = make

    @property
    def model(self):
        return self._model
    @model.setter
    def model(self, model):
        self._model = model

    @property
    def year(self):
        return self._year
    @year.setter
    def year(self, year):
        self._year = year
    
    @property
    def mileage(self):
        return self._mileage
    @mileage.setter
    def mileage(self, mileage):
        self._mileage = mileage

    @property
    def services(self):
        return self._services
    @services.setter
    def services(self, service):
        self._services.append(service)


    def __str__(self):
        return(f"""ID: {self.id}
Make: {self.make}
Model: {self.model}
Year: {self.year}
Mileage: {self.mileage}
Services: {self.services}""")

# Terminal program
def run_manager():
    choice = input("""----------WELCOME----------
[1] Add a car
[2] View all cars
[3] View total number of cars
[4] See a car's details
[5] Service a car
[6] Update mileage
[7] Quit\n""")
    match choice:
        case "1":
            id = 1
            make = input("Enter the car's make: ")
            model = input("Enter the car's model: ")
            year = input("Enter the car's manufacturing year: ")
            CarManager(id,make,model,year)
            print(f"Car(id: {id}) added successfully.")
            print(CarManager.all_cars[id])
            return run_manager()
        case "2":
            print("All Cars:")
            for car in CarManager.all_cars.values():
                print(f"{car.year} {car.make} {car.model}")
            return run_manager()
        case "3":
            print(f"Total number of cars: {CarManager.total_cars}")
            return run_manager()
        case "4":
            id = input("What is the car's ID?   ")
            print(CarManager.all_cars.get(id))
            return run_manager()
        case "5":
            id = input("What is the car's ID?   ")
            car = CarManager.all_cars.get(id)
            service = input("Enter service description:   ")
            car.services = service
            return run_manager()
        case "6":
            id = input("What is the car's ID?   ")
            car = CarManager.all_cars.get(id)
            mileage = input("Enter new mileage:   ")
            car.mileage = mileage
            return run_manager()
        case "7":
            print("Goodbye!")
        case _:
            print("Invalid input.")
            return run_manager()


"""
TODO:
Validation
Car not found
increment id
helper functions
car class?
confirmations
submenus
"""
# manager = CarManager(1,"Kia","Soul",2015)
# print(manager)

run_manager()