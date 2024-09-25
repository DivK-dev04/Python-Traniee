class car:
    def __init__(self, make, model, last_service_mileage):
        self.make = make 
        self.model = model
        self.last_service_mileage = last_service_mileage

    def service(self, current_mileage):
        if current_mileage - self.last_service_mileage > 10000:
            print("Car need Service.")
        else:
            print("NO service")

    def update_mileage(self, new_mileage):
        self.last_service_mileage = new_mileage

    def display(self):
        print(f"Make : {self.make} , Model : {self.model} , Last Mileage : {self.last_service_mileage}")

cars = car("Ford" , "Mustang" , 20000)
cars.service(222500)
cars.update_mileage(222500)
cars.display()    