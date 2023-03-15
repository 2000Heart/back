from typing import Generic, TypeVar, Optional

from pydantic.generics import GenericModel

data = TypeVar("data")


class Block(GenericModel, Generic[data]):
    d: Optional[data]
    t: Optional[data]
