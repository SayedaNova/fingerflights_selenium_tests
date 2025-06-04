from tests.WholeCrudOperation.crud_operation import crud
from tests.Demo_Data.user_data import SUPERADMIN_EMAIL, SUPERADMIN_PASSWORD, ADMIN_EMAIL, ADMIN_PASSWORD
from tests.AdminProfileUpdate.adminprofileupdate import admin_profile_update

if __name__ == "__main__":
    # Step 1: SuperAdmin creates everything
    driver = crud(SUPERADMIN_EMAIL, SUPERADMIN_PASSWORD)

    #Step 2: Admin Profile update
    admin_profile_update(ADMIN_EMAIL, ADMIN_PASSWORD, driver=driver)




