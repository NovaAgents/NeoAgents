import json
import logging
import sys
from dataclasses import asdict, is_dataclass
from datetime import datetime
from typing import Any

from ..agents import ChatMessage, StopMessage, TextMessage
from ._events import ContentPublishEvent, SelectSpeakerEvent, TerminationEvent, ToolCallEvent, ToolCallResultEvent

TRACE_LOGGER_NAME = "autogen_agentchat"
EVENT_LOGGER_NAME = "autogen_agentchat.events"


class ConsoleLogHandler(logging.Handler):
    @staticmethod
    def serialize_chat_message(message: ChatMessage) -> str:
        if isinstance(message, TextMessage | StopMessage):
            return message.content
        else:
            d = message.model_dump()
            assert "content" in d
            return json.dumps(d["content"], indent=2)

    def emit(self, record: logging.LogRecord) -> None:
        ts = datetime.fromtimestamp(record.created).isoformat()
        if isinstance(record.msg, ContentPublishEvent):
            if record.msg.source is None:
                sys.stdout.write(
                    f"\n{'-'*75} \n"
                    f"\033[91m[{ts}]:\033[0m\n"
                    f"\n{self.serialize_chat_message(record.msg.agent_message)}"
                )
            else:
                sys.stdout.write(
                    f"\n{'-'*75} \n"
                    f"\033[91m[{ts}], {record.msg.source.type}:\033[0m\n"
                    f"\n{self.serialize_chat_message(record.msg.agent_message)}"
                )
            sys.stdout.flush()
        elif isinstance(record.msg, ToolCallEvent):
            sys.stdout.write(
                f"\n{'-'*75} \n"
                f"\033[91m[{ts}], Tool Call:\033[0m\n"
                f"\n{self.serialize_chat_message(record.msg.agent_message)}"
            )
            sys.stdout.flush()
        elif isinstance(record.msg, ToolCallResultEvent):
            sys.stdout.write(
                f"\n{'-'*75} \n"
                f"\033[91m[{ts}], Tool Call Result:\033[0m\n"
                f"\n{self.serialize_chat_message(record.msg.agent_message)}"
            )
            sys.stdout.flush()
        elif isinstance(record.msg, SelectSpeakerEvent):
            sys.stdout.write(
                f"\n{'-'*75} \n" f"\033[91m[{ts}], Selected Next Speaker:\033[0m\n" f"\n{record.msg.selected_speaker}"
            )
            sys.stdout.flush()
        elif isinstance(record.msg, TerminationEvent):
            sys.stdout.write(
                f"\n{'-'*75} \n"
                f"\033[91m[{ts}], Termination:\033[0m\n"
                f"\n{self.serialize_chat_message(record.msg.agent_message)}"
            )
            sys.stdout.flush()
        else:
            raise ValueError(f"Unexpected log record: {record.msg}")


class FileLogHandler(logging.Handler):
    def __init__(self, filename: str) -> None:
        super().__init__()
        self.filename = filename
        self.file_handler = logging.FileHandler(filename)

    def emit(self, record: logging.LogRecord) -> None:
        ts = datetime.fromtimestamp(record.created).isoformat()
        if isinstance(record.msg, ContentPublishEvent | ToolCallEvent | ToolCallResultEvent | TerminationEvent):
            log_entry = json.dumps(
                {
                    "timestamp": ts,
                    "source": record.msg.source,
                    "agent_message": record.msg.agent_message.model_dump(),
                    "type": record.msg.__class__.__name__,
                },
                default=self.json_serializer,
            )
        elif isinstance(record.msg, SelectSpeakerEvent):
            log_entry = json.dumps(
                {
                    "timestamp": ts,
                    "source": record.msg.source,
                    "selected_speaker": record.msg.selected_speaker,
                    "type": "SelectSpeakerEvent",
                },
                default=self.json_serializer,
            )
        else:
            raise ValueError(f"Unexpected log record: {record.msg}")
        file_record = logging.LogRecord(
            name=record.name,
            level=record.levelno,
            pathname=record.pathname,
            lineno=record.lineno,
            msg=log_entry,
            args=(),
            exc_info=record.exc_info,
        )
        self.file_handler.emit(file_record)

    def close(self) -> None:
        self.file_handler.close()
        super().close()

    @staticmethod
    def json_serializer(obj: Any) -> Any:
        if is_dataclass(obj) and not isinstance(obj, type):
            return asdict(obj)
        elif isinstance(obj, type):
            return str(obj)
        return str(obj)
