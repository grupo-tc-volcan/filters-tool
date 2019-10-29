# Project modules
from app.approximators.butterworth import ButterworthApprox
from app.approximators.chebyshev_i import ChebyshevIApprox
from app.approximators.legendre import LegendreApprox

from app.approximators.approximator import ApproximationErrorCode

# Third-Party modules
from matplotlib import pyplot
from scipy import signal
import pytest

# Python native modules
import numpy as np


# --------------------------- #
#  DECLARING USEFUL ELEMENTS  #
# --------------------------- #

@pytest.fixture
def approximator():
    # Change the returning approximation to test it!
    return LegendreApprox()


def run_by_template(
        approximator,
        filter_type,
        fpl=0, fpr=0,
        apl=0, apr=0,
        fal=0, far=0,
        aal=0, aar=0,
        gain=0
):
    approximator.type = filter_type
    approximator.gain = gain

    approximator.fpl = fpl
    approximator.fpr = fpr
    approximator.fal = fal
    approximator.far = far

    approximator.Apl = apl
    approximator.Apr = apr

    approximator.Aal = aal
    approximator.Aar = aar

    results = []
    if approximator.compute() is ApproximationErrorCode.OK:
        results.append(("Denormalised |H(f)| [dB]", approximator.h_denorm))
        results.append(("Normalised |H(f)| [dB]", approximator.h_norm))
    else:
        input("[ERROR] => {}".format(approximator.error_code))
    plot_results(results)


def plot_results(results):
    pyplot.figure()
    for name, h in results:
        w, m, p = signal.bode(h, n=100000)
        pyplot.semilogx(w / (2 * np.pi), m, label="{}".format(name))
    pyplot.legend()
    pyplot.show()


# ------------ #
# TEST MODULES #
# ------------ #

def test_by_fixed_order(approximator):
    approximator.type = "low-pass"
    approximator.gain = 0
    approximator.fpl = 1000
    approximator.Apl = 3.5

    results = []
    for order in range(1, 10):
        approximator.ord = order

        if approximator.compute() is ApproximationErrorCode.OK:
            results.append(("Approximation n={}".format(order), approximator.h_denorm))
        else:
            print("[ERROR] => {}".format(approximator.error_code))

    plot_results(results)


def test_by_max_q(approximator):
    approximator.type = "low-pass"
    approximator.gain = 0
    approximator.fpl = 1000
    approximator.Apl = 2

    results = []
    for max_q in np.linspace(0.1, 0.6, 20):
        approximator.q = max_q

        print("Using MaxQ={} and Order={}".format(max_q, approximator.ord))
        if approximator.compute() is ApproximationErrorCode.OK:
            for pole in approximator.get_zpk().poles:
                print("fo: {} Q: {}".format(
                    approximator.calculate_frequency(pole),
                    approximator.calculate_selectivity(pole)
                ))
            print("\n")
            results.append(("Approximation MaxQ={}".format(max_q), approximator.h_denorm))
        else:
            print("[ERROR] => {}".format(approximator.error_code))

    plot_results(results)


def test_by_template_denorm(approximator):
    approximator.type = "low-pass"
    approximator.gain = 0

    approximator.fpl = 1000
    approximator.Apl = 2
    approximator.fal = 10000
    approximator.Aal = 20

    results = []
    for denorm in range(0, 101, 10):
        approximator.denorm = denorm if denorm != 0 else 1

        if approximator.compute() is ApproximationErrorCode.OK:
            results.append(("Approximation Denorm={}".format(denorm), approximator.h_denorm))
        else:
            print("[ERROR] => {}".format(approximator.error_code))

    plot_results(results)


def test_band_pass(approximator):
    run_by_template(
        approximator,
        "band-pass",
        fpl=4000,
        fpr=6000,
        apl=2,
        apr=2,
        fal=1000,
        far=10000,
        aal=10,
        aar=10,
        gain=0
    )


def test_band_stop(approximator):
    run_by_template(
        approximator,
        "band-stop",
        fal=2500,
        far=4000,
        apl=2,
        apr=2,
        fpl=100,
        fpr=100000,
        aal=5,
        aar=5
    )


def test_high_pass(approximator):
    run_by_template(
        approximator,
        "high-pass",
        fpl=3000,
        apl=2,
        fal=1000,
        aal=10
    )


def test_low_pass(approximator):
    run_by_template(
        approximator,
        "low-pass",
        fpl=1000,
        apl=2,
        fal=3000,
        aal=10
    )
