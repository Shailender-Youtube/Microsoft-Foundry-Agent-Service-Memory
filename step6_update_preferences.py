"""
Step 6: Update Preferences Over Time - Memory Evolution
"""
import os
import time
from dotenv import load_dotenv
load_dotenv()

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import MemorySearchTool, PromptAgentDefinition
from azure.identity import DefaultAzureCredential

print("\n" + "="*60)
print("  STEP 6: MEMORY EVOLUTION - UPDATING PREFERENCES")
print("="*60)

print("\n📌 What happens when preferences change?")
print("   Memory isn't static - it evolves over time!")
print("   When new info conflicts with old, memory consolidates.")
print("   The system keeps the most recent, relevant information.")
input("\n👉 Press Enter to initialize clients...")

# Initialize project client
project_client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)

# Get OpenAI client
openai_client = project_client.get_openai_client()
print("✅ Clients initialized!")

input("\n👉 Press Enter to recreate agent for hiker_001...")

memory_store_name = "trail_finder_memory"
scope = "hiker_001"

# Recreate agent for hiker_001 (since we deleted memories in step8)
tool = MemorySearchTool(
    memory_store_name=memory_store_name,
    scope=scope,
    update_delay=60,
)

agent = project_client.agents.create_version(
    agent_name="TrailFinderAgent",
    definition=PromptAgentDefinition(
        model="gpt-4.1",
        instructions=(
            "You are a helpful trail finder assistant. You help users discover hiking and "
            "walking trails based on their preferences, fitness level, and constraints. "
            "Always consider their past preferences."
        ),
        tools=[tool],
    )
)
print(f"✅ Agent ready for hiker_001")

input("\n👉 Press Enter to create conversation...")

# Create conversation
conversation = openai_client.conversations.create()
print(f"✅ Conversation created")
print(f"   ID: {conversation.id}")

input("\n👉 Press Enter to share UPDATED fitness information...")

# User shares updated information
user_message = (
    "I've been doing strength training for 3 weeks now. I think I can handle "
    "slightly more challenging trails with moderate elevation."
)

print("\n📌 User Message (sharing improvement):")
print("="*50)
print(f"👤 {user_message}")
print("="*50)

print("\n📌 What the memory system will do:")
print("   OLD: 'No steep elevation' (from knee injury)")
print("   NEW: 'Can handle moderate elevation' (fitness improved)")
print("   → Memory consolidation will reconcile these!")

input("\n👉 Press Enter to get response...")

# Get response
response = openai_client.responses.create(
    input=user_message,
    conversation=conversation.id,
    extra_body={"agent": {"name": agent.name, "type": "agent_reference"}},
)

print("\n📌 Agent Response:")
print("="*50)
print(f"🤖 {response.output_text}")
print("="*50)

input("\n👉 Press Enter to wait for memory consolidation...")

print("\n⏳ Waiting 65 seconds for memory to update...")
for i in range(65, 0, -5):
    print(f"   {i} seconds remaining...", end="\r")
    time.sleep(5)

print("\n✅ Memory updated!")

input("\n👉 Press Enter to test with a new conversation...")

# Create another new conversation to test updated memory
new_conversation = openai_client.conversations.create()
print(f"✅ New conversation created")
print(f"   ID: {new_conversation.id}")

# Test updated memory
test_message = "Recommend a trail for today."

print(f"\n📌 Testing with: '{test_message}'")

input("\n👉 Press Enter to see updated recommendations...")

test_response = openai_client.responses.create(
    input=test_message,
    conversation=new_conversation.id,
    extra_body={"agent": {"name": agent.name, "type": "agent_reference"}},
)

print("\n📌 Agent Response (with updated memory):")
print("="*50)
print(f"🤖 {test_response.output_text}")
print("="*50)

print("\n" + "="*60)
print("  ✅ MEMORY EVOLUTION DEMONSTRATED!")
print("="*60)
print("\n   🔄 The memory has evolved:")
print("   • Kept: Forest preference, knee awareness")
print("   • Updated: Can now handle moderate elevation")
print("   • Result: Suggestions adapt to current fitness level!")
print("\n💡 Next: Run step7_list_memory_stores.py to inspect stores")
input("\n👉 Press Enter to exit...")
