def year_can_retire(age, salary, saving, goal):
    """
    Input user's current age, annual salary, percentage saved (savings matched
    by employer - so double amount saved). Input desired retirement savings
    goal. Output what age savings goal will be met. You can assume death at
    100 years(therefore, indicate if the savings goal is not met).
    :param age: current age of individual
    :param salary:
    :param saving:
    :param goal:
    :return:
    """

    if isinstance(age, (int, float)) is False:
        raise ValueError("Age must be a number!")

    if isinstance(salary, (int, float)) is False:
        raise ValueError("Salary must be a number!")

    if isinstance(saving, (int, float)) is False:
        raise ValueError("Saving must be a number!")

    if isinstance(goal, (int, float)) is False:
        raise ValueError("Goal must be a number!")

    if age < 0:
        raise ValueError("Can not have a negative age")

    if salary <= 0:
        raise ValueError("Can not have a positive salary")

    if saving > 1 or saving < 0:
        raise ValueError("Saving must be bound between 0 and 1")

    if goal < 0:
        raise ValueError("Can not have a negative goal")

    return min(age + (goal / (salary*saving*2)), 100)
