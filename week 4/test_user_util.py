from user_util import UserUtil


def test_generate_user_id_9_digits():
    uid = UserUtil.generate_user_id()
    assert isinstance(uid, int)
    assert len(str(uid)) == 9


def test_generate_password_is_strong():
    pwd = UserUtil.generate_password()
    assert UserUtil.is_strong_password(pwd) is True


def test_generate_email_and_validate():
    email = UserUtil.generate_email("John", "Doe", "gmail.com")
    assert email == "john.doe@gmail.com"
    assert UserUtil.validate_email(email) is True
