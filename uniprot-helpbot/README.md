# A helpbot for Uniprot

Very simple, dumb implementation of a bot you can ask questions in natural language and get sensible, referenced answers from.

The process to create this looks like:

1. Get the uniprot help files in a helpful format
    * I cloned the unprot help git repo
    * Rename all the markdown files to .txt (because paper-qa will treat them as code otherwise)
2. Embed 3k character chunks of text using OpenAI enbeddings 
    * This is the default in paper-qa - can also use local models like Llama
3. Store the embedded chunks in a pickle file (`uniprot_help.pkl`)
4. Add a gradio frontend so you can query it in the browser

I've included the pickled docstore, so if you clone this repo, you should be able to get this demo running straight away.


## Limitations

- Treating markdown as plain text is wrong, and results in some mangled formatting. Best would be to add a markdown processor to paper-qa.
- If it isn't in the docs, this bot doesn't know about it (e.g. SPARQL)
- Uses a lot of OpenAI API calls, which may get expensive