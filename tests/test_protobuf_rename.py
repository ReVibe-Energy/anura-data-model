import datetime
import uuid

from generated.proto import Origin, RenamedOrigin


def test_serialized_data_can_be_read_after_rename():
    gateway_id = "gateway_id"
    node_id = "node_id"
    timestamp = datetime.datetime.now(datetime.timezone.utc)
    is_synced = True
    snapshot_id = str(uuid.uuid4())
    message = Origin(gateway_id, node_id, timestamp, is_synced, snapshot_id)
    serialized = bytes(message)

    deserialized = RenamedOrigin().parse(serialized)
    assert deserialized.gateway_id == gateway_id
    assert deserialized.node_id == node_id
    assert deserialized.timestamp == timestamp
    assert deserialized.is_synced == is_synced
    assert deserialized.snapshot_id == snapshot_id
