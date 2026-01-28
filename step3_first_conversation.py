"""
Step 3: First Conversation - User Shares Trail Preferences
"""
import os
import time
from dotenv import load_dotenv
load_dotenv()

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

print("\n" + "="*60)
print("  STEP 3: FIRST CONVERSATION - SHARING PREFERENCES")
print("="*60)

print("\n📌 What happens in this step?")
print("   The user shares their preferences and constraints.")
print("   The agent will extract and store this information in memory.")
input("\n👉 Press Enter to initialize clients...")

# Initialize project client
project_client = AIProjectClient(
    endpoint=os.environ["FOUNDRY_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)

# Get OpenAI client
openai_client = project_client.get_openai_client()
print("✅ Clients initialized!")

input("\n👉 Press Enter to create a new conversation...")

# Agent details
agent_name = "TrailFinderAgent"

# Create first conversation
conversation = openai_client.conversations.create()
print(f"✅ Conversation created!")
print(f"   ID: {conversation.id}")

input("\n👉 Press Enter to send the user message with preferences...")

# User shares their preferences and constraints
user_message = (
    "I have a knee injury so I need low-impact trails. I prefer forest trails with shade, "
    "and I can handle up to 8 kilometers. I don't like very steep elevation gains."
)

print("\n📌 User Message (containing preferences):")
print("="*50)
print(f"👤 {user_message}")
print("="*50)

input("\n👉 Press Enter to get agent response...")

# Get agent response
response = openai_client.responses.create(
    input=user_message,
    conversation=conversation.id,
    extra_body={"agent": {"name": agent_name, "type": "agent_reference"}},
)

print("\n📌 Agent Response:")
print("="*50)
print(f"🤖 {response.output_text}")
print("="*50)

input("\n👉 Press Enter to wait for memory consolidation...")

print("\n📌 Memory Consolidation Phase:")
print("   The system is now extracting key information from the conversation:")
print("   • Knee injury → mobility constraint")
print("   • Forest trails with shade → terrain preference")
print("   • Up to 8 kilometers → distance limit")
print("   • No steep elevation → elevation constraint")

print("\n⏳ Waiting 65 seconds for memory extraction and consolidation...")
print("   (update_delay is 60 seconds, plus buffer time)")

for i in range(65, 0, -5):
    print(f"   {i} seconds remaining...", end="\r")
    time.sleep(5)

print("\n" + "="*60)
print("  ✅ MEMORY CONSOLIDATION COMPLETE!")
print("="*60)
print("\n   The agent has stored these preferences:")
print("   • Knee injury (low-impact needed)")
print("   • Forest/shade preference")
print("   • 8km distance limit")
print("   • Avoid steep elevation")
print("\n💡 Next: Run step4_second_conversation.py to test memory recall")
input("\n👉 Press Enter to exit...")
