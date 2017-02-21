class BodyMassIndex:
    def __init__(self, height, weight):
        self.mass_index = 0
        self.height = height
        self.weight = weight
        self.metric_height = 0
        self.metric_weight = 0
        self.bmi_category = ""

    # convert from lbs to metric
    def convert_weight(self, weight):
        self.metric_weight = weight * 0.45
        return self.metric_weight

    # convert from inches to metric
    def convert_height(self, height):
        self.metric_height = height * 0.025
        return self.metric_height

    # calculate total BMI
    def calculate_bmi(self, height, weight):
        metric_height = self.convert_height(height)
        metric_weight = self.convert_weight(weight)
        height_squared = metric_height * metric_height
        self.mass_index = metric_weight / height_squared
        return self.mass_index

    # determine if under, over, or normal weight
    def determine_bmi_category(self, mass_index):
        if mass_index <= 18.5:
            self.bmi_category = "Underweight"
        elif mass_index >= 25:
            self.bmi_category = "Overweight"
        else:
            self.bmi_category = "Normal"

        return self.bmi_category

if __name__ == '__main__':
    BMI = BodyMassIndex()
class BodyMassIndex:
    def __init__(self, height, weight):
        self.mass_index = 0
        self.height = height
        self.weight = weight
        self.metric_height = 0
        self.metric_weight = 0
        self.bmi_category = ""

    # convert from lbs to metric
    def convert_weight(self, weight):
        self.metric_weight = weight * 0.45
        return self.metric_weight

    # convert from inches to metric
    def convert_height(self, height):
        self.metric_height = height * 0.025
        return self.metric_height

    # calculate total BMI
    def calculate_bmi(self, height, weight):
        metric_height = self.convert_height(height)
        metric_weight = self.convert_weight(weight)
        height_squared = metric_height * metric_height
        self.mass_index = metric_weight / height_squared
        return self.mass_index

    # determine if under, over, or normal weight
    def determine_bmi_category(self, mass_index):
        if mass_index <= 18.5:
            self.bmi_category = "Underweight"
        elif mass_index >= 25:
            self.bmi_category = "Overweight"
        else:
            self.bmi_category = "Normal"

        return self.bmi_category

if __name__ == '__main__':
    BMI = BodyMassIndex()