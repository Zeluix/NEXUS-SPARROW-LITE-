"""
SPARROW - Mini Local Agent
===========================
Lightweight persona-locked agent for Qwen 2.5 0.5B running on Ollama.
Part of the MEGANX ecosystem.
"""

import subprocess
import re
from typing import Optional

# ============================================================================
# CONFIGURATION
# ============================================================================

SPARROW_MODEL = "sparrow:latest"  # Custom model created from Modelfile
FALLBACK_MODEL = "qwen2.5:0.5b"   # Fallback if custom model not available
SIGNATURE = "[SPARROW]:"

# ============================================================================
# MESSAGE SANITIZER
# ============================================================================

def sanitize_message(message: str) -> str:
    """
    Sanitize user input to prevent injection attacks.
    Removes attempts to override system prompt or persona.
    """
    # Dangerous patterns that could break persona
    dangerous_patterns = [
        r"<\|system\|>",
        r"<\|IDENTITY\|>",
        r"<\|CONSTRAINTS",
        r"<<CONTEXT-ENVELOPE",
        r"ignore.*previous.*instructions",
        r"forget.*everything",
        r"you are now",
        r"pretend to be",
        r"act as",
        r"roleplay as",
    ]
    
    sanitized = message
    for pattern in dangerous_patterns:
        sanitized = re.sub(pattern, "[BLOCKED]", sanitized, flags=re.IGNORECASE)
    
    return sanitized


# ============================================================================
# SIGNATURE VALIDATION
# ============================================================================

def validate_signature(response: str) -> tuple[bool, str]:
    """
    Validate that response starts with SPARROW signature.
    If missing, prepend it to maintain persona consistency.
    """
    if response.strip().startswith(SIGNATURE):
        return True, response
    
    # Signature missing - prepend it
    corrected = f"{SIGNATURE} {response}"
    return False, corrected


# ============================================================================
# CORE AGENT
# ============================================================================

class SparrowAgent:
    """
    SPARROW Mini-Agent wrapper for Ollama.
    Implements persona anchoring with validation layer.
    """
    
    def __init__(self, model: str = SPARROW_MODEL):
        self.model = model
        self.history = []
        
    def _call_ollama(self, prompt: str) -> str:
        """Call Ollama CLI and return response."""
        try:
            result = subprocess.run(
                ["ollama", "run", self.model, prompt],
                capture_output=True,
                text=True,
                timeout=60
            )
            return result.stdout.strip()
        except subprocess.TimeoutExpired:
            return f"{SIGNATURE} [TIMEOUT] Request took too long. Try a simpler question."
        except Exception as e:
            return f"{SIGNATURE} [ERROR] Failed to process: {str(e)}"
    
    def chat(self, user_message: str) -> str:
        """
        Send a message to SPARROW with full protection.
        
        1. Sanitize input
        2. Call model
        3. Validate signature
        4. Return response
        """
        # Step 1: Sanitize
        clean_message = sanitize_message(user_message)
        
        # Step 2: Call Ollama
        raw_response = self._call_ollama(clean_message)
        
        # Step 3: Validate signature
        is_valid, final_response = validate_signature(raw_response)
        
        if not is_valid:
            print("[SPARROW-SYSTEM] Signature was missing, auto-corrected.")
        
        # Step 4: Store in history
        self.history.append({
            "user": clean_message,
            "assistant": final_response
        })
        
        return final_response
    
    def reset(self):
        """Reset conversation history."""
        self.history = []
        return f"{SIGNATURE} Memory cleared. Ready for new conversation."


# ============================================================================
# CLI INTERFACE
# ============================================================================

def main():
    """Interactive CLI for SPARROW."""
    print("=" * 50)
    print("  SPARROW - Mini Local Agent")
    print("  Part of the MEGANX Ecosystem")
    print("  Type 'exit' to quit, 'reset' to clear memory")
    print("=" * 50)
    print()
    
    agent = SparrowAgent()
    
    # Initial greeting
    print(f"{SIGNATURE} Online. Running on local hardware. How can I help?")
    print()
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() == "exit":
                print(f"\n{SIGNATURE} Goodbye, Architect.")
                break
            
            if user_input.lower() == "reset":
                print(agent.reset())
                continue
            
            response = agent.chat(user_input)
            print(f"\n{response}\n")
            
        except KeyboardInterrupt:
            print(f"\n\n{SIGNATURE} Interrupted. Goodbye.")
            break


if __name__ == "__main__":
    main()
