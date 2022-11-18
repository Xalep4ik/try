# function calculate average spends

# function Escaped bugs, x = found bugs on prod, y = bugs found before release (20% to much)
def escaped_bugs(x, y):
    esc= (x/y)*100
    if (esc > 20):
        print(esc , "% Is too much")
    else:
        print(esc , "% Escaped bugs found")

# function Test coverage, a = amount of run test, b = amount of planed tests, c = req covered, d = amount of req
def test_coverage (a, b, c, d):
    test_execution = (a / b) * 100
    requirements_coverage = (c / d) * 100
    return print("Execution state: ", test_execution, "%",
                 "Req coverage:",  requirements_coverage, "%")


# function Test effort : z = sum of tests, v = time consume, u = sum of found bugs, i = time spends fo tests
def test_effort (z,v,u,i,):
    test_per_hour = z / v
    speed_find_bug = u / i
    average_bug_per_test = u / z
    return print("Test per hour :", test_per_hour,
                 "Speed find bug :", speed_find_bug,
                 "Average bug per test :", average_bug_per_test)

test_effort(10,3,60,34,)
