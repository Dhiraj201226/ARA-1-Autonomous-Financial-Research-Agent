import yfinance as yf
from tools.base_tool import BaseTool


class FinanceTool(BaseTool):

    @property
    def name(self):
        return "finance_tool"

    @property
    def description(self):
        return "Gets company financial information"

    def execute(self, ticker):

        stock = yf.Ticker(ticker)

        info = stock.info

        return {
            "company": info.get("longName"),
            "sector": info.get("sector"),
            "market_cap": info.get("marketCap"),
            "current_price": info.get("currentPrice")
        }