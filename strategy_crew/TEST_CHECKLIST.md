# Strategy Crew - Test & Verify Checklist

## Pre-Flight Check ✈️

Run these commands to verify everything is set up correctly:

### 1. Check Ollama Model
```bash
ollama list | grep qwen3:30b
```
**Expected**: Should see `qwen3:30b-instruct` in the list

**If not**:
```bash
ollama pull qwen3:30b-instruct
```

### 2. Verify Symlinks
```bash
ls -la /Users/dimitrios.vasileiou-kalfas/Projects/my-projects/dev-team/strategy_crew/inputs/
```
**Expected**: Should see two symlinks:
```
competitor-plugin -> /Users/dimitrios.vasileiou-kalfas/Projects/my-projects/dev-team/inputs/competitor-plugin
skeleton-plugin -> /Users/dimitrios.vasileiou-kalfas/Projects/my-projects/dev-team/inputs/skeleton-plugin
```

### 3. Test Python Imports
```bash
cd /Users/dimitrios.vasileiou-kalfas/Projects/my-projects/dev-team/strategy_crew
python -c "from strategy_crew.crew import StrategyCrew; print('✅ Crew import OK')"
python -c "from strategy_crew.tools.custom_tool import FileReaderTool; print('✅ Tools import OK')"
```
**Expected**: Both should print ✅ messages

### 4. Verify Competitor Plugin Exists
```bash
ls /Users/dimitrios.vasileiou-kalfas/Projects/my-projects/dev-team/inputs/competitor-plugin/
```
**Expected**: Should see plugin files

### 5. Check Outputs Folder
```bash
ls -la /Users/dimitrios.vasileiou-kalfas/Projects/my-projects/dev-team/strategy_crew/outputs/
```
**Expected**: Folder exists (may be empty)

---

## Run Strategy Crew 🚀

```bash
cd /Users/dimitrios.vasileiou-kalfas/Projects/my-projects/dev-team/strategy_crew
crewai run
```

---

## What to Watch For 👀

### Phase 1: analyze_competitor (15-20 min)
- Should see: "list_directory" tool calls
- Should see: "read_file" tool calls for each PHP file
- Agent should read 20-50+ files systematically
- Output: `outputs/technical-analysis.md` created

**Red flags**:
- "File not found" errors
- Only reading 2-3 files
- Hallucinating file names

### Phase 2: research_market (5-8 min)
- Should use context from Phase 1
- Should identify market gaps
- Should list specific opportunities
- Output: `outputs/market-research.md` created

**Red flags**:
- Generic market research (not product-specific)
- No connection to competitor analysis
- Out-of-scope feature suggestions

### Phase 3: create_roadmap (3-5 min)
- Should synthesize both previous reports
- Should define 3 milestones (MVP, Parity, Differentiation)
- Should create plugin metadata
- Outputs: `outputs/product-roadmap.md` + `outputs/plugin-metadata.json` created

**Red flags**:
- Generic roadmap (not based on analysis)
- Missing plugin-metadata.json
- Milestone features don't match analysis

---

## Post-Run Verification ✅

### 1. Check All Outputs Created
```bash
cd /Users/dimitrios.vasileiou-kalfas/Projects/my-projects/dev-team/strategy_crew
ls -la outputs/
```

**Expected files**:
- [ ] `technical-analysis.md`
- [ ] `market-research.md`
- [ ] `product-roadmap.md`
- [ ] `plugin-metadata.json`

### 2. Verify Technical Analysis Quality
```bash
head -50 outputs/technical-analysis.md
```

**Should contain**:
- [ ] Plugin name and purpose identified
- [ ] Specific file names mentioned
- [ ] Actual code quotes or line numbers
- [ ] Security vulnerabilities with specifics
- [ ] Architecture problems explained
- [ ] No "hallucinated" file names

**Check for problems**:
```bash
grep "INFERRED" outputs/technical-analysis.md
grep "file1.php, file2.php" outputs/technical-analysis.md  # Should NOT find generic names
```

### 3. Verify Market Research Quality
```bash
head -50 outputs/market-research.md
```

**Should contain**:
- [ ] Product-specific market analysis
- [ ] Feature gaps WITHIN plugin scope
- [ ] Niche opportunities identified
- [ ] Competitive positioning
- [ ] NOT generic market research

### 4. Verify Product Roadmap
```bash
head -50 outputs/product-roadmap.md
grep -A 5 "Milestone 1" outputs/product-roadmap.md
```

**Should contain**:
- [ ] 3 milestones defined
- [ ] Features based on analysis (not generic)
- [ ] Acceptance criteria for features
- [ ] Technical requirements

### 5. Verify Plugin Metadata
```bash
cat outputs/plugin-metadata.json
```

**Should be valid JSON with**:
```json
{
  "name": "...",
  "slug": "...",
  "namespace": "...",
  "version": "...",
  "author": "..."
}
```

**Check validity**:
```bash
python -m json.tool outputs/plugin-metadata.json
```

---

## Success Criteria ✅

Strategy Crew is working correctly if:

- [x] All 4 output files created
- [x] technical-analysis.md has specific file names and line numbers
- [x] market-research.md is product-specific (not generic)
- [x] product-roadmap.md has 3 clear milestones
- [x] plugin-metadata.json is valid JSON with all fields
- [x] No hallucinations (fake file names)
- [x] Features are in-scope (not unrelated functionality)
- [x] Runtime was 20-35 minutes (thorough analysis takes time)

---

## Common Issues & Fixes 🔧

### Issue: "Cannot find competitor-plugin"
**Fix**:
```bash
cd /Users/dimitrios.vasileiou-kalfas/Projects/my-projects/dev-team/strategy_crew/inputs
ln -s ../../inputs/competitor-plugin competitor-plugin
```

### Issue: "Model not found"
**Fix**:
```bash
ollama pull qwen3:30b-instruct
```

### Issue: Agent hallucinating file names
**Cause**: Temperature too high or not reading actual files
**Check**: Look for "read_file" tool calls in output
**Expected**: Should see 20-50+ read_file calls

### Issue: Outputs are empty or generic
**Cause**: Tasks not getting proper context
**Check**: Verify tasks.yaml has correct `context:` fields
**Expected**: 
- research_market should have `context: [analyze_competitor]`
- create_roadmap should have `context: [analyze_competitor, research_market]`

### Issue: Very slow (1+ hour)
**Cause**: Competitor Analyst reading many large files
**Normal**: 25-30 minutes is expected for thorough analysis
**Concerning**: 1+ hours suggests stuck or infinite loop
**Fix**: Check Ollama logs, may need to restart

---

## What to Do After Successful Run 🎯

1. **Review Quality**: Read through all 4 output files
2. **Validate Plugin Name**: Check if plugin-metadata.json makes sense
3. **Share Results**: Copy outputs to safe location if needed
4. **Document Learnings**: Note any issues for Architecture Crew migration
5. **Next Step**: Plan Architecture Crew creation

---

## Questions to Ask Yourself 🤔

After reviewing outputs:

1. Does the technical analysis accurately describe what the competitor plugin does?
2. Are the security issues and code problems specific and actionable?
3. Does the market research focus on THIS product's market (not generic)?
4. Are the roadmap milestones realistic and based on the analysis?
5. Does the plugin name/slug make sense for the target market?
6. Are you confident passing these outputs to an Architecture Crew?

---

## Ready to Test? 🚀

**Final command**:
```bash
cd /Users/dimitrios.vasileiou-kalfas/Projects/my-projects/dev-team/strategy_crew
crewai run
```

**Grab coffee ☕** - It'll take 25-30 minutes!

---

**Created**: December 17, 2024  
**Purpose**: Test & verify strategy crew migration
**Status**: Ready for first run

