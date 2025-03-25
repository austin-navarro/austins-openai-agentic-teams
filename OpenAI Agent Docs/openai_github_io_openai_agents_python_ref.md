[Skip to content](https://openai.github.io/openai-agents-python/ref/#agents-module)

# Agents module

### set\_default\_openai\_key

```md-code__content
set_default_openai_key(
    key: str, use_for_tracing: bool = True
) -> None

```

Set the default OpenAI API key to use for LLM requests (and optionally tracing(). This is
only necessary if the OPENAI\_API\_KEY environment variable is not already set.

If provided, this key will be used instead of the OPENAI\_API\_KEY environment variable.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `key` | `str` | The OpenAI key to use. | _required_ |
| `use_for_tracing` | `bool` | Whether to also use this key to send traces to OpenAI. Defaults to True<br>If False, you'll either need to set the OPENAI\_API\_KEY environment variable or call<br>set\_tracing\_export\_api\_key() with the API key you want to use for tracing. | `True` |

Source code in `src/agents/__init__.py`

|     |     |
| --- | --- |
| ```<br>103<br>104<br>105<br>106<br>107<br>108<br>109<br>110<br>111<br>112<br>113<br>114<br>115<br>``` | ```md-code__content<br>def set_default_openai_key(key: str, use_for_tracing: bool = True) -> None:<br>    """Set the default OpenAI API key to use for LLM requests (and optionally tracing(). This is<br>    only necessary if the OPENAI_API_KEY environment variable is not already set.<br>    If provided, this key will be used instead of the OPENAI_API_KEY environment variable.<br>    Args:<br>        key: The OpenAI key to use.<br>        use_for_tracing: Whether to also use this key to send traces to OpenAI. Defaults to True<br>            If False, you'll either need to set the OPENAI_API_KEY environment variable or call<br>            set_tracing_export_api_key() with the API key you want to use for tracing.<br>    """<br>    _config.set_default_openai_key(key, use_for_tracing)<br>``` |

### set\_default\_openai\_client

```md-code__content
set_default_openai_client(
    client: AsyncOpenAI, use_for_tracing: bool = True
) -> None

```

Set the default OpenAI client to use for LLM requests and/or tracing. If provided, this
client will be used instead of the default OpenAI client.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `client` | `AsyncOpenAI` | The OpenAI client to use. | _required_ |
| `use_for_tracing` | `bool` | Whether to use the API key from this client for uploading traces. If False,<br>you'll either need to set the OPENAI\_API\_KEY environment variable or call<br>set\_tracing\_export\_api\_key() with the API key you want to use for tracing. | `True` |

Source code in `src/agents/__init__.py`

|     |     |
| --- | --- |
| ```<br>118<br>119<br>120<br>121<br>122<br>123<br>124<br>125<br>126<br>127<br>128<br>``` | ```md-code__content<br>def set_default_openai_client(client: AsyncOpenAI, use_for_tracing: bool = True) -> None:<br>    """Set the default OpenAI client to use for LLM requests and/or tracing. If provided, this<br>    client will be used instead of the default OpenAI client.<br>    Args:<br>        client: The OpenAI client to use.<br>        use_for_tracing: Whether to use the API key from this client for uploading traces. If False,<br>            you'll either need to set the OPENAI_API_KEY environment variable or call<br>            set_tracing_export_api_key() with the API key you want to use for tracing.<br>    """<br>    _config.set_default_openai_client(client, use_for_tracing)<br>``` |

### set\_default\_openai\_api

```md-code__content
set_default_openai_api(
    api: Literal["chat_completions", "responses"],
) -> None

```

Set the default API to use for OpenAI LLM requests. By default, we will use the responses API
but you can set this to use the chat completions API instead.

Source code in `src/agents/__init__.py`

|     |     |
| --- | --- |
| ```<br>131<br>132<br>133<br>134<br>135<br>``` | ```md-code__content<br>def set_default_openai_api(api: Literal["chat_completions", "responses"]) -> None:<br>    """Set the default API to use for OpenAI LLM requests. By default, we will use the responses API<br>    but you can set this to use the chat completions API instead.<br>    """<br>    _config.set_default_openai_api(api)<br>``` |

### set\_tracing\_export\_api\_key

```md-code__content
set_tracing_export_api_key(api_key: str) -> None

```

Set the OpenAI API key for the backend exporter.

Source code in `src/agents/tracing/__init__.py`

|     |     |
| --- | --- |
| ```<br> 96<br> 97<br> 98<br> 99<br>100<br>``` | ```md-code__content<br>def set_tracing_export_api_key(api_key: str) -> None:<br>    """<br>    Set the OpenAI API key for the backend exporter.<br>    """<br>    default_exporter().set_api_key(api_key)<br>``` |

### set\_tracing\_disabled

```md-code__content
set_tracing_disabled(disabled: bool) -> None

```

Set whether tracing is globally disabled.

Source code in `src/agents/tracing/__init__.py`

|     |     |
| --- | --- |
| ```<br>89<br>90<br>91<br>92<br>93<br>``` | ```md-code__content<br>def set_tracing_disabled(disabled: bool) -> None:<br>    """<br>    Set whether tracing is globally disabled.<br>    """<br>    GLOBAL_TRACE_PROVIDER.set_disabled(disabled)<br>``` |

### set\_trace\_processors

```md-code__content
set_trace_processors(
    processors: list[TracingProcessor],
) -> None

```

Set the list of trace processors. This will replace the current list of processors.

Source code in `src/agents/tracing/__init__.py`

|     |     |
| --- | --- |
| ```<br>82<br>83<br>84<br>85<br>86<br>``` | ```md-code__content<br>def set_trace_processors(processors: list[TracingProcessor]) -> None:<br>    """<br>    Set the list of trace processors. This will replace the current list of processors.<br>    """<br>    GLOBAL_TRACE_PROVIDER.set_processors(processors)<br>``` |

### enable\_verbose\_stdout\_logging

```md-code__content
enable_verbose_stdout_logging()

```

Enables verbose logging to stdout. This is useful for debugging.

Source code in `src/agents/__init__.py`

|     |     |
| --- | --- |
| ```<br>138<br>139<br>140<br>141<br>142<br>``` | ```md-code__content<br>def enable_verbose_stdout_logging():<br>    """Enables verbose logging to stdout. This is useful for debugging."""<br>    logger = logging.getLogger("openai.agents")<br>    logger.setLevel(logging.DEBUG)<br>    logger.addHandler(logging.StreamHandler(sys.stdout))<br>``` |