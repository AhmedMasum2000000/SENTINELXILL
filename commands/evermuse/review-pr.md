---
description: Review a PR against code quality, the spec it should satisfy, and the actual customer asks behind it — flagging where the diff diverges from what customers requested
argument-hint: "[PR number or branch]"
---

# /evermuse:review-pr — Customer-aware PR review

Invoke the **review-pr** skill with `$ARGUMENTS`. Fetch the PR/diff (`gh` CLI or the Evermuse GitHub bridge, degrade gracefully), find the intent (shaping note by branch/PR number, or local spec), ground in the feature's customer asks, and review in three passes: code quality / spec conformance / customer-voice conformance. Lead with a clear verdict.
