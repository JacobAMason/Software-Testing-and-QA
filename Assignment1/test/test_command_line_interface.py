import pytest
from Assignment1.command_line_interface import CommandLineInterface


class TestValidateCommands:
    def test_throws_error_with_non_string_command(self):
        assert CommandLineInterface.run_command(None) == \
               "Command must be type string!"

    def test_returns_bad_arguement_when_bad_arguement(self):
        assert CommandLineInterface.run_command("bad arguement") == \
               "Bad argument: bad"

    def test_returns_need_command_when_empty_string(self):
        assert CommandLineInterface.run_command("") == \
               "Need command.."

    def test_should_return_list_of_commands(self):
        assert CommandLineInterface.get_commands() == \
               "commands: " \
               "\n\temailval <email>" \
               "\n\tbmi <feet> <inches> <weight>" \
               "\n\tdist <x1> <y1> <x2> <y2>" \
               "\n\tretire <age> <salary> <percent saving> <goal>" \
               "\n\texit"

    def test_should_exit_program(self):
        with pytest.raises(SystemExit):
            CommandLineInterface.run_command("exit")


class TestValidateEmailCommand:
    def test_returns_bad_with_wrong_number_of_arguements(self):
        assert CommandLineInterface.run_command("emailval a b") == \
               "emailval takes only 1 arguments"

    def test_email_works(self):
        assert CommandLineInterface.run_command("emailval eli@me.com") == \
               "Valid email"

    def test_email_will_fail(self):
        assert CommandLineInterface.run_command("emailval elime.com") == \
               "Invalid email"


class TestValidateDistanceCommand:
    def test_return_bad_with_wrong_number_of_arguements(self):
        assert CommandLineInterface.run_command("dist a b") == \
               "dist takes 4 arguments"

    def test_dist_works(self):
        assert CommandLineInterface.run_command("dist 0 0 0 1") == \
               "Distance from (0.0, 0.0) to (0.0, 1.0) = 1.0"

    def test_dist_will_fail_to_calculate(self):
        assert CommandLineInterface.run_command("dist h 1 3 1") == \
               "Invalid argument: h"


class TestValidateRetirementCommand:
    def test_return_bad_with_wrong_number_of_arguements(self):
        assert CommandLineInterface.run_command("retire a b") == \
               "dist takes 4 arguments"

    def test_retire_works(self):
        assert CommandLineInterface.run_command(
            "retire 35 100000 0.1 500000") == "You can retire at: 60.0"

    def test_retire_recovers_from_invalid_aruements(self):
        assert CommandLineInterface.run_command("retire h 1 3 1") == \
               "Invalid argument: h"

    def test_retire_recovers_from_unbounded_aruements(self):
        assert CommandLineInterface.run_command("retire -35 100 0.1 500") == \
               "Error running command:\n\tCan not have a negative age"


class TestValidateBMICommand:
    def test_return_bad_with_wrong_number_of_arguements(self):
        assert CommandLineInterface.run_command("bmi a b") == \
               "bmi takes 3 arguments"

    def test_bmi_works(self):
        assert CommandLineInterface.run_command("bmi 5 11 150") == \
               "You have a BMI of 21.42 making you Normal"

    def test_bmi_recovers_from_invalid_aruements(self):
        assert CommandLineInterface.run_command("bmi a b c") == \
               "Invalid argument: a"
