Based on my analysis of these issues, here are the **complex, time-intensive issues (6+ hours) that would be difficult for AI to solve (target: 0-40% AI solve rate)**:

## 🔴 **Top Candidates for AI Training Data:**

### 1. **#17833: WAL corruption stops compaction indefinitely**

- **Complexity**: High (5/5)
- **Time**: 6-8+ hours
- **Why AI-hard**:
    - Requires deep TSDB compaction understanding
    - Complex edge cases around WAL corruption
    - Safety-critical: wrong fix could cause data loss
    - Need to understand retention policies + compaction lifecycle
    - Design decision: skip corrupted segments vs fail-safe

### 2. **#17857: RW2 sends disconnected exemplars without samples**

- **Complexity**: High (5/5)
- **Time**: 8-12+ hours
- **Why AI-hard**:
    - Requires understanding Remote Write 2.0 spec deeply
    - Complex architectural change (exemplar-per-series → exemplar-per-sample)
    - Storage layer interaction complexity
    - Sharding implications
    - Multiple codepaths (WAL, storage, sending)

### 3. **#17900: Move scrape.isSeriesPartOfFamily to text parser and optimize**

- **Complexity**: Medium-High (4/5)
- **Time**: 6-8 hours
- **Why AI-hard**:
    - Parser optimization with correctness requirements
    - Edge cases in text format parsing
    - Performance-critical (expensive operation)
    - AppenderV2 flow integration
    - Metadata API implications

### 4. **#17862: Sporadic histogram_quantile results with NHCB conversion**

- **Complexity**: Very High (5/5)
- **Time**: 8-12+ hours
- **Why AI-hard**:
    - Intermittent/sporadic bug (hardest to debug)
    - Native histogram with custom buckets (NHCB) complexity
    - Aggregation + rate calculation interaction
    - Requires understanding histogram conversion logic
    - Data corruption investigation
    - May span scraping → ingestion → query execution

### 5. **#17799: sort_by_label does not sort numbers in scientific notation**

- **Complexity**: Medium (3-4/5)
- **Time**: 4-6 hours
- **Why AI-hard**:
    - Natural sort algorithm modification
    - Edge cases (e.g., `foo2e4bar` should NOT parse as scientific)
    - Performance considerations (sorting is hot path)
    - Need to handle multiple number formats correctly

## 🟡 **Medium Complexity (borderline):**

### 6. **#17950: Missing hash shard lock in deleteSeriesByID**

- **Complexity**: Medium (3/5)
- **Time**: 3-5 hours
- **Why somewhat AI-hard**: Concurrency bugs, but solution is already outlined in issue

### 7. **#17931: info() function incorrectly handles negated **name** matchers**

- **Complexity**: Medium (3/5)
- **Time**: 4-6 hours
- **Root cause identified**, but fix requires careful handling of matcher logic

### 8. **#17841: Validate bad requests around sample ordering/dups**

- **Complexity**: Medium-High (4/5)
- **Time**: 6-8 hours
- **Investigation + design** required, not just implementation

## 📊 **My Recommendation:**

For AI training data, I'd suggest **#17833 (WAL corruption), #17857 (RW2 exemplars), or #17862 (NHCB histogram bug)** because:

- All are 6-12+ hour problems
- Complex architectural/design decisions required
- Multiple interacting components
- Safety/correctness critical
- Likely 0-20% AI solve rate

**Which one interests you most?**