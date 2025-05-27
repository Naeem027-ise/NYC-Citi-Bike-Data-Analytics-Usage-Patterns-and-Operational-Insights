### NYC-Citi-Bike-Data-Analytics-Usage-Patterns-and-Operational-Insights

### Problem
Citi Bike lacked a data-driven view of 2022 usage, making it hard to balance docks, schedule rebalancing runs, and target promotions. Raw logs (≈30 M rows) were scattered across 12 CSVs, contained nulls/outliers, and were too large for manual analysis.

### Solution Approach (key steps)

Unified the data pipeline – Concatenated 12 monthly files with Python (pandas), converted 29.8 M rows to typed, deduplicated, and null-free tables, cutting preprocessing time from hours to minutes.

Exploratory visuals in Tableau – Built heatmaps and trend lines that exposed August as the seasonal peak (~3.6 M rides) and Wednesday 6 PM as the busiest slot, guiding rebalancing crew schedules.

Statistical segmentation – Ran Python T-tests showing members ride significantly shorter than casual users (t = –79.5, p < 0.001); used correlation matrices to confirm ride duration is nearly independent of hour-of-day, informing pricing tweaks.

Actionable station insights – Mapped >20 K-trip docks to highlight top 1 % stations for added bikes and flagged low-use areas for marketing pilots.

Deliverables – Interactive Tableau workbook, Jupyter notebook, and a one-page executive brief that translate analytics into concrete capacity-planning, scheduling, and promotion recommendations
