# Lab 4: Agent page
# TODO: Rename this file to fit your page. Keep the number at the front.
#
# Your chatbot again, but now the agent can call your own Python functions as tools
# (see "Giving Your Agent Tools" on Canvas).
# It should:
#   - include at least 2 data-processing functions for your API, written by you, with type
#     hints and docstrings (the agent reads these to decide when to use each tool)
#   - include at least 2 extra tools, which you may build with help from AI. Base these tools
#     on the "cool things to do" in your Dream Project Plan (see "Building Tools for Your Plan" on Canvas)
#   - leave a comment on each tool, and any other code, that AI helped you write
#   - give your tools to a Pydantic AI Agent with tools=[...]
#   - use Streamlit's chat elements, remember the conversation, and use try/except
#   - show what the agent did: which tools it called, and a display of their results
#     (see "Displaying What the Agent Does" on Canvas)

import requests
import streamlit as st
from pydantic_ai import Agent


# Your tools go here (You must define your tools before your agent!):




# Your agent goes here: