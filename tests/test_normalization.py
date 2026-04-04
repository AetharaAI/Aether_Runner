from aether_runner.models.schemas import ChatCompletionRequest, ContentItem, Message, ResponsesRequest, ResponsesAPIInputItem
from aether_runner.services.normalization import from_chat_request, from_responses_request


def test_chat_normalization_generates_canonical_request() -> None:
    req = ChatCompletionRequest(
        model="gemma-4-31b-it",
        messages=[Message(role="user", content=[ContentItem(type="text", text="hello")])],
        stream=True,
        temperature=0.2,
        top_p=0.8,
        max_tokens=111,
    )
    c = from_chat_request(req)
    assert c.model == "gemma-4-31b-it"
    assert c.route == "/v1/chat/completions"
    assert c.stream is True
    assert c.sampling.max_output_tokens == 111
    assert "text" in c.modalities()


def test_responses_normalization_string_input() -> None:
    req = ResponsesRequest(model="gemma-4-31b-it", input="hi", max_output_tokens=42)
    c = from_responses_request(req)
    assert c.route == "/v1/responses"
    assert c.messages[0].role == "user"
    assert c.messages[0].content[0].text == "hi"
    assert c.sampling.max_output_tokens == 42


def test_responses_normalization_array_input() -> None:
    req = ResponsesRequest(
        model="gemma-4-31b-it",
        input=[
            ResponsesAPIInputItem(
                role="user",
                content=[ContentItem(type="input_image", asset_id="asset_1"), ContentItem(type="text", text="describe")],
            )
        ],
    )
    c = from_responses_request(req)
    assert "image" in c.modalities()
