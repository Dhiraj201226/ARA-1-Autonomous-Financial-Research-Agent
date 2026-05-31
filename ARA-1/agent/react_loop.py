class ReActLoop:

    def __init__(
        self,
        planner,
        registry,
        synthesizer,
        memory,
        embedder
    ):
        self.planner = planner
        self.registry = registry
        self.synthesizer = synthesizer
        self.memory = memory
        self.embedder = embedder

    def run(
        self,
        query,
        ticker
    ):

        print("\n=== MEMORY CHECK ===")

        query_embedding = self.embedder.embed(
            query
        )

        memory_results = self.memory.search(
            query_embedding,
            n_results=1
        )

        print(
            "Memory Retrieved:",
            memory_results["documents"]
        )

        print("\n=== PLANNING ===")

        tool_names = self.planner.plan(
            query
        )

        results = []

        print("\n=== EXECUTION ===")

        for tool in tool_names:

            print(
                f"\nAction: {tool}"
            )

            observation = (
                self.registry.execute(
                    tool,
                    ticker=ticker
                )
            )

            print(
                f"Observation: {observation}"
            )

            results.append(
                observation
            )

        print("\n=== SYNTHESIS ===")

        combined = (
            self.synthesizer.combine(
                *results
            )
        )

        print(
            "Combined Data:",
            combined
        )

        return combined