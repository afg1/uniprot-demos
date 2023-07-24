## Residue Specific Information

A prompt and some tooling to see if we can automatically extract residue specific information from text.

Examples given in `examples.csv` have passages pulled from the paper, along with a label for the presence of residue information and, where present, the residue information itself.

We tried to de a few shot prompt, with two positive examples anf their corresponding residue tables.

Requires an OpenAI account and that you have an OPENAI_KEY in your environment.


## Limitations

1. This tool relies on the ChatGPT API, so we are somewhat at the whim of chatGPT as to getting a sensible reply.
2. There is no negative example in the prompt, and it isn't clear if there should be. When we tried explicitly telling the model to say 'N/A' when there was no information, it said 'N/A' to everything.