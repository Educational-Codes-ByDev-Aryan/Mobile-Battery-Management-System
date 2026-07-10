# Mobile Battery Management System using Python OOP

class Mobile:
    company = "Samsung"  # Class Variable

    def __init__(self, Model_name, Battery_percentage):
        self.Model_name = Model_name
        self.Battery_percentage = Battery_percentage
        self.charge_amount = 0

    # Instance Method
    def show_mobile(self):
        print(
            f"The company of the mobile is {Mobile.company} and the model name is {self.Model_name} and the battery remaining is {self.Battery_percentage}%"
        )
        print(f"Charging Time : {Mobile.charging_time(self.charge_amount)} minutes")

    # Instance Method
    def charge_battery(self, amount):
        self.charge_amount = amount
        self.Battery_percentage += amount

        if self.Battery_percentage > 100:
            self.Battery_percentage = 100

    # Class Method
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    # Static Method
    @staticmethod
    def charging_time(battery_needed):
        groups = battery_needed / 10
        charge_time = groups * 5
        return charge_time

    # New Method for Flask
    def get_details(self):
        return {
            "company": Mobile.company,
            "model": self.Model_name,
            "battery": self.Battery_percentage,
            "charge_amount": self.charge_amount,
            "charging_time": Mobile.charging_time(self.charge_amount)
        }