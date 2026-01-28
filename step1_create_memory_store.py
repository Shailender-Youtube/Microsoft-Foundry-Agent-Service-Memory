"""
Step 1: Create Memory Store for Trail Finder Agent
"""
import os
from dotenv import load_dotenv
load_dotenv()

from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import MemoryStoreDefaultDefinition, MemoryStoreDefaultOptions
from azure.identity import DefaultAzureCredential

print("\n" + "="*60)
print("  STEP 1: CREATE MEMORY STORE")
print("="*60)

print("\n📌 What is a Memory Store?")
print("   A memory store is a container that holds all memories for an agent.")
print("   It defines WHAT types of information the agent should remember.")
input("\n👉 Press Enter to initialize the project client...")

# Initialize project client
project_client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)
print("✅ Project client initialized!")

input("\n👉 Press Enter to configure memory store options...")

print("\n📌 Configuring Memory Store Options:")
print("   • chat_summary_enabled=True  → Remember context from conversations")
print("   • user_profile_enabled=True  → Remember static user preferences")
print("   • user_profile_details       → What specific info to extract")

memory_store_name = "trail_finder_memory"

# Specify memory store options for trail finder
options = MemoryStoreDefaultOptions(
    chat_summary_enabled=True,
    user_profile_enabled=True,
    user_profile_details=(
        "Focus on fitness level, mobility constraints, preferred trail difficulty, "
        "terrain preferences, distance range, elevation tolerance, weather preferences, "
        "and previously suggested trails. Avoid storing sensitive data like precise home "
        "location or financial information."
    )
)

print("\n✅ Memory options configured:")
print(f"   User Profile Details: {options.user_profile_details[:80]}...")

input("\n👉 Press Enter to create the memory store...")

print("\n📌 Creating Memory Store with:")
print("   • Chat Model: gpt-4.1 (for extraction & consolidation)")
print("   • Embedding Model: text-embedding-3-small (for semantic search)")

# Create memory store
definition = MemoryStoreDefaultDefinition(
    chat_model="gpt-4.1",
    embedding_model="text-embedding-3-small",
    options=options
)

memory_store = project_client.memory_stores.create(
    name=memory_store_name,
    definition=definition,
    description="Memory store for Trail Finder Agent",
)

print("\n" + "="*60)
print("  ✅ MEMORY STORE CREATED SUCCESSFULLY!")
print("="*60)
print(f"\n   Name: {memory_store.name}")
print(f"   Description: {memory_store.description}")
print("\n💡 Next: Run step2_create_agent.py to create the agent")
input("\n👉 Press Enter to exit...")
