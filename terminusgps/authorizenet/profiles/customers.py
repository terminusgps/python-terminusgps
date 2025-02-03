from authorizenet.apicontrollers import (
    createCustomerProfileController,
    deleteCustomerProfileController,
    getCustomerProfileController,
    updateCustomerProfileController,
)
from authorizenet.apicontractsv1 import (
    customerProfileType,
    createCustomerProfileRequest,
    deleteCustomerProfileRequest,
    getCustomerProfileRequest,
    updateCustomerProfileRequest,
)

from terminusgps.authorizenet.profiles.base import AuthorizenetProfileBase


class CustomerProfile(AuthorizenetProfileBase):
    def create(self, **kwargs) -> int:
        if not kwargs.get("email"):
            raise ValueError("'email' is required for creation.")

        request = createCustomerProfileRequest(
            merchantAuthentication=self.merchantAuthentication,
            profile=customerProfileType(
                merchantCustomerId=self.merchantCustomerId,
                email=kwargs["email"],
                description=kwargs.get("desc", ""),
            ),
        )
        controller = createCustomerProfileController(request)
        response = self.execute_controller(controller)
        return int(response.customerProfileId)

    def update(self, merchant_id: str, email: str, desc: str = "") -> None:
        request = updateCustomerProfileRequest(
            merchantAuthentication=self.merchantAuthentication,
            profile=CustomerProfile(
                self.id, merchantCustomerId=merchant_id, email=email, description=desc
            ),
        )
        controller = updateCustomerProfileController(request)
        self.execute_controller(controller)

    def delete(self) -> None:
        request = deleteCustomerProfileRequest(
            merchantAuthentication=self.merchantAuthentication,
            customerProfileId=str(self.id),
        )
        controller = deleteCustomerProfileController(request)
        self.execute_controller(controller)

    @property
    def payment_profiles(self) -> list[dict]:
        request = getCustomerProfileRequest(
            merchantAuthentication=self.merchantAuthentication,
            customerProfileId=self.id,
            includeIssuerInfo="true",
        )
        controller = getCustomerProfileController(request)
        response = self.execute_controller(controller)
        return response


def main() -> None:
    profile = CustomerProfile(merchant_id=55, id=522226003)
    profile.delete()
    return


if __name__ == "__main__":
    main()
