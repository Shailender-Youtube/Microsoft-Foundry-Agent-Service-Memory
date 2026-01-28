"""
Step 9: Cleanup - Delete Entire Memory Store
"""
import os
from dotenv import load_dotenv
load_dotenv()

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

print("\n" + "="*60)
print("  STEP 9: CLEANUP - DELETE MEMORY STORE")
print("="*60)

print("\n⚠️  WARNING: This step deletes the ENTIRE memory store!")
print("   • All memories across ALL scopes will be deleted")
print("   • All users lose their stored preferences")
print("   • This operation is IRREVERSIBLE!")
input("\n👉 Press Enter to initialize client...")

# Initialize project client
project_client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)
print("✅ Client initialized!")

memory_store_name = "trail_finder_memory"

input("\n👉 Press Enter to see current memory stores...")

# List current stores
stores_list = list(project_client.memory_stores.list())
print(f"\n📊 Current memory stores ({len(stores_list)}):")
for store in stores_list:
    print(f"   • {store.name}")

input(f"\n👉 Press Enter to DELETE '{memory_store_name}'...")

print(f"\n🗑️  Deleting memory store: {memory_store_name}")
print("   This will remove:")
print("   • All user profile memories")
print("   • All chat summary memories")
print("   • All scopes and their data")

# Delete the entire memory store
delete_response = project_client.memory_stores.delete(memory_store_name)

print(f"\n✅ Memory store deleted: {delete_response.deleted}")

input("\n👉 Press Enter to verify deletion...")

# Verify deletion
remaining_stores = list(project_client.memory_stores.list())
print(f"\n📊 Remaining memory stores ({len(remaining_stores)}):")
if remaining_stores:
    for store in remaining_stores:
        print(f"   • {store.name}")
else:
    print("   (none)")

trail_store_exists = any(s.name == memory_store_name for s in remaining_stores)
if not trail_store_exists:
    print(f"\n✅ Confirmed: '{memory_store_name}' has been deleted!")

print("\n" + "="*60)
print("  ✅ CLEANUP COMPLETE!")
print("="*60)
print("\n   🧹 Results:")
print(f"   • Memory store '{memory_store_name}' deleted")
print("   • All associated memories removed")
print("   • Agents using this store will lose memory access")
print("\n   📝 Note:")
print("   • To re-run the demo, start from step1_create_memory_store.py")
print("   • Each run creates fresh infrastructure")

print("\n" + "="*60)
print("  🎉 DEMO COMPLETE!")
print("="*60)
print("\n   You have learned:")
print("   ✓ How to create memory stores")
print("   ✓ How to attach memory to agents")
print("   ✓ How memory persists across conversations")
print("   ✓ How scope isolates user memories")
print("   ✓ How memory evolves over time")
print("   ✓ How to manage and delete memories")
print("\n   Thank you for watching! 🙏")
input("\n👉 Press Enter to exit...")
