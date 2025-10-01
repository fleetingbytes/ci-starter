# Technical Decisions

## Way of replacing placeholders in semantic-release.toml

Most placeholders in the _semantic-release.toml_ asset file are substrings in a larger string.
We do not parse the .toml file at all. Instead we read it as one big string and replace the placeholder substrings.
This is more efficient than parsing the toml into a dict object, searching parts of the dict, which contain placeholders 
and replacing the placeholders in smaller string objects.


## Way of replacing placeholders in wokflow files

We chose not to use any kind of placeholders in the workflow assets.
Everything settable is situated in the _env_ dictionary.
Parsing the workflow file to a dict object and replacing the values there seems to be the most straightforward approach,
especially when considering that in the future we want to support updating the
action versions in steps tagged `!step` in already established workflows.
For that a parsing to some sort of structured object seems to be the cleanest way.
