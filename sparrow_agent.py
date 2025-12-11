"""
SPARROW - Mini Local Agent with Tools
======================================
Lightweight agent with actual capabilities:
- File operations
- System info
- Calculator
- Date/Time
Part of the MEGANX ecosystem.
"""

import subprocess
import os
import datetime
import platform
import re
from pathlib import Path

# ============================================================================
# CONFIGURATION
# ============================================================================

SPARROW_MODEL = "sparrow"
SIGNATURE = "[SPARROW]:"

# ============================================================================
# TOOLS - Agent Capabilities
# ============================================================================

def tool_list_files(path: str = ".") -> str:
    """List files in a directory."""
    try:
        files = os.listdir(path)
        if not files:
            return f"📁 Directory '{path}' is empty."
        result = f"📁 Files in '{path}':\n"
        for f in files[:20]:  # Limit to 20
            full_path = os.path.join(path, f)
            if os.path.isdir(full_path):
                result += f"  📂 {f}/\n"
            else:
                size = os.path.getsize(full_path)
                result += f"  📄 {f} ({size} bytes)\n"
        return result
    except Exception as e:
        return f"❌ Error: {str(e)}"

def tool_read_file(path: str) -> str:
    """Read a text file (first 500 chars)."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read(500)
            if len(content) == 500:
                content += "\n... (truncated)"
            return f"📄 Content of '{path}':\n{content}"
    except Exception as e:
        return f"❌ Error reading file: {str(e)}"

def tool_system_info() -> str:
    """Get system information."""
    info = f"""💻 System Info:
  OS: {platform.system()} {platform.release()}
  Machine: {platform.machine()}
  Processor: {platform.processor()}
  Python: {platform.python_version()}
  User: {os.getenv('USERNAME', 'unknown')}
  CWD: {os.getcwd()}
"""
    return info

def tool_datetime() -> str:
    """Get current date and time."""
    now = datetime.datetime.now()
    return f"🕐 Date/Time: {now.strftime('%Y-%m-%d %H:%M:%S')}"

def tool_calculate(expression: str) -> str:
    """Safe calculator for basic math."""
    try:
        # Only allow safe characters
        if not re.match(r'^[\d\s\+\-\*\/\.\(\)]+$', expression):
            return "❌ Invalid expression. Use only: 0-9 + - * / . ( )"
        result = eval(expression)
        return f"🧮 {expression} = {result}"
    except Exception as e:
        return f"❌ Calculation error: {str(e)}"

def tool_disk_space() -> str:
    """Check disk space."""
    try:
        if platform.system() == "Windows":
            import shutil
            total, used, free = shutil.disk_usage("C:")
            return f"""💾 Disk Space (C:):
  Total: {total // (1024**3)} GB
  Used: {used // (1024**3)} GB
  Free: {free // (1024**3)} GB"""
        else:
            return "💾 Disk check only available on Windows"
    except Exception as e:
        return f"❌ Error: {str(e)}"

# ============================================================================
# TOOL DISPATCHER
# ============================================================================

TOOLS = {
    "files": tool_list_files,
    "read": tool_read_file,
    "system": tool_system_info,
    "time": tool_datetime,
    "calc": tool_calculate,
    "disk": tool_disk_space,
}

def parse_tool_command(user_input: str) -> tuple:
    """Parse /command syntax."""
    if user_input.startswith("/"):
        parts = user_input[1:].split(" ", 1)
        cmd = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else None
        return cmd, arg
    return None, None

def execute_tool(cmd: str, arg: str) -> str:
    """Execute a tool command."""
    if cmd == "help":
        return """🛠️ Available Commands:
  /files [path]  - List files in directory
  /read <file>   - Read a text file
  /system        - System information
  /time          - Current date/time
  /calc <expr>   - Calculator (e.g., /calc 2+2)
  /disk          - Disk space info
  /help          - Show this help
"""
    
    if cmd in TOOLS:
        tool = TOOLS[cmd]
        if arg:
            return tool(arg)
        else:
            return tool()
    
    return f"❌ Unknown command: /{cmd}. Type /help for available commands."

# ============================================================================
# LLM CALLER
# ============================================================================

def call_sparrow(prompt: str) -> str:
    """Call SPARROW via Ollama."""
    try:
        result = subprocess.run(
            ["ollama", "run", SPARROW_MODEL, prompt],
            capture_output=True,
            text=True,
            timeout=60
        )
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return f"{SIGNATURE} [TIMEOUT] Request took too long."
    except Exception as e:
        return f"{SIGNATURE} [ERROR] {str(e)}"

# ============================================================================
# MAIN AGENT LOOP
# ============================================================================

def main():
    print("=" * 50)
    print("  🐦 SPARROW - Mini Local Agent")
    print("  Part of the MEGANX Ecosystem")
    print("  Type /help for commands, 'exit' to quit")
    print("=" * 50)
    print()
    print(f"{SIGNATURE} Online. Ready to assist!")
    print()
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() == "exit":
                print(f"\n{SIGNATURE} Goodbye, Architect! 🐦")
                break
            
            # Check for tool commands
            cmd, arg = parse_tool_command(user_input)
            if cmd:
                result = execute_tool(cmd, arg)
                print(f"\n{result}\n")
                continue
            
            # Otherwise, use LLM
            response = call_sparrow(user_input)
            print(f"\n{response}\n")
            
        except KeyboardInterrupt:
            print(f"\n\n{SIGNATURE} Interrupted. Goodbye!")
            break


if __name__ == "__main__":
    main()
