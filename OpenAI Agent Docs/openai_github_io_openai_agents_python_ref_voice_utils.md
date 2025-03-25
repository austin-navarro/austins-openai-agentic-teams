[Skip to content](https://openai.github.io/openai-agents-python/ref/voice/utils/#utils)

# `Utils`

### get\_sentence\_based\_splitter

```md-code__content
get_sentence_based_splitter(
    min_sentence_length: int = 20,
) -> Callable[[str], tuple[str, str]]

```

Returns a function that splits text into chunks based on sentence boundaries.

Parameters:

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| `min_sentence_length` | `int` | The minimum length of a sentence to be included in a chunk. | `20` |

Returns:

| Type | Description |
| --- | --- |
| `Callable[[str], tuple[str, str]]` | A function that splits text into chunks based on sentence boundaries. |

Source code in `src/agents/voice/utils.py`

|     |     |
| --- | --- |
| ```<br> 5<br> 6<br> 7<br> 8<br> 9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>``` | ```md-code__content<br>def get_sentence_based_splitter(<br>    min_sentence_length: int = 20,<br>) -> Callable[[str], tuple[str, str]]:<br>    """Returns a function that splits text into chunks based on sentence boundaries.<br>    Args:<br>        min_sentence_length: The minimum length of a sentence to be included in a chunk.<br>    Returns:<br>        A function that splits text into chunks based on sentence boundaries.<br>    """<br>    def sentence_based_text_splitter(text_buffer: str) -> tuple[str, str]:<br>        """<br>        A function to split the text into chunks. This is useful if you want to split the text into<br>        chunks before sending it to the TTS model rather than waiting for the whole text to be<br>        processed.<br>        Args:<br>            text_buffer: The text to split.<br>        Returns:<br>            A tuple of the text to process and the remaining text buffer.<br>        """<br>        sentences = re.split(r"(?<=[.!?])\s+", text_buffer.strip())<br>        if len(sentences) >= 1:<br>            combined_sentences = " ".join(sentences[:-1])<br>            if len(combined_sentences) >= min_sentence_length:<br>                remaining_text_buffer = sentences[-1]<br>                return combined_sentences, remaining_text_buffer<br>        return "", text_buffer<br>    return sentence_based_text_splitter<br>``` |