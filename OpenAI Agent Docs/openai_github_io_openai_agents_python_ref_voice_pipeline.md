[Skip to content](https://openai.github.io/openai-agents-python/ref/voice/pipeline/#pipeline)

# `Pipeline`

### VoicePipeline

An opinionated voice agent pipeline. It works in three steps:
1\. Transcribe audio input into text.
2\. Run the provided `workflow`, which produces a sequence of text responses.
3\. Convert the text responses into streaming audio output.

Source code in `src/agents/voice/pipeline.py`

|     |     |
| --- | --- |
| ```<br> 15<br> 16<br> 17<br> 18<br> 19<br> 20<br> 21<br> 22<br> 23<br> 24<br> 25<br> 26<br> 27<br> 28<br> 29<br> 30<br> 31<br> 32<br> 33<br> 34<br> 35<br> 36<br> 37<br> 38<br> 39<br> 40<br> 41<br> 42<br> 43<br> 44<br> 45<br> 46<br> 47<br> 48<br> 49<br> 50<br> 51<br> 52<br> 53<br> 54<br> 55<br> 56<br> 57<br> 58<br> 59<br> 60<br> 61<br> 62<br> 63<br> 64<br> 65<br> 66<br> 67<br> 68<br> 69<br> 70<br> 71<br> 72<br> 73<br> 74<br> 75<br> 76<br> 77<br> 78<br> 79<br> 80<br> 81<br> 82<br> 83<br> 84<br> 85<br> 86<br> 87<br> 88<br> 89<br> 90<br> 91<br> 92<br> 93<br> 94<br> 95<br> 96<br> 97<br> 98<br> 99<br>100<br>101<br>102<br>103<br>104<br>105<br>106<br>107<br>108<br>109<br>110<br>111<br>112<br>113<br>114<br>115<br>116<br>117<br>118<br>119<br>120<br>121<br>122<br>123<br>124<br>125<br>126<br>127<br>128<br>129<br>130<br>131<br>132<br>133<br>134<br>135<br>136<br>137<br>138<br>139<br>140<br>141<br>142<br>143<br>144<br>145<br>146<br>147<br>148<br>149<br>150<br>151<br>``` | ```md-code__content<br>class VoicePipeline:<br>    """An opinionated voice agent pipeline. It works in three steps:<br>    1. Transcribe audio input into text.<br>    2. Run the provided `workflow`, which produces a sequence of text responses.<br>    3. Convert the text responses into streaming audio output.<br>    """<br>    def __init__(<br>        self,<br>        *,<br>        workflow: VoiceWorkflowBase,<br>        stt_model: STTModel | str | None = None,<br>        tts_model: TTSModel | str | None = None,<br>        config: VoicePipelineConfig | None = None,<br>    ):<br>        """Create a new voice pipeline.<br>        Args:<br>            workflow: The workflow to run. See `VoiceWorkflowBase`.<br>            stt_model: The speech-to-text model to use. If not provided, a default OpenAI<br>                model will be used.<br>            tts_model: The text-to-speech model to use. If not provided, a default OpenAI<br>                model will be used.<br>            config: The pipeline configuration. If not provided, a default configuration will be<br>                used.<br>        """<br>        self.workflow = workflow<br>        self.stt_model = stt_model if isinstance(stt_model, STTModel) else None<br>        self.tts_model = tts_model if isinstance(tts_model, TTSModel) else None<br>        self._stt_model_name = stt_model if isinstance(stt_model, str) else None<br>        self._tts_model_name = tts_model if isinstance(tts_model, str) else None<br>        self.config = config or VoicePipelineConfig()<br>    async def run(self, audio_input: AudioInput | StreamedAudioInput) -> StreamedAudioResult:<br>        """Run the voice pipeline.<br>        Args:<br>            audio_input: The audio input to process. This can either be an `AudioInput` instance,<br>                which is a single static buffer, or a `StreamedAudioInput` instance, which is a<br>                stream of audio data that you can append to.<br>        Returns:<br>            A `StreamedAudioResult` instance. You can use this object to stream audio events and<br>            play them out.<br>        """<br>        if isinstance(audio_input, AudioInput):<br>            return await self._run_single_turn(audio_input)<br>        elif isinstance(audio_input, StreamedAudioInput):<br>            return await self._run_multi_turn(audio_input)<br>        else:<br>            raise UserError(f"Unsupported audio input type: {type(audio_input)}")<br>    def _get_tts_model(self) -> TTSModel:<br>        if not self.tts_model:<br>            self.tts_model = self.config.model_provider.get_tts_model(self._tts_model_name)<br>        return self.tts_model<br>    def _get_stt_model(self) -> STTModel:<br>        if not self.stt_model:<br>            self.stt_model = self.config.model_provider.get_stt_model(self._stt_model_name)<br>        return self.stt_model<br>    async def _process_audio_input(self, audio_input: AudioInput) -> str:<br>        model = self._get_stt_model()<br>        return await model.transcribe(<br>            audio_input,<br>            self.config.stt_settings,<br>            self.config.trace_include_sensitive_data,<br>            self.config.trace_include_sensitive_audio_data,<br>        )<br>    async def _run_single_turn(self, audio_input: AudioInput) -> StreamedAudioResult:<br>        # Since this is single turn, we can use the TraceCtxManager to manage starting/ending the<br>        # trace<br>        with TraceCtxManager(<br>            workflow_name=self.config.workflow_name or "Voice Agent",<br>            trace_id=None,  # Automatically generated<br>            group_id=self.config.group_id,<br>            metadata=self.config.trace_metadata,<br>            disabled=self.config.tracing_disabled,<br>        ):<br>            input_text = await self._process_audio_input(audio_input)<br>            output = StreamedAudioResult(<br>                self._get_tts_model(), self.config.tts_settings, self.config<br>            )<br>            async def stream_events():<br>                try:<br>                    async for text_event in self.workflow.run(input_text):<br>                        await output._add_text(text_event)<br>                    await output._turn_done()<br>                    await output._done()<br>                except Exception as e:<br>                    logger.error(f"Error processing single turn: {e}")<br>                    await output._add_error(e)<br>                    raise e<br>            output._set_task(asyncio.create_task(stream_events()))<br>            return output<br>    async def _run_multi_turn(self, audio_input: StreamedAudioInput) -> StreamedAudioResult:<br>        with TraceCtxManager(<br>            workflow_name=self.config.workflow_name or "Voice Agent",<br>            trace_id=None,<br>            group_id=self.config.group_id,<br>            metadata=self.config.trace_metadata,<br>            disabled=self.config.tracing_disabled,<br>        ):<br>            output = StreamedAudioResult(<br>                self._get_tts_model(), self.config.tts_settings, self.config<br>            )<br>            transcription_session = await self._get_stt_model().create_session(<br>                audio_input,<br>                self.config.stt_settings,<br>                self.config.trace_include_sensitive_data,<br>                self.config.trace_include_sensitive_audio_data,<br>            )<br>            async def process_turns():<br>                try:<br>                    async for input_text in transcription_session.transcribe_turns():<br>                        result = self.workflow.run(input_text)<br>                        async for text_event in result:<br>                            await output._add_text(text_event)<br>                        await output._turn_done()<br>                except Exception as e:<br>                    logger.error(f"Error processing turns: {e}")<br>                    await output._add_error(e)<br>                    raise e<br>                finally:<br>                    await transcription_session.close()<br>                    await output._done()<br>            output._set_task(asyncio.create_task(process_turns()))<br>            return output<br>``` |

#### \_\_init\_\_

```md-code__content
__init__(
    *,
    workflow: VoiceWorkflowBase,
    stt_model: STTModel | str | None = None,
    tts_model: TTSModel | str | None = None,
    config: VoicePipelineConfig | None = None,
)

```

Create a new voice pipeline.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `workflow` | `VoiceWorkflowBase` | The workflow to run. See `VoiceWorkflowBase`. | _required_ |
| `stt_model` | `STTModel | str | None` | The speech-to-text model to use. If not provided, a default OpenAI<br>model will be used. | `None` |
| `tts_model` | `TTSModel | str | None` | The text-to-speech model to use. If not provided, a default OpenAI<br>model will be used. | `None` |
| `config` | `VoicePipelineConfig | None` | The pipeline configuration. If not provided, a default configuration will be<br>used. | `None` |

Source code in `src/agents/voice/pipeline.py`

|     |     |
| --- | --- |
| ```<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>``` | ```md-code__content<br>def __init__(<br>    self,<br>    *,<br>    workflow: VoiceWorkflowBase,<br>    stt_model: STTModel | str | None = None,<br>    tts_model: TTSModel | str | None = None,<br>    config: VoicePipelineConfig | None = None,<br>):<br>    """Create a new voice pipeline.<br>    Args:<br>        workflow: The workflow to run. See `VoiceWorkflowBase`.<br>        stt_model: The speech-to-text model to use. If not provided, a default OpenAI<br>            model will be used.<br>        tts_model: The text-to-speech model to use. If not provided, a default OpenAI<br>            model will be used.<br>        config: The pipeline configuration. If not provided, a default configuration will be<br>            used.<br>    """<br>    self.workflow = workflow<br>    self.stt_model = stt_model if isinstance(stt_model, STTModel) else None<br>    self.tts_model = tts_model if isinstance(tts_model, TTSModel) else None<br>    self._stt_model_name = stt_model if isinstance(stt_model, str) else None<br>    self._tts_model_name = tts_model if isinstance(tts_model, str) else None<br>    self.config = config or VoicePipelineConfig()<br>``` |

#### run`async`

```md-code__content
run(
    audio_input: AudioInput | StreamedAudioInput,
) -> StreamedAudioResult

```

Run the voice pipeline.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `audio_input` | `AudioInput | StreamedAudioInput` | The audio input to process. This can either be an `AudioInput` instance,<br>which is a single static buffer, or a `StreamedAudioInput` instance, which is a<br>stream of audio data that you can append to. | _required_ |

Returns:

| Type | Description |
| --- | --- |
| `StreamedAudioResult` | A `StreamedAudioResult` instance. You can use this object to stream audio events and |
| `StreamedAudioResult` | play them out. |

Source code in `src/agents/voice/pipeline.py`

|     |     |
| --- | --- |
| ```<br>48<br>49<br>50<br>51<br>52<br>53<br>54<br>55<br>56<br>57<br>58<br>59<br>60<br>61<br>62<br>63<br>64<br>65<br>``` | ```md-code__content<br>async def run(self, audio_input: AudioInput | StreamedAudioInput) -> StreamedAudioResult:<br>    """Run the voice pipeline.<br>    Args:<br>        audio_input: The audio input to process. This can either be an `AudioInput` instance,<br>            which is a single static buffer, or a `StreamedAudioInput` instance, which is a<br>            stream of audio data that you can append to.<br>    Returns:<br>        A `StreamedAudioResult` instance. You can use this object to stream audio events and<br>        play them out.<br>    """<br>    if isinstance(audio_input, AudioInput):<br>        return await self._run_single_turn(audio_input)<br>    elif isinstance(audio_input, StreamedAudioInput):<br>        return await self._run_multi_turn(audio_input)<br>    else:<br>        raise UserError(f"Unsupported audio input type: {type(audio_input)}")<br>``` |