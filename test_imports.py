#!/usr/bin/env python
import sys

print("Testing imports...")
print(f"Python: {sys.version}\n")

try:
    from langchain.agents import create_agent
    print("✓ create_agent")
except ImportError as e:
    print(f"✗ create_agent: {e}\n")

try:
    from langchain_groq import ChatGroq
    print("✓ ChatGroq")
except ImportError as e:
    print(f"✗ ChatGroq: {e}\n")

try:
    from langchain_core.prompts import ChatPromptTemplate
    print("✓ ChatPromptTemplate")
except ImportError as e:
    print(f"✗ ChatPromptTemplate: {e}\n")

try:
    from langchain_core.output_parsers import StrOutputParser
    print("✓ StrOutputParser")
except ImportError as e:
    print(f"✗ StrOutputParser: {e}\n")

try:
    from tools import web_search, scrape_url
    print("✓ tools (web_search, scrape_url)")
except ImportError as e:
    print(f"✗ tools: {e}\n")

print("\nAll critical imports tested!")
