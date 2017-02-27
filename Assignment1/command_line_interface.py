from Assignment1.email_verifier import EmailVerifier
from Assignment1.distance_formula import DistanceFormulaCalculator
from Assignment1.retirement import year_can_retire
from Assignment1.body_mass_index_calculator import BodyMassIndexCalculator


class CommandLineInterface:

    @staticmethod
    def get_commands():
        return "commands: " \
               "\n\temailval <email>" \
               "\n\tbmi <feet> <inches> <weight>" \
               "\n\tdist <x1> <y1> <x2> <y2>" \
               "\n\tretire <age> <salary> <percent saving> <goal>" \
               "\n\texit"

    @staticmethod
    def run_command(command):
        """
        Runs a given command and returns output as a string
        :param command:
        :return:
        """

        if isinstance(command, str) is False:
            return "Command must be type string!"

        if command == "":
            return "Need command.."

        args = command.split()
        valid_arguments = ['dist', 'bmi', 'emailval', 'retire', 'exit']

        if args[0] not in valid_arguments:
            return "Bad argument: " + args[0]

        # Email
        if args[0] == 'emailval':

            if len(args) != 2:
                return "emailval takes only 1 arguments"

            if EmailVerifier.is_valid_email(args[1]):
                return 'Valid email'
            else:
                return 'Invalid email'

        # Distance
        if args[0] == 'dist':

            if len(args) != 5:
                return "dist takes 4 arguments"

            for arg in args[1:]:
                try:
                    float(arg)
                except:
                    return "Invalid argument: " + arg

            x1 = float(args[1])
            y1 = float(args[2])
            x2 = float(args[3])
            y2 = float(args[4])

            dist = DistanceFormulaCalculator.compute_distance(x1,
                                                              y1,
                                                              x2,
                                                              y2)

            return "Distance from ({0}, {1}) to ({2}, {3}) = {4}"\
                .format(x1, y1, x2, y2, dist)

        # Retirement
        if args[0] == 'retire':

            if len(args) != 5:
                return "dist takes 4 arguments"

            for arg in args[1:]:
                try:
                    float(arg)
                except:
                    return "Invalid argument: " + arg

            age = float(args[1])
            salary = float(args[2])
            saving = float(args[3])
            goal = float(args[4])

            try:
                retire_at = year_can_retire(age, salary, saving, goal)
                return "You can retire at: {0}".format(retire_at)
            except ValueError as err:
                return "Error running command:\n\t{0}".format(err)

        if args[0] == 'bmi':

            if len(args) != 4:
                return "bmi takes 3 arguments"

            for arg in args[1:]:
                try:
                    float(arg)
                except:
                    return "Invalid argument: " + arg

            feet = float(args[1])
            inches = float(args[2])
            weight = float(args[3])

            bmi = BodyMassIndexCalculator.calculate_bmi((feet*12)+inches,
                                                        weight)
            category = BodyMassIndexCalculator.determine_bmi_category(bmi)

            return "You have a BMI of {0:.2f} making you {1}"\
                .format(bmi, category)


if __name__ == '__main__':
    while True:
        print(CommandLineInterface.get_commands()+"\n")
        command = input("> ")

        if command == 'exit':
            exit()

        print(CommandLineInterface.run_command(command)+"\n")
