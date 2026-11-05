---
name: setup-evermuse
description: This skill sets up the Evermuse MCP extension prototype inside your agentic app. It will guide you through the setup process, asking key questions along the way using our UI rendering tools and skills.
category: Delivery & Engineering
tags:
- install
- product
- customer voice
---

# Setup Evermuse Extension Prototype

This is a skill to set up Evermuse-powered scheduled tasks in this agentic app.

IMPORTANT: Some of the steps below have old UI element associated with them that are no longer in the prototype. Please ignore those and follow the steps in sequence below using text, custom widgets, and the question asking tool instead of any hardcoded UIs.

Steps 2, 3 and 5 lean on capabilities the **host app** provides — a scheduler and subagents — rather than on the Evermuse MCP. Each of those steps tells you how to find the host's version before concluding it doesn't exist; on most hosts these tools are present but not loaded into context by default. Never present a missing host capability to the user as an Evermuse limitation.

One thing *is* a real Evermuse limit and can interrupt any step: running out of credits. See "Anytime: the workspace runs out of credits" below.

## Steps in Sequence
Please follow these steps in the prototype:

0. Welcome the User
1. Source Selection 
2. Schedule Ingest Tasks
3. Schedule Daily Report
4. Backfill Selection
5. Ingest Sources
6. Post Ingestion View


## Anytime: the workspace runs out of credits

A zero balance pauses every Evermuse tool except the skills library. Most often it hits partway through the step 5 backfill. Recognize it by any of these failed-tool-result texts:

* `MCP access is paused: ...` — no credits, or below this call's cost.
* `Insufficient credits to run subagent. ...` — from `run_subagent`.
* HTTP `402` with `"error": "INSUFFICIENT_CREDITS"`.

**Never retry, reword, or switch tools** — all of them fail identically until credits are added. Instead, stop and tell the user:

> **Evermuse is out of credits.** Processing is paused until you add more; everything already ingested is safe.
> **[Upgrade your plan](https://www.evermuse.com/pricing)** — or use the **Upgrade** button in the Evermuse sidebar.

Always include the URL. Then say where you stopped: before step 5, nothing was ingested and you'll resume at the same step; mid-step-5, give the real count of records that landed and offer to resume the rest — don't run step 6 as if the backfill finished. Leave any tasks scheduled in steps 2–3 in place; they start working once credits are added.

When the user says they've upgraded, retry only the failed call and continue from there. Never restart the skill or re-ask answered questions.


## 0. Welcome the User

Render the Evermuse setup header as a visual widget (mcp__visualize__show_widget), HTML mode:

- Wrapper: <div style="display:block; width:100%; box-sizing:border-box; text-align:center; padding:1rem 0;">
- Logomark: the SVG below at width="80" height="80", viewBox="0 0 160 160", style="display:block; margin:0 auto". Use the paths verbatim — do not restyle, recolor, or theme them.
- Heading: <h1 style="font-size:22px; font-weight:500; margin:16px 0 0; text-align:center;">Welcome to Evermuse Setup</h1>
- Subtitle: <p style="font-size:16px; font-weight:400; line-height:1.7; color:var(--text-secondary); margin:8px auto 0; max-width:520px; text-align:center;">We'll be selecting sources to process, storage options, and historical import preferences to get you set up.</p>
- Start with <h2 class="sr-only"> describing the header for screen readers.
- No card border, no background, nothing else in the widget.

<svg width="80" height="80" viewBox="0 0 160 160" fill="none" role="img" style="display:block; margin:0 auto"><title>Evermuse logomark</title><desc>Two overlapping petal shapes, left yellow and right pink.</desc><path d="M61.9648 68.3047C50.1805 66.4199 42.6607 66.2318 39.4053 67.7405L36.1416 67.8549C34.0916 67.8549 32.2375 68.4666 30.5791 69.69C28.9206 70.913 27.7747 72.515 27.1412 74.494C26.5078 76.474 26.1911 78.349 26.1911 80.121C26.1911 81.892 26.1422 84.301 26.0443 87.348C25.9465 90.394 26.0105 94.244 26.2363 98.896C26.4621 103.549 27.7395 108.947 30.0685 115.09C32.3975 121.232 36.7321 125.223 43.0725 127.063C49.4128 128.902 56.0515 129.426 62.9886 128.636C69.9256 127.845 75.681 125.185 80.255 120.654C84.829 116.124 87.132 109.895 87.166 101.968C87.2 94.04 85.954 86.919 83.429 80.604C80.904 74.289 73.749 70.19 61.9648 68.3047Z" fill="#FFC921" stroke="#FFC921" stroke-width="4"/><path d="M100.161 69.7441C88.66 67.9039 81.322 67.7202 78.145 69.1932L74.96 69.3049C72.959 69.3049 71.15 69.9022 69.5312 71.097C67.9128 72.291 66.7944 73.855 66.1762 75.787C65.5581 77.72 65.249 79.551 65.249 81.281C65.249 83.01 65.2012 85.362 65.1058 88.336C65.0103 91.311 65.0728 95.069 65.2931 99.612C65.5135 104.154 66.7601 109.424 69.033 115.422C71.306 121.419 75.536 125.316 81.724 127.111C87.911 128.907 94.39 129.419 101.16 128.647C107.93 127.875 113.546 125.278 118.01 120.854C122.474 116.431 124.722 110.35 124.755 102.61C124.787 94.871 123.572 87.918 121.107 81.753C118.643 75.587 111.661 71.584 100.161 69.7441Z" fill="#FF4A8E" stroke="#FF4A8E" stroke-width="4"/></svg>

CHAT BODY: Ready to get started?

If they answer positively, then move to the next step. If they answer negatively, ask if they would like to schedule a 1-on-1 session with a Product expert to walk them through the setup. If they reply positively to that, send them this link: https://calendly.com/d/cwbw-zmn-r5k/30-minute-evermuse-live-demo



## 1. Source Selection

First - scan the currently connected MCPs and identify those that might be relevant sources of customer communication. These include call recorders, chat platforms, support ticketing systems, CRMs, email providers, and other sources that may contain customer feedback.
Then output the following title and subtitle in chat:
H1 TITLE: **Hi there, where does your customer feedback come from today?**
SUBTITLE: Please select all that applies.

Then please use the question asking tool (or the show_widget tool if there are more than 4 options) to choose any of the tools you found in a multi-select list. If none are found, skip this step and go straight to asking of other, non-connected tools.

Once they made a selection, acknowledge the selection, and ask if there are any others customer sources they'd like to process. Respond positively to any answer. If there are available connectors for those sources, please help them to connect those sources. (If you have a nice connector card you can pull up please do so.) If there are no ready made connectors on your side, do a quick web search to see if there are any official MCP pages from these vendors and direct them to those. Then ask them if they'd like to hold or skip and proceed with the setup.

(If there are no sources connected, please let them know that much of the value of Evermuse is in processing customer feedback, and that they can always come back to this setup later once they have connected sources. Give them the option to connect sources now, or to cancel the setup and come back later. If they choose to connect sources now, please help them to do so. If they choose to cancel the setup, remind them they can always call the setup-evermuse skill via the Evermuse MCP. Then finish running this skill and exit gracefully.)


## 2. Schedule Ingest Tasks

Output the following title and subtitle in chat:
H1 TITLE: **Great! Let's schedule daily tasks to process your selected sources.**
SUBTITLE: Relevant records from these sources will be processed for insights and added to my memory on Evermuse.

### 2a. Find the host's scheduling tool before you conclude you can't schedule

Steps 2 and 3 both create scheduled tasks. Do this discovery once, here, and reuse the result in step 3. Work the list in order and stop at the first thing that works:

1. **Check your loaded tools** for one that *creates a recurring job* — names usually contain `cron`, `schedule`, `routine`, `task`, `reminder`, or `automation`. In Claude Code this is `CronCreate` (with `CronList` / `CronDelete` alongside it).
2. **Search the host's deferred tools.** Some hosts (Claude Code among them) advertise tools by name only and require you to load the schema before the tool is callable — an unloaded tool is invisible in your visible tool list but fully available. Run the host's tool-search tool with `select:CronCreate,CronList,CronDelete`, and again with the keywords `schedule cron recurring task`, before concluding anything is missing. **This is the most common false negative in this skill — assume the scheduler exists and you simply haven't loaded it yet.**
3. **Check for a scheduling skill or slash command** in the host (e.g. a `schedule` skill that creates cron-scheduled cloud agents). Invoking it to create the jobs is perfectly valid.
4. Only when all three come back empty does the host genuinely lack a scheduler — follow the fallback in 2c.

Whatever you find or don't find, never narrate it to the user as a "prototype gap", a "limitation", or a missing tool. Either the tasks get scheduled, or you hand the user ready-to-paste task definitions per 2c. Both are a successful setup.

### 2b. Create one ingest task per source

For each source the user selected in step 1 that you can actually reach, create one recurring daily task that runs in the evening in the user's local timezone.

A scheduled run starts in a fresh context with none of this conversation, so each task's prompt must be self-contained. Use this shape, substituting the source:

> Fetch every `<source>` record from the last 24 hours. First read the `using-evermuse` skill from the Evermuse MCP and follow its grounding rules. For each record containing verbatim customer feedback, send the full conversation or transcript to Evermuse with the `add_source` tool — one `add_source` call per conversation or record. Send only the customer's actual words plus the surrounding context needed to understand them; never send summaries or second-hand reports. If Evermuse replies that MCP access is paused for lack of credits, stop without retrying and report that the workspace is out of credits — top up at https://www.evermuse.com/pricing. Finish with a short list of what you sent.

Stagger the sources a few minutes apart so they don't all fire at once, and avoid the `:00` and `:30` minute marks.

Then confirm to the user — read the jobs back (using the scheduler's list tool if it has one) as a compact table of source / when it runs / what it does. If the mechanism you used has real constraints, state them in one plain sentence and offer the persistent alternative: Claude Code's cron jobs, for example, live only in the current session and auto-expire after 7 days, so offer to hand over the same definitions for the host's own Tasks UI (per 2c).

### 2c. Fallback when the host has no scheduler

Don't stall and don't apologize at length. Present the exact tasks you would have created — for each one, a name, the time it should run, and the full prompt text in a copy-paste code block — and tell the user where to add them in their host (usually Settings → Tasks, the same place any existing scheduled tasks of theirs live). Then ask whether they'd like to add them now or keep going and add them later. Either answer continues to step 3.


## 3. Schedule Daily Report

Ask the user how they'd like to get the daily report: In a Slack channel, a private Slack message, or an email. (Make sure you have access to these tools). You can also allow Other, letting the user choose any channel that is available to you via connectors.

Then ask the user what time of day they'd like to receive the daily report. (Suggest a morning report at 7am) Please schedule the daily report task accordingly, and confirm with the user that it is scheduled. The daily report task should include a search of signals and sources via the Evermuse MCP and a summary of everything that was learned by Evermuse in the past 24 hours.

Use the scheduling mechanism you already found in 2a — don't rediscover it, and don't fall back to 2c unless 2a genuinely found nothing. As in 2b, the report task's prompt must be self-contained: it has to name the Evermuse MCP search it should run, the 24-hour window, and the exact delivery tool and destination the user chose (channel, DM recipient, or email address), because the scheduled run won't remember this conversation.


## 4. Backfill Selection

First output the following title and subtitle in chat:
H1 TITLE: How far back should I scan sources for insights?
SUBTITLE: Please select your backfill preference.

Make sure the title and subtitle landed, then draw an in-chat backfill options plan via a side by side plan comparison.
Here is what the options should show:

* 7 Days
  * Fewer tokens
  * Faster start
* 30 Days [Recommended]
  * More insights
  * More tokens
  * Deeper context
* Longer Periods [Premium]
  * 100% of sources
  * 100% of insights
  * Easy migration API
  * Custom import plan

Please then load the question asking tool to single-select one of the three options. Acknowledge the selection. IF they choose Longer Periods, please let them know they have to schedule a appointment with our team to discuss a custom import plan. Ask if they would like to schedule that now, or choose one of the other options. If they choose schedule a custom import plan appointment, send them this link: https://calendly.com/d/cwbw-zmn-r5k/30-minute-evermuse-live-demo. Otherwise proceed with the other options.



## 5. Ingest Sources

First output the following title and subtitle in chat:
H1 TITLE: Great! Let me process the last N days and send what I find to be processed. When I'm done, I can write my initial report.
(N is the backfill window the user chose in step 4 — write the real number.)
SUBTITLE: You can leave this thread and come back later.

Then, proceed to launch as many subagents as are required to complete the task of processing all selected sources from Step 1, and sending all relevant conversations from the last 7 or 30 days to Evermuse using the add_source tool.

### 5a. Find the host's subagent tool before you conclude you can't parallelize

Same discovery discipline as 2a, and the same most-common false negative — assume the tool exists and you simply haven't loaded it yet:

1. **Check your loaded tools** for one that *dispatches a subagent* — usually `Task` or `Agent`.
2. **Search the host's deferred tools** with `select:Task,Agent` and again with the keywords `subagent parallel task`. Note that Evermuse's own `run_subagent` is not available to API-key/plugin sessions, so don't count on it.
3. If neither turns one up, run the ingestion inline and serially instead: handle one record at a time — fetch it, submit it with `add_source`, then move on without holding the full transcript in context. Say once, plainly, that you're processing them one at a time; don't call it a gap or a limitation. If the user picked the 30-day backfill, tell them a serial run may exhaust the context window before it finishes and offer to narrow the window or split it across several threads.

### Some rules to follow
 1. Each source on Evermuse is one conversation or record: Example one call on Gong, one customer update on a CRM, one chat on Intercom, one day of back and forth messages with a customer in Slack, one ticket on Zendesk. 
 2. Only direct quotes from customers should be sent to Evermuse. Do not summarize 2nd hand reports, automated summaries, or any other non-verbatim content. Only send the actual words of the customer such as a call, a ticket, an email - along with surrounding context as is needed to understand it (for example a full transcript of a call, or the full back and forth of a chat).
 3. There could be hundreds of calls in a 30 day period, so use subagents intelligently to avoid running out of context window space. Do not send the smallest agents to do task that require genuine good judgement but only for technical routine tasks. (If 5a found no subagent tool, the same constraint applies to you directly — keep only one record in context at a time.)
 4. Each agent should be asked to read the using-evermuse skill and its references before starting the task, and to follow the grounding mechanics in that skill to find relevant evidence. Each agent should be asked to return a report of what it found, with citations, and to send full transcripts of relevant communications or conversations to Evermuse using the add_source tool.
 5. This step is the most likely to exhaust the workspace's credits. Tell every agent that if `add_source` reports MCP access paused for lack of credits, it must stop immediately, not retry, and return what it sent plus what it didn't. On that error — yours or an agent's — stop dispatching and follow "Anytime: the workspace runs out of credits" above.

If you are able at this step - output a custom live-updating progress bar showing a real percentage of ingestion done. Below it please output a message in chat that says "Processing your sources now. This may take a while. I recommend you leave this thread and come back later today."


## 6. Post-Ingestion View

Build this message from what you actually processed in step 5. Every source name, unit and number below is a placeholder — none of them are text to reuse.

H1 TITLE: **All done! I've processed your sources for the past N days.**
(N is the backfill window the user chose in step 4 — write the real number.)

SUBTITLE: one clause per source you actually ingested from, each with its real count and that source's own unit — calls for a call recorder, tickets for a support tool, threads or channels for chat, records for a CRM, emails for a mailbox. Close with "I've learned so much, and I'll remember it with Evermuse!"

Never name a source the user didn't select in step 1, and never carry Gong, Zendesk or Slack into the sentence unless those are genuinely what you just processed. The example below is there to show the shape of the sentence, nothing more — it is from a run that happened to use those three:

> I've scanned **301 calls on Gong**, **17 Zendesk tickets**, and **32 Slack Connect channels**. I've learned so much, and I'll remember it with Evermuse!

Two cases to get right:

* **Some sources came back empty.** Leave them out of the subtitle and account for them in one short sentence underneath — "Nothing new in Slack or Linear in this window." Don't pass over them in silence, and don't pad the subtitle with zeros.
* **Everything came back empty.** Don't manufacture a win. Say the window turned up nothing, name the sources you checked, and offer to widen the backfill or revisit once the daily tasks from steps 2 and 3 have had a night to run.

Here are some things you can do from here:

--

Make sure the title and subtitle landed, then use the show_widget tool to show a stylish single-select one of the following options:
* Get my initial report
* Dive into a topic
* Write a spec
* Write an interview script
* Find the gaps
* See all new capabilities






