from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AllMessage(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: bytes
    def __init__(self, message: _Optional[bytes] = ...) -> None: ...

class EmptyMessage(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class FoodMessage(_message.Message):
    __slots__ = ["message"]
    class MessageEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: _containers.ScalarMap[str, float]
    def __init__(self, message: _Optional[_Mapping[str, float]] = ...) -> None: ...

class IntMessage(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: int
    def __init__(self, message: _Optional[int] = ...) -> None: ...

class MulType(_message.Message):
    __slots__ = ["food", "i", "str", "tup"]
    FOOD_FIELD_NUMBER: _ClassVar[int]
    I_FIELD_NUMBER: _ClassVar[int]
    STR_FIELD_NUMBER: _ClassVar[int]
    TUP_FIELD_NUMBER: _ClassVar[int]
    food: FoodMessage
    i: int
    str: str
    tup: TupleMessage
    def __init__(self, str: _Optional[str] = ..., tup: _Optional[_Union[TupleMessage, _Mapping]] = ..., food: _Optional[_Union[FoodMessage, _Mapping]] = ..., i: _Optional[int] = ...) -> None: ...

class StringMessage(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class TupleMessage(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, message: _Optional[_Iterable[str]] = ...) -> None: ...
