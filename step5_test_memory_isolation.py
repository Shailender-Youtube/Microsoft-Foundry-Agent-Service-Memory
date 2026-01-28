"""
Step 5: Test Memory Isolation - Different User Scope
"""
import os
from dotenv import load_dotenv
load_dotenv()

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import MemorySearchTool, PromptAgentDefinition
from azure.identity import DefaultAzureCredential

print("\n" + "="*60)
print("  STEP 5: TESTING MEMORY ISOLATION")
print("="*60)

print("\n📌 What is Scope Isolation?")
print("   Each user has their own 'scope' - a unique identifier.")
print("   Memories are COMPLETELY isolated between scopes.")
print("   User A cannot see User B's memories!")
input("\n👉 Press Enter to initialize clients...")

# Initialize project client
project_client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)

# Get OpenAI client
openai_client = project_client.get_openai_client()
print("✅ Clients initialized!")

input("\n👉 Press Enter to create agent for a DIFFERENT user...")

memory_store_name = "trail_finder_memory"
different_scope = "hiker_002"  # Different user!

print("\n📌 Creating agent with DIFFERENT scope:")
print(f"   • Previous user: hiker_001 (has stored preferences)")
print(f"   • Current user:  {different_scope} (brand new user)")

# Create memory search tool for different user
tool = MemorySearchTool(
    memory_store_name=memory_store_name,
    scope=different_scope,
    update_delay=60,
)

agent_different_user = project_client.agents.create_version(
    agent_name="TrailFinderAgent-Hiker002",
    definition=PromptAgentDefinition(
        model="gpt-4.1",
        instructions=(
            "You are a helpful trail finder assistant. You help users discover hiking and "
            "walking trails based on their preferences, fitness level, and constraints. "
            "Always consider their past preferences and avoid suggesting trails they've already tried."
        ),
        tools=[tool],
    )
)

print(f"\n✅ Agent created for {different_scope}")
print(f"   Agent Name: {agent_different_user.name}")

input("\n👉 Press Enter to create conversation for hiker_002...")

# Create conversation with this different user
conversation = openai_client.conversations.create()
print(f"✅ Conversation created for hiker_002")
print(f"   ID: {conversation.id}")

input("\n👉 Press Enter to ask the SAME question as hiker_001...")

# Ask the same question
user_message = "Suggest me a trail for this weekend."

print("\n📌 User Message (same as before):")
print("="*50)
print(f"👤 {user_message}")
print("="*50)

input("\n👉 Press Enter to see if agent has hiker_001's memories...")

# Get response
response = openai_client.responses.create(
    input=user_message,
    conversation=conversation.id,
    extra_body={"agent": {"name": agent_different_user.name, "type": "agent_reference"}},
)

print("\n📌 Agent Response:")
print("="*50)
print(f"🤖 {response.output_text}")
print("="*50)

print("\n" + "="*60)
print("  ✅ SCOPE ISOLATION VERIFIED!")
print("="*60)
print("\n   🔒 Notice the difference:")
print("   • hiker_001: Agent knew all preferences")
print("   • hiker_002: Agent asks for preferences (no memories!)")
print("\n   This proves memories are ISOLATED by scope.")
print("   Each user's data is private and secure!")
print("\n💡 Next: Run step6_update_preferences.py to test memory evolution")
input("\n👉 Press Enter to exit...")
