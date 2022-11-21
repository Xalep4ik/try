# function Time to test: a = time to create, b = sum of created tests,
# c = sum of time to run tests, d = sum pf complete tests
def time_to_test(a, b, c, d):
    avg_time_to_create = a / b
    avg_time_to_run = c / d
    return print("Average time to create tests :", avg_time_to_create,
                 "Average time to run tests :", avg_time_to_run)


# function Escaped bugs, x = found bugs on prod, y = bugs found before release (20% to much)
def escaped_bugs(x, y):
    esc = (x / y) * 100
    if esc > 20:
        print(esc, "% Is too much")
    else:
        print(esc, "% Escaped bugs found")


# function Test coverage, a = amount of run test, b = amount of planed tests, c = req covered, d = amount of req
def test_coverage(a, b, c, d):
    test_execution = (a / b) * 100
    requirements_coverage = (c / d) * 100
    return print("Execution state: ", test_execution, "%",
                 "Req coverage:", requirements_coverage, "%")


# function Test effort : a = sum of tests run, b = time consume, c = sum of found bugs, d = time spends fo tests
def test_effort(a, b, c, d):
    test_per_hour = a / b
    speed_find_bug = c / d
    average_bug_per_test = c / a
    return print("Test per hour :", test_per_hour,
                 "Speed find bug :", speed_find_bug,
                 "Average bug per test :", average_bug_per_test)


# function Coast per bug fix : a = time to fix, b = fixed bugs, c = rate of developer
def cost_per_bug_fix(a, b, c):
    time_to_fix = a / b
    return print("Cost per bug fix ", time_to_fix * c, "$")


# function Test case effectiveness : a = total of found bugs, b = total of test runs
def test_case_eff(a, b):
    eff_test_case = a / b * 100
    return print("Effectiveness of test cases : ", eff_test_case, "%")


# function Test execution status: a = total of successful tests, b = total of tests, c = total of failed tests
def test_exe_status(a, b, c):
    percent_of_success = a / b * 100
    percent_of_failed = c / b * 100
    return print("Percent of successful run :", percent_of_success, "%, ",
                 "Percent of failed run :", percent_of_failed, "%")
