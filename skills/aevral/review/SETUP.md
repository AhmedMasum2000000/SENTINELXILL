# Setting up Aevral

Catch security flaws before you merge. Aevral reviews pull requests for
authorization, IDOR, and business-logic flaws, with a suggested fix you apply.
It runs as a GitHub App, so the review happens server-side, not on your machine.

## Boundary

This plugin does not review code locally. Installing a GitHub App is an
account-owner action. No agent can do it for you. MCP is not live. Do not
uninstall and reinstall to repair a missing repository. Use Setup in the
console, then Sync.

## Step 1. Tagged console login (you)

Open the login that matches the tool that sent you here, so the listing source
is stored before sign-in:

- Claude Code: https://app.aevral.com/login?ref=claude-plugin
- Codex CLI: https://app.aevral.com/login?ref=codex-cli
- Cursor: https://app.aevral.com/login?ref=cursor
- GitHub Copilot CLI: https://app.aevral.com/login?ref=copilot-cli
- Gemini CLI: https://app.aevral.com/login?ref=gemini-cli
- Grok: https://app.aevral.com/login?ref=grok-plugin
- Anything else: https://app.aevral.com/login?ref=agent-plugin

Continue with GitHub. Email login cannot connect an install.

## Step 2. Install the GitHub App (you)

https://github.com/apps/aevral

Choose the account or organization, pick the repositories, Install. Permissions:
Contents read, Metadata, Checks write, Pull requests read and write. No write
access to your code.

After this click, the next pull request can already be reviewed, including
before anyone signs in to the console.

## Step 3. Confirm in the console

Same GitHub user as the App install. The console connects a matching install.
Confirm the intended organization and repository. Empty list: Sync from GitHub.
If they are not visible: Connection not verified.

The owner can turn reviews off in Setup. If they are already off, leave them off.

## Step 4. Optional scan

A whole-repo scan is a second product. Press Scan only if you want a
default-branch report. Setup is already done for reviews without it.

## Pricing

Public repositories are free up to 500 reviews per organization per month.
Private repositories are free up to 25. Paid plans: https://aevral.com/pricing

## Links

- Official agent prompt: https://docs.aevral.com/agent-setup/prompt.md
- Setup with an agent: https://docs.aevral.com/docs/setup-with-an-agent
- GitHub App permissions: https://docs.aevral.com/docs/github-app-permissions
- Pricing: https://aevral.com/pricing
- Privacy: https://trust.ismscopilot.com/en/privacy-policy
- Terms: https://trust.ismscopilot.com/en/terms
