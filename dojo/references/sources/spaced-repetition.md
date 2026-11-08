# Spaced repetition and the Anki mindset

> Status: from James's write-up (2026-11), formatting tidied by Claude; content unchanged. The binding rules are in `rules.md` and the pitfalls in `pitfalls.md`; this file is the evidence and detail behind them.

## Principles supported

- S4: retrieval practice (the testing effect)
- S5: understand first, memorize second
- S6: honest self-assessment, recognition vs. recall
- S3: interleaving
- S7: spacing and the forgetting curve
- A2: a small daily habit that compounds

## Caveats

Spacing and retrieval are among the most replicated findings in learning research (established). Specific algorithms (SM-2, FSRS) and lifetime-cost estimates are practitioner figures. Cards keep knowledge; they don't build skill.

---

## Part 1: The science, or why it works
### 1. The forgetting curve

In the 1880s, Hermann Ebbinghaus showed that memories fade quickly and predictably, fastest just after learning, unless they’re reinforced. Every successful review makes the curve flatter, so the memory lasts longer before the next review is needed.

What Anki does: It tracks each card separately and times reviews against that card’s own decay. Easy cards fade into the background and hard ones come back often.
### 2. The spacing effect

Reviews spread out over time produce much better long-term retention than the same number of reviews crammed together. This is one of the most replicated findings in cognitive psychology. Cramming can work for tomorrow’s exam but collapses within weeks.

What Anki does: Intervals grow, for example 1 day, then 3, 8, 3 weeks, 2 months, 6 months and so on. Each success earns a longer gap.
### 3. The testing effect (retrieval practice)

Pulling information out of memory strengthens it far more than putting it in again by rereading. This is Ultralearning’s Retrieval principle.

What Anki does: Every card forces active recall. You see a question and have to produce the answer before revealing it.
### 4. Desirable difficulty

Robert and Elizabeth Bjork showed that learning that feels harder in the moment often sticks better. Their model separates two kinds of memory strength:

Storage strength: how deeply something is learned.
Retrieval strength: how easily you can recall it right now.

Retrieving something when retrieval strength is low, so it’s a struggle, gives the biggest gain in storage strength.

What Anki does: It deliberately waits until a card is nearly forgotten. That’s why reviews feel effortful: the struggle is when the learning happens.
### 5. Honest self-assessment (metacognition)

People are bad at judging what they know. Rereading notes feels like knowing because the material is familiar, an illusion of competence. Recognizing an answer isn’t the same as being able to recall it.

What Anki does: It shows you the gap between “that looks familiar” and “I can produce it,” every day.
### 6. Interleaving

Mixing different topics during practice leads to better long-term retention and discrimination than studying them in blocks.

What Anki does: Reviews come up shuffled across topics and ages, so your brain has to work out what each card is asking before answering it.
### 7. Efficiency

Because reviews thin out as cards mature, a well-made card might cost only a few minutes of total review time over years. Michael Nielsen and others estimate that’s a tiny lifetime cost for permanent recall.

The result: Long-term memory goes from something unreliable to something you can plan and budget.
## Part 2: The mindset

What makes Anki powerful isn’t just the software. It’s a particular attitude toward memory and learning.

### 1. Memory is a choice

This is Michael Nielsen’s framing in his essay Augmenting Long-Term Memory. Normally, what you remember is mostly luck. With spaced repetition you decide what you’ll remember, and if you put it into Anki and keep reviewing, you’ll know it.

In practice: When you meet something worth knowing long-term, make a card instead of hoping it sticks.
### 2. Small daily effort compounds

Anki rewards consistency, not intensity. Twenty minutes a day for a year beats a week of marathon sessions. Missed days create a growing review backlog, but daily reviews keep the load manageable.

In practice: Do your reviews every day, like brushing your teeth. Treat it as a non-negotiable habit, not a study session that needs motivation.
### 3. Trust the system and outsource scheduling

You don’t decide what to review or when; the algorithm does. That frees you from planning and from the urge to over-review what you already know or avoid what you don’t.

In practice: Don’t second-guess intervals or cram the night before. Let the scheduler work.
### 4. Grade honestly

The system is only as good as your answers. If you mark a half-remembered card as “Good” to feel better, it gets scheduled too far out and you forget it.

In practice: If you couldn’t recall it cleanly and in time, press “Again.” Failure is information, not judgment. (This links to Flow’s point about dropping self-consciousness.)
### 5. Understand first, memorize second

Anki is for retaining knowledge, not for understanding it. Memorizing something you don’t understand gives you brittle, isolated facts.

In practice: Learn the concept first (read, solve problems, explain it). Then use cards to keep it.
### 6. Make knowledge atomic

Woźniak’s minimum information principle says each card should test one small idea. Big cards (“List the 12 causes of WW1”) are hard to grade and quickly turn into chores.

In practice: Break complex ideas into small cards that each ask exactly one thing.
### 7. Memory is the base of thinking

A common objection is that you can always look things up. But you can’t think with, notice connections between, or creatively combine knowledge you don’t have in your head. Expertise is largely a huge store of well-organized, quickly available knowledge.

In practice: Memorize the basics of a field (vocabulary, key facts, core formulas, principles) so your working memory is free for higher-level thinking.
## Part 3: Best practices
Write your own cards when you can. Writing cards is part of learning: it forces you to process and restate the idea. Premade decks are useful in some fields (medicine, languages), but you lose that benefit.
One fact per card.
Ask for recall, not recognition. “What does X do?” is better than “Is X involved in Y?”
Add context and connections. Images, examples, mnemonics and links to things you know make cards stick and easier to recall in real life.
Use cloze deletions (fill-in-the-blank) for facts that belong in context.
Make cards from both directions where it matters, such as word to meaning and meaning to word in languages.
Delete or rewrite troublesome cards. A card you keep failing (a “leech”) is usually badly designed, not a sign you’re stupid. Split it, add context or drop it.
Cap new cards per day. New cards create reviews for weeks. Ten to twenty new cards a day can soon mean 100 to 200 reviews.
Be selective. Only card what’s worth remembering long-term. A common rule of thumb, popularized by Gwern, is to memorize something if you’d otherwise spend more than about 5 minutes over your lifetime looking it up.
On modern Anki, enable FSRS and set a target retention, usually around 85 to 90%. Higher targets increase your review load sharply.
Common pitfalls
Pitfall	Why it happens	Fix
Review debt and burnout	Too many new cards, missed days	Lower new cards per day; never skip reviews
Memorizing without understanding	Making cards before learning the concept	Understand first, then card
Bloated cards	Several facts on one card	Split into small cards
Recognition illusion	Cards that are too easy or yes/no	Ask for genuine recall
Grading yourself too kindly	Ego, impatience	Be strict; “Again” is fine
Knowledge in a vacuum	Cards isolated from real use	Combine with direct practice
“Ease hell” (older SM-2)	Repeated failures shrink intervals permanently	Switch to FSRS
