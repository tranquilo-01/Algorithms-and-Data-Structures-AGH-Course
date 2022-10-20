# zad2test_spec.py

ALLOWED_TIME = 2


# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TEST_SPEC = [
# n, maxint, hint
  (5, 10, 3),
  (50, 100, 40),
  (100, 1000, 88),
  (10000, 10000, 9767),
  (20000, 10000, 19901),
  (50000, 10000, 49858),
  (10**5, 50000, 99290),
  (10**5, 10**5, 99523),
  (2*10**5, 10**5, 198985),
  (2*10**5, 10**8, 198408)
]

