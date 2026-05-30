class ToolRegistry:

    def __init__(self):
        self.tools = {}

    def register(self, tool):

        self.tools[tool.name] = tool

    def get_tool(self, name):

        return self.tools.get(name)

    def list_tools(self):

        return list(self.tools.keys())

    def execute(self, tool_name, **kwargs):

        tool = self.get_tool(tool_name)

        if tool is None:
            raise ValueError(
                f"Tool {tool_name} not found"
            )

        return tool.execute(**kwargs)
    
    def get_tool_descriptions(self):

     return [
        {
            "name": tool.name,
            "description": tool.description
        }
        for tool in self.tools.values()
     ]