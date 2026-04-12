# TODO Tracker Skill

## Name
TODO Tracker

## Purpose
Maintain a persistent `TODO.md` scratch pad in the workspace root so tasks can be added, viewed, completed, or removed consistently.

## File Location
- `TODO.md` in the workspace root

## When to Use
Use this skill when the user wants to:
- view pending tasks
- add a task to a running TODO list
- mark a task as done
- remove a task from the TODO list
- maintain a simple persistent scratch pad for action items

## Trigger Phrases

### View TODO
Examples:
- “what's on the TODO?”
- “show TODO”
- “pending tasks?”
- “show me my task list”

Command:
```bash
cat TODO.md
```

### Add Item
Examples:
- “add X to TODO”
- “TODO: X”
- “remember to X”

Command:
```bash
bash skills/todo-tracker/scripts/todo.sh add "<priority>" "<item>"
```

Priority values:
- `high`
- `medium`
- `low`

Default priority:
- `medium`

### Mark Done
Examples:
- “mark X done”
- “completed X”
- “finished X”

Command:
```bash
bash skills/todo-tracker/scripts/todo.sh done "<item-pattern>"
```

### Remove Item
Examples:
- “remove X from TODO”
- “delete X from TODO”

Command:
```bash
bash skills/todo-tracker/scripts/todo.sh remove "<item-pattern>"
```

## Workflow
1. Check whether `TODO.md` already exists in the workspace root.
2. If it does not exist, initialize it using the required format.
3. Interpret the user’s intent:
   - view
   - add
   - mark done
   - remove
4. Run the appropriate command.
5. Return the updated TODO content or a brief confirmation, depending on the user request.

## Heartbeat / Maintenance
On heartbeat, inspect `TODO.md` for stale unfinished items older than 7 days.

Suggested maintenance checks:
- identify unfinished stale items
- keep the `Last updated` field current
- preserve completed items in the `Done` section unless explicitly removed

## Required TODO.md Format

```md
# TODO

*Last updated: 2026-01-17*

## 🔴 High Priority
- [ ] Item one (added: 2026-01-17)

## 🟡 Medium Priority
- [ ] Item two (added: 2026-01-17)

## 🟢 Nice to Have
- [ ] Item three (added: 2026-01-17)

## ✅ Done
- [x] Completed item (done: 2026-01-17)
```

## Behavior Rules
- Keep all active tasks grouped by priority.
- Preserve task metadata such as `added:` and `done:` dates.
- Use checkbox format consistently.
- Do not guess missing task details unless the user’s wording is clear.
- Default to `medium` priority when the priority is not specified.
- Match items using a reasonable text pattern when marking done or removing items.

## Example Requests and Actions

### Example 1
User:
> Add “Send Cynthia the deck” to TODO with high priority

Action:
```bash
bash skills/todo-tracker/scripts/todo.sh add "high" "Send Cynthia the deck"
```

### Example 2
User:
> Mark “Send Cynthia” done

Action:
```bash
bash skills/todo-tracker/scripts/todo.sh done "Send Cynthia"
```

### Example 3
User:
> Remove “book venue” from TODO

Action:
```bash
bash skills/todo-tracker/scripts/todo.sh remove "book venue"
```

### Example 4
User:
> Show TODO

Action:
```bash
cat TODO.md
```

## Output Style
- For view requests: show the current `TODO.md` content.
- For add / done / remove requests: provide a concise confirmation and optionally show the updated list when helpful.

## Notes
- This skill assumes the helper script exists at:
  `skills/todo-tracker/scripts/todo.sh`
- This skill is designed for lightweight persistent task tracking inside the workspace.
