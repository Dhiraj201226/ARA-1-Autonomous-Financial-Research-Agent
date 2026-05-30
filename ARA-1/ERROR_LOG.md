# ERROR_LOG.md

## Error 1: Incorrect Source Reliability Hierarchy

### Location

Section A6.2 – Source Reliability Hierarchy

### Document Statement

Tier 4: Social media posts and anonymous forums

Tier 5: Major news outlets (Reuters, Bloomberg News, Financial Times)

### Why It Is Incorrect

The hierarchy places anonymous social media and forums above professional financial journalism.

Reuters, Bloomberg News, and Financial Times have editorial review, fact-checking, and accountability mechanisms, making them significantly more reliable than anonymous forum discussions.

### Correct Version

SEC Filings > Professional Financial Data Providers > Earnings Calls > Major News Outlets > Social Media / Forums

Reference: Page 21.

## Error 2: Memory Utilization Formula

### Location

Section A5.2 – Metric AB-4

### Document Statement

Memory utilization is defined as a ratio of memory hits to API calls, but then states:

memory_hits multiplied by total_api_calls

### Why It Is Incorrect

A ratio cannot be computed using multiplication.

### Correct Formula

memory_hits / total_api_calls

Reference: Page 19.

## Error 3: SCAP and Dodd-Frank Timeline

### Location

Section A7.3

### Document Statement

"The first US bank stress tests under SCAP were conducted in 2007 following the Dodd-Frank Act."

### Why It Is Incorrect

SCAP stress tests were conducted in 2009.

The Dodd-Frank Act became law in 2010.

Therefore SCAP could not have occurred after Dodd-Frank.

### Correct Version

SCAP occurred in 2009 during the financial crisis and preceded Dodd-Frank.

Reference: Page 24.

## Error 4: Tool Count Inconsistency

### Location

Parts A and B

### Document Statement

The project repeatedly specifies a minimum of 10 tools.

Later, the Full Stack Badge requires successful use of all 12 tools.

### Why It Is Incorrect

The specification alternates between 10-tool and 12-tool requirements without defining two additional mandatory tools.

### Correct Version

The project should consistently specify either 10 or 12 required tools.

Reference: Pages 7–9 and Page 34.

## Error 5: Financial Data API Reliability Ranking

### Location

Section A6.2

### Document Statement

Financial data APIs are ranked above earnings call transcripts.

### Why It Is Potentially Incorrect

The hierarchy treats all financial APIs as universally more reliable than direct management commentary.

In practice, earnings calls are primary-source disclosures while many APIs are secondary aggregators.

The blanket ranking is logically inconsistent.

### Suggested Correction

SEC Filings > Earnings Calls / Official IR > Curated Financial APIs > News > Social Media

Reference: Page 21.

## Error 6: Challenge Difficulty Scaling Conflict

### Location

Challenge Design

### Document Statement

Challenge 8 simulates 50% failure rates while still expecting a complete 15–20 page research report.

### Why It Is Incorrect

A system suffering simultaneous failures of SEC and financial-data tools may not have enough authoritative data to satisfy report completeness requirements.

The evaluation criteria conflict with the graceful degradation requirements defined earlier.

### Correct Version

Report completeness requirements should be reduced when major tool failures occur.

Reference: Graceful degradation requirements and Challenge 8 expectations.

## Error 7: Repository Structure Contradiction

### Location

Day 1–5 instructions versus Required Repository Structure

### Document Statement

Different sections prescribe different repository structures.

### Why It Is Incorrect

The project should define one canonical structure.

The required repository structure later contains files and directories not required in earlier sections.

### Correct Version

The structure in Section D3 should be the authoritative repository layout.

Reference: Page 57.
