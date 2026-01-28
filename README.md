# Trail Finder Agent with Memory - Demo Code

This folder contains the complete step-by-step Python code for demonstrating Foundry Agent Memory with a Trail Finder Agent.

## Prerequisites

1. Azure subscription with Foundry project
2. Chat model deployed (e.g., `gpt-4.1`)
3. Embedding model deployed (e.g., `text-embedding-3-small`)
4. Python 3.8+
5. Required packages:
   ```bash
   pip install azure-ai-projects azure-identity
   ```
6. Environment variable set:
   ```powershell
   $env:FOUNDRY_PROJECT_ENDPOINT = "https://{your-ai-services-account}.services.ai.azure.com/api/projects/{project-name}"
   ```

## Demo Steps

### Step 1: Create Memory Store
**File:** `step1_create_memory_store.py`
- Creates memory store with trail-specific profile settings
- Enables user profile and chat summary memory
- Configures what to remember (fitness, preferences, constraints)

### Step 2: Create Agent with Memory Tool
**File:** `step2_create_agent.py`
- Creates Trail Finder Agent
- Attaches MemorySearchTool with scope `hiker_001`
- Sets update delay to 60 seconds for demo

### Step 3: First Conversation - Share Preferences
**File:** `step3_first_conversation.py`
- User shares: knee injury, forest preference, 8km limit, low elevation
- Agent suggests a trail
- Waits 65 seconds for memory consolidation

### Step 4: Second Conversation - Agent Recalls
**File:** `step4_second_conversation.py`
- New conversation (days later simulation)
- User asks for trail WITHOUT repeating preferences
- Agent recalls memory and suggests new trail

### Step 5: Test Memory Isolation
**File:** `step5_test_memory_isolation.py`
- Creates agent with different scope (`hiker_002`)
- Shows that different user has NO access to `hiker_001` memories
- Demonstrates scope-based isolation

### Step 6: Update Preferences Over Time
**File:** `step6_update_preferences.py`
- User shares fitness improvement (can handle elevation now)
- Memory consolidates new fact with old constraints
- Shows memory evolution and conflict resolution

### Step 7: List Memory Stores
**File:** `step7_list_memory_stores.py`
- Lists all memory stores in the project
- Shows store metadata and configuration

### Step 8: Delete by Scope
**File:** `step8_delete_by_scope.py`
- Deletes all memories for `hiker_001`
- Shows agent starts fresh after deletion
- Demonstrates privacy compliance capability

### Step 9: Cleanup
**File:** `step9_cleanup.py`
- Deletes entire memory store
- Irreversible operation
- Removes all memories across all scopes

## Running the Demo

Run each file in order:

```powershell
python step1_create_memory_store.py
python step2_create_agent.py
python step3_first_conversation.py
python step4_second_conversation.py
python step5_test_memory_isolation.py
python step6_update_preferences.py
python step7_list_memory_stores.py
python step8_delete_by_scope.py
python step9_cleanup.py
```

## Key Concepts Demonstrated

- ✅ Memory store creation and configuration
- ✅ Scope-based user isolation
- ✅ Memory types (user profile + chat summaries)
- ✅ Extraction → Consolidation → Retrieval lifecycle
- ✅ Update delay and debouncing
- ✅ Memory evolution over time
- ✅ Privacy controls (deletion by scope)
- ✅ Memory vs chat history distinction

## Notes

- Step 3 and Step 6 include 65-second waits for memory consolidation
- Agent names must match across steps
- Scope values must be consistent for the same user
- Each step is independent but builds on previous setup
