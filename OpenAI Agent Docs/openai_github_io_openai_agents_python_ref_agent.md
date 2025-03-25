[Skip to content](https://openai.github.io/openai-agents-python/ref/agent/#agents)

# `Agents`

### ToolsToFinalOutputFunction`module-attribute`

```md-code__content
ToolsToFinalOutputFunction: TypeAlias = Callable[\
    [RunContextWrapper[TContext], list[FunctionToolResult]],\
    MaybeAwaitable[ToolsToFinalOutputResult],\
]

```

A function that takes a run context and a list of tool results, and returns a
`ToolToFinalOutputResult`.

### ToolsToFinalOutputResult`dataclass`

Source code in `src/agents/agent.py`

|     |     |
| --- | --- |
| ```<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>``` | ```md-code__content<br>@dataclass<br>class ToolsToFinalOutputResult:<br>    is_final_output: bool<br>    """Whether this is the final output. If False, the LLM will run again and receive the tool call<br>    output.<br>    """<br>    final_output: Any | None = None<br>    """The final output. Can be None if `is_final_output` is False, otherwise must match the<br>    `output_type` of the agent.<br>    """<br>``` |

#### is\_final\_output`instance-attribute`

```md-code__content
is_final_output: bool

```

Whether this is the final output. If False, the LLM will run again and receive the tool call
output.

#### final\_output`class-attribute``instance-attribute`

```md-code__content
final_output: Any | None = None

```

The final output. Can be None if `is_final_output` is False, otherwise must match the
`output_type` of the agent.

### StopAtTools

Bases: `TypedDict`

Source code in `src/agents/agent.py`

|     |     |
| --- | --- |
| ```<br>49<br>50<br>51<br>``` | ```md-code__content<br>class StopAtTools(TypedDict):<br>    stop_at_tool_names: list[str]<br>    """A list of tool names, any of which will stop the agent from running further."""<br>``` |

#### stop\_at\_tool\_names`instance-attribute`

```md-code__content
stop_at_tool_names: list[str]

```

A list of tool names, any of which will stop the agent from running further.

### Agent`dataclass`

Bases: `Generic[TContext]`

An agent is an AI model configured with instructions, tools, guardrails, handoffs and more.

We strongly recommend passing `instructions`, which is the "system prompt" for the agent. In
addition, you can pass `handoff_description`, which is a human-readable description of the
agent, used when the agent is used inside tools/handoffs.

Agents are generic on the context type. The context is a (mutable) object you create. It is
passed to tool functions, handoffs, guardrails, etc.

Source code in `src/agents/agent.py`

|     |     |
| --- | --- |
| ```<br> 54<br> 55<br> 56<br> 57<br> 58<br> 59<br> 60<br> 61<br> 62<br> 63<br> 64<br> 65<br> 66<br> 67<br> 68<br> 69<br> 70<br> 71<br> 72<br> 73<br> 74<br> 75<br> 76<br> 77<br> 78<br> 79<br> 80<br> 81<br> 82<br> 83<br> 84<br> 85<br> 86<br> 87<br> 88<br> 89<br> 90<br> 91<br> 92<br> 93<br> 94<br> 95<br> 96<br> 97<br> 98<br> 99<br>100<br>101<br>102<br>103<br>104<br>105<br>106<br>107<br>108<br>109<br>110<br>111<br>112<br>113<br>114<br>115<br>116<br>117<br>118<br>119<br>120<br>121<br>122<br>123<br>124<br>125<br>126<br>127<br>128<br>129<br>130<br>131<br>132<br>133<br>134<br>135<br>136<br>137<br>138<br>139<br>140<br>141<br>142<br>143<br>144<br>145<br>146<br>147<br>148<br>149<br>150<br>151<br>152<br>153<br>154<br>155<br>156<br>157<br>158<br>159<br>160<br>161<br>162<br>163<br>164<br>165<br>166<br>167<br>168<br>169<br>170<br>171<br>172<br>173<br>174<br>175<br>176<br>177<br>178<br>179<br>180<br>181<br>182<br>183<br>184<br>185<br>186<br>187<br>188<br>189<br>190<br>191<br>192<br>193<br>194<br>195<br>196<br>197<br>198<br>199<br>200<br>201<br>202<br>203<br>204<br>205<br>206<br>207<br>``` | ````md-code__content<br>@dataclass<br>class Agent(Generic[TContext]):<br>    """An agent is an AI model configured with instructions, tools, guardrails, handoffs and more.<br>    We strongly recommend passing `instructions`, which is the "system prompt" for the agent. In<br>    addition, you can pass `handoff_description`, which is a human-readable description of the<br>    agent, used when the agent is used inside tools/handoffs.<br>    Agents are generic on the context type. The context is a (mutable) object you create. It is<br>    passed to tool functions, handoffs, guardrails, etc.<br>    """<br>    name: str<br>    """The name of the agent."""<br>    instructions: (<br>        str<br>        | Callable[<br>            [RunContextWrapper[TContext], Agent[TContext]],<br>            MaybeAwaitable[str],<br>        ]<br>        | None<br>    ) = None<br>    """The instructions for the agent. Will be used as the "system prompt" when this agent is<br>    invoked. Describes what the agent should do, and how it responds.<br>    Can either be a string, or a function that dynamically generates instructions for the agent. If<br>    you provide a function, it will be called with the context and the agent instance. It must<br>    return a string.<br>    """<br>    handoff_description: str | None = None<br>    """A description of the agent. This is used when the agent is used as a handoff, so that an<br>    LLM knows what it does and when to invoke it.<br>    """<br>    handoffs: list[Agent[Any] | Handoff[TContext]] = field(default_factory=list)<br>    """Handoffs are sub-agents that the agent can delegate to. You can provide a list of handoffs,<br>    and the agent can choose to delegate to them if relevant. Allows for separation of concerns and<br>    modularity.<br>    """<br>    model: str | Model | None = None<br>    """The model implementation to use when invoking the LLM.<br>    By default, if not set, the agent will use the default model configured in<br>    `model_settings.DEFAULT_MODEL`.<br>    """<br>    model_settings: ModelSettings = field(default_factory=ModelSettings)<br>    """Configures model-specific tuning parameters (e.g. temperature, top_p).<br>    """<br>    tools: list[Tool] = field(default_factory=list)<br>    """A list of tools that the agent can use."""<br>    input_guardrails: list[InputGuardrail[TContext]] = field(default_factory=list)<br>    """A list of checks that run in parallel to the agent's execution, before generating a<br>    response. Runs only if the agent is the first agent in the chain.<br>    """<br>    output_guardrails: list[OutputGuardrail[TContext]] = field(default_factory=list)<br>    """A list of checks that run on the final output of the agent, after generating a response.<br>    Runs only if the agent produces a final output.<br>    """<br>    output_type: type[Any] | None = None<br>    """The type of the output object. If not provided, the output will be `str`."""<br>    hooks: AgentHooks[TContext] | None = None<br>    """A class that receives callbacks on various lifecycle events for this agent.<br>    """<br>    tool_use_behavior: (<br>        Literal["run_llm_again", "stop_on_first_tool"] | StopAtTools | ToolsToFinalOutputFunction<br>    ) = "run_llm_again"<br>    """This lets you configure how tool use is handled.<br>    - "run_llm_again": The default behavior. Tools are run, and then the LLM receives the results<br>        and gets to respond.<br>    - "stop_on_first_tool": The output of the first tool call is used as the final output. This<br>        means that the LLM does not process the result of the tool call.<br>    - A list of tool names: The agent will stop running if any of the tools in the list are called.<br>        The final output will be the output of the first matching tool call. The LLM does not<br>        process the result of the tool call.<br>    - A function: If you pass a function, it will be called with the run context and the list of<br>      tool results. It must return a `ToolToFinalOutputResult`, which determines whether the tool<br>      calls result in a final output.<br>      NOTE: This configuration is specific to FunctionTools. Hosted tools, such as file search,<br>      web search, etc are always processed by the LLM.<br>    """<br>    def clone(self, **kwargs: Any) -> Agent[TContext]:<br>        """Make a copy of the agent, with the given arguments changed. For example, you could do:<br>        ```<br>        new_agent = agent.clone(instructions="New instructions")<br>        ```<br>        """<br>        return dataclasses.replace(self, **kwargs)<br>    def as_tool(<br>        self,<br>        tool_name: str | None,<br>        tool_description: str | None,<br>        custom_output_extractor: Callable[[RunResult], Awaitable[str]] | None = None,<br>    ) -> Tool:<br>        """Transform this agent into a tool, callable by other agents.<br>        This is different from handoffs in two ways:<br>        1. In handoffs, the new agent receives the conversation history. In this tool, the new agent<br>           receives generated input.<br>        2. In handoffs, the new agent takes over the conversation. In this tool, the new agent is<br>           called as a tool, and the conversation is continued by the original agent.<br>        Args:<br>            tool_name: The name of the tool. If not provided, the agent's name will be used.<br>            tool_description: The description of the tool, which should indicate what it does and<br>                when to use it.<br>            custom_output_extractor: A function that extracts the output from the agent. If not<br>                provided, the last message from the agent will be used.<br>        """<br>        @function_tool(<br>            name_override=tool_name or _transforms.transform_string_function_style(self.name),<br>            description_override=tool_description or "",<br>        )<br>        async def run_agent(context: RunContextWrapper, input: str) -> str:<br>            from .run import Runner<br>            output = await Runner.run(<br>                starting_agent=self,<br>                input=input,<br>                context=context.context,<br>            )<br>            if custom_output_extractor:<br>                return await custom_output_extractor(output)<br>            return ItemHelpers.text_message_outputs(output.new_items)<br>        return run_agent<br>    async def get_system_prompt(self, run_context: RunContextWrapper[TContext]) -> str | None:<br>        """Get the system prompt for the agent."""<br>        if isinstance(self.instructions, str):<br>            return self.instructions<br>        elif callable(self.instructions):<br>            if inspect.iscoroutinefunction(self.instructions):<br>                return await cast(Awaitable[str], self.instructions(run_context, self))<br>            else:<br>                return cast(str, self.instructions(run_context, self))<br>        elif self.instructions is not None:<br>            logger.error(f"Instructions must be a string or a function, got {self.instructions}")<br>        return None<br>```` |

#### name`instance-attribute`

```md-code__content
name: str

```

The name of the agent.

#### instructions`class-attribute``instance-attribute`

```md-code__content
instructions: (
    str
    | Callable[\
        [RunContextWrapper[TContext], Agent[TContext]],\
        MaybeAwaitable[str],\
    ]
    | None
) = None

```

The instructions for the agent. Will be used as the "system prompt" when this agent is
invoked. Describes what the agent should do, and how it responds.

Can either be a string, or a function that dynamically generates instructions for the agent. If
you provide a function, it will be called with the context and the agent instance. It must
return a string.

#### handoff\_description`class-attribute``instance-attribute`

```md-code__content
handoff_description: str | None = None

```

A description of the agent. This is used when the agent is used as a handoff, so that an
LLM knows what it does and when to invoke it.

#### handoffs`class-attribute``instance-attribute`

```md-code__content
handoffs: list[Agent[Any] | Handoff[TContext]] = field(
    default_factory=list
)

```

Handoffs are sub-agents that the agent can delegate to. You can provide a list of handoffs,
and the agent can choose to delegate to them if relevant. Allows for separation of concerns and
modularity.

#### model`class-attribute``instance-attribute`

```md-code__content
model: str | Model | None = None

```

The model implementation to use when invoking the LLM.

By default, if not set, the agent will use the default model configured in
`model_settings.DEFAULT_MODEL`.

#### model\_settings`class-attribute``instance-attribute`

```md-code__content
model_settings: ModelSettings = field(
    default_factory=ModelSettings
)

```

Configures model-specific tuning parameters (e.g. temperature, top\_p).

#### tools`class-attribute``instance-attribute`

```md-code__content
tools: list[Tool] = field(default_factory=list)

```

A list of tools that the agent can use.

#### input\_guardrails`class-attribute``instance-attribute`

```md-code__content
input_guardrails: list[InputGuardrail[TContext]] = field(
    default_factory=list
)

```

A list of checks that run in parallel to the agent's execution, before generating a
response. Runs only if the agent is the first agent in the chain.

#### output\_guardrails`class-attribute``instance-attribute`

```md-code__content
output_guardrails: list[OutputGuardrail[TContext]] = field(
    default_factory=list
)

```

A list of checks that run on the final output of the agent, after generating a response.
Runs only if the agent produces a final output.

#### output\_type`class-attribute``instance-attribute`

```md-code__content
output_type: type[Any] | None = None

```

The type of the output object. If not provided, the output will be `str`.

#### hooks`class-attribute``instance-attribute`

```md-code__content
hooks: AgentHooks[TContext] | None = None

```

A class that receives callbacks on various lifecycle events for this agent.

#### tool\_use\_behavior`class-attribute``instance-attribute`

```md-code__content
tool_use_behavior: (
    Literal["run_llm_again", "stop_on_first_tool"]
    | StopAtTools
    | ToolsToFinalOutputFunction
) = "run_llm_again"

```

This lets you configure how tool use is handled.
\- "run\_llm\_again": The default behavior. Tools are run, and then the LLM receives the results
and gets to respond.
\- "stop\_on\_first\_tool": The output of the first tool call is used as the final output. This
means that the LLM does not process the result of the tool call.
\- A list of tool names: The agent will stop running if any of the tools in the list are called.
The final output will be the output of the first matching tool call. The LLM does not
process the result of the tool call.
\- A function: If you pass a function, it will be called with the run context and the list of
tool results. It must return a `ToolToFinalOutputResult`, which determines whether the tool
calls result in a final output.

NOTE: This configuration is specific to FunctionTools. Hosted tools, such as file search,
web search, etc are always processed by the LLM.

#### clone

```md-code__content
clone(**kwargs: Any) -> Agent[TContext]

```

Make a copy of the agent, with the given arguments changed. For example, you could do:

```md-code__content
new_agent = agent.clone(instructions="New instructions")

```

Source code in `src/agents/agent.py`

|     |     |
| --- | --- |
| ```<br>146<br>147<br>148<br>149<br>150<br>151<br>152<br>``` | ````md-code__content<br>def clone(self, **kwargs: Any) -> Agent[TContext]:<br>    """Make a copy of the agent, with the given arguments changed. For example, you could do:<br>    ```<br>    new_agent = agent.clone(instructions="New instructions")<br>    ```<br>    """<br>    return dataclasses.replace(self, **kwargs)<br>```` |

#### as\_tool

```md-code__content
as_tool(
    tool_name: str | None,
    tool_description: str | None,
    custom_output_extractor: Callable[\
        [RunResult], Awaitable[str]\
    ]
    | None = None,
) -> Tool

```

Transform this agent into a tool, callable by other agents.

This is different from handoffs in two ways:
1\. In handoffs, the new agent receives the conversation history. In this tool, the new agent
receives generated input.
2\. In handoffs, the new agent takes over the conversation. In this tool, the new agent is
called as a tool, and the conversation is continued by the original agent.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `tool_name` | `str | None` | The name of the tool. If not provided, the agent's name will be used. | _required_ |
| `tool_description` | `str | None` | The description of the tool, which should indicate what it does and<br>when to use it. | _required_ |
| `custom_output_extractor` | `Callable[[RunResult], Awaitable[str]] | None` | A function that extracts the output from the agent. If not<br>provided, the last message from the agent will be used. | `None` |

Source code in `src/agents/agent.py`

|     |     |
| --- | --- |
| ```<br>154<br>155<br>156<br>157<br>158<br>159<br>160<br>161<br>162<br>163<br>164<br>165<br>166<br>167<br>168<br>169<br>170<br>171<br>172<br>173<br>174<br>175<br>176<br>177<br>178<br>179<br>180<br>181<br>182<br>183<br>184<br>185<br>186<br>187<br>188<br>189<br>190<br>191<br>192<br>193<br>``` | ```md-code__content<br>def as_tool(<br>    self,<br>    tool_name: str | None,<br>    tool_description: str | None,<br>    custom_output_extractor: Callable[[RunResult], Awaitable[str]] | None = None,<br>) -> Tool:<br>    """Transform this agent into a tool, callable by other agents.<br>    This is different from handoffs in two ways:<br>    1. In handoffs, the new agent receives the conversation history. In this tool, the new agent<br>       receives generated input.<br>    2. In handoffs, the new agent takes over the conversation. In this tool, the new agent is<br>       called as a tool, and the conversation is continued by the original agent.<br>    Args:<br>        tool_name: The name of the tool. If not provided, the agent's name will be used.<br>        tool_description: The description of the tool, which should indicate what it does and<br>            when to use it.<br>        custom_output_extractor: A function that extracts the output from the agent. If not<br>            provided, the last message from the agent will be used.<br>    """<br>    @function_tool(<br>        name_override=tool_name or _transforms.transform_string_function_style(self.name),<br>        description_override=tool_description or "",<br>    )<br>    async def run_agent(context: RunContextWrapper, input: str) -> str:<br>        from .run import Runner<br>        output = await Runner.run(<br>            starting_agent=self,<br>            input=input,<br>            context=context.context,<br>        )<br>        if custom_output_extractor:<br>            return await custom_output_extractor(output)<br>        return ItemHelpers.text_message_outputs(output.new_items)<br>    return run_agent<br>``` |

#### get\_system\_prompt`async`

```md-code__content
get_system_prompt(
    run_context: RunContextWrapper[TContext],
) -> str | None

```

Get the system prompt for the agent.

Source code in `src/agents/agent.py`

|     |     |
| --- | --- |
| ```<br>195<br>196<br>197<br>198<br>199<br>200<br>201<br>202<br>203<br>204<br>205<br>206<br>207<br>``` | ```md-code__content<br>async def get_system_prompt(self, run_context: RunContextWrapper[TContext]) -> str | None:<br>    """Get the system prompt for the agent."""<br>    if isinstance(self.instructions, str):<br>        return self.instructions<br>    elif callable(self.instructions):<br>        if inspect.iscoroutinefunction(self.instructions):<br>            return await cast(Awaitable[str], self.instructions(run_context, self))<br>        else:<br>            return cast(str, self.instructions(run_context, self))<br>    elif self.instructions is not None:<br>        logger.error(f"Instructions must be a string or a function, got {self.instructions}")<br>    return None<br>``` |