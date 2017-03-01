def year_can_retire(age, salary, percent_saving, goal):
    """
    Input user's current age, annual salary, percentage saved (savings matched
    by employer - so double amount saved). Input desired retirement savings
    goal. Output what age savings goal will be met. You can assume death at
    100 years(therefore, indicate if the savings goal is not met).
    :param age: current age of individual
    :param salary:
    :param percent_saving:
    :param goal:
    :return:
    """

    if isinstance(age, (int, float)) is False:
        raise ValueError("Age must be a number!")

    if isinstance(salary, (int, float)) is False:
        raise ValueError("Salary must be a number!")

    if isinstance(percent_saving, (int, float)) is False:
        raise ValueError("Saving must be a number!")

    if isinstance(goal, (int, float)) is False:
        raise ValueError("Goal must be a number!")

    if age < 0:
        raise ValueError("Can not have a negative age")

    if salary < 0:
        raise ValueError("Salary must be greater than 0")

    if percent_saving > 1 or percent_saving < 0:
        raise ValueError("Saving must be bound between 0 and 1")

    if goal < 0:
        raise ValueError("Can not have a negative goal")

    if goal > 0 and (salary == 0 or percent_saving == 0):
        return 100

    return min(age + (goal / (salary * percent_saving * 2)), 100)
