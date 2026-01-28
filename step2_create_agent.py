"""
Step 2: Create Trail Finder Agent with Memory Tool
"""
import os
from dotenv import load_dotenv
load_dotenv()

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import MemorySearchTool, PromptAgentDefinition
from azure.identity import DefaultAzureCredential

print("\n" + "="*60)
print("  STEP 2: CREATE AGENT WITH MEMORY TOOL")
print("="*60)

print("\n📌 What is a Memory Search Tool?")
print("   It's a tool that lets the agent READ from and WRITE to memory.")
print("   The agent automatically uses stored memories during conversations.")
input("\n👉 Press Enter to initialize the project client...")

# Initialize project client
project_client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)
print("✅ Project client initialized!")

input("\n👉 Press Enter to configure the Memory Search Tool...")

memory_store_name = "trail_finder_memory"
scope = "hiker_001"  # Unique identifier for this user

print("\n📌 Memory Search Tool Configuration:")
print(f"   • memory_store_name: {memory_store_name}")
print(f"   • scope: {scope}  (isolates memories per user)")
print("   • update_delay: 60 seconds (debounce before saving)")

# Create memory search tool
tool = MemorySearchTool(
    memory_store_name=memory_store_name,
    scope=scope,
    update_delay=60,
)
print("\n✅ Memory Search Tool configured!")

input("\n👉 Press Enter to create the agent...")

print("\n📌 Creating Trail Finder Agent:")
print("   • Model: gpt-4.1")
print("   • Tool: MemorySearchTool (for persistent memory)")
print("   • Instructions: Help users find trails based on their preferences")

# Create a prompt agent with memory search tool
agent = project_client.agents.create_version(
    agent_name="TrailFinderAgent",
    definition=PromptAgentDefinition(
        model="gpt-4.1",
        instructions=(
            "You are a helpful trail finder assistant. You help users discover hiking and "
            "walking trails based on their preferences, fitness level, and constraints. "
            "Always consider their past preferences and avoid suggesting trails they've already tried. "
            "Be friendly, encouraging, and safety-conscious."
        ),
        tools=[tool],
    )
)

print("\n" + "="*60)
print("  ✅ AGENT CREATED SUCCESSFULLY!")
print("="*60)
print(f"\n   Agent ID: {agent.id}")
print(f"   Agent Name: {agent.name}")
print(f"   Version: {agent.version}")
print(f"   Memory Store: {memory_store_name}")
print(f"   Scope: {scope}")
print("\n💡 Next: Run step3_first_conversation.py to start a conversation")
input("\n👉 Press Enter to exit...")
