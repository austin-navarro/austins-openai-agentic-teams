[Skip to content](https://openai.github.io/openai-agents-python/models/#models)

# Models

The Agents SDK comes with out-of-the-box support for OpenAI models in two flavors:

- **Recommended**: the [`OpenAIResponsesModel`](https://openai.github.io/openai-agents-python/ref/models/openai_responses/#agents.models.openai_responses.OpenAIResponsesModel "OpenAIResponsesModel"), which calls OpenAI APIs using the new [Responses API](https://platform.openai.com/docs/api-reference/responses).
- The [`OpenAIChatCompletionsModel`](https://openai.github.io/openai-agents-python/ref/models/openai_chatcompletions/#agents.models.openai_chatcompletions.OpenAIChatCompletionsModel "OpenAIChatCompletionsModel"), which calls OpenAI APIs using the [Chat Completions API](https://platform.openai.com/docs/api-reference/chat).

## Mixing and matching models

Within a single workflow, you may want to use different models for each agent. For example, you could use a smaller, faster model for triage, while using a larger, more capable model for complex tasks. When configuring an [`Agent`](https://openai.github.io/openai-agents-python/ref/agent/#agents.agent.Agent "Agent            dataclass   "), you can select a specific model by either:

1. Passing the name of an OpenAI model.
2. Passing any model name + a [`ModelProvider`](https://openai.github.io/openai-agents-python/ref/models/interface/#agents.models.interface.ModelProvider "ModelProvider") that can map that name to a Model instance.
3. Directly providing a [`Model`](https://openai.github.io/openai-agents-python/ref/models/interface/#agents.models.interface.Model "Model") implementation.

Note

While our SDK supports both the [`OpenAIResponsesModel`](https://openai.github.io/openai-agents-python/ref/models/openai_responses/#agents.models.openai_responses.OpenAIResponsesModel "OpenAIResponsesModel") and the [`OpenAIChatCompletionsModel`](https://openai.github.io/openai-agents-python/ref/models/openai_chatcompletions/#agents.models.openai_chatcompletions.OpenAIChatCompletionsModel "OpenAIChatCompletionsModel") shapes, we recommend using a single model shape for each workflow because the two shapes support a different set of features and tools. If your workflow requires mixing and matching model shapes, make sure that all the features you're using are available on both.

```md-code__content
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
import asyncio

spanish_agent = Agent(
    name="Spanish agent",
    instructions="You only speak Spanish.",
    model="o3-mini",
)

english_agent = Agent(
    name="English agent",
    instructions="You only speak English",
    model=OpenAIChatCompletionsModel(
        model="gpt-4o",
        openai_client=AsyncOpenAI()
    ),
)

triage_agent = Agent(
    name="Triage agent",
    instructions="Handoff to the appropriate agent based on the language of the request.",
    handoffs=[spanish_agent, english_agent],
    model="gpt-3.5-turbo",
)

async def main():
    result = await Runner.run(triage_agent, input="Hola, ¿cómo estás?")
    print(result.final_output)

```

## Using other LLM providers

You can use other LLM providers in 3 ways (examples [here](https://github.com/openai/openai-agents-python/tree/main/examples/model_providers/)):

1. [`set_default_openai_client`](https://openai.github.io/openai-agents-python/ref/#agents.set_default_openai_client "set_default_openai_client") is useful in cases where you want to globally use an instance of `AsyncOpenAI` as the LLM client. This is for cases where the LLM provider has an OpenAI compatible API endpoint, and you can set the `base_url` and `api_key`. See a configurable example in [examples/model\_providers/custom\_example\_global.py](https://github.com/openai/openai-agents-python/tree/main/examples/model_providers/custom_example_global.py).
2. [`ModelProvider`](https://openai.github.io/openai-agents-python/ref/models/interface/#agents.models.interface.ModelProvider "ModelProvider") is at the `Runner.run` level. This lets you say "use a custom model provider for all agents in this run". See a configurable example in [examples/model\_providers/custom\_example\_provider.py](https://github.com/openai/openai-agents-python/tree/main/examples/model_providers/custom_example_provider.py).
3. [`Agent.model`](https://openai.github.io/openai-agents-python/ref/agent/#agents.agent.Agent.model "model            class-attribute       instance-attribute   ") lets you specify the model on a specific Agent instance. This enables you to mix and match different providers for different agents. See a configurable example in [examples/model\_providers/custom\_example\_agent.py](https://github.com/openai/openai-agents-python/tree/main/examples/model_providers/custom_example_agent.py).

In cases where you do not have an API key from `platform.openai.com`, we recommend disabling tracing via `set_tracing_disabled()`, or setting up a [different tracing processor](https://openai.github.io/openai-agents-python/tracing/).

Note

In these examples, we use the Chat Completions API/model, because most LLM providers don't yet support the Responses API. If your LLM provider does support it, we recommend using Responses.

## Common issues with using other LLM providers

### Tracing client error 401

If you get errors related to tracing, this is because traces are uploaded to OpenAI servers, and you don't have an OpenAI API key. You have three options to resolve this:

1. Disable tracing entirely: [`set_tracing_disabled(True)`](https://openai.github.io/openai-agents-python/ref/#agents.set_tracing_disabled "set_tracing_disabled").
2. Set an OpenAI key for tracing: [`set_tracing_export_api_key(...)`](https://openai.github.io/openai-agents-python/ref/#agents.set_tracing_export_api_key "set_tracing_export_api_key"). This API key will only be used for uploading traces, and must be from [platform.openai.com](https://platform.openai.com/).
3. Use a non-OpenAI trace processor. See the [tracing docs](https://openai.github.io/openai-agents-python/tracing/#custom-tracing-processors).

### Responses API support

The SDK uses the Responses API by default, but most other LLM providers don't yet support it. You may see 404s or similar issues as a result. To resolve, you have two options:

1. Call [`set_default_openai_api("chat_completions")`](https://openai.github.io/openai-agents-python/ref/#agents.set_default_openai_api "set_default_openai_api"). This works if you are setting `OPENAI_API_KEY` and `OPENAI_BASE_URL` via environment vars.
2. Use [`OpenAIChatCompletionsModel`](https://openai.github.io/openai-agents-python/ref/models/openai_chatcompletions/#agents.models.openai_chatcompletions.OpenAIChatCompletionsModel "OpenAIChatCompletionsModel"). There are examples [here](https://github.com/openai/openai-agents-python/tree/main/examples/model_providers/).

### Structured outputs support

Some model providers don't have support for [structured outputs](https://platform.openai.com/docs/guides/structured-outputs). This sometimes results in an error that looks something like this:

```md-code__content
BadRequestError: Error code: 400 - {'error': {'message': "'response_format.type' : value is not one of the allowed values ['text','json_object']", 'type': 'invalid_request_error'}}

```

This is a shortcoming of some model providers - they support JSON outputs, but don't allow you to specify the `json_schema` to use for the output. We are working on a fix for this, but we suggest relying on providers that do have support for JSON schema output, because otherwise your app will often break because of malformed JSON.