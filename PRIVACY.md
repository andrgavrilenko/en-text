# Privacy

en-text collects nothing, stores nothing, and sends nothing anywhere.

The plugin is a set of instructions and reference files that Claude reads. It runs
no code of its own when it is installed or used, has no server, and includes no
analytics. The one script in the repository, `tests/check_corpus.py`, checks the
corpus during development and is never run by the plugin.

The text you pass to `en-check` or `en-score`, or ask the base skill to edit, is
read by Claude inside your own session, under the terms that already govern that
session. The review skills deny themselves every tool that could write a file, run a
command, reach the network, start another agent, send a message, or call an MCP
server, so nothing in a reviewed text can make them send it elsewhere.

Questions go to the issue tracker:
https://github.com/andrgavrilenko/en-text/issues
