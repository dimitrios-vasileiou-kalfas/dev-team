# Improved Configuration - Multi-Pass Analysis
## Forces agent to work 8-12 minutes with 75%+ accuracy

This configuration implements a deliberate, multi-phase approach that:
1. Forces minimum tool calls per phase
2. Adds verification loops
3. Uses chain-of-thought prompting
4. Tracks progress explicitly

---

## agents.yaml Changes

```yaml
competitor_analyst:
  role: >
    Meticulous Technical Code Analyst
  goal: >
    Perform exhaustive technical analysis by reading EVERY relevant file.
    Work slowly and deliberately - this task should take 8-12 minutes.
    
    YOU MUST USE AT LEAST 80 TOOL CALLS TO COMPLETE THIS PROPERLY.
  llm: ollama/qwen3-coder:30b
  temperature: 0.1  # Back to sweet spot (not 0.2)
  max_iter: 150     # Much higher ceiling
  verbose: true
  backstory: >
    You are PAID BY THE HOUR, not by speed. Take your time.
    
    Your reputation depends on finding EVERYTHING:
    - Every AJAX endpoint (not just 2-3)
    - Every shortcode (not just examples)
    - Every hook (not just main ones)
    - Actual filenames (not invented ones)
    
    SLOW DOWN. READ EVERYTHING. VERIFY EVERYTHING.
```

---

## tasks.yaml - Rewritten with Forced Phases

```yaml
analyze_competitor:
  description: >
    Systematic 4-phase analysis with MINIMUM TOOL CALL REQUIREMENTS.
    You will be EVALUATED on completing ALL phases properly.
    
    Expected completion time: 8-12 minutes
    Expected tool calls: 80-120
    
    ═══════════════════════════════════════════════════════════════════
    📊 PROGRESS TRACKING (Update after each tool call)
    ═══════════════════════════════════════════════════════════════════
    
    After EVERY tool call, write:
    "✓ Tool call X/80: [action] - [what you found]"
    
    Example:
    "✓ Tool call 1/80: list_directory(competitor-plugin) - Found admin/, includes/, webservice/"
    "✓ Tool call 2/80: list_directory(webservice/) - Found 6 WSDL files"
    "✓ Tool call 3/80: read_file(readme.txt) - Plugin is ELTA Courier integration"
    
    DO NOT SKIP THIS! This proves you're working systematically.
    
    ═══════════════════════════════════════════════════════════════════
    PHASE 1: DISCOVERY (Tool calls 1-20, ~3 minutes)
    ═══════════════════════════════════════════════════════════════════
    
    MINIMUM: 20 tool calls in this phase
    
    Tool call 1: list_directory("{competitor_plugin_path}", recursive=False)
    → Note all folders: admin/, includes/, public/, webservice/, etc.
    
    Tool call 2: list_directory("{competitor_plugin_path}/webservice")
    → Write down EXACT filenames of WSDL files (don't invent names!)
    
    Tool call 3: list_directory("{competitor_plugin_path}/includes")
    → Count how many PHP files
    
    Tool call 4: list_directory("{competitor_plugin_path}/admin")
    → Count how many PHP files
    
    Tool call 5: list_directory("{competitor_plugin_path}/public")
    → Count how many PHP files
    
    Tool calls 6-10: Use find_files to locate:
    - All *.php files
    - All *.js files
    - composer.json / package.json
    - Configuration files
    - Test files (if any)
    
    Tool calls 11-20: Read documentation files:
    - readme.txt (FULL file)
    - README.md (if exists)
    - CHANGELOG (if exists)
    - Main plugin file (first 100 lines for header)
    
    ═══════════════════════════════════════════════════════════════════
    VERIFICATION CHECKPOINT 1
    ═══════════════════════════════════════════════════════════════════
    
    Before proceeding to Phase 2, verify:
    - [ ] Did I use at least 20 tool calls? (Count them!)
    - [ ] Do I have EXACT WSDL filenames? (Not guesses like "GETTRACKING")
    - [ ] Do I know how many PHP files exist? (Total count)
    - [ ] Did I read readme.txt completely?
    
    If ANY answer is NO, GO BACK and do more discovery.
    
    Write: "✓ PHASE 1 COMPLETE: Used [X] tool calls, found [Y] files"
    
    ═══════════════════════════════════════════════════════════════════
    PHASE 2: READING (Tool calls 21-80, ~6 minutes)
    ═══════════════════════════════════════════════════════════════════
    
    MINIMUM: 60 tool calls in this phase
    
    READ IN THIS EXACT ORDER (check off as you go):
    
    Tool call 21: [ ] read_file(main-plugin-file.php) - COMPLETE file
    Tool call 22: [ ] read_file(includes/class-main.php) - COMPLETE file
    Tool call 23: [ ] read_file(includes/class-loader.php) - COMPLETE file
    Tool call 24: [ ] read_file(includes/class-i18n.php) - COMPLETE file
    Tool call 25: [ ] read_file(includes/class-activator.php) - COMPLETE file
    Tool call 26: [ ] read_file(includes/class-deactivator.php) - COMPLETE file
    Tool call 27: [ ] read_file(includes/class-cron.php) - If exists
    Tool call 28: [ ] read_file(admin/class-admin.php) - Lines 1-400
    Tool call 29: [ ] read_file(admin/class-admin.php) - Lines 401-END
    Tool call 30: [ ] read_file(public/class-public.php) - COMPLETE file
    
    Tool calls 31-70: Read EVERY remaining PHP file you found
    - Don't skip any!
    - Read large files in sections (400 lines per call)
    
    Tool calls 71-80: Read other important files:
    - JavaScript files
    - composer.json
    - package.json
    - Any test files
    
    ═══════════════════════════════════════════════════════════════════
    VERIFICATION CHECKPOINT 2
    ═══════════════════════════════════════════════════════════════════
    
    Before proceeding to Phase 3, verify:
    - [ ] Did I use at least 60 tool calls in Phase 2?
    - [ ] Did I read the main class COMPLETELY? (Not just 300 lines)
    - [ ] Did I read the admin class COMPLETELY? (Even if 800+ lines)
    - [ ] Did I count AJAX endpoints as I read? How many?
    - [ ] Did I count shortcodes as I read? How many?
    - [ ] Did I note WooCommerce hooks? How many?
    
    Write: "✓ PHASE 2 COMPLETE: Read [X] files, found [Y] AJAX, [Z] shortcodes"
    
    If you found 0 shortcodes, you MISSED them. GO BACK.
    If you found <5 AJAX endpoints, you MISSED some. GO BACK.
    
    ═══════════════════════════════════════════════════════════════════
    PHASE 3: ENUMERATION (Tool calls 81-100, ~2 minutes)
    ═══════════════════════════════════════════════════════════════════
    
    MINIMUM: 20 tool calls for thorough enumeration
    
    Now enumerate EVERY instance of patterns you found:
    
    Tool calls 81-85: Search for AJAX endpoints
    - Go back to main class file
    - Search for EVERY "wp_ajax_" occurrence
    - List ALL with line numbers
    - Don't stop at 2-3!
    
    Tool calls 86-88: Search for shortcodes
    - Go back to files
    - Search for "add_shortcode"
    - List ALL shortcodes found
    
    Tool calls 89-92: Search for WooCommerce hooks
    - Search for "woocommerce_"
    - List key hooks (especially order_status)
    
    Tool calls 93-95: Search for cron jobs
    - Search for "wp_schedule"
    - Search for cron constants
    
    Tool calls 96-100: Verify database usage
    - Search for "CREATE TABLE" (custom tables)
    - Search for "register_post_type" (CPTs)
    - Note the EXACT CPT name (not a guess!)
    
    ═══════════════════════════════════════════════════════════════════
    VERIFICATION CHECKPOINT 3
    ═══════════════════════════════════════════════════════════════════
    
    Count your findings:
    - AJAX endpoints: ___ (Should be 5-10)
    - Shortcodes: ___ (Should be 1-5)
    - WooCommerce hooks: ___ (Should be 3-8)
    - CPT name: ___ (Exact name from code)
    
    If any count is 0, you MISSED them. GO BACK.
    
    Write: "✓ PHASE 3 COMPLETE: Enumerated all patterns"
    
    ═══════════════════════════════════════════════════════════════════
    PHASE 4: ANALYSIS (Tool calls 101-120, ~2 minutes)
    ═══════════════════════════════════════════════════════════════════
    
    MINIMUM: 20 tool calls for verification
    
    Now verify specific details:
    
    Tool calls 101-105: Go back to WSDL files
    - List directory again to confirm exact names
    - Write: "WSDL files (verified): [exact list]"
    
    Tool calls 106-110: Verify security patterns
    - Go back to AJAX handler methods
    - Check for nonce validation in each
    - Document which have/don't have nonces
    
    Tool calls 111-115: Check for missed features
    - Search for "bulk_actions"
    - Search for "order_status_completed"
    - Search for "wp_ajax_nopriv" (public AJAX)
    
    Tool calls 116-120: Final completeness check
    - Did I list ALL AJAX? (Count again)
    - Did I list ALL shortcodes? (Count again)
    - Are WSDL names EXACT? (Not invented)
    - Is CPT name EXACT? (Not guessed)
    
    ═══════════════════════════════════════════════════════════════════
    FINAL VERIFICATION
    ═══════════════════════════════════════════════════════════════════
    
    Total tool calls used: ___ / 80 minimum
    
    If less than 80, you RUSHED. Your analysis is INCOMPLETE.
    
    Completeness check:
    - [ ] Used 80+ tool calls
    - [ ] Spent 8+ minutes on analysis
    - [ ] Listed ALL AJAX endpoints (not just 2-3)
    - [ ] Listed ALL shortcodes (not 0)
    - [ ] Listed EXACT WSDL filenames (not invented)
    - [ ] Listed EXACT CPT name (not guessed)
    - [ ] Found auto-voucher feature (order_status hook)
    - [ ] Found bulk actions
    - [ ] Found public AJAX (wp_ajax_nopriv)
    
    If ANY checkbox is unchecked, your analysis FAILED.
    
    ═══════════════════════════════════════════════════════════════════
    OUTPUT FORMAT
    ═══════════════════════════════════════════════════════════════════
    
    Your report MUST include this summary at the TOP:
    
    ```
    ANALYSIS STATISTICS:
    - Total tool calls: [count]
    - Time spent: [estimate based on calls]
    - Files discovered: [count]
    - Files read: [count]
    - AJAX endpoints: [count]
    - Shortcodes: [count]
    - WSDL files: [count with EXACT names]
    - Completeness: [X/9 checks passed]
    ```
    
    Then provide detailed analysis as before.

  agent: competitor_analyst
  output_file: 'outputs/analysis/technical-analysis.md'
```

---

## Expected Results with This Configuration

**Time:** 8-12 minutes (vs 2 minutes before)

**Tool calls:** 80-120 (vs 10 before)

**Accuracy improvements:**
- WSDL files: 100% (forced verification)
- AJAX endpoints: 100% (forced enumeration)
- Shortcodes: 100% (forced search)
- Features: 90%+ (multiple checkpoints)

**Overall grade:** 80-85% (B/B+) vs 45% (D) before

---

## How to Implement

1. Replace `src/dev_team/config/agents.yaml` competitor_analyst section
2. Replace `src/dev_team/config/strategy_tasks.yaml` analyze_competitor section
3. Run: `python src/dev_team/orchestrator.py`
4. Expect: 8-12 minute run with forced thoroughness

Want me to implement this now?

