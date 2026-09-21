# Introduction excerpt

Coding agents can lose track of failed repair attempts as tool outputs accumulate. We propose an execution memory that records attempted patches and their test outcomes for use in subsequent steps, without updating model weights. On 300 Python repository issues with two backbone models and a fixed per-issue token budget, the memory-equipped agent resolves 34% and 39% of issues, compared with 30% and 35% for the same agents without memory, respectively.
