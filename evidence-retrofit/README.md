# Evidence Retrofitting

This demo aims to address those entries whose annotations/assertions do not explicitly have evidence associated with them.

To do this, we embed the literature (abstracts in this case) attached to an entry, then use natural language to query it. This should allow curators to quickly see which paper talks about the annotations they are looking at, with references and a rough location in the abstract.

To make this easier, we are using OpenAI embeddings, the process looks like:

1. Get the abstracts for the papers we want to search
    * We did this manually for a few, in the `papers` folder
2. Embed each and place in a FAISS vector store
3. Add a Gradio frontend and some code to allow querying


## Limitations
- Manually adding the abstracts to the vector store is tedious. It would be better to link this up with an API to automate it
- The exact wording of the query you need isn't totally clear. I think it needs to look like the middle of a sentence you would like to see, so for example "ADHII is located in the" 
- If there is no relevant information, you will get some random collection of statements which are no use
- Tuning the retrieval parameters could be tricky - 