[Skip to content](https://openai.github.io/openai-agents-python/ref/voice/models/openai_provider/#openaivoicemodelprovider)

# `OpenAIVoiceModelProvider`

### OpenAIVoiceModelProvider

Bases: `VoiceModelProvider`

A voice model provider that uses OpenAI models.

Source code in `src/agents/voice/models/openai_model_provider.py`

|     |     |
| --- | --- |
| ```<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>71<br>72<br>73<br>74<br>75<br>76<br>77<br>78<br>79<br>80<br>81<br>82<br>83<br>84<br>85<br>86<br>87<br>88<br>89<br>90<br>91<br>92<br>93<br>94<br>95<br>96<br>97<br>``` | ```md-code__content<br>class OpenAIVoiceModelProvider(VoiceModelProvider):<br>    """A voice model provider that uses OpenAI models."""<br>    def __init__(<br>        self,<br>        *,<br>        api_key: str | None = None,<br>        base_url: str | None = None,<br>        openai_client: AsyncOpenAI | None = None,<br>        organization: str | None = None,<br>        project: str | None = None,<br>    ) -> None:<br>        """Create a new OpenAI voice model provider.<br>        Args:<br>            api_key: The API key to use for the OpenAI client. If not provided, we will use the<br>                default API key.<br>            base_url: The base URL to use for the OpenAI client. If not provided, we will use the<br>                default base URL.<br>            openai_client: An optional OpenAI client to use. If not provided, we will create a new<br>                OpenAI client using the api_key and base_url.<br>            organization: The organization to use for the OpenAI client.<br>            project: The project to use for the OpenAI client.<br>        """<br>        if openai_client is not None:<br>            assert api_key is None and base_url is None, (<br>                "Don't provide api_key or base_url if you provide openai_client"<br>            )<br>            self._client: AsyncOpenAI | None = openai_client<br>        else:<br>            self._client = None<br>            self._stored_api_key = api_key<br>            self._stored_base_url = base_url<br>            self._stored_organization = organization<br>            self._stored_project = project<br>    # We lazy load the client in case you never actually use OpenAIProvider(). Otherwise<br>    # AsyncOpenAI() raises an error if you don't have an API key set.<br>    def _get_client(self) -> AsyncOpenAI:<br>        if self._client is None:<br>            self._client = _openai_shared.get_default_openai_client() or AsyncOpenAI(<br>                api_key=self._stored_api_key or _openai_shared.get_default_openai_key(),<br>                base_url=self._stored_base_url,<br>                organization=self._stored_organization,<br>                project=self._stored_project,<br>                http_client=shared_http_client(),<br>            )<br>        return self._client<br>    def get_stt_model(self, model_name: str | None) -> STTModel:<br>        """Get a speech-to-text model by name.<br>        Args:<br>            model_name: The name of the model to get.<br>        Returns:<br>            The speech-to-text model.<br>        """<br>        return OpenAISTTModel(model_name or DEFAULT_STT_MODEL, self._get_client())<br>    def get_tts_model(self, model_name: str | None) -> TTSModel:<br>        """Get a text-to-speech model by name.<br>        Args:<br>            model_name: The name of the model to get.<br>        Returns:<br>            The text-to-speech model.<br>        """<br>        return OpenAITTSModel(model_name or DEFAULT_TTS_MODEL, self._get_client())<br>``` |

#### \_\_init\_\_

```md-code__content
__init__(
    *,
    api_key: str | None = None,
    base_url: str | None = None,
    openai_client: AsyncOpenAI | None = None,
    organization: str | None = None,
    project: str | None = None,
) -> None

```

Create a new OpenAI voice model provider.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `api_key` | `str | None` | The API key to use for the OpenAI client. If not provided, we will use the<br>default API key. | `None` |
| `base_url` | `str | None` | The base URL to use for the OpenAI client. If not provided, we will use the<br>default base URL. | `None` |
| `openai_client` | `AsyncOpenAI | None` | An optional OpenAI client to use. If not provided, we will create a new<br>OpenAI client using the api\_key and base\_url. | `None` |
| `organization` | `str | None` | The organization to use for the OpenAI client. | `None` |
| `project` | `str | None` | The project to use for the OpenAI client. | `None` |

Source code in `src/agents/voice/models/openai_model_provider.py`

|     |     |
| --- | --- |
| ```<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    *,<br>    api_key: str | None = None,<br>    base_url: str | None = None,<br>    openai_client: AsyncOpenAI | None = None,<br>    organization: str | None = None,<br>    project: str | None = None,<br>) -> None:<br>    """Create a new OpenAI voice model provider.<br>    Args:<br>        api_key: The API key to use for the OpenAI client. If not provided, we will use the<br>            default API key.<br>        base_url: The base URL to use for the OpenAI client. If not provided, we will use the<br>            default base URL.<br>        openai_client: An optional OpenAI client to use. If not provided, we will create a new<br>            OpenAI client using the api_key and base_url.<br>        organization: The organization to use for the OpenAI client.<br>        project: The project to use for the OpenAI client.<br>    """<br>    if openai_client is not None:<br>        assert api_key is None and base_url is None, (<br>            "Don't provide api_key or base_url if you provide openai_client"<br>        )<br>        self._client: AsyncOpenAI | None = openai_client<br>    else:<br>        self._client = None<br>        self._stored_api_key = api_key<br>        self._stored_base_url = base_url<br>        self._stored_organization = organization<br>        self._stored_project = project<br>``` |

#### get\_stt\_model

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

Source code in `src/agents/voice/models/openai_model_provider.py`

|     |     |
| --- | --- |
| ```<br>77<br>78<br>79<br>80<br>81<br>82<br>83<br>84<br>85<br>86<br>``` | ```md-code__content<br>def get_stt_model(self, model_name: str | None) -> STTModel:<br>    """Get a speech-to-text model by name.<br>    Args:<br>        model_name: The name of the model to get.<br>    Returns:<br>        The speech-to-text model.<br>    """<br>    return OpenAISTTModel(model_name or DEFAULT_STT_MODEL, self._get_client())<br>``` |

#### get\_tts\_model

```md-code__content
get_tts_model(model_name: str | None) -> TTSModel

```

Get a text-to-speech model by name.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `model_name` | `str | None` | The name of the model to get. | _required_ |

Returns:

| Type | Description |
| --- | --- |
| `TTSModel` | The text-to-speech model. |

Source code in `src/agents/voice/models/openai_model_provider.py`

|     |     |
| --- | --- |
| ```<br>88<br>89<br>90<br>91<br>92<br>93<br>94<br>95<br>96<br>97<br>``` | ```md-code__content<br>def get_tts_model(self, model_name: str | None) -> TTSModel:<br>    """Get a text-to-speech model by name.<br>    Args:<br>        model_name: The name of the model to get.<br>    Returns:<br>        The text-to-speech model.<br>    """<br>    return OpenAITTSModel(model_name or DEFAULT_TTS_MODEL, self._get_client())<br>``` |