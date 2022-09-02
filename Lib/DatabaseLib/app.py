from dotenv import dotenv_values
from timeit import default_timer as timer
from fake_data import gen_dummy_data
from Lib.BaseLib.LogMessage import LogMessage, LOG_INFO, LOG_ERROR, LOG_WARN


def run_with_parameters(controllers, n_tests: int):
    """

    :param controllers:
    :param n_tests:
    :return:
    """
    time_result = list()
    LogMessage(level=LOG_WARN, module="run_with_parameters", msg=f"start generating dummy data")
    (cr_data, updata) = gen_dummy_data(n_tests)
    #
