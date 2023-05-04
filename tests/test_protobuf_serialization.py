from generated.proto import TheTestMessage, Node, Root


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


def test_serialization_of_optional_field_with_default_value():
    message = TheTestMessage(an_optional_field=0)
    serialized = bytes(message)
    assert serialized == b'\x10\x00'
    deserialized = TheTestMessage().parse(serialized)
    assert deserialized.a_normal_field == 0
    assert deserialized.an_optional_field is not None
    assert deserialized.an_optional_field == 0


def test_serialization_of_empty_nested_message():
    root = Root()
    serialized = bytes(root)
    assert serialized == b''
    deserialized = Root().parse(serialized)
    assert deserialized.node.an_optional_field is None
    assert deserialized.node is not None
    assert deserialized.optional_node is None


def test_serialization_of_nested_message():
    node = Node()
    optional_node = Node()
    root = Root(node=node, optional_node=optional_node)
    serialized = bytes(root)
    assert serialized == b'\n\x00'
    deserialized = Root().parse(serialized)
    assert deserialized.node.an_optional_field is None
    assert deserialized.node is not None
    assert deserialized.optional_node is not None
    assert deserialized.optional_node.an_optional_field is None


def test_serialization_of_nested_message_with_optional_value():
    node = Node(an_optional_field=2)
    root = Root(node=node)
    serialized = bytes(root)
    assert serialized == b'\x12\x02\x10\x02'
