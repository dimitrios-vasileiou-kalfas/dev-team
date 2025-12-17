# Fix Applied: Forcing Tool Usage with 3-Phase Analysis

## Problem Summary

The competitor_analyst agent was NOT using the file reading tools, resulting in generic boilerplate analysis instead of specific findings from the actual competitor plugin code.

## Solution Applied

### 1. Tool Enforcement Strategy ✅

**Question:** Is `result_as_answer=True` how to enforce tools?

**Answer:** **NO**. That parameter only forces the tool's output to be the final answer. It doesn't force the agent to USE the tool.

**Correct Approach:**
- ✅ **Explicit instructions** in the task description
- ✅ **Step-by-step commands** telling agent to call specific tools
- ✅ **Verification checklist** at the end
- ✅ **Examples** of tool usage with exact syntax
- ✅ **More iterations** (max_iter: 50) to give time for thorough analysis

### 2. Three-Phase Analysis Structure ✅

Restructured the analyze_competitor task into **3 clear phases**:

#### 📋 **PHASE 1: FEATURE EXTRACTION** (What does it do?)

**Actions:**
1. `list_directory()` - See folder structure
2. `read_file(readme.txt)` - Read documentation
3. `read_file(main-file.php)` - Read plugin header

**Output:**
```
Product: [Name] v[Version]
Purpose: [One sentence]
Target Users: [Specific audience]
Market/Niche: [Geographic/industry]

Key Features:
1. Supports 2 languages: Greek & English
2. Creates ELTA courier vouchers automatically
3. Prints A4/A6 labels
4. Tracks shipment status
5. API integration with ELTA webservice
... [all features from README]
```

#### 🔧 **PHASE 2: TECHNICAL IMPLEMENTATION** (How is it built?)

**Actions:**
1. `find_files(pattern="*.php")` - Map all PHP files
2. `read_file()` for each critical file (minimum 8 files)
3. Analyze: APIs, databases, AJAX, cron, architecture

**Output:**
```
Technical Stack:
- Platform: WordPress + WooCommerce
- PHP: [version]
- Frontend: [jQuery/React/etc.]

External Integrations:
- ELTA Courier SOAP API: 6 WSDL files in webservice/
  Files: CREATEAWB.wsdl, PELTT01.wsdl, etc.
  Purpose: Create vouchers, track packages

Database:
- Custom Tables: wp_voucher_jobs
- Custom Post Types: we_voucher_job

AJAX Endpoints: 5 endpoints
- wp_ajax_elta_courier_create_voucher
- wp_ajax_elta_courier_cancel_voucher
... [all endpoints with file:line]

Cron Jobs:
- Hourly status check: file:line - purpose
```

#### 🔍 **PHASE 3: GAP ANALYSIS** (What's wrong?)

**Actions:**
- Check AJAX endpoints for nonce validation
- Check credential storage (encrypted or plain text?)
- Check for performance issues (blocking calls, missing cache)
- Check code quality (God objects, no namespaces)
- Check for missing modern features

**Output:**
```
Security Vulnerabilities: 3 found
1. [HIGH] Missing Nonce on AJAX Delete
   File: admin/class-admin.php:245
   Code: add_action('wp_ajax_elta_courier_cancel_voucher'...)
   Risk: CSRF attack
   Fix: Add wp_verify_nonce()

Performance Bottlenecks: 2 found
1. Synchronous SOAP Calls
   File: admin/class-admin.php:180
   Problem: Blocks request for 3-5 seconds
   Fix: Queue async processing

Code Quality Issues: 1 found
1. God Object Pattern
   File: admin/class-admin.php (847 lines!)
   Problem: Violates Single Responsibility

Missing Modern Features:
- ❌ No REST API (uses legacy admin-ajax)
- ❌ No Gutenberg blocks
- ❌ No WP-CLI commands
```

### 3. Forced Tool Usage Instructions ✅

Added explicit tool calling syntax:

```yaml
**ACTION 1.1:** Use list_directory tool
```
list_directory(directory_path="{competitor_plugin_path}", recursive=False)
```

**ACTION 1.2:** Read documentation
```
read_file(file_path="{competitor_plugin_path}/readme.txt")
read_file(file_path="{competitor_plugin_path}/main-file.php")
```

**ACTION 2.1:** Map codebase
```
find_files(directory_path="{competitor_plugin_path}", pattern="*.php")
```

**ACTION 2.2:** Read each file found
MUST READ: [list of 8+ files]
```

### 4. Verification Checklist ✅

Added end-of-task checklist:

```yaml
**VERIFICATION CHECKLIST:**

Before finishing, ask yourself:
- [ ] Did I use list_directory?
- [ ] Did I read readme.txt?
- [ ] Did I read main plugin file?
- [ ] Did I read at least 5 more PHP files?
- [ ] Did I identify external APIs?
- [ ] Did I list AJAX endpoints with security check?
- [ ] Did I provide actual code quotes?
- [ ] Did I avoid generic advice?

If any answer is NO, go back and complete that step!
```

### 5. Increased Max Iterations ✅

**Changed in `agents.yaml`:**
```yaml
competitor_analyst:
  max_iter: 50  # Increased from 30
```

**Why:** Reading 8+ files + analyzing each takes many iterations. 30 wasn't enough.

### 6. Output Requirements ✅

**Mandatory elements:**
- ✅ Phase 1: Feature list
- ✅ Phase 2: Technical implementation details
- ✅ Phase 3: Gap analysis with specific issues
- ✅ At least 8 files listed
- ✅ At least 5 code quotes with file:line
- ✅ NO generic advice
- ✅ NO invented code examples

## Why This Approach Works

### 1. **Phased Structure = Clear Goals**
Agent knows exactly what to do in each phase:
- Phase 1: Extract features
- Phase 2: Understand implementation
- Phase 3: Find problems

### 2. **Explicit Tool Commands = Forced Usage**
Instead of:
> "Read the competitor plugin files"

Now:
> "Execute: list_directory(directory_path='{path}', recursive=False)"

The agent sees **exact tool syntax** to use.

### 3. **Examples = Template to Follow**
Agent sees output format for each phase, knows exactly what structure to produce.

### 4. **Verification = Self-Check**
Agent has a checklist to ensure it didn't skip steps.

### 5. **More Iterations = Thorough Analysis**
50 iterations allows:
- 1 iteration: list_directory
- 8-10 iterations: read_file for 8-10 files
- 10-15 iterations: analyze and document findings
- 10-15 iterations: write comprehensive report
- Reserve: 10 iterations for tool errors/retries

## Expected Improvements

### Before (Generic):
```
"The plugin has security issues. Consider adding nonce validation."
```

### After (Specific):
```
Security Vulnerability: Missing Nonce on AJAX Endpoint
File: admin/class-elta-courier-voucher-for-woocommerce-admin.php:245
Code:
add_action('wp_ajax_elta_courier_cancel_voucher', array($this, 'cancel_voucher'));

public function cancel_voucher() {
    $voucher_id = $_POST['voucher_id']; // No nonce check!
    wp_delete_post($voucher_id);
}

Risk: CSRF attack - malicious site can trick logged-in users into deleting vouchers
Fix: Add wp_verify_nonce($_POST['nonce'], 'cancel_voucher_nonce') before processing
```

## Testing the Fix

Run the orchestrator:
```bash
cd /Users/dimitrios.vasileiou-kalfas/Projects/my-projects/dev-team
uv run python src/dev_team/orchestrator.py
```

**Expected behavior:**
1. ✅ Agent lists directory structure
2. ✅ Agent reads readme.txt
3. ✅ Agent identifies "ELTA Courier Voucher for WooCommerce"
4. ✅ Agent finds 6 WSDL files in webservice/
5. ✅ Agent reads 8+ PHP files
6. ✅ Agent lists specific AJAX endpoints with file:line
7. ✅ Agent identifies missing nonce validation
8. ✅ Agent provides code quotes from actual files

**Check the output:**
```bash
cat outputs/analysis/technical-analysis.md
```

Look for:
- ✅ Product name and version
- ✅ Feature list (10+ features)
- ✅ File paths (8+ files listed)
- ✅ Code quotes with line numbers
- ✅ ELTA SOAP API mentioned
- ✅ Specific security issues
- ✅ NO generic advice
- ✅ NO made-up code examples

## Alternative: If This Still Doesn't Work

If the agent STILL doesn't use tools after this fix, try:

### Option A: Different Model
```yaml
llm: ollama/deepseek-coder-v2:16b  # Better tool usage
# OR
llm: ollama/codellama:34b  # Strong code understanding
```

### Option B: ReAct Prompting
Add to task description:
```yaml
Use this format:
Thought: I need to see the directory structure first
Action: list_directory
Action Input: {competitor_plugin_path}
Observation: [wait for tool result]
Thought: Now I see admin/, includes/, webservice/ folders...
Action: read_file
Action Input: {competitor_plugin_path}/readme.txt
Observation: [wait for tool result]
...
```

### Option C: Force First Action
Start description with:
```yaml
IMMEDIATE ACTION REQUIRED: 
Before reading ANY of this task description, execute this command:
list_directory(directory_path="{competitor_plugin_path}", recursive=True)

[Then continue with rest of instructions]
```

## Summary

✅ **Changed:** Task structure to 3 phases (Feature → Implementation → Gaps)
✅ **Added:** Explicit tool calling syntax with examples
✅ **Added:** Verification checklist
✅ **Added:** Output requirements
✅ **Increased:** max_iter from 30 to 50
✅ **Removed:** Generic instructions replaced with specific actions

The agent now has:
- Clear phase-by-phase goals
- Explicit tool commands to execute
- More iterations to work with
- Self-verification checklist
- Specific output format to follow

**Result:** Should produce detailed, specific, evidence-based analysis instead of generic boilerplate! 🎯

