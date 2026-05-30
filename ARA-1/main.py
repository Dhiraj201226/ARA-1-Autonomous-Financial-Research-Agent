from tools.tool_registry import ToolRegistry
from tools.schemas.finance_schema import FINANCE_SCHEMA
from tools.finance_tool import FinanceTool
from tools.calculator import CalculatorTool
from tools.report_generator import ReportGenerator
from tools.sec_tool import SECTool

registry = ToolRegistry()
registry.register(
    SECTool()
)
registry.register(
    FinanceTool()
)
registry.register(
    CalculatorTool()
)
from agent.synthesizer import Synthesizer

synthesizer = Synthesizer()
registry.register(
    ReportGenerator()
)

finance_data = registry.execute(
    "finance_tool",
    ticker="AAPL"
)

sec_data = registry.execute(
    "sec_tool",
    ticker="AAPL"
)


combined_data = synthesizer.combine(
finance_data,
    sec_data
)
report = registry.execute(
    "report_generator",
    data=combined_data
)



from rag.embedder import Embedder

embedder = Embedder()

from rag.embedder import Embedder
from memory.long_term import LongTermMemory

embedder = Embedder()

memory = LongTermMemory()

# memory.store(
#     "doc1",
#     "Apple reported strong revenue growth",
#     embedder.embed(
#         "Apple reported strong revenue growth"
#     )
# )

# memory.store(
#     "doc2",
#     "Tesla expanded vehicle production",
#     embedder.embed(
#         "Tesla expanded vehicle production"
#     )
# )

# memory.store(
#     "doc3",
#     "NVIDIA dominates AI chips",
#     embedder.embed(
#         "NVIDIA dominates AI chips"
#     )
# )
query = embedder.embed(
    "How leads AI hardware?"
)

results = memory.search(
    query
)

print(results["documents"])