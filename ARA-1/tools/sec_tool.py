from tools.base_tool import BaseTool


class SECTool(BaseTool):

    @property
    def name(self):
        return "sec_tool"

    @property
    def description(self):
        return "Get SEC filing information"

    def execute(self, ticker):

        return {
            "ticker": ticker,
            "filing_type": "10-K",
            "risk_factor":
                "Competition in AI market",
            "business_summary":
                "Technology company"
        }