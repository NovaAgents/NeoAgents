"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import cloudevent_pb2
import google.protobuf.any_pb2
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class AgentId(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_FIELD_NUMBER: builtins.int
    KEY_FIELD_NUMBER: builtins.int
    type: builtins.str
    key: builtins.str
    def __init__(
        self,
        *,
        type: builtins.str = ...,
        key: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["key", b"key", "type", b"type"]) -> None: ...

global___AgentId = AgentId

@typing.final
class RegisterAgentTypeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUEST_ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    type: builtins.str
    def __init__(
        self,
        *,
        request_id: builtins.str = ...,
        type: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["request_id", b"request_id", "type", b"type"]) -> None: ...

global___RegisterAgentTypeRequest = RegisterAgentTypeRequest

@typing.final
class RegisterAgentTypeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUEST_ID_FIELD_NUMBER: builtins.int
    SUCCESS_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    success: builtins.bool
    error: builtins.str
    def __init__(
        self,
        *,
        request_id: builtins.str = ...,
        success: builtins.bool = ...,
        error: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_error", b"_error", "error", b"error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_error", b"_error", "error", b"error", "request_id", b"request_id", "success", b"success"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_error", b"_error"]) -> typing.Literal["error"] | None: ...

global___RegisterAgentTypeResponse = RegisterAgentTypeResponse

@typing.final
class TypeSubscription(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOPIC_TYPE_FIELD_NUMBER: builtins.int
    AGENT_TYPE_FIELD_NUMBER: builtins.int
    topic_type: builtins.str
    agent_type: builtins.str
    def __init__(
        self,
        *,
        topic_type: builtins.str = ...,
        agent_type: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["agent_type", b"agent_type", "topic_type", b"topic_type"]) -> None: ...

global___TypeSubscription = TypeSubscription

@typing.final
class TypePrefixSubscription(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOPIC_TYPE_PREFIX_FIELD_NUMBER: builtins.int
    AGENT_TYPE_FIELD_NUMBER: builtins.int
    topic_type_prefix: builtins.str
    agent_type: builtins.str
    def __init__(
        self,
        *,
        topic_type_prefix: builtins.str = ...,
        agent_type: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["agent_type", b"agent_type", "topic_type_prefix", b"topic_type_prefix"]) -> None: ...

global___TypePrefixSubscription = TypePrefixSubscription

@typing.final
class Subscription(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPESUBSCRIPTION_FIELD_NUMBER: builtins.int
    TYPEPREFIXSUBSCRIPTION_FIELD_NUMBER: builtins.int
    @property
    def typeSubscription(self) -> global___TypeSubscription: ...
    @property
    def typePrefixSubscription(self) -> global___TypePrefixSubscription: ...
    def __init__(
        self,
        *,
        typeSubscription: global___TypeSubscription | None = ...,
        typePrefixSubscription: global___TypePrefixSubscription | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["subscription", b"subscription", "typePrefixSubscription", b"typePrefixSubscription", "typeSubscription", b"typeSubscription"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["subscription", b"subscription", "typePrefixSubscription", b"typePrefixSubscription", "typeSubscription", b"typeSubscription"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["subscription", b"subscription"]) -> typing.Literal["typeSubscription", "typePrefixSubscription"] | None: ...

global___Subscription = Subscription

@typing.final
class AddSubscriptionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUEST_ID_FIELD_NUMBER: builtins.int
    SUBSCRIPTION_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    @property
    def subscription(self) -> global___Subscription: ...
    def __init__(
        self,
        *,
        request_id: builtins.str = ...,
        subscription: global___Subscription | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["subscription", b"subscription"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["request_id", b"request_id", "subscription", b"subscription"]) -> None: ...

global___AddSubscriptionRequest = AddSubscriptionRequest

@typing.final
class AddSubscriptionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REQUEST_ID_FIELD_NUMBER: builtins.int
    SUCCESS_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    request_id: builtins.str
    success: builtins.bool
    error: builtins.str
    def __init__(
        self,
        *,
        request_id: builtins.str = ...,
        success: builtins.bool = ...,
        error: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_error", b"_error", "error", b"error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_error", b"_error", "error", b"error", "request_id", b"request_id", "success", b"success"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_error", b"_error"]) -> typing.Literal["error"] | None: ...

global___AddSubscriptionResponse = AddSubscriptionResponse

@typing.final
class AgentState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AGENT_ID_FIELD_NUMBER: builtins.int
    ETAG_FIELD_NUMBER: builtins.int
    BINARY_DATA_FIELD_NUMBER: builtins.int
    TEXT_DATA_FIELD_NUMBER: builtins.int
    PROTO_DATA_FIELD_NUMBER: builtins.int
    eTag: builtins.str
    binary_data: builtins.bytes
    text_data: builtins.str
    @property
    def agent_id(self) -> global___AgentId: ...
    @property
    def proto_data(self) -> google.protobuf.any_pb2.Any: ...
    def __init__(
        self,
        *,
        agent_id: global___AgentId | None = ...,
        eTag: builtins.str = ...,
        binary_data: builtins.bytes = ...,
        text_data: builtins.str = ...,
        proto_data: google.protobuf.any_pb2.Any | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["agent_id", b"agent_id", "binary_data", b"binary_data", "data", b"data", "proto_data", b"proto_data", "text_data", b"text_data"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["agent_id", b"agent_id", "binary_data", b"binary_data", "data", b"data", "eTag", b"eTag", "proto_data", b"proto_data", "text_data", b"text_data"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["data", b"data"]) -> typing.Literal["binary_data", "text_data", "proto_data"] | None: ...

global___AgentState = AgentState

@typing.final
class GetStateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AGENT_STATE_FIELD_NUMBER: builtins.int
    SUCCESS_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    success: builtins.bool
    error: builtins.str
    @property
    def agent_state(self) -> global___AgentState: ...
    def __init__(
        self,
        *,
        agent_state: global___AgentState | None = ...,
        success: builtins.bool = ...,
        error: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_error", b"_error", "agent_state", b"agent_state", "error", b"error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_error", b"_error", "agent_state", b"agent_state", "error", b"error", "success", b"success"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_error", b"_error"]) -> typing.Literal["error"] | None: ...

global___GetStateResponse = GetStateResponse

@typing.final
class SaveStateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUCCESS_FIELD_NUMBER: builtins.int
    ERROR_FIELD_NUMBER: builtins.int
    success: builtins.bool
    error: builtins.str
    def __init__(
        self,
        *,
        success: builtins.bool = ...,
        error: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_error", b"_error", "error", b"error"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_error", b"_error", "error", b"error", "success", b"success"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_error", b"_error"]) -> typing.Literal["error"] | None: ...

global___SaveStateResponse = SaveStateResponse

@typing.final
class Message(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLOUDEVENT_FIELD_NUMBER: builtins.int
    REGISTERAGENTTYPEREQUEST_FIELD_NUMBER: builtins.int
    REGISTERAGENTTYPERESPONSE_FIELD_NUMBER: builtins.int
    ADDSUBSCRIPTIONREQUEST_FIELD_NUMBER: builtins.int
    ADDSUBSCRIPTIONRESPONSE_FIELD_NUMBER: builtins.int
    @property
    def cloudEvent(self) -> cloudevent_pb2.CloudEvent: ...
    @property
    def registerAgentTypeRequest(self) -> global___RegisterAgentTypeRequest: ...
    @property
    def registerAgentTypeResponse(self) -> global___RegisterAgentTypeResponse: ...
    @property
    def addSubscriptionRequest(self) -> global___AddSubscriptionRequest: ...
    @property
    def addSubscriptionResponse(self) -> global___AddSubscriptionResponse: ...
    def __init__(
        self,
        *,
        cloudEvent: cloudevent_pb2.CloudEvent | None = ...,
        registerAgentTypeRequest: global___RegisterAgentTypeRequest | None = ...,
        registerAgentTypeResponse: global___RegisterAgentTypeResponse | None = ...,
        addSubscriptionRequest: global___AddSubscriptionRequest | None = ...,
        addSubscriptionResponse: global___AddSubscriptionResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["addSubscriptionRequest", b"addSubscriptionRequest", "addSubscriptionResponse", b"addSubscriptionResponse", "cloudEvent", b"cloudEvent", "message", b"message", "registerAgentTypeRequest", b"registerAgentTypeRequest", "registerAgentTypeResponse", b"registerAgentTypeResponse"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["addSubscriptionRequest", b"addSubscriptionRequest", "addSubscriptionResponse", b"addSubscriptionResponse", "cloudEvent", b"cloudEvent", "message", b"message", "registerAgentTypeRequest", b"registerAgentTypeRequest", "registerAgentTypeResponse", b"registerAgentTypeResponse"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["message", b"message"]) -> typing.Literal["cloudEvent", "registerAgentTypeRequest", "registerAgentTypeResponse", "addSubscriptionRequest", "addSubscriptionResponse"] | None: ...

global___Message = Message
