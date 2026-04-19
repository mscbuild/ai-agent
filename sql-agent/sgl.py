import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent

# 1. Load the API key (create a .env file with OPENAI_API_KEY=your_key)
load_dotenv()

# 2. Connect to the database (example for SQLite)
# For PostgreSQL, use: "postgresql+psycopg2://user:pass@host:port/dbname"
db = SQLDatabase.from_uri("sqlite:///example.db")

# 3. Initialize the "brain" (LLM)
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# 4. Create the agent
# The agent automatically obtains tools: sql_db_query, sql_db_schema, etc.
agent_executor = create_sql_agent(
llm=llm,
db=db,
agent_type="openai-tools", # Optimal for OpenAI models
verbose=True # To see the agent's "thinking" process
)

# 5. Running the Query
question = "Which user placed the most expensive order and for what amount?"
response = agent_executor.invoke({"input": question})

print("\n--- Final answer ---")
print(response["output"])
