[Skip to content](https://openai.github.io/openai-agents-python/ref/voice/pipeline_config/#pipeline-config)

# `Pipeline Config`

### VoicePipelineConfig`dataclass`

Configuration for a `VoicePipeline`.

Source code in `src/agents/voice/pipeline_config.py`

|     |     |
| --- | --- |
| ```<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>``` | ```md-code__content<br>@dataclass<br>class VoicePipelineConfig:<br>    """Configuration for a `VoicePipeline`."""<br>    model_provider: VoiceModelProvider = field(default_factory=OpenAIVoiceModelProvider)<br>    """The voice model provider to use for the pipeline. Defaults to OpenAI."""<br>    tracing_disabled: bool = False<br>    """Whether to disable tracing of the pipeline. Defaults to `False`."""<br>    trace_include_sensitive_data: bool = True<br>    """Whether to include sensitive data in traces. Defaults to `True`. This is specifically for the<br>      voice pipeline, and not for anything that goes on inside your Workflow."""<br>    trace_include_sensitive_audio_data: bool = True<br>    """Whether to include audio data in traces. Defaults to `True`."""<br>    workflow_name: str = "Voice Agent"<br>    """The name of the workflow to use for tracing. Defaults to `Voice Agent`."""<br>    group_id: str = field(default_factory=gen_group_id)<br>    """<br>    A grouping identifier to use for tracing, to link multiple traces from the same conversation<br>    or process. If not provided, we will create a random group ID.<br>    """<br>    trace_metadata: dict[str, Any] | None = None<br>    """<br>    An optional dictionary of additional metadata to include with the trace.<br>    """<br>    stt_settings: STTModelSettings = field(default_factory=STTModelSettings)<br>    """The settings to use for the STT model."""<br>    tts_settings: TTSModelSettings = field(default_factory=TTSModelSettings)<br>    """The settings to use for the TTS model."""<br>``` |

#### model\_provider`class-attribute``instance-attribute`

```md-code__content
model_provider: VoiceModelProvider = field(
    default_factory=OpenAIVoiceModelProvider
)

```

The voice model provider to use for the pipeline. Defaults to OpenAI.

#### tracing\_disabled`class-attribute``instance-attribute`

```md-code__content
tracing_disabled: bool = False

```

Whether to disable tracing of the pipeline. Defaults to `False`.

#### trace\_include\_sensitive\_data`class-attribute``instance-attribute`

```md-code__content
trace_include_sensitive_data: bool = True

```

Whether to include sensitive data in traces. Defaults to `True`. This is specifically for the
voice pipeline, and not for anything that goes on inside your Workflow.

#### trace\_include\_sensitive\_audio\_data`class-attribute``instance-attribute`

```md-code__content
trace_include_sensitive_audio_data: bool = True

```

Whether to include audio data in traces. Defaults to `True`.

#### workflow\_name`class-attribute``instance-attribute`

```md-code__content
workflow_name: str = 'Voice Agent'

```

The name of the workflow to use for tracing. Defaults to `Voice Agent`.

#### group\_id`class-attribute``instance-attribute`

```md-code__content
group_id: str = field(default_factory=gen_group_id)

```

A grouping identifier to use for tracing, to link multiple traces from the same conversation
or process. If not provided, we will create a random group ID.

#### trace\_metadata`class-attribute``instance-attribute`

```md-code__content
trace_metadata: dict[str, Any] | None = None

```

An optional dictionary of additional metadata to include with the trace.

#### stt\_settings`class-attribute``instance-attribute`

```md-code__content
stt_settings: STTModelSettings = field(
    default_factory=STTModelSettings
)

```

The settings to use for the STT model.

#### tts\_settings`class-attribute``instance-attribute`

```md-code__content
tts_settings: TTSModelSettings = field(
    default_factory=TTSModelSettings
)

```

The settings to use for the TTS model.