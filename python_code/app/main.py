from python_code.app.runner_backend import BackendApproach
from python_code.app.runner_data import DataApproach


def main():
    """
    Execute both Backend and Data approaches sequentially.
    """
    print(f"Executing Backend Approach")
    BackendApproach()()
    print(f"Executing Data Approach")
    DataApproach()()


main()
