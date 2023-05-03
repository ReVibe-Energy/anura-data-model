from generated.proto import TheTestMessage


def test_serialization_without_optional():
    message = TheTestMessage(a_normal_field=22)
    serialized = bytes(message)
    assert serialized == b'\x08\x16'
    deserialized = TheTestMessage().parse(serialized)
    assert deserialized.a_normal_field == 22
    assert deserialized.an_optional_field is None


def test_serialization_without_any_field():
    message = TheTestMessage()
    serialized = bytes(message)
    assert serialized == b''
    deserialized = TheTestMessage().parse(serialized)
    assert deserialized.a_normal_field == 0
    assert deserialized.an_optional_field is None


def test_serialization_with_only_optional_field():
    message = TheTestMessage(an_optional_field=22)
    serialized = bytes(message)
    assert serialized == b'\x10\x16'
    deserialized = TheTestMessage().parse(serialized)
    assert deserialized.a_normal_field == 0
    assert deserialized.an_optional_field is not None
    assert deserialized.an_optional_field == 22


def test_serialization_with_default_value():
    message = TheTestMessage(a_normal_field=0)
    serialized = bytes(message)
    assert serialized == b''
    deserialized = TheTestMessage().parse(serialized)
    assert deserialized.a_normal_field == 0
    assert deserialized.an_optional_field is None
