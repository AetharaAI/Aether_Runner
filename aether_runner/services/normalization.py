from __future__ import annotations

from aether_runner.models.schemas import (
    CanonicalRequest,
    ChatCompletionRequest,
    ContentItem,
    LegacyCompletionRequest,
    Message,
    ResponsesRequest,
)


def from_chat_request(req: ChatCompletionRequest) -> CanonicalRequest:
    return CanonicalRequest(
        model=req.model,
        route="/v1/chat/completions",
        mode="chat",
        messages=req.messages,
        tools=req.tools,
        tool_choice=req.tool_choice,
        response_format=req.response_format,
        stream=req.stream,
        sampling={
            "temperature": req.temperature,
            "top_p": req.top_p,
            "max_output_tokens": req.max_tokens,
        },
    )


def from_responses_request(req: ResponsesRequest) -> CanonicalRequest:
    if isinstance(req.input, str):
        messages = [Message(role="user", content=[ContentItem(type="text", text=req.input)])]
    else:
        messages = [Message(role=item.role, content=item.content) for item in req.input]

    return CanonicalRequest(
        model=req.model,
        route="/v1/responses",
        mode="responses",
        messages=messages,
        tools=req.tools,
        tool_choice=req.tool_choice,
        stream=req.stream,
        sampling={
            "temperature": req.temperature,
            "top_p": req.top_p,
            "max_output_tokens": req.max_output_tokens,
        },
    )


def from_completion_request(req: LegacyCompletionRequest) -> CanonicalRequest:
    return CanonicalRequest(
        model=req.model,
        route="/v1/completions",
        mode="completion",
        messages=[Message(role="user", content=[ContentItem(type="text", text=req.prompt)])],
        stream=req.stream,
        sampling={
            "temperature": req.temperature,
            "top_p": req.top_p,
            "max_output_tokens": req.max_tokens,
        },
    )
