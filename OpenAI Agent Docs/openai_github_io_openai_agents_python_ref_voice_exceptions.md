[Skip to content](https://openai.github.io/openai-agents-python/ref/voice/exceptions/#exceptions)

# `Exceptions`

### STTWebsocketConnectionError

Bases: `AgentsException`

Exception raised when the STT websocket connection fails.

Source code in `src/agents/voice/exceptions.py`

|     |     |
| --- | --- |
| ```<br>4<br>5<br>6<br>7<br>8<br>``` | ```md-code__content<br>class STTWebsocketConnectionError(AgentsException):<br>    """Exception raised when the STT websocket connection fails."""<br>    def __init__(self, message: str):<br>        self.message = message<br>``` |