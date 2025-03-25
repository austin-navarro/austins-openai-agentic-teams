[Skip to content](https://openai.github.io/openai-agents-python/ref/voice/model/#model)

# `Model`

### TTSModelSettings`dataclass`

Settings for a TTS model.

Source code in `src/agents/voice/model.py`

|     |     |
| --- | --- |
| ```<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>``` | ```md-code__content<br>@dataclass<br>class TTSModelSettings:<br>    """Settings for a TTS model."""<br>    voice: (<br>        Literal["alloy", "ash", "coral", "echo", "fable", "onyx", "nova", "sage", "shimmer"] | None<br>    ) = None<br>    """<br>    The voice to use for the TTS model. If not provided, the default voice for the respective model<br>    will be used.<br>    """<br>    buffer_size: int = 120<br>    """The minimal size of the chunks of audio data that are being streamed out."""<br>    dtype: npt.DTypeLike = np.int16<br>    """The data type for the audio data to be returned in."""<br>    transform_data: (<br>        Callable[[npt.NDArray[np.int16 | np.float32]], npt.NDArray[np.int16 | np.float32]] | None<br>    ) = None<br>    """<br>    A function to transform the data from the TTS model. This is useful if you want the resulting<br>    audio stream to have the data in a specific shape already.<br>    """<br>    instructions: str = (<br>        "You will receive partial sentences. Do not complete the sentence just read out the text."<br>    )<br>    """<br>    The instructions to use for the TTS model. This is useful if you want to control the tone of the<br>    audio output.<br>    """<br>    text_splitter: Callable[[str], tuple[str, str]] = get_sentence_based_splitter()<br>    """<br>    A function to split the text into chunks. This is useful if you want to split the text into<br>    chunks before sending it to the TTS model rather than waiting for the whole text to be<br>    processed.<br>    """<br>    speed: float | None = None<br>    """The speed with which the TTS model will read the text. Between 0.25 and 4.0."""<br>``` |

#### voice`class-attribute``instance-attribute`

```md-code__content
voice: (
    Literal[\
        "alloy",\
        "ash",\
        "coral",\
        "echo",\
        "fable",\
        "onyx",\
        "nova",\
        "sage",\
        "shimmer",\
    ]
    | None
) = None

```

The voice to use for the TTS model. If not provided, the default voice for the respective model
will be used.

#### buffer\_size`class-attribute``instance-attribute`

```md-code__content
buffer_size: int = 120

```

The minimal size of the chunks of audio data that are being streamed out.

#### dtype`class-attribute``instance-attribute`

```md-code__content
dtype: DTypeLike = int16

```

The data type for the audio data to be returned in.

#### transform\_data`class-attribute``instance-attribute`

```md-code__content
transform_data: (
    Callable[\
        [NDArray[int16 | float32]], NDArray[int16 | float32]\
    ]
    | None
) = None

```

A function to transform the data from the TTS model. This is useful if you want the resulting
audio stream to have the data in a specific shape already.

#### instructions`class-attribute``instance-attribute`

```md-code__content
instructions: str = "You will receive partial sentences. Do not complete the sentence just read out the text."

```

The instructions to use for the TTS model. This is useful if you want to control the tone of the
audio output.

#### text\_splitter`class-attribute``instance-attribute`

```md-code__content
text_splitter: Callable[[str], tuple[str, str]] = (
    get_sentence_based_splitter()
)

```

A function to split the text into chunks. This is useful if you want to split the text into
chunks before sending it to the TTS model rather than waiting for the whole text to be
processed.

#### speed`class-attribute``instance-attribute`

```md-code__content
speed: float | None = None

```

The speed with which the TTS model will read the text. Between 0.25 and 4.0.

### TTSModel

Bases: `ABC`

A text-to-speech model that can convert text into audio output.

Source code in `src/agents/voice/model.py`

|     |     |
| --- | --- |
| ```<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>71<br>72<br>73<br>74<br>75<br>76<br>77<br>78<br>79<br>80<br>81<br>82<br>``` | ```md-code__content<br>class TTSModel(abc.ABC):<br>    """A text-to-speech model that can convert text into audio output."""<br>    @property<br>    @abc.abstractmethod<br>    def model_name(self) -> str:<br>        """The name of the TTS model."""<br>        pass<br>    @abc.abstractmethod<br>    def run(self, text: str, settings: TTSModelSettings) -> AsyncIterator[bytes]:<br>        """Given a text string, produces a stream of audio bytes, in PCM format.<br>        Args:<br>            text: The text to convert to audio.<br>        Returns:<br>            An async iterator of audio bytes, in PCM format.<br>        """<br>        pass<br>``` |

#### model\_name`abstractmethod``property`

```md-code__content
model_name: str

```

The name of the TTS model.

#### run`abstractmethod`

```md-code__content
run(
    text: str, settings: TTSModelSettings
) -> AsyncIterator[bytes]

```

Given a text string, produces a stream of audio bytes, in PCM format.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `text` | `str` | The text to convert to audio. | _required_ |

Returns:

| Type | Description |
| --- | --- |
| `AsyncIterator[bytes]` | An async iterator of audio bytes, in PCM format. |

Source code in `src/agents/voice/model.py`

|     |     |
| --- | --- |
| ```<br>72<br>73<br>74<br>75<br>76<br>77<br>78<br>79<br>80<br>81<br>82<br>``` | ```md-code__content<br>@abc.abstractmethod<br>def run(self, text: str, settings: TTSModelSettings) -> AsyncIterator[bytes]:<br>    """Given a text string, produces a stream of audio bytes, in PCM format.<br>    Args:<br>        text: The text to convert to audio.<br>    Returns:<br>        An async iterator of audio bytes, in PCM format.<br>    """<br>    pass<br>``` |

### StreamedTranscriptionSession

Bases: `ABC`

A streamed transcription of audio input.

Source code in `src/agents/voice/model.py`

|     |     |
| --- | --- |
| ```<br>85<br>86<br>87<br>88<br>89<br>90<br>91<br>92<br>93<br>94<br>95<br>96<br>97<br>98<br>99<br>``` | ```md-code__content<br>class StreamedTranscriptionSession(abc.ABC):<br>    """A streamed transcription of audio input."""<br>    @abc.abstractmethod<br>    def transcribe_turns(self) -> AsyncIterator[str]:<br>        """Yields a stream of text transcriptions. Each transcription is a turn in the conversation.<br>        This method is expected to return only after `close()` is called.<br>        """<br>        pass<br>    @abc.abstractmethod<br>    async def close(self) -> None:<br>        """Closes the session."""<br>        pass<br>``` |

#### transcribe\_turns`abstractmethod`

```md-code__content
transcribe_turns() -> AsyncIterator[str]

```

Yields a stream of text transcriptions. Each transcription is a turn in the conversation.

This method is expected to return only after `close()` is called.

Source code in `src/agents/voice/model.py`

|     |     |
| --- | --- |
| ```<br>88<br>89<br>90<br>91<br>92<br>93<br>94<br>``` | ```md-code__content<br>@abc.abstractmethod<br>def transcribe_turns(self) -> AsyncIterator[str]:<br>    """Yields a stream of text transcriptions. Each transcription is a turn in the conversation.<br>    This method is expected to return only after `close()` is called.<br>    """<br>    pass<br>``` |

#### close`abstractmethod``async`

```md-code__content
close() -> None

```

Closes the session.

Source code in `src/agents/voice/model.py`

|     |     |
| --- | --- |
| ```<br>96<br>97<br>98<br>99<br>``` | ```md-code__content<br>@abc.abstractmethod<br>async def close(self) -> None:<br>    """Closes the session."""<br>    pass<br>``` |

### STTModelSettings`dataclass`

Settings for a speech-to-text model.

Source code in `src/agents/voice/model.py`

|     |     |
| --- | --- |
| ```<br>102<br>103<br>104<br>105<br>106<br>107<br>108<br>109<br>110<br>111<br>112<br>113<br>114<br>115<br>116<br>``` | ```md-code__content<br>@dataclass<br>class STTModelSettings:<br>    """Settings for a speech-to-text model."""<br>    prompt: str | None = None<br>    """Instructions for the model to follow."""<br>    language: str | None = None<br>    """The language of the audio input."""<br>    temperature: float | None = None<br>    """The temperature of the model."""<br>    turn_detection: dict[str, Any] | None = None<br>    """The turn detection settings for the model when using streamed audio input."""<br>``` |

#### prompt`class-attribute``instance-attribute`

```md-code__content
prompt: str | None = None

```

Instructions for the model to follow.

#### language`class-attribute``instance-attribute`

```md-code__content
language: str | None = None

```

The language of the audio input.

#### temperature`class-attribute``instance-attribute`

```md-code__content
temperature: float | None = None

```

The temperature of the model.

#### turn\_detection`class-attribute``instance-attribute`

```md-code__content
turn_detection: dict[str, Any] | None = None

```

The turn detection settings for the model when using streamed audio input.

### STTModel

Bases: `ABC`

A speech-to-text model that can convert audio input into text.

Source code in `src/agents/voice/model.py`

|     |     |
| --- | --- |
| ```<br>119<br>120<br>121<br>122<br>123<br>124<br>125<br>126<br>127<br>128<br>129<br>130<br>131<br>132<br>133<br>134<br>135<br>136<br>137<br>138<br>139<br>140<br>141<br>142<br>143<br>144<br>145<br>146<br>147<br>148<br>149<br>150<br>151<br>152<br>153<br>154<br>155<br>156<br>157<br>158<br>159<br>160<br>161<br>162<br>163<br>164<br>165<br>166<br>167<br>168<br>169<br>``` | ```md-code__content<br>class STTModel(abc.ABC):<br>    """A speech-to-text model that can convert audio input into text."""<br>    @property<br>    @abc.abstractmethod<br>    def model_name(self) -> str:<br>        """The name of the STT model."""<br>        pass<br>    @abc.abstractmethod<br>    async def transcribe(<br>        self,<br>        input: AudioInput,<br>        settings: STTModelSettings,<br>        trace_include_sensitive_data: bool,<br>        trace_include_sensitive_audio_data: bool,<br>    ) -> str:<br>        """Given an audio input, produces a text transcription.<br>        Args:<br>            input: The audio input to transcribe.<br>            settings: The settings to use for the transcription.<br>            trace_include_sensitive_data: Whether to include sensitive data in traces.<br>            trace_include_sensitive_audio_data: Whether to include sensitive audio data in traces.<br>        Returns:<br>            The text transcription of the audio input.<br>        """<br>        pass<br>    @abc.abstractmethod<br>    async def create_session(<br>        self,<br>        input: StreamedAudioInput,<br>        settings: STTModelSettings,<br>        trace_include_sensitive_data: bool,<br>        trace_include_sensitive_audio_data: bool,<br>    ) -> StreamedTranscriptionSession:<br>        """Creates a new transcription session, which you can push audio to, and receive a stream<br>        of text transcriptions.<br>        Args:<br>            input: The audio input to transcribe.<br>            settings: The settings to use for the transcription.<br>            trace_include_sensitive_data: Whether to include sensitive data in traces.<br>            trace_include_sensitive_audio_data: Whether to include sensitive audio data in traces.<br>        Returns:<br>            A new transcription session.<br>        """<br>        pass<br>``` |

#### model\_name`abstractmethod``property`

```md-code__content
model_name: str

```

The name of the STT model.

#### transcribe`abstractmethod``async`

```md-code__content
transcribe(
    input: AudioInput,
    settings: STTModelSettings,
    trace_include_sensitive_data: bool,
    trace_include_sensitive_audio_data: bool,
) -> str

```

Given an audio input, produces a text transcription.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `input` | `AudioInput` | The audio input to transcribe. | _required_ |
| `settings` | `STTModelSettings` | The settings to use for the transcription. | _required_ |
| `trace_include_sensitive_data` | `bool` | Whether to include sensitive data in traces. | _required_ |
| `trace_include_sensitive_audio_data` | `bool` | Whether to include sensitive audio data in traces. | _required_ |

Returns:

| Type | Description |
| --- | --- |
| `str` | The text transcription of the audio input. |

Source code in `src/agents/voice/model.py`

|     |     |
| --- | --- |
| ```<br>128<br>129<br>130<br>131<br>132<br>133<br>134<br>135<br>136<br>137<br>138<br>139<br>140<br>141<br>142<br>143<br>144<br>145<br>146<br>147<br>``` | ```md-code__content<br>@abc.abstractmethod<br>async def transcribe(<br>    self,<br>    input: AudioInput,<br>    settings: STTModelSettings,<br>    trace_include_sensitive_data: bool,<br>    trace_include_sensitive_audio_data: bool,<br>) -> str:<br>    """Given an audio input, produces a text transcription.<br>    Args:<br>        input: The audio input to transcribe.<br>        settings: The settings to use for the transcription.<br>        trace_include_sensitive_data: Whether to include sensitive data in traces.<br>        trace_include_sensitive_audio_data: Whether to include sensitive audio data in traces.<br>    Returns:<br>        The text transcription of the audio input.<br>    """<br>    pass<br>``` |

#### create\_session`abstractmethod``async`

```md-code__content
create_session(
    input: StreamedAudioInput,
    settings: STTModelSettings,
    trace_include_sensitive_data: bool,
    trace_include_sensitive_audio_data: bool,
) -> StreamedTranscriptionSession

```

Creates a new transcription session, which you can push audio to, and receive a stream
of text transcriptions.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `input` | `StreamedAudioInput` | The audio input to transcribe. | _required_ |
| `settings` | `STTModelSettings` | The settings to use for the transcription. | _required_ |
| `trace_include_sensitive_data` | `bool` | Whether to include sensitive data in traces. | _required_ |
| `trace_include_sensitive_audio_data` | `bool` | Whether to include sensitive audio data in traces. | _required_ |

Returns:

| Type | Description |
| --- | --- |
| `StreamedTranscriptionSession` | A new transcription session. |

Source code in `src/agents/voice/model.py`

|     |     |
| --- | --- |
| ```<br>149<br>150<br>151<br>152<br>153<br>154<br>155<br>156<br>157<br>158<br>159<br>160<br>161<br>162<br>163<br>164<br>165<br>166<br>167<br>168<br>169<br>``` | ```md-code__content<br>@abc.abstractmethod<br>async def create_session(<br>    self,<br>    input: StreamedAudioInput,<br>    settings: STTModelSettings,<br>    trace_include_sensitive_data: bool,<br>    trace_include_sensitive_audio_data: bool,<br>) -> StreamedTranscriptionSession:<br>    """Creates a new transcription session, which you can push audio to, and receive a stream<br>    of text transcriptions.<br>    Args:<br>        input: The audio input to transcribe.<br>        settings: The settings to use for the transcription.<br>        trace_include_sensitive_data: Whether to include sensitive data in traces.<br>        trace_include_sensitive_audio_data: Whether to include sensitive audio data in traces.<br>    Returns:<br>        A new transcription session.<br>    """<br>    pass<br>``` |

### VoiceModelProvider

Bases: `ABC`

The base interface for a voice model provider.

A model provider is responsible for creating speech-to-text and text-to-speech models, given a
name.

Source code in `src/agents/voice/model.py`

|     |     |
| --- | --- |
| ```<br>172<br>173<br>174<br>175<br>176<br>177<br>178<br>179<br>180<br>181<br>182<br>183<br>184<br>185<br>186<br>187<br>188<br>189<br>190<br>191<br>192<br>193<br>``` | ```md-code__content<br>class VoiceModelProvider(abc.ABC):<br>    """The base interface for a voice model provider.<br>    A model provider is responsible for creating speech-to-text and text-to-speech models, given a<br>    name.<br>    """<br>    @abc.abstractmethod<br>    def get_stt_model(self, model_name: str | None) -> STTModel:<br>        """Get a speech-to-text model by name.<br>        Args:<br>            model_name: The name of the model to get.<br>        Returns:<br>            The speech-to-text model.<br>        """<br>        pass<br>    @abc.abstractmethod<br>    def get_tts_model(self, model_name: str | None) -> TTSModel:<br>        """Get a text-to-speech model by name."""<br>``` |

#### get\_stt\_model`abstractmethod`

```md-code__content
get_stt_model(model_name: str | None) -> STTModel

```

Get a speech-to-text model by name.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `model_name` | `str | None` | The name of the model to get. | _required_ |

Returns:

| Type | Description |
| --- | --- |
| `STTModel` | The speech-to-text model. |

Source code in `src/agents/voice/model.py`

|     |     |
| --- | --- |
| ```<br>179<br>180<br>181<br>182<br>183<br>184<br>185<br>186<br>187<br>188<br>189<br>``` | ```md-code__content<br>@abc.abstractmethod<br>def get_stt_model(self, model_name: str | None) -> STTModel:<br>    """Get a speech-to-text model by name.<br>    Args:<br>        model_name: The name of the model to get.<br>    Returns:<br>        The speech-to-text model.<br>    """<br>    pass<br>``` |

#### get\_tts\_model`abstractmethod`

```md-code__content
get_tts_model(model_name: str | None) -> TTSModel

```

Get a text-to-speech model by name.

Source code in `src/agents/voice/model.py`

|     |     |
| --- | --- |
| ```<br>191<br>192<br>193<br>``` | ```md-code__content<br>@abc.abstractmethod<br>def get_tts_model(self, model_name: str | None) -> TTSModel:<br>    """Get a text-to-speech model by name."""<br>``` |