from tests.WholeCrudOperation.crud_operation import create
from tests.Module_Data.user_data import SUPERADMIN_EMAIL, SUPERADMIN_PASSWORD, ADMIN_EMAIL, ADMIN_PASSWORD
from tests.AdminProfileUpdate.adminprofileupdate import admin_profile_update

if __name__ == "__main__":
    # Step 1: SuperAdmin creates everything
    driver = create(SUPERADMIN_EMAIL, SUPERADMIN_PASSWORD)

    # # Step 2: Logout SuperAdmin
    # logout_user(driver, SUPERADMIN_EMAIL)

    #Step 3: Admin Profile update
    # admin_profile_update(ADMIN_EMAIL, ADMIN_PASSWORD, driver=driver)

    # # Step 2: Logout Admin
    # logout_user(driver, ADMIN_EMAIL)




