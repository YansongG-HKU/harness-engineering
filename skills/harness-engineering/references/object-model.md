# Object Model Reference

This packaged copy keeps the installed `harness-engineering` skill usable after
`skill-installer` copies only this directory.

In the source repository, the canonical source lives at
docs/architecture/object-model.md.

## Primary Objects

- Workflow
- Prompt Asset
- Tool Contract
- Eval
- Trace
- Policy

## Object-First Review Rule

When a run fails, ask:

1. Was the workflow wrong?
2. Was the prompt asset wrong?
3. Was the tool contract unclear or unsafe?
4. Was the eval too weak or misaligned?
5. Was the policy missing or violated?
6. Did the trace fail to expose the problem?

## Why Skill Is Not a Primary Object

Skills route people into the canonical objects. They do not replace them.
