from tools.base_tool import BaseTool

class CalculatorTool(BaseTool):

    @property
    def name(self):
        return "calculator"

    @property
    def description(self):
        return "Financial calculations"

    def execute(self,
                revenue,
                profit):

        margin = (
            profit / revenue
        ) * 100

        return {
            "profit_margin": round(
                margin,
                2
            )
        }