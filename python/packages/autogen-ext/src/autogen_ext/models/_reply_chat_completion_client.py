from __future__ import annotations

import logging
from typing import Any, AsyncGenerator, List, Mapping, Optional, Sequence, Union

from autogen_core.application.logging import EVENT_LOGGER_NAME
from autogen_core.base import CancellationToken
from autogen_core.components.models import (
    ChatCompletionClient,
    CreateResult,
    LLMMessage,
    ModelCapabilities,
    RequestUsage,
)
from autogen_core.components.tools import Tool, ToolSchema

logger = logging.getLogger(EVENT_LOGGER_NAME)


class ReplayChatCompletionClient:
    """A mock chat completion client that replays predefined responses."""

    __protocol__: ChatCompletionClient

    # TODO: Support FunctionCall in responses
    # TODO: Support logprobs in Responses
    # TODO: Support model capabilities
    def __init__(
        self,
        chat_completions: Sequence[Union[str, CreateResult]],
    ):
        """Initialize with a list of chat completions to replay.

        Args:
            chat_completions: List of responses to return. Each response can be:
                - A string (will be wrapped in a completion response)
                - A CreateResult object
        """
        self.chat_completions = list(chat_completions)
        self._cur_usage = RequestUsage(prompt_tokens=0, completion_tokens=0)
        self._total_usage = RequestUsage(prompt_tokens=0, completion_tokens=0)
        self.provided_message_count = len(self.chat_completions)
        self._model_capabilities = ModelCapabilities(vision=False, function_calling=False, json_output=False)
        self._total_available_tokens = 10000

    async def create(
        self,
        messages: Sequence[LLMMessage],
        tools: Sequence[Tool | ToolSchema] = [],
        json_output: Optional[bool] = None,
        extra_create_args: Mapping[str, Any] = {},
        cancellation_token: Optional[CancellationToken] = None,
    ) -> CreateResult:
        """Return the next completion from the list."""
        if not self.chat_completions:
            raise ValueError("No more mock responses available")

        response = self.chat_completions.pop(0)
        _, prompt_token_count = self._tokenize(messages)
        if isinstance(response, str):
            _, output_token_count = self._tokenize(response)
            self._cur_usage = RequestUsage(prompt_tokens=prompt_token_count, completion_tokens=output_token_count)
            response = CreateResult(finish_reason="stop", content=response, usage=self._cur_usage, cached=True)
        else:
            self._cur_usage = RequestUsage(
                prompt_tokens=prompt_token_count, completion_tokens=response.usage.completion_tokens
            )

        self._update_total_usage()
        return response

    async def create_stream(
        self,
        messages: Sequence[LLMMessage],
        tools: Sequence[Tool | ToolSchema] = [],
        json_output: Optional[bool] = None,
        extra_create_args: Mapping[str, Any] = {},
        cancellation_token: Optional[CancellationToken] = None,
    ) -> AsyncGenerator[Union[str, CreateResult], None]:
        """Return the next completion as a stream."""
        if not self.chat_completions:
            raise ValueError("No more mock responses available")

        response = self.chat_completions.pop(0)
        _, prompt_token_count = self._tokenize(messages)
        if isinstance(response, str):
            output_tokens, output_token_count = self._tokenize(response)
            self._cur_usage = RequestUsage(prompt_tokens=prompt_token_count, completion_tokens=output_token_count)

            for i, token in enumerate(output_tokens):
                if i < len(output_tokens) - 1:
                    yield token + " "
                else:
                    yield token
            self._update_total_usage()
        else:
            self._cur_usage = RequestUsage(
                prompt_tokens=prompt_token_count, completion_tokens=response.usage.completion_tokens
            )
            yield response
            self._update_total_usage()

    def actual_usage(self) -> RequestUsage:
        return self._cur_usage

    def total_usage(self) -> RequestUsage:
        return self._total_usage

    def count_tokens(self, messages: Sequence[LLMMessage], tools: Sequence[Tool | ToolSchema] = []) -> int:
        _, token_count = self._tokenize(messages)
        return token_count

    def remaining_tokens(self, messages: Sequence[LLMMessage], tools: Sequence[Tool | ToolSchema] = []) -> int:
        return max(
            0, self._total_available_tokens - self._total_usage.prompt_tokens - self._total_usage.completion_tokens
        )

    def _tokenize(self, messages: Union[str, LLMMessage, Sequence[LLMMessage]]) -> tuple[list[str], int]:
        total_tokens = 0
        all_tokens: List[str] = []
        if isinstance(messages, str):
            tokens = messages.split()
            total_tokens += len(tokens)
            all_tokens.extend(tokens)
        elif hasattr(messages, "content"):
            if isinstance(messages.content, str):  # type: ignore [reportAttributeAccessIssue]
                tokens = messages.content.split()  # type: ignore [reportAttributeAccessIssue]
                total_tokens += len(tokens)
                all_tokens.extend(tokens)
            else:
                logger.warning("Token count has been done only on string content", RuntimeWarning)
        elif isinstance(messages, Sequence):
            for message in messages:
                if isinstance(message.content, str):  # type: ignore [reportAttributeAccessIssue, union-attr]
                    tokens = message.content.split()  # type: ignore [reportAttributeAccessIssue, union-attr]
                    total_tokens += len(tokens)
                    all_tokens.extend(tokens)
                else:
                    logger.warning("Token count has been done only on string content", RuntimeWarning)
        return all_tokens, total_tokens

    def _update_total_usage(self) -> None:
        self._total_usage.completion_tokens += self._cur_usage.completion_tokens
        self._total_usage.prompt_tokens += self._cur_usage.prompt_tokens

    @property
    def capabilities(self) -> ModelCapabilities:
        """Return mock capabilities."""
        return self._model_capabilities