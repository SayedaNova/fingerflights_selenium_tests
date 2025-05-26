from tests.CreateUserandB2B.createuserb2b import create
from tests.UserHelpers.create_utils import email, password
from tests.AuthHelpers.logout_utils import logout_user


if __name__ == "__main__":
    driver = create(email, password)
    logout_user(driver, email)



