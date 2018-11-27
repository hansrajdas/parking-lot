class Vehicle:
    def __init__(self, registration_num, color):
        self.registration_num = registration_num
        self.color = color

    def update_registration_number(self, registration_num):
        self.registration_num = registration_num

    def update_color(self, color):
        self.color = color

    def get_registration_number(self):
        return self.registration_num

    def get_color(self):
        return self.color
