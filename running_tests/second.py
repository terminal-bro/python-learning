def sign(value):
    if value < 0:
        return -1
    else:
        return 1
    
def test_sign_positive():
    assert sign(-3) == -1

def test_sign_negative():
    assert sign(19) == 1

def test_sign_zero():
    assert sign(0) == 0

def test_sign_error():
    assert sgn(8) == 1


def run_tests(all_tests):
    results = {
        "pass" : 0,
        "error" : 0,
        "fail" : 0
    }
    for test in TESTS:
        try:
            test()
            results["pass"] += 1
        except AssertionError:
            results["fail"] += 1
        except Exception:
            results["error"] += 1

        print(results)

TESTS = [
    test_sign_error,
    test_sign_negative,
    test_sign_positive,
    test_sign_zero
]

run_tests(TESTS)