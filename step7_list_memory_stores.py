"""
Step 7: List and Inspect Memory Stores
"""
import os
from dotenv import load_dotenv
load_dotenv()

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

print("\n" + "="*60)
print("  STEP 7: LIST MEMORY STORES")
print("="*60)

print("\n📌 Managing Memory Stores")
print("   You can have multiple memory stores in a project.")
print("   Each store can serve different agents or use cases.")
input("\n👉 Press Enter to initialize client...")

# Initialize project client
project_client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)
print("✅ Client initialized!")

input("\n👉 Press Enter to list all memory stores...")

# List all memory stores in the project
stores_list = list(project_client.memory_stores.list())

print("\n" + "="*60)
print(f"  📊 FOUND {len(stores_list)} MEMORY STORE(S)")
print("="*60)

for i, store in enumerate(stores_list, 1):
    print(f"\n  [{i}] Memory Store:")
    print(f"      📁 Name: {store.name}")
    print(f"      📝 Description: {store.description or '(no description)'}")
    print(f"      🆔 ID: {store.id}")

print("\n" + "-"*60)
print("\n💡 Tips:")
print("   • Create separate stores for different agents")
print("   • Each store has its own configuration")
print("   • Stores maintain clean boundaries for memory access")
print("\n💡 Next: Run step8_delete_by_scope.py to delete user memories")
input("\n👉 Press Enter to exit...")
