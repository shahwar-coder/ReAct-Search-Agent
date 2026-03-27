# =========================
# 🎯 INTERVIEW Q&A: Tavily (Simple + Complete)
# =========================

# Q: What is Tavily?

answer_1 = """
Tavily is an AI-powered search API designed for LLMs and agents.

In simple terms:
it lets an AI model search the internet and get clean, useful information.
"""


# Q: What problem does Tavily solve?

answer_2 = """
LLMs have limitations:

- no real-time data
- can hallucinate
- cannot browse the web

Tavily solves this by providing up-to-date and reliable web information.
"""


# Q: What makes Tavily different from normal search?

answer_3 = """
Normal search engines return messy data like ads and HTML pages.

Tavily returns:
- clean text
- summarized content
- relevant results

This makes it easier for LLMs to understand and use the data.
"""


# Q: Key capabilities of Tavily

answer_4 = """
1. Real-time search → latest information
2. Semantic search → understands meaning, not just keywords
3. Structured output → clean and LLM-ready
4. Source attribution → provides links for trust
5. Content extraction → removes noise from web pages
6. Agent integration → works directly with LangChain / LangGraph
"""


# Q: How does Tavily work in an agent?

answer_5 = """
Flow:

User → LLM → decides to search
     → calls Tavily
     → gets results
     → generates final answer

So Tavily acts like the "internet access" of the agent.
"""


# Q: Why is Tavily important?

answer_6 = """
It reduces hallucinations and improves accuracy.

Instead of guessing, the model uses real data,
which makes AI systems more reliable and production-ready.
"""


# Q: When should you use Tavily?

answer_7 = """
Use Tavily when:

- building AI agents
- need real-time information
- doing web-based retrieval (RAG)
"""


# Q: When not to use it?

answer_8 = """
Avoid Tavily when:

- data is static
- working with internal/private data
- offline systems
"""


# Q: Short interview answer

answer_short = """
Tavily is an AI-native search API that provides real-time, clean, and structured web data to LLMs,
helping reduce hallucinations and enabling agents to access up-to-date information.
"""