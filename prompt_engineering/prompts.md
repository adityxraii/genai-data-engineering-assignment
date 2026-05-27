# Prompt 1 – SQL Optimization

Context:
I am working with a sales warehouse containing billions of rows.

Role:
Act as Senior Data Warehouse Optimization Engineer.

Task:
Optimize SQL query performance.

Constraints:
- Focus on performance only
- Assume Snowflake / Databricks
- Reduce scans

Format:
1. Optimized SQL
2. Explanation
3. Improvements



# Prompt 2 – Data Quality

Context:
Dataset contains null values, duplicates and invalid dates.

Role:
Act as Senior Data Quality Engineer.

Task:
Suggest cleaning strategy.

Constraints:
- Preserve business rules
- Avoid deleting data unnecessarily

Format:
{
cleaning_steps:[],
validation_rules:[],
recommendations:[]
}



# Prompt 3 – ETL Monitoring

Context:
Night ETL jobs fail intermittently.

Role:
Act as DataOps Specialist.

Task:
Identify root cause.

Constraints:
- Prioritize failures
- Assume Azure pipeline

Format:
1. Cause
2. Severity
3. Solution
4. Prevention