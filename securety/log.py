import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import tool

# 1. Setup Environment
load_dotenv()
llm = ChatOpenAI(model="gpt-4", temperature=0)

# 2. Define Security Tools
@tool
def quarantine_ip(ip_address: str):
    """Adds an IP address to the firewall blocklist."""
    # In a real scenario, this would call an API (AWS, Cloudflare, etc.)
    return f"SUCCESS: IP {ip_address} has been quarantined and blocked."

tools = [quarantine_ip]

# 3. Create the Security Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a Senior SOC (Security Operations Center) Agent. 
    Your job is to analyze logs for SQL injection, brute force, or unauthorized access.
    If you find a clear threat, use the 'quarantine_ip' tool immediately.
    Always provide a brief reasoning for your actions."""),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

# 4. Initialize Agent
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 5. Test with a Security Event
raw_logs = """
192.168.1.45 - - [18/Apr/2026:22:15:01] "POST /login HTTP/1.1" 401
192.168.1.45 - - [18/Apr/2026:22:15:02] "POST /login HTTP/1.1" 401
192.168.1.45 - - [18/Apr/2026:22:15:03] "POST /login HTTP/1.1" 401
192.168.1.45 - - [18/Apr/2026:22:15:04] "SELECT * FROM users WHERE id = '1' OR '1'='1'" 200
"""

agent_executor.invoke({"input": f"Analyze these logs and take action: {raw_logs}"})
