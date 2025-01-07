from tools import execute_command

tool_list=[execute_command]

tool_map={}

for tool in tool_list:
    tool_map[tool.__name__]=tool

tool_descriptions=[{
    "type": "function",
    "function": {
        "name": "execute_command",
        "description": '''Executes terminal commands and returns the output, error, and status.''',
        "parameters": {
            "type": "object",
            "properties": {
            "command": {
                "type": "string",
                "description": "The terminal command to execute."
            }
            },
            "required": ["command"]
        }
    }
}]