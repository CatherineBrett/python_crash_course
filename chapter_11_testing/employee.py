class Employee:
    """A class to represent an employee."""

    def __init__(self, first_name, last_name, salary):
        """Construct the employee object's attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, salary_increase=""):
        """Increase employee's salary by either given amount or $5,000 by
        default."""
        if salary_increase:
            self.salary += salary_increase
        else:
            self.salary += 5000
        return self.salary
