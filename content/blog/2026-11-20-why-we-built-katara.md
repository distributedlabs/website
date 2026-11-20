+++
title = "Why we built Katara: the brief after the meeting"
description = "A project handoff shows why people and AI agents need the same decisions, source documents and boundaries."
date = 2026-11-20
slug = "why-we-built-katara"

[extra]
cover = "images/blog/katara.svg"
category = "AI Memory Engineering"
+++

Picture a developer picking up a checkout redesign on Monday. The ticket says “remove guest checkout.” The approved brief says to keep it. Both documents came from the client. Which one should the developer trust?

<!-- more -->

The account lead knows: on Friday the client agreed to remove guest checkout from the wholesale store only. It stays on the retail site. The ticket lost those last two words. Give that ticket to a coding agent and it could produce a perfectly good change to the wrong store.

Victor Castell and Matthew Rossi built [Katara](https://katara.ai/) for the part of the job that comes before writing code: knowing enough about the project to do the right work. We call it a context layer for humans and AI. A person picking up a ticket and an agent helping with it should be able to work from the same decision and check where it came from.

## What goes in a Brain?

Katara calls its shared knowledge spaces *Brains*. Take the checkout example. A useful starting set would be the approved brief, the note from Friday’s call and a short decision the account lead has reviewed: “Guest checkout stays on retail. Remove it from wholesale.” The note matters because the sentence on its own won’t tell the next person why the scope changed.

When someone asks about checkout, Katara can retrieve relevant material from that knowledge rather than making the person paste the whole project history into another chat. Access matters here. An agency may run two shops on the same platform for different clients; a relevant document from the other account is still the wrong document to retrieve. Katara’s retrieval takes permissions into account.

A disagreement between sources is also useful information. If the Friday decision hasn’t been recorded, we’d rather have a developer notice the conflict and ask the account lead than have an agent quietly choose a version. No memory system can recover an agreement that never made it out of the meeting.

## Where Hermes fits

We run our own project with Hermes Agent. In an agency workflow, we think of the division of work like this: Katara supplies the project context; Hermes can use it to prepare the next piece of work. In our example, that might be a revised ticket that names the wholesale store and leaves retail alone. The developer can check it against the decision before touching either checkout.

If you want to try this with your team, pick a question that keeps landing on the same person’s desk. Give a colleague the source material they’re allowed to see and ask them to answer it. Then ask an agent the same question. Can both tell you what was decided, and point to the document that settles it? That’s a more useful first test than counting how many files you’ve uploaded.

[Explore Katara](https://katara.ai/) or read our earlier piece on [what makes AI memory useful](@/blog/2026-08-21-memory-is-a-product-surface.md).
