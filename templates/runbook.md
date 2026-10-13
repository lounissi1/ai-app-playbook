# Runbook: <Symptom, e.g. "API returns 5xx">

## Signal

<Which alert fires, or what a user reports.>

## Impact

<Who is affected and how badly.>

## Check first

1. <Dashboard or query to open>
2. <Recent deploys: was anything released in the last hour?>
3. <Dependencies: database, storage, external APIs>

## Fix

| Cause | Action |
|---|---|
| Bad release | Roll back to the previous revision |
|  |  |

## Escalate

<When and to whom.>

## After

- Write a postmortem using `templates/postmortem.md` if users were affected.
