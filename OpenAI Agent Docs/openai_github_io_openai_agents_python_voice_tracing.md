[Skip to content](https://openai.github.io/openai-agents-python/voice/tracing/#tracing)

# Tracing

Just like the way [agents are traced](https://openai.github.io/openai-agents-python/tracing/), voice pipelines are also automatically traced.

You can read the tracing doc above for basic tracing information, but you can additionally configure tracing of a pipeline via [`VoicePipelineConfig`](https://openai.github.io/openai-agents-python/ref/voice/pipeline_config/#agents.voice.pipeline_config.VoicePipelineConfig "VoicePipelineConfig            dataclass   ").

Key tracing related fields are:

- [`tracing_disabled`](https://openai.github.io/openai-agents-python/ref/voice/pipeline_config/#agents.voice.pipeline_config.VoicePipelineConfig.tracing_disabled "tracing_disabled            class-attribute       instance-attribute   "): controls whether tracing is disabled. By default, tracing is enabled.
- [`trace_include_sensitive_data`](https://openai.github.io/openai-agents-python/ref/voice/pipeline_config/#agents.voice.pipeline_config.VoicePipelineConfig.trace_include_sensitive_data "trace_include_sensitive_data            class-attribute       instance-attribute   "): controls whether traces include potentially sensitive data, like audio transcripts. This is specifically for the voice pipeline, and not for anything that goes on inside your Workflow.
- [`trace_include_sensitive_audio_data`](https://openai.github.io/openai-agents-python/ref/voice/pipeline_config/#agents.voice.pipeline_config.VoicePipelineConfig.trace_include_sensitive_audio_data "trace_include_sensitive_audio_data            class-attribute       instance-attribute   "): controls whether traces include audio data.
- [`workflow_name`](https://openai.github.io/openai-agents-python/ref/voice/pipeline_config/#agents.voice.pipeline_config.VoicePipelineConfig.workflow_name "workflow_name            class-attribute       instance-attribute   "): The name of the trace workflow.
- [`group_id`](https://openai.github.io/openai-agents-python/ref/voice/pipeline_config/#agents.voice.pipeline_config.VoicePipelineConfig.group_id "group_id            class-attribute       instance-attribute   "): The `group_id` of the trace, which lets you link multiple traces.
- [`trace_metadata`](https://openai.github.io/openai-agents-python/ref/voice/pipeline_config/#agents.voice.pipeline_config.VoicePipelineConfig.tracing_disabled "tracing_disabled            class-attribute       instance-attribute   "): Additional metadata to include with the trace.