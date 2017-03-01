class BodyMassIndexCalculator:

    # https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmicalc.htm

    @staticmethod
    def convert_lbs_to_kgs(lbs):
        return lbs * 0.45

    @staticmethod
    def convert_height_to_inches(feet, inches):
        return (feet * 12) + inches

    @staticmethod
    def convert_inches_to_meters(height_inches):
        return height_inches * 0.025

    @staticmethod
    def calculate_bmi(height_inches, lbs):
        metric_height = BodyMassIndexCalculator.convert_inches_to_meters(
            height_inches)
        metric_weight = BodyMassIndexCalculator.convert_lbs_to_kgs(lbs)
        height_squared = metric_height * metric_height
        return metric_weight / height_squared

    @staticmethod
    def determine_bmi_category(mass_index):
        if mass_index < 18.5:
            return "Underweight"
        elif mass_index >= 25:
            return "Overweight"
        else:
            return "Normal"


if __name__ == '__main__':
    BMI = BodyMassIndexCalculator()
