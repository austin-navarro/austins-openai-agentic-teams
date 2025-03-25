[Skip to content](https://openai.github.io/openai-agents-python/ref/voice/models/openai_tts/#openai-tts)

# `OpenAI TTS`

### OpenAITTSModel

Bases: `TTSModel`

A text-to-speech model for OpenAI.

Source code in `src/agents/voice/models/openai_tts.py`

|     |     |
| --- | --- |
| ```<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>``` | ```md-code__content<br>class OpenAITTSModel(TTSModel):<br>    """A text-to-speech model for OpenAI."""<br>    def __init__(<br>        self,<br>        model: str,<br>        openai_client: AsyncOpenAI,<br>    ):<br>        """Create a new OpenAI text-to-speech model.<br>        Args:<br>            model: The name of the model to use.<br>            openai_client: The OpenAI client to use.<br>        """<br>        self.model = model<br>        self._client = openai_client<br>    @property<br>    def model_name(self) -> str:<br>        return self.model<br>    async def run(self, text: str, settings: TTSModelSettings) -> AsyncIterator[bytes]:<br>        """Run the text-to-speech model.<br>        Args:<br>            text: The text to convert to speech.<br>            settings: The settings to use for the text-to-speech model.<br>        Returns:<br>            An iterator of audio chunks.<br>        """<br>        response = self._client.audio.speech.with_streaming_response.create(<br>            model=self.model,<br>            voice=settings.voice or DEFAULT_VOICE,<br>            input=text,<br>            response_format="pcm",<br>            extra_body={<br>                "instructions": settings.instructions,<br>            },<br>        )<br>        async with response as stream:<br>            async for chunk in stream.iter_bytes(chunk_size=1024):<br>                yield chunk<br>``` |

#### \_\_init\_\_

```md-code__content
__init__(model: str, openai_client: AsyncOpenAI)

```

Create a new OpenAI text-to-speech model.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `model` | `str` | The name of the model to use. | _required_ |
| `openai_client` | `AsyncOpenAI` | The OpenAI client to use. | _required_ |

Source code in `src/agents/voice/models/openai_tts.py`

|     |     |
| --- | --- |
| ```<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    model: str,<br>    openai_client: AsyncOpenAI,<br>):<br>    """Create a new OpenAI text-to-speech model.<br>    Args:<br>        model: The name of the model to use.<br>        openai_client: The OpenAI client to use.<br>    """<br>    self.model = model<br>    self._client = openai_client<br>``` |

#### run`async`

```md-code__content
run(
    text: str, settings: TTSModelSettings
) -> AsyncIterator[bytes]

```

Run the text-to-speech model.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `text` | `str` | The text to convert to speech. | _required_ |
| `settings` | `TTSModelSettings` | The settings to use for the text-to-speech model. | _required_ |

Returns:

| Type | Description |
| --- | --- |
| `AsyncIterator[bytes]` | An iterator of audio chunks. |

Source code in `src/agents/voice/models/openai_tts.py`

|     |     |
| --- | --- |
| ```<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>``` | ```md-code__content<br>async def run(self, text: str, settings: TTSModelSettings) -> AsyncIterator[bytes]:<br>    """Run the text-to-speech model.<br>    Args:<br>        text: The text to convert to speech.<br>        settings: The settings to use for the text-to-speech model.<br>    Returns:<br>        An iterator of audio chunks.<br>    """<br>    response = self._client.audio.speech.with_streaming_response.create(<br>        model=self.model,<br>        voice=settings.voice or DEFAULT_VOICE,<br>        input=text,<br>        response_format="pcm",<br>        extra_body={<br>            "instructions": settings.instructions,<br>        },<br>    )<br>    async with response as stream:<br>        async for chunk in stream.iter_bytes(chunk_size=1024):<br>            yield chunk<br>``` |