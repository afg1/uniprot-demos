# UniProt Demos

This repo contains three demos we worked on during the UniProt LLM workshop.

They are very much hacked together, and will need a lot of work to make fully serviceable, but they show the basic premise.


## Evidence Retrofit
Some entries have assertions, but don't necessarily have the evidence alongside to back them up. 

This demo stops short of actually editing the entries, and instead shows users sections of the the papers attached to an entry that might fit the assertion made. For example, what evidence of the subsellular localisation is there in the literature attached to a given protein.


## Residue Specific Information
Some papers have information about individual residues in a protein, which we would like to be able to automatically extract. 

This demo extracts the residue location, name and a note of what the paper says about it. We tried to get it to say 'N/A' if there was no information present in a given passage.

This one comes with a bunch of examples prepared by Alex.


## UniProt helpbot
One of the ideas we discussed was creating a bot that can answer users' questions, preferably with links to the documentation.

This demo tries to do that by encoding the documentation into a vector store and allowing the user to query it using natural language. It works pretty well, but the implementation is suboptimal given the input data type.