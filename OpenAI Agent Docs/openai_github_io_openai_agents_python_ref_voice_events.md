[Skip to content](https://openai.github.io/openai-agents-python/ref/voice/events/#events)

# `Events`

### VoiceStreamEvent`module-attribute`

```md-code__content
VoiceStreamEvent: TypeAlias = Union[\
    VoiceStreamEventAudio,\
    VoiceStreamEventLifecycle,\
    VoiceStreamEventError,\
]

```

An event from the `VoicePipeline`, streamed via `StreamedAudioResult.stream()`.

### VoiceStreamEventAudio`dataclass`

Streaming event from the VoicePipeline

Source code in `src/agents/voice/events.py`

|     |     |
| --- | --- |
| ```<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>``` | ```md-code__content<br>@dataclass<br>class VoiceStreamEventAudio:<br>    """Streaming event from the VoicePipeline"""<br>    data: npt.NDArray[np.int16 | np.float32] | None<br>    """The audio data."""<br>    type: Literal["voice_stream_event_audio"] = "voice_stream_event_audio"<br>    """The type of event."""<br>``` |

#### data`instance-attribute`

```md-code__content
data: NDArray[int16 | float32] | None

```

The audio data.

#### type`class-attribute``instance-attribute`

```md-code__content
type: Literal["voice_stream_event_audio"] = (
    "voice_stream_event_audio"
)

```

The type of event.

### VoiceStreamEventLifecycle`dataclass`

Streaming event from the VoicePipeline

Source code in `src/agents/voice/events.py`

|     |     |
| --- | --- |
| ```<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>``` | ```md-code__content<br>@dataclass<br>class VoiceStreamEventLifecycle:<br>    """Streaming event from the VoicePipeline"""<br>    event: Literal["turn_started", "turn_ended", "session_ended"]<br>    """The event that occurred."""<br>    type: Literal["voice_stream_event_lifecycle"] = "voice_stream_event_lifecycle"<br>    """The type of event."""<br>``` |

#### event`instance-attribute`

```md-code__content
event: Literal[\
    "turn_started", "turn_ended", "session_ended"\
]

```

The event that occurred.

#### type`class-attribute``instance-attribute`

```md-code__content
type: Literal["voice_stream_event_lifecycle"] = (
    "voice_stream_event_lifecycle"
)

```

The type of event.

### VoiceStreamEventError`dataclass`

Streaming event from the VoicePipeline

Source code in `src/agents/voice/events.py`

|     |     |
| --- | --- |
| ```<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>``` | ```md-code__content<br>@dataclass<br>class VoiceStreamEventError:<br>    """Streaming event from the VoicePipeline"""<br>    error: Exception<br>    """The error that occurred."""<br>    type: Literal["voice_stream_event_error"] = "voice_stream_event_error"<br>    """The type of event."""<br>``` |

#### error`instance-attribute`

```md-code__content
error: Exception

```

The error that occurred.

#### type`class-attribute``instance-attribute`

```md-code__content
type: Literal["voice_stream_event_error"] = (
    "voice_stream_event_error"
)

```

The type of event.