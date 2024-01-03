import solver


def is_solved():
    assert solver.solver()


def test_solver():
    assert solver.solver(1, 5) == 19
