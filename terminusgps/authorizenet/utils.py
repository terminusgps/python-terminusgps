import typing

T_contract = typing.TypeVar("T_contract")


class AuthorizenetContractBuilder(typing.Generic[T_contract]):
    def __init__(self, contract_cls: type[T_contract]) -> None:
        self.contract_cls = contract_cls

    def build(self, fields: dict[str, typing.Any]) -> T_contract:
        contract = self.contract_cls()
        for field, value in fields.items():
            setattr(contract, field, value)
        return contract
