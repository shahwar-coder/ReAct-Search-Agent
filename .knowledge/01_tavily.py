# =========================
# 🎯 INTERVIEW Q&A: What is Tavily?
# =========================

# Q: What is Tavily?

answer_1 = """
Tavily is an AI-powered search API designed for LLM applications and agents.

In simple terms:
it allows AI models to search the internet and get real-time information.
"""


# Q: Why do we need Tavily?

answer_2 = """
LLMs like GPT or Mistral:

- don’t have real-time data
- can hallucinate (make up answers)
- cannot browse the internet

Tavily solves this by providing fresh and relevant web data to the model.
"""


# Q: How does Tavily work in an agent?

answer_3 = """
In an agent workflow:

- User asks a question
- LLM decides it needs external information
- It calls Tavily as a tool
- Tavily returns structured results
- LLM uses that to generate a better answer

So Tavily acts like the “internet access” for the agent.
"""


# Q: What makes Tavily special?

answer_4 = """
Unlike normal search APIs, Tavily returns:

- clean summaries
- relevant content
- useful links

This makes it easy for LLMs to understand and use the data directly.
"""


# Q: How is it used in LangChain?

answer_5 = """
In LangChain, Tavily is used as a tool.

Example:

from langchain_community.tools.tavily_search import TavilySearchResults

tool = TavilySearchResults()

This tool can then be used inside agents.
"""


# Q: Why is Tavily important?

answer_6 = """
Tavily helps:

- reduce hallucinations
- provide real-time knowledge
- improve answer accuracy

This is very important for production AI systems.
"""


# Q: Short interview answer

answer_short = """
Tavily is an AI-native search API that gives LLMs real-time, structured web data,
and is commonly used as a tool in agents to improve accuracy and reduce hallucinations.
"""