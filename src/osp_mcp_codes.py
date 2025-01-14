import os
from mcp.server.fastmcp import FastMCP

server = FastMCP(
    "OSPEditingCodes",
    dependencies=[
        "pydantic>=2.0",
    ]
)

@server.resource("osp://editing-codes")
def get_osp_editing_codes() -> str:
    """Get the OSP editing codes documentation"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(script_dir, 'codes-llm.md'), 'r') as f:
            content = f.read()
            # Debug print to see what we're actually reading
            print("Content first 50 characters:", repr(content[:50]))
            return content
    except FileNotFoundError as e:
        print(f"File not found error: {e}")
        print(f"Attempted path: {os.path.join(script_dir, 'codes-llm.md')}")
        print(f"Current directory: {os.getcwd()}")
        raise FileNotFoundError(
            "Required file 'codes-llm.md' not found. "
            "This file must be present in the same directory as the script."
        )

if __name__ == "__main__":
    try:
        print(f"Starting server from directory: {os.getcwd()}")
        server.run()
    except Exception as e:
        print(f"Server failed to start: {str(e)}")
        print(f"Error type: {type(e)}")
        # Print the full error traceback
        import traceback
        traceback.print_exc()
        raise