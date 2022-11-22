from datetime import date

from pydantic import ValidationError

from hexgem.model import User


def test_model_with_correct_data():
    data = dict(id=1234, email="xxx@gmail.com", username="frank", github_page="www.xxx.com")
    user = User(**data)


def test_model_with_full_data():
    data = dict(id=1234,
                email="xxx@gmail.com",
                username="frank",
                github_page="www.xxx.com",
                organization=['google', 'facebook'],
                is_contributor=False,
                starred_timestamp=date(2022, 10, 1))
    user = User(**data)


def test_model_with_coerced_datatype():
    data = dict(
        id=1234,
        email="xxx@gmail.com",
        username=1234,
        github_page="www.xxx.com",
    )
    user = User(**data)
    assert isinstance(user.username, str)


def test_model_with_missing_data():
    data = dict(
        id=1234,
        email="xxx@gmail.com",
        username="frank",
    )

    error_flag = False
    try:
        user = User(**data)
    except ValidationError as e:
        error_flag = True
    assert error_flag
