from tools import execute_command, read_from_file, write_to_file

tool_list=[execute_command, read_from_file, write_to_file]

tool_map={}

for tool in tool_list:
    tool_map[tool.__name__]=tool

tool_descriptions=[{
    "type": "function",
    "function": {
        "name": "execute_command",
        "description": "Executes terminal commands and returns the output, error, and status.",
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
}, {
    "type": "function",
    "function": {
        "name": "write_to_file",
        "description": "Writes data to a specified file. If the file exists, it will be overwritten.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path to the file where data will be written."
                },
                "data": {
                    "type": "string",
                    "description": "The data to write to the file."
                }
            },
            "required": ["file_path", "data"]
        }
    }
}, {
    "type": "function",
    "function": {
        "name": "read_from_file",
        "description": "Reads data from a specified file and returns it. If the file does not exist, it raises an error.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path to the file to read from."
                }
            },
            "required": ["file_path"]
        }
    }
}]
