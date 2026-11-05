---
description: "Run AI-powered browser testing against any URL using personality-driven agents. Each agent approaches the app differently — impatient speedrunners, chaos gremlins, skeptical executives, and more. Surfaces bugs, UX friction, and edge cases that uniform testing misses."
---

# AI Beta Tester

Run personality-driven browser tests against a target URL using the `ai-beta-test` CLI.

## Step 1: Check installation

Run:

```bash
which ai-beta-test
```

If the command is not found, output the following and stop:

---

**`ai-beta-test` is not installed.** Install it first:

```bash
# From the repo (development)
pip install -e ~/Development/ai-beta-tester

# Or once published
pip install ai-beta-tester
```

Also ensure Node.js 18+ is installed (required for the Playwright MCP server):

```bash
brew install node   # macOS
```

Then re-run `/beta-test`.

---

## Step 2: Gather inputs

Ask the user for the following (if not provided in $ARGUMENTS):

1. **Target URL** — the URL to test (e.g. `https://myapp.com`)
2. **Goal** — one sentence describing what to test (e.g. "Complete the onboarding flow")
3. **Personalities** — which agents to run (see list below, or say `default`)

### Available Personalities

| Name | Mindset | What it surfaces |
|------|---------|-----------------|
| `speedrunner` | *"I don't have time for this."* | Missing loading states, unclear primary actions, broken fast-paths |
| `chaos_gremlin` | *"What happens if I do this?"* | Input validation gaps, error handling issues, state corruption |
| `skeptical_exec` | *"I don't trust this tool yet. Don't make me think."* | Cognitive load, trust breaks, unexpected transitions |
| `methodical_newcomer` | *"I am new here. Please tell me exactly what to do."* | Missing guidance, confusing labels, dead ends, unclear errors |
| `overloaded_manager` | *"I have 30 seconds. Show me the big button or I'm gone."* | Poor hierarchy, information overload, slow landing, UX friction |
| `calm_operator` | *"Slow and steady. I want to understand what I'm looking at before I touch it."* | Missing feedback, inconsistency, unclear state |
| `adhd_founder` | *"Oh look, a shiny feature! Wait, what was I doing? Let me just fix this first."* | Poor resumption, brittle state, punitive flows |
| `privacy_paranoid` | *"Why do you need to know that? Where did you get this data?"* | Trust breaks, missing provenance, dark patterns |
| `feature_explorer` | *"I need to understand everything this app can do."* | Undiscoverable features, missing affordances, navigation gaps |
| `interactive_explorer` | *"I won't just look at features - I'll use every single one."* | Incomplete flows, missing feedback, broken conversation flows |
| `technical_exploit` | *"I don't play by the rules; I rewrite them via the console."* | Security hints, exposed storage, validation bypasses |
| `hybrid_auditor` | *"I don't just look at the surface; I read the blueprints and check the foundation."* | Security risks, logic errors, API failures |
| `agentic_interface_tester` | *"UX researcher specializing in AI-driven interfaces, focused on trust and transparency"* | Mode selection errors, decision transparency, override friction |

**Default:** `speedrunner,chaos_gremlin,skeptical_exec`

If the user says "default", use those three. If they pick specific personalities, comma-join the names.

## Step 3: Run the test

```bash
ai-beta-test run <URL> --goal "<GOAL>" --agents <PERSONALITIES>
```

Stream the output as it runs. Example:

```bash
ai-beta-test run https://myapp.com --goal "Complete the signup flow" --agents speedrunner,chaos_gremlin
```

## Step 4: Save the report

After the run completes, find the generated report (the CLI saves to `./reports/` by default). Copy it to the current project's `.claude/` directory:

```bash
TIMESTAMP=$(date +%Y%m%dT%H%M%S)
SLUG=$(echo "<URL>" | sed 's|https\?://||' | sed 's|[^a-zA-Z0-9]|-|g' | cut -c1-40)
mkdir -p .claude/beta-test-reports
REPORT_FILE=$(ls -t reports/*.md 2>/dev/null | head -1)
if [ -n "$REPORT_FILE" ]; then
  cp "$REPORT_FILE" ".claude/beta-test-reports/${TIMESTAMP}-${SLUG}.md"
  echo "Report saved to: .claude/beta-test-reports/${TIMESTAMP}-${SLUG}.md"
fi
```

Then read and display a summary of findings from the report: count of findings by severity, top issues found, and which personalities ran.
