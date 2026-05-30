# agent/synthesizer.py

class Synthesizer:

    def combine(self, *sources):

        combined = {}

        for source in sources:
            combined.update(source)

        return combined