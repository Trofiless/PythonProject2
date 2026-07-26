import pytest


@pytest.fixture
def operations():
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        {
            "id": 2,
            "state": "CANCELED",
            "date": "2018-06-30T02:08:58.425572",
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
        },
        {
            "id": 4,
            "state": "PENDING",
            "date": "2020-01-01T12:00:00.000000",
        },
    ]