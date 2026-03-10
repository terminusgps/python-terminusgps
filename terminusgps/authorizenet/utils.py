import typing

T_contract = typing.TypeVar("T_contract")


def build_contract(
    contract_cls: type[T_contract], fields: dict[str, typing.Any]
) -> T_contract:
    contract = contract_cls()
    for key, value in fields.items():
        if value:
            setattr(contract, key, value)
    return contract
