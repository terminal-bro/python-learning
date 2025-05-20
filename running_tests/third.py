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

results = {
    "pass" : 0,
    "error" : 0,
    "fail" : 0
}

def find_tests(prefix):
    for (name, test) in globals().items():
        if not name.startswith(prefix):
            continue
        try:
            test()
            results["pass"] += 1
        except AssertionError:
            results["fail"] += 1
        except Exception:
            results["error"] += 1


find_tests("test_")
print(results)