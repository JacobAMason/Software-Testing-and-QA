class BodyMassIndex:
    def __init__(self, feet, inches, weight):
        self.mass_index = 0
        self.feet = feet
        self.inches = inches
        self.weight = weight
        self.height_inches = 0
        self.metric_height = 0
        self.metric_weight = 0
        self.bmi_category = ""

    # convert from lbs to metric
    def convert_weight(self, weight):
        self.metric_weight = weight * 0.45
        return self.metric_weight

    # convert ft and in to full inches
    def convert_height_inches(self, feet, inches):
        self.height_inches = (feet * 12) + inches
        return self.height_inches

    # convert from inches to metric
    def convert_height_metric(self, height_inches):
        self.metric_height = height_inches * 0.025
        return self.metric_height

    # calculate total BMI
    def calculate_bmi(self, height_inches, weight):
        metric_height = self.convert_height_metric(height_inches)
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
