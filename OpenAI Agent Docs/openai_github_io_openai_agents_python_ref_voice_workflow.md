[Skip to content](https://openai.github.io/openai-agents-python/ref/voice/workflow/#workflow)

# `Workflow`

### VoiceWorkflowBase

Bases: `ABC`

A base class for a voice workflow. You must implement the `run` method. A "workflow" is any
code you want, that receives a transcription and yields text that will be turned into speech
by a text-to-speech model.
In most cases, you'll create `Agent` s and use `Runner.run_streamed()` to run them, returning
some or all of the text events from the stream. You can use the `VoiceWorkflowHelper` class to
help with extracting text events from the stream.
If you have a simple workflow that has a single starting agent and no custom logic, you can
use `SingleAgentVoiceWorkflow` directly.

Source code in `src/agents/voice/workflow.py`

|     |     |
| --- | --- |
| ```<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>``` | ```md-code__content<br>class VoiceWorkflowBase(abc.ABC):<br>    """<br>    A base class for a voice workflow. You must implement the `run` method. A "workflow" is any<br>    code you want, that receives a transcription and yields text that will be turned into speech<br>    by a text-to-speech model.<br>    In most cases, you'll create `Agent`s and use `Runner.run_streamed()` to run them, returning<br>    some or all of the text events from the stream. You can use the `VoiceWorkflowHelper` class to<br>    help with extracting text events from the stream.<br>    If you have a simple workflow that has a single starting agent and no custom logic, you can<br>    use `SingleAgentVoiceWorkflow` directly.<br>    """<br>    @abc.abstractmethod<br>    def run(self, transcription: str) -> AsyncIterator[str]:<br>        """<br>        Run the voice workflow. You will receive an input transcription, and must yield text that<br>        will be spoken to the user. You can run whatever logic you want here. In most cases, the<br>        final logic will involve calling `Runner.run_streamed()` and yielding any text events from<br>        the stream.<br>        """<br>        pass<br>``` |

#### run`abstractmethod`

```md-code__content
run(transcription: str) -> AsyncIterator[str]

```

Run the voice workflow. You will receive an input transcription, and must yield text that
will be spoken to the user. You can run whatever logic you want here. In most cases, the
final logic will involve calling `Runner.run_streamed()` and yielding any text events from
the stream.

Source code in `src/agents/voice/workflow.py`

|     |     |
| --- | --- |
| ```<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>``` | ```md-code__content<br>@abc.abstractmethod<br>def run(self, transcription: str) -> AsyncIterator[str]:<br>    """<br>    Run the voice workflow. You will receive an input transcription, and must yield text that<br>    will be spoken to the user. You can run whatever logic you want here. In most cases, the<br>    final logic will involve calling `Runner.run_streamed()` and yielding any text events from<br>    the stream.<br>    """<br>    pass<br>``` |

### VoiceWorkflowHelper

Source code in `src/agents/voice/workflow.py`

|     |     |
| --- | --- |
| ```<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>``` | ```md-code__content<br>class VoiceWorkflowHelper:<br>    @classmethod<br>    async def stream_text_from(cls, result: RunResultStreaming) -> AsyncIterator[str]:<br>        """Wraps a `RunResultStreaming` object and yields text events from the stream."""<br>        async for event in result.stream_events():<br>            if (<br>                event.type == "raw_response_event"<br>                and event.data.type == "response.output_text.delta"<br>            ):<br>                yield event.data.delta<br>``` |

#### stream\_text\_from`async``classmethod`

```md-code__content
stream_text_from(
    result: RunResultStreaming,
) -> AsyncIterator[str]

```

Wraps a `RunResultStreaming` object and yields text events from the stream.

Source code in `src/agents/voice/workflow.py`

|     |     |
| --- | --- |
| ```<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>``` | ```md-code__content<br>@classmethod<br>async def stream_text_from(cls, result: RunResultStreaming) -> AsyncIterator[str]:<br>    """Wraps a `RunResultStreaming` object and yields text events from the stream."""<br>    async for event in result.stream_events():<br>        if (<br>            event.type == "raw_response_event"<br>            and event.data.type == "response.output_text.delta"<br>        ):<br>            yield event.data.delta<br>``` |

### SingleAgentWorkflowCallbacks

Source code in `src/agents/voice/workflow.py`

|     |     |
| --- | --- |
| ```<br>48<br>49<br>50<br>51<br>``` | ```md-code__content<br>class SingleAgentWorkflowCallbacks:<br>    def on_run(self, workflow: SingleAgentVoiceWorkflow, transcription: str) -> None:<br>        """Called when the workflow is run."""<br>        pass<br>``` |

#### on\_run

```md-code__content
on_run(
    workflow: SingleAgentVoiceWorkflow, transcription: str
) -> None

```

Called when the workflow is run.

Source code in `src/agents/voice/workflow.py`

|     |     |
| --- | --- |
| ```<br>49<br>50<br>51<br>``` | ```md-code__content<br>def on_run(self, workflow: SingleAgentVoiceWorkflow, transcription: str) -> None:<br>    """Called when the workflow is run."""<br>    pass<br>``` |

### SingleAgentVoiceWorkflow

Bases: `VoiceWorkflowBase`

A simple voice workflow that runs a single agent. Each transcription and result is added to
the input history.
For more complex workflows (e.g. multiple Runner calls, custom message history, custom logic,
custom configs), subclass `VoiceWorkflowBase` and implement your own logic.

Source code in `src/agents/voice/workflow.py`

|     |     |
| --- | --- |
| ```<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>71<br>72<br>73<br>74<br>75<br>76<br>77<br>78<br>79<br>80<br>81<br>82<br>83<br>84<br>85<br>86<br>87<br>88<br>89<br>90<br>91<br>92<br>93<br>``` | ```md-code__content<br>class SingleAgentVoiceWorkflow(VoiceWorkflowBase):<br>    """A simple voice workflow that runs a single agent. Each transcription and result is added to<br>    the input history.<br>    For more complex workflows (e.g. multiple Runner calls, custom message history, custom logic,<br>    custom configs), subclass `VoiceWorkflowBase` and implement your own logic.<br>    """<br>    def __init__(self, agent: Agent[Any], callbacks: SingleAgentWorkflowCallbacks | None = None):<br>        """Create a new single agent voice workflow.<br>        Args:<br>            agent: The agent to run.<br>            callbacks: Optional callbacks to call during the workflow.<br>        """<br>        self._input_history: list[TResponseInputItem] = []<br>        self._current_agent = agent<br>        self._callbacks = callbacks<br>    async def run(self, transcription: str) -> AsyncIterator[str]:<br>        if self._callbacks:<br>            self._callbacks.on_run(self, transcription)<br>        # Add the transcription to the input history<br>        self._input_history.append(<br>            {<br>                "role": "user",<br>                "content": transcription,<br>            }<br>        )<br>        # Run the agent<br>        result = Runner.run_streamed(self._current_agent, self._input_history)<br>        # Stream the text from the result<br>        async for chunk in VoiceWorkflowHelper.stream_text_from(result):<br>            yield chunk<br>        # Update the input history and current agent<br>        self._input_history = result.to_input_list()<br>        self._current_agent = result.last_agent<br>``` |

#### \_\_init\_\_

```md-code__content
__init__(
    agent: Agent[Any],
    callbacks: SingleAgentWorkflowCallbacks | None = None,
)

```

Create a new single agent voice workflow.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `agent` | `Agent[Any]` | The agent to run. | _required_ |
| `callbacks` | `SingleAgentWorkflowCallbacks | None` | Optional callbacks to call during the workflow. | `None` |

Source code in `src/agents/voice/workflow.py`

|     |     |
| --- | --- |
| ```<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>``` | ```md-code__content<br>def __init__(self, agent: Agent[Any], callbacks: SingleAgentWorkflowCallbacks | None = None):<br>    """Create a new single agent voice workflow.<br>    Args:<br>        agent: The agent to run.<br>        callbacks: Optional callbacks to call during the workflow.<br>    """<br>    self._input_history: list[TResponseInputItem] = []<br>    self._current_agent = agent<br>    self._callbacks = callbacks<br>``` |