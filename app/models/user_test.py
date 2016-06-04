from user import User


def test_user_should_have_correct_repr():
    user = User(id=1)
    assert "User" in repr(user)
    assert "1" in repr(user)
