[Skip to content](https://openai.github.io/openai-agents-python/ref/tracing/create/#creating-tracesspans)

# `Creating traces/spans`

### trace

```md-code__content
trace(
    workflow_name: str,
    trace_id: str | None = None,
    group_id: str | None = None,
    metadata: dict[str, Any] | None = None,
    disabled: bool = False,
) -> Trace

```

Create a new trace. The trace will not be started automatically; you should either use
it as a context manager ( `with trace(...):`) or call `trace.start()` \+ `trace.finish()`
manually.

In addition to the workflow name and optional grouping identifier, you can provide
an arbitrary metadata dictionary to attach additional user-defined information to
the trace.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `workflow_name` | `str` | The name of the logical app or workflow. For example, you might provide<br>"code\_bot" for a coding agent, or "customer\_support\_agent" for a customer support agent. | _required_ |
| `trace_id` | `str | None` | The ID of the trace. Optional. If not provided, we will generate an ID. We<br>recommend using `util.gen_trace_id()` to generate a trace ID, to guarantee that IDs are<br>correctly formatted. | `None` |
| `group_id` | `str | None` | Optional grouping identifier to link multiple traces from the same conversation<br>or process. For instance, you might use a chat thread ID. | `None` |
| `metadata` | `dict[str, Any] | None` | Optional dictionary of additional metadata to attach to the trace. | `None` |
| `disabled` | `bool` | If True, we will return a Trace but the Trace will not be recorded. This will<br>not be checked if there's an existing trace and `even_if_trace_running` is True. | `False` |

Returns:

| Type | Description |
| --- | --- |
| `Trace` | The newly created trace object. |

Source code in `src/agents/tracing/create.py`

|     |     |
| --- | --- |
| ```<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>66<br>67<br>68<br>69<br>70<br>``` | ```md-code__content<br>def trace(<br>    workflow_name: str,<br>    trace_id: str | None = None,<br>    group_id: str | None = None,<br>    metadata: dict[str, Any] | None = None,<br>    disabled: bool = False,<br>) -> Trace:<br>    """<br>    Create a new trace. The trace will not be started automatically; you should either use<br>    it as a context manager (`with trace(...):`) or call `trace.start()` + `trace.finish()`<br>    manually.<br>    In addition to the workflow name and optional grouping identifier, you can provide<br>    an arbitrary metadata dictionary to attach additional user-defined information to<br>    the trace.<br>    Args:<br>        workflow_name: The name of the logical app or workflow. For example, you might provide<br>            "code_bot" for a coding agent, or "customer_support_agent" for a customer support agent.<br>        trace_id: The ID of the trace. Optional. If not provided, we will generate an ID. We<br>            recommend using `util.gen_trace_id()` to generate a trace ID, to guarantee that IDs are<br>            correctly formatted.<br>        group_id: Optional grouping identifier to link multiple traces from the same conversation<br>            or process. For instance, you might use a chat thread ID.<br>        metadata: Optional dictionary of additional metadata to attach to the trace.<br>        disabled: If True, we will return a Trace but the Trace will not be recorded. This will<br>            not be checked if there's an existing trace and `even_if_trace_running` is True.<br>    Returns:<br>        The newly created trace object.<br>    """<br>    current_trace = GLOBAL_TRACE_PROVIDER.get_current_trace()<br>    if current_trace:<br>        logger.warning(<br>            "Trace already exists. Creating a new trace, but this is probably a mistake."<br>        )<br>    return GLOBAL_TRACE_PROVIDER.create_trace(<br>        name=workflow_name,<br>        trace_id=trace_id,<br>        group_id=group_id,<br>        metadata=metadata,<br>        disabled=disabled,<br>    )<br>``` |

### get\_current\_trace

```md-code__content
get_current_trace() -> Trace | None

```

Returns the currently active trace, if present.

Source code in `src/agents/tracing/create.py`

|     |     |
| --- | --- |
| ```<br>73<br>74<br>75<br>``` | ```md-code__content<br>def get_current_trace() -> Trace | None:<br>    """Returns the currently active trace, if present."""<br>    return GLOBAL_TRACE_PROVIDER.get_current_trace()<br>``` |

### get\_current\_span

```md-code__content
get_current_span() -> Span[Any] | None

```

Returns the currently active span, if present.

Source code in `src/agents/tracing/create.py`

|     |     |
| --- | --- |
| ```<br>78<br>79<br>80<br>``` | ```md-code__content<br>def get_current_span() -> Span[Any] | None:<br>    """Returns the currently active span, if present."""<br>    return GLOBAL_TRACE_PROVIDER.get_current_span()<br>``` |

### agent\_span

```md-code__content
agent_span(
    name: str,
    handoffs: list[str] | None = None,
    tools: list[str] | None = None,
    output_type: str | None = None,
    span_id: str | None = None,
    parent: Trace | Span[Any] | None = None,
    disabled: bool = False,
) -> Span[AgentSpanData]

```

Create a new agent span. The span will not be started automatically, you should either do
`with agent_span() ...` or call `span.start()` \+ `span.finish()` manually.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | `str` | The name of the agent. | _required_ |
| `handoffs` | `list[str] | None` | Optional list of agent names to which this agent could hand off control. | `None` |
| `tools` | `list[str] | None` | Optional list of tool names available to this agent. | `None` |
| `output_type` | `str | None` | Optional name of the output type produced by the agent. | `None` |
| `span_id` | `str | None` | The ID of the span. Optional. If not provided, we will generate an ID. We<br>recommend using `util.gen_span_id()` to generate a span ID, to guarantee that IDs are<br>correctly formatted. | `None` |
| `parent` | `Trace | Span[Any] | None` | The parent span or trace. If not provided, we will automatically use the current<br>trace/span as the parent. | `None` |
| `disabled` | `bool` | If True, we will return a Span but the Span will not be recorded. | `False` |

Returns:

| Type | Description |
| --- | --- |
| `Span[AgentSpanData]` | The newly created agent span. |

Source code in `src/agents/tracing/create.py`

|     |     |
| --- | --- |
| ```<br> 83<br> 84<br> 85<br> 86<br> 87<br> 88<br> 89<br> 90<br> 91<br> 92<br> 93<br> 94<br> 95<br> 96<br> 97<br> 98<br> 99<br>100<br>101<br>102<br>103<br>104<br>105<br>106<br>107<br>108<br>109<br>110<br>111<br>112<br>113<br>114<br>115<br>``` | ```md-code__content<br>def agent_span(<br>    name: str,<br>    handoffs: list[str] | None = None,<br>    tools: list[str] | None = None,<br>    output_type: str | None = None,<br>    span_id: str | None = None,<br>    parent: Trace | Span[Any] | None = None,<br>    disabled: bool = False,<br>) -> Span[AgentSpanData]:<br>    """Create a new agent span. The span will not be started automatically, you should either do<br>    `with agent_span() ...` or call `span.start()` + `span.finish()` manually.<br>    Args:<br>        name: The name of the agent.<br>        handoffs: Optional list of agent names to which this agent could hand off control.<br>        tools: Optional list of tool names available to this agent.<br>        output_type: Optional name of the output type produced by the agent.<br>        span_id: The ID of the span. Optional. If not provided, we will generate an ID. We<br>            recommend using `util.gen_span_id()` to generate a span ID, to guarantee that IDs are<br>            correctly formatted.<br>        parent: The parent span or trace. If not provided, we will automatically use the current<br>            trace/span as the parent.<br>        disabled: If True, we will return a Span but the Span will not be recorded.<br>    Returns:<br>        The newly created agent span.<br>    """<br>    return GLOBAL_TRACE_PROVIDER.create_span(<br>        span_data=AgentSpanData(name=name, handoffs=handoffs, tools=tools, output_type=output_type),<br>        span_id=span_id,<br>        parent=parent,<br>        disabled=disabled,<br>    )<br>``` |

### function\_span

```md-code__content
function_span(
    name: str,
    input: str | None = None,
    output: str | None = None,
    span_id: str | None = None,
    parent: Trace | Span[Any] | None = None,
    disabled: bool = False,
) -> Span[FunctionSpanData]

```

Create a new function span. The span will not be started automatically, you should either do
`with function_span() ...` or call `span.start()` \+ `span.finish()` manually.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | `str` | The name of the function. | _required_ |
| `input` | `str | None` | The input to the function. | `None` |
| `output` | `str | None` | The output of the function. | `None` |
| `span_id` | `str | None` | The ID of the span. Optional. If not provided, we will generate an ID. We<br>recommend using `util.gen_span_id()` to generate a span ID, to guarantee that IDs are<br>correctly formatted. | `None` |
| `parent` | `Trace | Span[Any] | None` | The parent span or trace. If not provided, we will automatically use the current<br>trace/span as the parent. | `None` |
| `disabled` | `bool` | If True, we will return a Span but the Span will not be recorded. | `False` |

Returns:

| Type | Description |
| --- | --- |
| `Span[FunctionSpanData]` | The newly created function span. |

Source code in `src/agents/tracing/create.py`

|     |     |
| --- | --- |
| ```<br>118<br>119<br>120<br>121<br>122<br>123<br>124<br>125<br>126<br>127<br>128<br>129<br>130<br>131<br>132<br>133<br>134<br>135<br>136<br>137<br>138<br>139<br>140<br>141<br>142<br>143<br>144<br>145<br>146<br>147<br>148<br>``` | ```md-code__content<br>def function_span(<br>    name: str,<br>    input: str | None = None,<br>    output: str | None = None,<br>    span_id: str | None = None,<br>    parent: Trace | Span[Any] | None = None,<br>    disabled: bool = False,<br>) -> Span[FunctionSpanData]:<br>    """Create a new function span. The span will not be started automatically, you should either do<br>    `with function_span() ...` or call `span.start()` + `span.finish()` manually.<br>    Args:<br>        name: The name of the function.<br>        input: The input to the function.<br>        output: The output of the function.<br>        span_id: The ID of the span. Optional. If not provided, we will generate an ID. We<br>            recommend using `util.gen_span_id()` to generate a span ID, to guarantee that IDs are<br>            correctly formatted.<br>        parent: The parent span or trace. If not provided, we will automatically use the current<br>            trace/span as the parent.<br>        disabled: If True, we will return a Span but the Span will not be recorded.<br>    Returns:<br>        The newly created function span.<br>    """<br>    return GLOBAL_TRACE_PROVIDER.create_span(<br>        span_data=FunctionSpanData(name=name, input=input, output=output),<br>        span_id=span_id,<br>        parent=parent,<br>        disabled=disabled,<br>    )<br>``` |

### generation\_span

```md-code__content
generation_span(
    input: Sequence[Mapping[str, Any]] | None = None,
    output: Sequence[Mapping[str, Any]] | None = None,
    model: str | None = None,
    model_config: Mapping[str, Any] | None = None,
    usage: dict[str, Any] | None = None,
    span_id: str | None = None,
    parent: Trace | Span[Any] | None = None,
    disabled: bool = False,
) -> Span[GenerationSpanData]

```

Create a new generation span. The span will not be started automatically, you should either
do `with generation_span() ...` or call `span.start()` \+ `span.finish()` manually.

This span captures the details of a model generation, including the
input message sequence, any generated outputs, the model name and
configuration, and usage data. If you only need to capture a model
response identifier, use `response_span()` instead.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `input` | `Sequence[Mapping[str, Any]] | None` | The sequence of input messages sent to the model. | `None` |
| `output` | `Sequence[Mapping[str, Any]] | None` | The sequence of output messages received from the model. | `None` |
| `model` | `str | None` | The model identifier used for the generation. | `None` |
| `model_config` | `Mapping[str, Any] | None` | The model configuration (hyperparameters) used. | `None` |
| `usage` | `dict[str, Any] | None` | A dictionary of usage information (input tokens, output tokens, etc.). | `None` |
| `span_id` | `str | None` | The ID of the span. Optional. If not provided, we will generate an ID. We<br>recommend using `util.gen_span_id()` to generate a span ID, to guarantee that IDs are<br>correctly formatted. | `None` |
| `parent` | `Trace | Span[Any] | None` | The parent span or trace. If not provided, we will automatically use the current<br>trace/span as the parent. | `None` |
| `disabled` | `bool` | If True, we will return a Span but the Span will not be recorded. | `False` |

Returns:

| Type | Description |
| --- | --- |
| `Span[GenerationSpanData]` | The newly created generation span. |

Source code in `src/agents/tracing/create.py`

|     |     |
| --- | --- |
| ```<br>151<br>152<br>153<br>154<br>155<br>156<br>157<br>158<br>159<br>160<br>161<br>162<br>163<br>164<br>165<br>166<br>167<br>168<br>169<br>170<br>171<br>172<br>173<br>174<br>175<br>176<br>177<br>178<br>179<br>180<br>181<br>182<br>183<br>184<br>185<br>186<br>187<br>188<br>189<br>190<br>191<br>192<br>193<br>194<br>195<br>196<br>``` | ```md-code__content<br>def generation_span(<br>    input: Sequence[Mapping[str, Any]] | None = None,<br>    output: Sequence[Mapping[str, Any]] | None = None,<br>    model: str | None = None,<br>    model_config: Mapping[str, Any] | None = None,<br>    usage: dict[str, Any] | None = None,<br>    span_id: str | None = None,<br>    parent: Trace | Span[Any] | None = None,<br>    disabled: bool = False,<br>) -> Span[GenerationSpanData]:<br>    """Create a new generation span. The span will not be started automatically, you should either<br>    do `with generation_span() ...` or call `span.start()` + `span.finish()` manually.<br>    This span captures the details of a model generation, including the<br>    input message sequence, any generated outputs, the model name and<br>    configuration, and usage data. If you only need to capture a model<br>    response identifier, use `response_span()` instead.<br>    Args:<br>        input: The sequence of input messages sent to the model.<br>        output: The sequence of output messages received from the model.<br>        model: The model identifier used for the generation.<br>        model_config: The model configuration (hyperparameters) used.<br>        usage: A dictionary of usage information (input tokens, output tokens, etc.).<br>        span_id: The ID of the span. Optional. If not provided, we will generate an ID. We<br>            recommend using `util.gen_span_id()` to generate a span ID, to guarantee that IDs are<br>            correctly formatted.<br>        parent: The parent span or trace. If not provided, we will automatically use the current<br>            trace/span as the parent.<br>        disabled: If True, we will return a Span but the Span will not be recorded.<br>    Returns:<br>        The newly created generation span.<br>    """<br>    return GLOBAL_TRACE_PROVIDER.create_span(<br>        span_data=GenerationSpanData(<br>            input=input,<br>            output=output,<br>            model=model,<br>            model_config=model_config,<br>            usage=usage,<br>        ),<br>        span_id=span_id,<br>        parent=parent,<br>        disabled=disabled,<br>    )<br>``` |

### response\_span

```md-code__content
response_span(
    response: Response | None = None,
    span_id: str | None = None,
    parent: Trace | Span[Any] | None = None,
    disabled: bool = False,
) -> Span[ResponseSpanData]

```

Create a new response span. The span will not be started automatically, you should either do
`with response_span() ...` or call `span.start()` \+ `span.finish()` manually.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `response` | `Response | None` | The OpenAI Response object. | `None` |
| `span_id` | `str | None` | The ID of the span. Optional. If not provided, we will generate an ID. We<br>recommend using `util.gen_span_id()` to generate a span ID, to guarantee that IDs are<br>correctly formatted. | `None` |
| `parent` | `Trace | Span[Any] | None` | The parent span or trace. If not provided, we will automatically use the current<br>trace/span as the parent. | `None` |
| `disabled` | `bool` | If True, we will return a Span but the Span will not be recorded. | `False` |

Source code in `src/agents/tracing/create.py`

|     |     |
| --- | --- |
| ```<br>199<br>200<br>201<br>202<br>203<br>204<br>205<br>206<br>207<br>208<br>209<br>210<br>211<br>212<br>213<br>214<br>215<br>216<br>217<br>218<br>219<br>220<br>221<br>222<br>``` | ```md-code__content<br>def response_span(<br>    response: Response | None = None,<br>    span_id: str | None = None,<br>    parent: Trace | Span[Any] | None = None,<br>    disabled: bool = False,<br>) -> Span[ResponseSpanData]:<br>    """Create a new response span. The span will not be started automatically, you should either do<br>    `with response_span() ...` or call `span.start()` + `span.finish()` manually.<br>    Args:<br>        response: The OpenAI Response object.<br>        span_id: The ID of the span. Optional. If not provided, we will generate an ID. We<br>            recommend using `util.gen_span_id()` to generate a span ID, to guarantee that IDs are<br>            correctly formatted.<br>        parent: The parent span or trace. If not provided, we will automatically use the current<br>            trace/span as the parent.<br>        disabled: If True, we will return a Span but the Span will not be recorded.<br>    """<br>    return GLOBAL_TRACE_PROVIDER.create_span(<br>        span_data=ResponseSpanData(response=response),<br>        span_id=span_id,<br>        parent=parent,<br>        disabled=disabled,<br>    )<br>``` |

### handoff\_span

```md-code__content
handoff_span(
    from_agent: str | None = None,
    to_agent: str | None = None,
    span_id: str | None = None,
    parent: Trace | Span[Any] | None = None,
    disabled: bool = False,
) -> Span[HandoffSpanData]

```

Create a new handoff span. The span will not be started automatically, you should either do
`with handoff_span() ...` or call `span.start()` \+ `span.finish()` manually.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `from_agent` | `str | None` | The name of the agent that is handing off. | `None` |
| `to_agent` | `str | None` | The name of the agent that is receiving the handoff. | `None` |
| `span_id` | `str | None` | The ID of the span. Optional. If not provided, we will generate an ID. We<br>recommend using `util.gen_span_id()` to generate a span ID, to guarantee that IDs are<br>correctly formatted. | `None` |
| `parent` | `Trace | Span[Any] | None` | The parent span or trace. If not provided, we will automatically use the current<br>trace/span as the parent. | `None` |
| `disabled` | `bool` | If True, we will return a Span but the Span will not be recorded. | `False` |

Returns:

| Type | Description |
| --- | --- |
| `Span[HandoffSpanData]` | The newly created handoff span. |

Source code in `src/agents/tracing/create.py`

|     |     |
| --- | --- |
| ```<br>225<br>226<br>227<br>228<br>229<br>230<br>231<br>232<br>233<br>234<br>235<br>236<br>237<br>238<br>239<br>240<br>241<br>242<br>243<br>244<br>245<br>246<br>247<br>248<br>249<br>250<br>251<br>252<br>253<br>``` | ```md-code__content<br>def handoff_span(<br>    from_agent: str | None = None,<br>    to_agent: str | None = None,<br>    span_id: str | None = None,<br>    parent: Trace | Span[Any] | None = None,<br>    disabled: bool = False,<br>) -> Span[HandoffSpanData]:<br>    """Create a new handoff span. The span will not be started automatically, you should either do<br>    `with handoff_span() ...` or call `span.start()` + `span.finish()` manually.<br>    Args:<br>        from_agent: The name of the agent that is handing off.<br>        to_agent: The name of the agent that is receiving the handoff.<br>        span_id: The ID of the span. Optional. If not provided, we will generate an ID. We<br>            recommend using `util.gen_span_id()` to generate a span ID, to guarantee that IDs are<br>            correctly formatted.<br>        parent: The parent span or trace. If not provided, we will automatically use the current<br>            trace/span as the parent.<br>        disabled: If True, we will return a Span but the Span will not be recorded.<br>    Returns:<br>        The newly created handoff span.<br>    """<br>    return GLOBAL_TRACE_PROVIDER.create_span(<br>        span_data=HandoffSpanData(from_agent=from_agent, to_agent=to_agent),<br>        span_id=span_id,<br>        parent=parent,<br>        disabled=disabled,<br>    )<br>``` |

### custom\_span

```md-code__content
custom_span(
    name: str,
    data: dict[str, Any] | None = None,
    span_id: str | None = None,
    parent: Trace | Span[Any] | None = None,
    disabled: bool = False,
) -> Span[CustomSpanData]

```

Create a new custom span, to which you can add your own metadata. The span will not be
started automatically, you should either do `with custom_span() ...` or call
`span.start()` \+ `span.finish()` manually.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | `str` | The name of the custom span. | _required_ |
| `data` | `dict[str, Any] | None` | Arbitrary structured data to associate with the span. | `None` |
| `span_id` | `str | None` | The ID of the span. Optional. If not provided, we will generate an ID. We<br>recommend using `util.gen_span_id()` to generate a span ID, to guarantee that IDs are<br>correctly formatted. | `None` |
| `parent` | `Trace | Span[Any] | None` | The parent span or trace. If not provided, we will automatically use the current<br>trace/span as the parent. | `None` |
| `disabled` | `bool` | If True, we will return a Span but the Span will not be recorded. | `False` |

Returns:

| Type | Description |
| --- | --- |
| `Span[CustomSpanData]` | The newly created custom span. |

Source code in `src/agents/tracing/create.py`

|     |     |
| --- | --- |
| ```<br>256<br>257<br>258<br>259<br>260<br>261<br>262<br>263<br>264<br>265<br>266<br>267<br>268<br>269<br>270<br>271<br>272<br>273<br>274<br>275<br>276<br>277<br>278<br>279<br>280<br>281<br>282<br>283<br>284<br>285<br>``` | ```md-code__content<br>def custom_span(<br>    name: str,<br>    data: dict[str, Any] | None = None,<br>    span_id: str | None = None,<br>    parent: Trace | Span[Any] | None = None,<br>    disabled: bool = False,<br>) -> Span[CustomSpanData]:<br>    """Create a new custom span, to which you can add your own metadata. The span will not be<br>    started automatically, you should either do `with custom_span() ...` or call<br>    `span.start()` + `span.finish()` manually.<br>    Args:<br>        name: The name of the custom span.<br>        data: Arbitrary structured data to associate with the span.<br>        span_id: The ID of the span. Optional. If not provided, we will generate an ID. We<br>            recommend using `util.gen_span_id()` to generate a span ID, to guarantee that IDs are<br>            correctly formatted.<br>        parent: The parent span or trace. If not provided, we will automatically use the current<br>            trace/span as the parent.<br>        disabled: If True, we will return a Span but the Span will not be recorded.<br>    Returns:<br>        The newly created custom span.<br>    """<br>    return GLOBAL_TRACE_PROVIDER.create_span(<br>        span_data=CustomSpanData(name=name, data=data or {}),<br>        span_id=span_id,<br>        parent=parent,<br>        disabled=disabled,<br>    )<br>``` |

### guardrail\_span

```md-code__content
guardrail_span(
    name: str,
    triggered: bool = False,
    span_id: str | None = None,
    parent: Trace | Span[Any] | None = None,
    disabled: bool = False,
) -> Span[GuardrailSpanData]

```

Create a new guardrail span. The span will not be started automatically, you should either
do `with guardrail_span() ...` or call `span.start()` \+ `span.finish()` manually.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `name` | `str` | The name of the guardrail. | _required_ |
| `triggered` | `bool` | Whether the guardrail was triggered. | `False` |
| `span_id` | `str | None` | The ID of the span. Optional. If not provided, we will generate an ID. We<br>recommend using `util.gen_span_id()` to generate a span ID, to guarantee that IDs are<br>correctly formatted. | `None` |
| `parent` | `Trace | Span[Any] | None` | The parent span or trace. If not provided, we will automatically use the current<br>trace/span as the parent. | `None` |
| `disabled` | `bool` | If True, we will return a Span but the Span will not be recorded. | `False` |

Source code in `src/agents/tracing/create.py`

|     |     |
| --- | --- |
| ```<br>288<br>289<br>290<br>291<br>292<br>293<br>294<br>295<br>296<br>297<br>298<br>299<br>300<br>301<br>302<br>303<br>304<br>305<br>306<br>307<br>308<br>309<br>310<br>311<br>312<br>313<br>``` | ```md-code__content<br>def guardrail_span(<br>    name: str,<br>    triggered: bool = False,<br>    span_id: str | None = None,<br>    parent: Trace | Span[Any] | None = None,<br>    disabled: bool = False,<br>) -> Span[GuardrailSpanData]:<br>    """Create a new guardrail span. The span will not be started automatically, you should either<br>    do `with guardrail_span() ...` or call `span.start()` + `span.finish()` manually.<br>    Args:<br>        name: The name of the guardrail.<br>        triggered: Whether the guardrail was triggered.<br>        span_id: The ID of the span. Optional. If not provided, we will generate an ID. We<br>            recommend using `util.gen_span_id()` to generate a span ID, to guarantee that IDs are<br>            correctly formatted.<br>        parent: The parent span or trace. If not provided, we will automatically use the current<br>            trace/span as the parent.<br>        disabled: If True, we will return a Span but the Span will not be recorded.<br>    """<br>    return GLOBAL_TRACE_PROVIDER.create_span(<br>        span_data=GuardrailSpanData(name=name, triggered=triggered),<br>        span_id=span_id,<br>        parent=parent,<br>        disabled=disabled,<br>    )<br>``` |

### transcription\_span

```md-code__content
transcription_span(
    model: str | None = None,
    input: str | None = None,
    input_format: str | None = "pcm",
    output: str | None = None,
    model_config: Mapping[str, Any] | None = None,
    span_id: str | None = None,
    parent: Trace | Span[Any] | None = None,
    disabled: bool = False,
) -> Span[TranscriptionSpanData]

```

Create a new transcription span. The span will not be started automatically, you should
either do `with transcription_span() ...` or call `span.start()` \+ `span.finish()` manually.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `model` | `str | None` | The name of the model used for the speech-to-text. | `None` |
| `input` | `str | None` | The audio input of the speech-to-text transcription, as a base64 encoded string of<br>audio bytes. | `None` |
| `input_format` | `str | None` | The format of the audio input (defaults to "pcm"). | `'pcm'` |
| `output` | `str | None` | The output of the speech-to-text transcription. | `None` |
| `model_config` | `Mapping[str, Any] | None` | The model configuration (hyperparameters) used. | `None` |
| `span_id` | `str | None` | The ID of the span. Optional. If not provided, we will generate an ID. We<br>recommend using `util.gen_span_id()` to generate a span ID, to guarantee that IDs are<br>correctly formatted. | `None` |
| `parent` | `Trace | Span[Any] | None` | The parent span or trace. If not provided, we will automatically use the current<br>trace/span as the parent. | `None` |
| `disabled` | `bool` | If True, we will return a Span but the Span will not be recorded. | `False` |

Returns:

| Type | Description |
| --- | --- |
| `Span[TranscriptionSpanData]` | The newly created speech-to-text span. |

Source code in `src/agents/tracing/create.py`

|     |     |
| --- | --- |
| ```<br>316<br>317<br>318<br>319<br>320<br>321<br>322<br>323<br>324<br>325<br>326<br>327<br>328<br>329<br>330<br>331<br>332<br>333<br>334<br>335<br>336<br>337<br>338<br>339<br>340<br>341<br>342<br>343<br>344<br>345<br>346<br>347<br>348<br>349<br>350<br>351<br>352<br>353<br>354<br>355<br>356<br>357<br>``` | ```md-code__content<br>def transcription_span(<br>    model: str | None = None,<br>    input: str | None = None,<br>    input_format: str | None = "pcm",<br>    output: str | None = None,<br>    model_config: Mapping[str, Any] | None = None,<br>    span_id: str | None = None,<br>    parent: Trace | Span[Any] | None = None,<br>    disabled: bool = False,<br>) -> Span[TranscriptionSpanData]:<br>    """Create a new transcription span. The span will not be started automatically, you should<br>    either do `with transcription_span() ...` or call `span.start()` + `span.finish()` manually.<br>    Args:<br>        model: The name of the model used for the speech-to-text.<br>        input: The audio input of the speech-to-text transcription, as a base64 encoded string of<br>            audio bytes.<br>        input_format: The format of the audio input (defaults to "pcm").<br>        output: The output of the speech-to-text transcription.<br>        model_config: The model configuration (hyperparameters) used.<br>        span_id: The ID of the span. Optional. If not provided, we will generate an ID. We<br>            recommend using `util.gen_span_id()` to generate a span ID, to guarantee that IDs are<br>            correctly formatted.<br>        parent: The parent span or trace. If not provided, we will automatically use the current<br>            trace/span as the parent.<br>        disabled: If True, we will return a Span but the Span will not be recorded.<br>    Returns:<br>        The newly created speech-to-text span.<br>    """<br>    return GLOBAL_TRACE_PROVIDER.create_span(<br>        span_data=TranscriptionSpanData(<br>            input=input,<br>            input_format=input_format,<br>            output=output,<br>            model=model,<br>            model_config=model_config,<br>        ),<br>        span_id=span_id,<br>        parent=parent,<br>        disabled=disabled,<br>    )<br>``` |

### speech\_span

```md-code__content
speech_span(
    model: str | None = None,
    input: str | None = None,
    output: str | None = None,
    output_format: str | None = "pcm",
    model_config: Mapping[str, Any] | None = None,
    first_content_at: str | None = None,
    span_id: str | None = None,
    parent: Trace | Span[Any] | None = None,
    disabled: bool = False,
) -> Span[SpeechSpanData]

```

Create a new speech span. The span will not be started automatically, you should either do
`with speech_span() ...` or call `span.start()` \+ `span.finish()` manually.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `model` | `str | None` | The name of the model used for the text-to-speech. | `None` |
| `input` | `str | None` | The text input of the text-to-speech. | `None` |
| `output` | `str | None` | The audio output of the text-to-speech as base64 encoded string of PCM audio bytes. | `None` |
| `output_format` | `str | None` | The format of the audio output (defaults to "pcm"). | `'pcm'` |
| `model_config` | `Mapping[str, Any] | None` | The model configuration (hyperparameters) used. | `None` |
| `first_content_at` | `str | None` | The time of the first byte of the audio output. | `None` |
| `span_id` | `str | None` | The ID of the span. Optional. If not provided, we will generate an ID. We<br>recommend using `util.gen_span_id()` to generate a span ID, to guarantee that IDs are<br>correctly formatted. | `None` |
| `parent` | `Trace | Span[Any] | None` | The parent span or trace. If not provided, we will automatically use the current<br>trace/span as the parent. | `None` |
| `disabled` | `bool` | If True, we will return a Span but the Span will not be recorded. | `False` |

Source code in `src/agents/tracing/create.py`

|     |     |
| --- | --- |
| ```<br>360<br>361<br>362<br>363<br>364<br>365<br>366<br>367<br>368<br>369<br>370<br>371<br>372<br>373<br>374<br>375<br>376<br>377<br>378<br>379<br>380<br>381<br>382<br>383<br>384<br>385<br>386<br>387<br>388<br>389<br>390<br>391<br>392<br>393<br>394<br>395<br>396<br>397<br>398<br>399<br>400<br>``` | ```md-code__content<br>def speech_span(<br>    model: str | None = None,<br>    input: str | None = None,<br>    output: str | None = None,<br>    output_format: str | None = "pcm",<br>    model_config: Mapping[str, Any] | None = None,<br>    first_content_at: str | None = None,<br>    span_id: str | None = None,<br>    parent: Trace | Span[Any] | None = None,<br>    disabled: bool = False,<br>) -> Span[SpeechSpanData]:<br>    """Create a new speech span. The span will not be started automatically, you should either do<br>    `with speech_span() ...` or call `span.start()` + `span.finish()` manually.<br>    Args:<br>        model: The name of the model used for the text-to-speech.<br>        input: The text input of the text-to-speech.<br>        output: The audio output of the text-to-speech as base64 encoded string of PCM audio bytes.<br>        output_format: The format of the audio output (defaults to "pcm").<br>        model_config: The model configuration (hyperparameters) used.<br>        first_content_at: The time of the first byte of the audio output.<br>        span_id: The ID of the span. Optional. If not provided, we will generate an ID. We<br>            recommend using `util.gen_span_id()` to generate a span ID, to guarantee that IDs are<br>            correctly formatted.<br>        parent: The parent span or trace. If not provided, we will automatically use the current<br>            trace/span as the parent.<br>        disabled: If True, we will return a Span but the Span will not be recorded.<br>    """<br>    return GLOBAL_TRACE_PROVIDER.create_span(<br>        span_data=SpeechSpanData(<br>            model=model,<br>            input=input,<br>            output=output,<br>            output_format=output_format,<br>            model_config=model_config,<br>            first_content_at=first_content_at,<br>        ),<br>        span_id=span_id,<br>        parent=parent,<br>        disabled=disabled,<br>    )<br>``` |

### speech\_group\_span

```md-code__content
speech_group_span(
    input: str | None = None,
    span_id: str | None = None,
    parent: Trace | Span[Any] | None = None,
    disabled: bool = False,
) -> Span[SpeechGroupSpanData]

```

Create a new speech group span. The span will not be started automatically, you should
either do `with speech_group_span() ...` or call `span.start()` \+ `span.finish()` manually.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `input` | `str | None` | The input text used for the speech request. | `None` |
| `span_id` | `str | None` | The ID of the span. Optional. If not provided, we will generate an ID. We<br>recommend using `util.gen_span_id()` to generate a span ID, to guarantee that IDs are<br>correctly formatted. | `None` |
| `parent` | `Trace | Span[Any] | None` | The parent span or trace. If not provided, we will automatically use the current<br>trace/span as the parent. | `None` |
| `disabled` | `bool` | If True, we will return a Span but the Span will not be recorded. | `False` |

Source code in `src/agents/tracing/create.py`

|     |     |
| --- | --- |
| ```<br>403<br>404<br>405<br>406<br>407<br>408<br>409<br>410<br>411<br>412<br>413<br>414<br>415<br>416<br>417<br>418<br>419<br>420<br>421<br>422<br>423<br>424<br>425<br>426<br>``` | ```md-code__content<br>def speech_group_span(<br>    input: str | None = None,<br>    span_id: str | None = None,<br>    parent: Trace | Span[Any] | None = None,<br>    disabled: bool = False,<br>) -> Span[SpeechGroupSpanData]:<br>    """Create a new speech group span. The span will not be started automatically, you should<br>    either do `with speech_group_span() ...` or call `span.start()` + `span.finish()` manually.<br>    Args:<br>        input: The input text used for the speech request.<br>        span_id: The ID of the span. Optional. If not provided, we will generate an ID. We<br>            recommend using `util.gen_span_id()` to generate a span ID, to guarantee that IDs are<br>            correctly formatted.<br>        parent: The parent span or trace. If not provided, we will automatically use the current<br>            trace/span as the parent.<br>        disabled: If True, we will return a Span but the Span will not be recorded.<br>    """<br>    return GLOBAL_TRACE_PROVIDER.create_span(<br>        span_data=SpeechGroupSpanData(input=input),<br>        span_id=span_id,<br>        parent=parent,<br>        disabled=disabled,<br>    )<br>``` |