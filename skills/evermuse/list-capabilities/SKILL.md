---
name: list-capabilities
description: 'Show the user everything Evermuse can do — announce it in chat, then render the interactive list-capabilities picker of every agentic skill, grouped by category, and wait for them to pick one. Use when the user picks "See all new capabilities", runs find_skills:list-capabilities, or asks ''what can you do'', ''what can Evermuse do'', ''show me all the skills'', ''what are my options'', ''list your capabilities'', or ''help me get started''. Trigger terms: what can you do, list capabilities, show all skills, what are my options, capabilities menu, what can Evermuse do, help me choose.'
category: Ops & Meta
tags:
- evermuse
- navigation
- onboarding
---

# List Capabilities (the capabilities picker)

The front door to everything Evermuse can do: a color-coded, category-grouped picker of every agentic skill. This skill is how a user who doesn't yet know what to ask for finds their footing — reached from the post-ingestion view's "See all new capabilities" option, via `/evermuse:list-capabilities`, or whenever someone asks "what can you do?". The job is to frame the moment in chat, render the picker, and let the user choose.


## Steps in sequence

### 1. Announce the menu in chat

First output **exactly** this title and subtitle as your chat message:

H1 TITLE: **What would you like to achieve today?**
SUBTITLE: Below are a list of things I can do for you with Evermuse.


### 2. Render a custom list of capabilities

Create a custom UI with the following skills (use human names), in a color coded way, broken by category, and clickable:

Technical name	Human name	Description	Category	Color
customer-journey-map	Customer Journey Map	Maps awareness→advocacy with the pain, emotion, and a verbatim quote at each stage, plus prioritized fixes.	Discovery & Research	#3B82F6
customer-research	Customer Research	Answers "what do customers think/need/complain about" with a quote-rich, source-linked brief from Evermuse.	Discovery & Research	#3B82F6
initial-report	Initial Report	Presents the first Evermuse report after the initial source scan and hands off to the interactive report UI.	Discovery & Research	#3B82F6
interview-script	Interview Script	Writes a Mom-Test interview guide targeting the gaps evidence hasn't already answered.	Discovery & Research	#3B82F6
user-personas	User Personas	Builds 3 evidence-backed personas with JTBD, pains, gains, and an "in their own words" quote block.	Discovery & Research	#3B82F6
analyze-feature-requests	Analyze Feature Requests	Triages feature requests into themes, merges duplicates, and surfaces the underlying need with quotes.	Customer Voice & Feedback	#EC4899
sentiment-analysis	Sentiment Analysis	Surfaces sentiment, themes, and satisfaction shifts over a period, scored per theme with labeled quotes.	Customer Voice & Feedback	#EC4899
using-evermuse	Using Evermuse	Foundational doctrine and mechanics for grounding work in Evermuse evidence; loaded by every other skill.	Customer Voice & Feedback	#EC4899
north-star-metric	North Star Metric	Defines a customer-centric North Star plus a tree of 3–5 input metrics that drive it.	Strategy & Vision	#8B5CF6
product-strategy	Product Strategy	Builds a 9-section Product Strategy Canvas with every pillar anchored in evidence and market context.	Strategy & Vision	#8B5CF6
product-vision	Product Vision	Crafts a product vision anchored in customers' own words about the future they want.	Strategy & Vision	#8B5CF6
strategy-frameworks	Strategy Frameworks	Runs SWOT, PESTLE, Porter's Five Forces, or Ansoff with every cell citing real evidence.	Strategy & Vision	#8B5CF6
strategy-red-team	Strategy Red Team	Adversarially attacks a strategy/PRD/roadmap by hunting counter-evidence; includes a pre-mortem mode.	Strategy & Vision	#8B5CF6
competitive-battlecard	Competitive Battlecard	Builds a sales-ready battlecard whose "they say / we say" rows are real objections from conversations.	Market & Competition	#F59E0B
competitor-analysis	Competitor Analysis	Finds differentiation openings by cross-checking capability data against what customers say about rivals.	Market & Competition	#F59E0B
market-sizing	Market Sizing	Estimates TAM/SAM/SOM top-down and bottom-up, validated against a real customer beachhead.	Market & Competition	#F59E0B
positioning-and-messaging	Positioning And Messaging	Generates positioning and campaign options in customers' mined vocabulary, each mapped to a proving quote.	Market & Competition	#F59E0B
beachhead-segment	Beachhead Segment	Picks the first beachhead segment on pain, willingness to pay, winnable share, and reachability.	Segmentation & Targeting	#06B6D4
ideal-customer-profile	Ideal Customer Profile	Builds an ICP from won-and-retained accounts: firmographics, behaviors, JTBD, pains.	Segmentation & Targeting	#06B6D4
segmentation	Segmentation	Segments a user base by evidence-based need differences into 3–5 groups with JTBD, pains, and quotes.	Segmentation & Targeting	#06B6D4
value-proposition	Value Proposition	Designs a 6-part JTBD value prop, then converts it into marketing/sales/onboarding statements.	Segmentation & Targeting	#06B6D4
brainstorm-ideas	Brainstorm Ideas	Generates ideas from PM/Designer/Engineer angles, seeded by real unmet needs, with idea→quote mapping.	Prioritization & Planning	#F97316
gap-analysis	Gap Analysis	Audits spec-vs-spec, spec-vs-code, and build-vs-customer-need, with evidence behind each finding.	Prioritization & Planning	#F97316
opportunity-solution-tree	Opportunity Solution Tree	Builds a Torres OST (outcome→opportunities→solutions→experiments), flagging unsupported nodes.	Prioritization & Planning	#F97316
outcome-roadmap	Outcome Roadmap	Rewrites a feature-list roadmap into outcome lanes citing the demand evidence behind each.	Prioritization & Planning	#F97316
prioritize-features	Prioritize Features	Ranks a backlog with Reach/Impact from actual account-level demand counts; returns a top-5 with quotes.	Prioritization & Planning	#F97316
assumptions	Assumptions	Surfaces risky assumptions, separates already-answered findings, scores by Impact × Risk, matches experiments.	Specs & Requirements	#10B981
create-prd	Create PRD	Produces an 8-section business PRD grounded in verbatim quotes, needs, and pains with source links.	Specs & Requirements	#10B981
user-stories	User Stories	Breaks a feature into INVEST-shaped user/job stories, each citing its motivating quote and criteria.	Specs & Requirements	#10B981
write-feature-spec	Write Feature Spec	Writes an SDD-structured feature spec: stories, Given/When/Then scenarios, requirements, success criteria.	Specs & Requirements	#10B981
development-plan	Development Plan	Builds a dev plan starting from what customers requested, then spec-driven phasing and ordered tasks.	Delivery & Engineering	#22C55E
review-pr	Review PR	Reviews a PR against code quality, the spec, and the actual customer asks behind it.	Delivery & Engineering	#22C55E
setup-evermuse	Setup Evermuse	Guides setup of the Evermuse MCP extension inside an agentic app using the UI rendering tools.	Delivery & Engineering	#22C55E
shipping-artifacts	Shipping Artifacts	Generates ship-readiness docs for vibe-coded features and reconstructs the missing "intent" section.	Delivery & Engineering	#22C55E
test-scenarios	Test Scenarios	Writes Given/When/Then QA scenarios from acceptance criteria plus real edge cases customers hit.	Delivery & Engineering	#22C55E
business-model	Business Model	Builds a 9-block Business Model Canvas with problem/segment boxes grounded in customer evidence.	Growth & GTM	#84CC16
gtm-strategy	GTM Strategy	Builds messaging, channels, segment focus, motions, metrics, and a launch timeline from evidence.	Growth & GTM	#84CC16
pricing-strategy	Pricing Strategy	Designs pricing from real willingness-to-pay signals and objections, with competitor pricing secondary.	Growth & GTM	#84CC16
brainstorm-okrs	Brainstorm OKRs	Drafts team OKRs where objectives map to evidenced customer outcomes and KRs measure real pain reduction.	Ops & Meta	#6B7280
list-capabilities	List Capabilities	Renders the interactive picker of every agentic skill, grouped by category, and waits for a pick.	Ops & Meta	#6B7280
release-notes	Release Notes	Generates changelogs from tickets/PRDs/git with a "You asked, we built" angle naming real requesters.	Ops & Meta	#6B7280
summarize-conversation	Summarize Conversation	Turns one interview or meeting into structured notes: participants, JTBD, timestamped quotes, decisions, actions.	Ops & Meta	#6B7280


When a user clicks on a skill in your rendering, run the corresponding skill please using read_skills.