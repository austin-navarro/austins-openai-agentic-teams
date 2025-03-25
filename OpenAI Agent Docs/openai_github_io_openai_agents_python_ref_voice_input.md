[Skip to content](https://openai.github.io/openai-agents-python/ref/voice/input/#input)

# `Input`

### AudioInput`dataclass`

Static audio to be used as input for the VoicePipeline.

Source code in `src/agents/voice/input.py`

|     |     |
| --- | --- |
| ```<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>71<br>``` | ```md-code__content<br>@dataclass<br>class AudioInput:<br>    """Static audio to be used as input for the VoicePipeline."""<br>    buffer: npt.NDArray[np.int16 | np.float32]<br>    """<br>    A buffer containing the audio data for the agent. Must be a numpy array of int16 or float32.<br>    """<br>    frame_rate: int = DEFAULT_SAMPLE_RATE<br>    """The sample rate of the audio data. Defaults to 24000."""<br>    sample_width: int = 2<br>    """The sample width of the audio data. Defaults to 2."""<br>    channels: int = 1<br>    """The number of channels in the audio data. Defaults to 1."""<br>    def to_audio_file(self) -> tuple[str, io.BytesIO, str]:<br>        """Returns a tuple of (filename, bytes, content_type)"""<br>        return _buffer_to_audio_file(self.buffer, self.frame_rate, self.sample_width, self.channels)<br>    def to_base64(self) -> str:<br>        """Returns the audio data as a base64 encoded string."""<br>        if self.buffer.dtype == np.float32:<br>            # convert to int16<br>            self.buffer = np.clip(self.buffer, -1.0, 1.0)<br>            self.buffer = (self.buffer * 32767).astype(np.int16)<br>        elif self.buffer.dtype != np.int16:<br>            raise UserError("Buffer must be a numpy array of int16 or float32")<br>        return base64.b64encode(self.buffer.tobytes()).decode("utf-8")<br>``` |

#### buffer`instance-attribute`

```md-code__content
buffer: NDArray[int16 | float32]

```

A buffer containing the audio data for the agent. Must be a numpy array of int16 or float32.

#### frame\_rate`class-attribute``instance-attribute`

```md-code__content
frame_rate: int = DEFAULT_SAMPLE_RATE

```

The sample rate of the audio data. Defaults to 24000.

#### sample\_width`class-attribute``instance-attribute`

```md-code__content
sample_width: int = 2

```

The sample width of the audio data. Defaults to 2.

#### channels`class-attribute``instance-attribute`

```md-code__content
channels: int = 1

```

The number of channels in the audio data. Defaults to 1.

#### to\_audio\_file

```md-code__content
to_audio_file() -> tuple[str, BytesIO, str]

```

Returns a tuple of (filename, bytes, content\_type)

Source code in `src/agents/voice/input.py`

|     |     |
| --- | --- |
| ```<br>58<br>59<br>60<br>``` | ```md-code__content<br>def to_audio_file(self) -> tuple[str, io.BytesIO, str]:<br>    """Returns a tuple of (filename, bytes, content_type)"""<br>    return _buffer_to_audio_file(self.buffer, self.frame_rate, self.sample_width, self.channels)<br>``` |

#### to\_base64

```md-code__content
to_base64() -> str

```

Returns the audio data as a base64 encoded string.

Source code in `src/agents/voice/input.py`

|     |     |
| --- | --- |
| ```<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>71<br>``` | ```md-code__content<br>def to_base64(self) -> str:<br>    """Returns the audio data as a base64 encoded string."""<br>    if self.buffer.dtype == np.float32:<br>        # convert to int16<br>        self.buffer = np.clip(self.buffer, -1.0, 1.0)<br>        self.buffer = (self.buffer * 32767).astype(np.int16)<br>    elif self.buffer.dtype != np.int16:<br>        raise UserError("Buffer must be a numpy array of int16 or float32")<br>    return base64.b64encode(self.buffer.tobytes()).decode("utf-8")<br>``` |

### StreamedAudioInput

Audio input represented as a stream of audio data. You can pass this to the `VoicePipeline`
and then push audio data into the queue using the `add_audio` method.

Source code in `src/agents/voice/input.py`

|     |     |
| --- | --- |
| ```<br>74<br>75<br>76<br>77<br>78<br>79<br>80<br>81<br>82<br>83<br>84<br>85<br>86<br>87<br>88<br>``` | ```md-code__content<br>class StreamedAudioInput:<br>    """Audio input represented as a stream of audio data. You can pass this to the `VoicePipeline`<br>    and then push audio data into the queue using the `add_audio` method.<br>    """<br>    def __init__(self):<br>        self.queue: asyncio.Queue[npt.NDArray[np.int16 | np.float32]] = asyncio.Queue()<br>    async def add_audio(self, audio: npt.NDArray[np.int16 | np.float32]):<br>        """Adds more audio data to the stream.<br>        Args:<br>            audio: The audio data to add. Must be a numpy array of int16 or float32.<br>        """<br>        await self.queue.put(audio)<br>``` |

#### add\_audio`async`

```md-code__content
add_audio(audio: NDArray[int16 | float32])

```

Adds more audio data to the stream.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `audio` | `NDArray[int16 | float32]` | The audio data to add. Must be a numpy array of int16 or float32. | _required_ |

Source code in `src/agents/voice/input.py`

|     |     |
| --- | --- |
| ```<br>82<br>83<br>84<br>85<br>86<br>87<br>88<br>``` | ```md-code__content<br>async def add_audio(self, audio: npt.NDArray[np.int16 | np.float32]):<br>    """Adds more audio data to the stream.<br>    Args:<br>        audio: The audio data to add. Must be a numpy array of int16 or float32.<br>    """<br>    await self.queue.put(audio)<br>``` |