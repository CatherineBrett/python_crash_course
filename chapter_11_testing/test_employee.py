from employee import Employee


def test_give_default_raise():
    """Test that the default raise of $5,000 is successfully applied."""
    employee_one = Employee("joe", "bloggs", 100_000)
    employee_one.give_raise()
    assert employee_one.salary == 105_000


def test_give_custom_raise():
    """Test that a custom raise amount is successfully applied."""
    employee_two = Employee("annette", "curtain", 100_000)
    employee_two.give_raise(7_000)
    assert employee_two.salary == 107_000
