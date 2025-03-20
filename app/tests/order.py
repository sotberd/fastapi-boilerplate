"""PyTest Order"""

v1_test_order_map = ["health"]


def get_pyorder(task: str) -> int:
    """Return test index number"""
    return v1_test_order_map.index(task)
