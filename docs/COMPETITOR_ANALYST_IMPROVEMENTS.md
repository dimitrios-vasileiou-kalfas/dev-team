# Competitor Analyst Agent Improvements

## Issues Fixed

The competitor analyst was producing **shallow, generic analysis** that missed critical details. Here's what was fixed:

### Problem Analysis

**Root Causes:**
1. ❌ No tools to systematically read files
2. ❌ Generic instructions without methodology  
3. ❌ No guidance on what to look for specifically
4. ❌ High temperature (default) causing creative but inaccurate output
5. ❌ No emphasis on reading ALL files thoroughly

**Result:** Agent made assumptions instead of reading code, missed external integrations, database schema, security issues, and specific implementation details.

## Solutions Implemented

### 1. Created File Reading Tools ✅

**New Tools in `tools/custom_tool.py`:**

```python
FileReaderTool()        # Reads file contents (up to 50k chars)
DirectoryListTool()     # Lists directory structure (recursive option)
FindFilesTool()         # Finds files matching patterns (*.php, *.js, etc.)
```

**Why This Helps:**
- Agent can now systematically explore the codebase
- Can locate README, main plugin file, configuration files
- Can read all PHP/JS files to understand implementation
- No more guessing - actual code reading

### 2. Enhanced Agent Configuration ✅

**Added in `agents.yaml`:**

```yaml
competitor_analyst:
  llm: ollama/qwen3-coder:30b
  temperature: 0.1      # NEW: Low temp for precise technical analysis
  max_iter: 30          # NEW: More iterations to read all files
  tools:                # NEW: File reading tools
    - list_directory
    - read_file
    - find_files
```

**Why This Helps:**
- **temperature: 0.1** → More deterministic, less creative interpretation
- **max_iter: 30** → Can perform more tool actions (read more files)
- **tools** → Agent knows it CAN and SHOULD use these tools

### 3. Systematic Analysis Methodology ✅

**Added detailed workflow in backstory:**

```
YOUR METHODOLOGY (FOLLOW STRICTLY):

1. IDENTIFY PLUGIN PURPOSE (CRITICAL - DO THIS FIRST)
   - List directory structure
   - Find and read README/main file
   - Answer: What does this solve? For whom? What market?

2. MAP THE CODEBASE SYSTEMATICALLY
   - Recursive directory listing
   - Find all PHP, JS, CSS files
   - Identify entry points and structure

3. READ CRITICAL FILES COMPLETELY
   - Main plugin file
   - All PHP classes
   - All JavaScript files
   - Config files (composer.json, package.json)
   - Database schema files
   - Test files (if any)
   
   DO NOT SKIP FILES - Read each using read_file tool

4. ANALYZE EACH ASPECT THOROUGHLY
   A. External Integrations (OFTEN MISSED)
      - What APIs? (payment, shipping, etc.)
      - How are credentials stored?
      - Error handling?
      - Retry logic?
      - Caching?
   
   B. Database Design
      - Custom tables?
      - Indexes?
      - N+1 queries?
      - Prepared statements?
   
   C. Security Vulnerabilities (BE SPECIFIC)
      - Nonce validation? (provide line numbers!)
      - Input sanitization?
      - SQL injection risks?
      - API credentials encryption?
   
   [... continues with Code Quality, Architecture, Performance, etc.]

5. DOCUMENT FINDINGS WITH SPECIFICS
   - Don't say "poor security"
   - Say "Line 245: AJAX endpoint missing nonce validation"
   - Quote actual code snippets
   - Provide file paths and line numbers
```

### 4. Specific Analysis Checklist ✅

**Agent now knows to check for:**

**External Integrations (Often Missed Before):**
- API endpoint URLs
- Authentication mechanisms
- Credential storage (encrypted vs plain text)
- Error handling and retry logic
- Rate limiting
- Response caching

**Database Schema:**
- Custom table structure
- Index optimization
- Query patterns (N+1 issues)
- Prepared statement usage

**Security Issues:**
- Missing nonce validation (with line numbers)
- Unsanitized input (with examples)
- SQL injection vectors (with code quotes)
- Unescaped output (with file paths)
- Plain text credential storage

**Code Quality:**
- God objects (files over 500 lines)
- SRP violations (classes doing too much)
- Code duplication
- Magic numbers
- Mixed procedural/OOP

**Architecture Problems:**
- Tight coupling (no abstraction layers)
- No dependency injection
- Global state usage
- SOLID violations

**Performance Bottlenecks:**
- Synchronous blocking API calls
- Missing caching
- Queries in loops
- Unoptimized assets

**Modern Features Missing:**
- REST API vs legacy admin-ajax
- Gutenberg blocks
- WP-CLI commands
- Webhooks

**Testing:**
- Test file existence
- Coverage analysis
- CI/CD setup

### 5. Common Mistakes to Avoid ✅

**Agent is explicitly told NOT to:**
- ❌ Analyze only main file and skip others
- ❌ Miss external API integrations
- ❌ Give generic findings without code references
- ❌ Skip database schema analysis
- ❌ Forget to check for test files
- ❌ Assume modern patterns exist
- ❌ Forget to identify product purpose first

## Expected Improvements

### Before (Shallow Analysis)
```
- Poor security implementation
- Code quality issues
- Missing modern features
- Performance problems
```

### After (Deep, Specific Analysis)
```
SECURITY VULNERABILITIES:
- Line 245 (elta-web-service.php): AJAX endpoint 'delete_voucher' 
  missing nonce validation - allows any user to delete vouchers
- Line 180: API credentials stored in plain text via get_option() 
  without encryption
- Line 320: Direct wpdb->query() without prepare() - SQL injection risk

EXTERNAL INTEGRATION ANALYSIS:
- ELTA Courier SOAP API integration at https://cloud.elta-courier.gr
- Authentication: Basic Auth with username/password from options table
- No retry logic for failed API calls (blocks for 5s on timeout)
- No caching of voucher data (queries ELTA API on every page load)
- Error messages expose technical details to users

DATABASE SCHEMA:
- Custom table: wp_eltawebservices_orderlist (753 rows in test DB)
- Missing index on 'order_id' column (slow queries on large datasets)
- No foreign key constraints (orphaned records possible)

CODE QUALITY:
- elta-web-service.php: 847 lines, violates SRP (handles API, UI, DB)
- 15 methods in one class (God object pattern)
- No namespaces (old PHP pattern, global scope pollution)
- Mixed procedural and OOP code (inconsistent)

PERFORMANCE BOTTLENECKS:
- Line 180: Synchronous SOAP call blocks request for 3-5 seconds
- No transient caching for voucher status
- Assets loaded on all admin pages (not conditionally enqueued)
- 12 database queries in order list loop (N+1 problem)

MISSING MODERN FEATURES:
- No REST API endpoints (uses admin-ajax.php only)
- No Gutenberg blocks for tracking display
- No WP-CLI commands for bulk operations
- Still uses deprecated WordPress functions (e.g., wp_register_script in footer)

TESTING INFRASTRUCTURE:
- ZERO tests - no PHPUnit, Jest, or E2E tests
- No CI/CD configuration
- No automated testing of ELTA API integration
```

## How to Use

The agent now has these tools available and will use them automatically:

```python
# Agent can now do:
list_directory(directory_path="inputs/competitor-plugin", recursive=True)
find_files(directory_path="inputs/competitor-plugin", pattern="*.php")
read_file(file_path="inputs/competitor-plugin/elta-web-service.php")
```

**No manual intervention needed** - the agent will use these tools based on the methodology in its backstory.

## Running the Improved Analysis

```bash
# Run normally - agent will use new tools automatically
uv run python src/dev_team/orchestrator.py
```

**What Will Happen:**
1. ✅ Agent lists directory structure first
2. ✅ Finds and reads README/main file
3. ✅ Identifies product purpose ("ELTA courier integration for WooCommerce")
4. ✅ Maps entire codebase with find_files
5. ✅ Reads each PHP/JS file systematically
6. ✅ Analyzes external integrations (ELTA SOAP API)
7. ✅ Examines database schema
8. ✅ Identifies specific security issues with line numbers
9. ✅ Documents findings with code quotes

## Temperature Setting Importance

**temperature: 0.1** is critical for technical analysis:

- **High temp (0.7-1.0):** Creative, varied, but less accurate
  - Good for: Creative writing, brainstorming
  - Bad for: Technical analysis, code review

- **Low temp (0.1-0.3):** Deterministic, precise, consistent
  - Good for: Technical analysis, code review, security audits
  - Bad for: Creative tasks

**For competitor analysis: Use LOW temperature (0.1)**

## Model Selection

**Using: ollama/qwen3-coder:30b**

Why this model:
- ✅ Code-specific training (understands PHP, JS, SQL)
- ✅ Large context window (can read big files)
- ✅ 30B parameters (good reasoning for analysis)
- ✅ Open source (runs locally with Ollama)

Alternative models to consider:
- `deepseek-coder-v2:16b` - Excellent code understanding
- `codellama:34b` - Strong technical analysis
- `qwen2.5-coder:32b` - Newer version with improvements

## Verification

To verify improvements, check the next technical analysis output for:

1. ✅ Clear product purpose statement at the beginning
2. ✅ External integration analysis (APIs, credentials, error handling)
3. ✅ Database schema documentation
4. ✅ Specific security issues with line numbers
5. ✅ Code quality issues with file names and line counts
6. ✅ Performance bottlenecks with specific causes
7. ✅ Testing infrastructure assessment (likely "zero tests")
8. ✅ Actual code snippets quoted in findings

If these are present, the improvements worked! If not, may need to adjust temperature lower or add more specific task instructions.

## Summary

✅ **Tools Created:** FileReaderTool, DirectoryListTool, FindFilesTool  
✅ **Configuration Enhanced:** temperature=0.1, max_iter=30, tools registered  
✅ **Methodology Added:** 5-step systematic analysis process  
✅ **Checklist Provided:** What to analyze and how to document  
✅ **Common Mistakes Addressed:** Explicit guidance on what NOT to do  

**Expected Result:** Deep, specific, actionable technical analysis with file paths, line numbers, and code quotes instead of generic observations.

🎯 The agent should now produce the level of detail you saw in my manual analysis!

