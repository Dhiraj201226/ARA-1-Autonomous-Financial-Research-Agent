from tools.base_tool import BaseTool


class ReportGenerator(BaseTool):

    @property
    def name(self):
        return "report_generator"

    @property
    def description(self):
        return "Generate formatted report"

    def execute(self, data):

        report = f"""
========================
COMPANY REPORT
========================

Company:
{data.get("company")}

Sector:
{data.get("sector")}

Current Price:
{data.get("current_price")}

Market Cap:
{data.get("market_cap")}
"""

        return report