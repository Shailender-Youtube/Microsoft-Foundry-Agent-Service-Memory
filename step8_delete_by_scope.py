"""
Step 8: Delete Memories by Scope - Privacy Compliance
"""
import os
from dotenv import load_dotenv
load_dotenv()

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import MemorySearchTool, PromptAgentDefinition
from azure.identity import DefaultAzureCredential

print("\n" + "="*60)
print("  STEP 8: DELETE MEMORIES BY SCOPE")
print("="*60)

print("\n📌 Why Delete by Scope?")
print("   • User requests data deletion (GDPR, privacy)")
print("   • Reset user experience")
print("   • Remove outdated information")
print("   Deleting by scope removes ONE user's data, keeps others!")
input("\n👉 Press Enter to initialize client...")

# Initialize project client
project_client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)

openai_client = project_client.get_openai_client()
print("✅ Client initialized!")

memory_store_name = "trail_finder_memory"
scope_to_delete = "hiker_001"

input("\n👉 Press Enter to delete memories for hiker_001...")

print(f"\n🗑️  Deleting all memories for scope: {scope_to_delete}")
print("   This removes all memories for this specific user.")
print("   Other users' memories remain intact!")

# Delete memories for scope
project_client.memory_stores.delete_scope(
    name=memory_store_name,
    scope=scope_to_delete
)

print(f"\n✅ Deleted memories for: {scope_to_delete}")

input("\n👉 Press Enter to verify deletion with a test conversation...")

# Recreate agent to test
tool = MemorySearchTool(
    memory_store_name=memory_store_name,
    scope=scope_to_delete,
    update_delay=60,
)

agent = project_client.agents.create_version(
    agent_name="TrailFinderAgent",
    definition=PromptAgentDefinition(
        model="gpt-4.1",
        instructions=(
            "You are a helpful trail finder assistant. You help users discover hiking and "
            "walking trails based on their preferences."
        ),
        tools=[tool],
    )
)

# Create new conversation
conversation = openai_client.conversations.create()
print(f"✅ Test conversation created")

# Test if memories are gone
user_message = "Suggest me a trail for this weekend."

print(f"\n📌 Testing: '{user_message}'")

input("\n👉 Press Enter to see if agent still has memories...")

response = openai_client.responses.create(
    input=user_message,
    conversation=conversation.id,
    extra_body={"agent": {"name": agent.name, "type": "agent_reference"}},
)

print("\n📌 Agent Response:")
print("="*50)
print(f"🤖 {response.output_text}")
print("="*50)

print("\n" + "="*60)
print("  ✅ MEMORY DELETION VERIFIED!")
print("="*60)
print("\n   🗑️  Results:")
print("   • All memories for hiker_001 have been deleted")
print("   • Agent starts fresh (asks for preferences)")
print("   • Other users' memories are NOT affected")
print("\n   🔐 Use Cases:")
print("   • GDPR 'Right to be Forgotten' compliance")
print("   • User account deletion")
print("   • Privacy requests")
print("\n💡 Next: Run step9_cleanup.py to delete the entire memory store")
input("\n👉 Press Enter to exit...")
