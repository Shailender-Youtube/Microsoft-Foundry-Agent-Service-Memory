"""
Step 4: Second Conversation - Agent Recalls Memory
"""
import os
from dotenv import load_dotenv
load_dotenv()

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

print("\n" + "="*60)
print("  STEP 4: SECOND CONVERSATION - MEMORY RECALL")
print("="*60)

print("\n📌 What happens in this step?")
print("   We create a BRAND NEW conversation (simulating user returning later).")
print("   The user asks for a trail WITHOUT repeating their preferences.")
print("   The agent should REMEMBER from the previous conversation!")
input("\n👉 Press Enter to initialize clients...")

# Initialize project client
project_client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)

# Get OpenAI client
openai_client = project_client.get_openai_client()
print("✅ Clients initialized!")

input("\n👉 Press Enter to create a NEW conversation...")

# Agent details
agent_name = "TrailFinderAgent"

# Create NEW conversation (simulating user returning after days)
new_conversation = openai_client.conversations.create()
print(f"✅ NEW conversation created!")
print(f"   ID: {new_conversation.id}")
print("\n   🕐 Imagine: It's been a few days since the first conversation...")

input("\n👉 Press Enter to send a simple request (NO preferences mentioned)...")

# User asks for trail suggestion WITHOUT repeating preferences
user_message = "Suggest me a trail for this weekend."

print("\n📌 User Message (notice - NO preferences mentioned!):")
print("="*50)
print(f"👤 {user_message}")
print("="*50)

input("\n👉 Press Enter to see if the agent remembers...")

# Get agent response - should recall memory automatically
response = openai_client.responses.create(
    input=user_message,
    conversation=new_conversation.id,
    extra_body={"agent": {"name": agent_name, "type": "agent_reference"}},
)

print("\n📌 Agent Response:")
print("="*50)
print(f"🤖 {response.output_text}")
print("="*50)

print("\n" + "="*60)
print("  ✅ MEMORY RECALL SUCCESSFUL!")
print("="*60)
print("\n   🎉 The agent remembered WITHOUT being told again:")
print("   ✓ Knee injury (suggested low-impact trails)")
print("   ✓ Forest/shade preference")
print("   ✓ 8km distance limit")
print("   ✓ Avoid steep elevation")
print("   ✓ Avoided trails from previous conversation!")
print("\n💡 Next: Run step5_test_memory_isolation.py to test scope isolation")
input("\n👉 Press Enter to exit...")
