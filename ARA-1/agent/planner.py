# agent/planner.py

class Planner:

    def plan(self, query):

        query = query.lower()

        tools = []

        if "analyze" in query:
            tools.append("finance_tool")
            tools.append("sec_tool")

        return tools