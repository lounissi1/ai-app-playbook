---
id: guide-release
type: guide
title: Release
status: draft
updated: 2026-10-13
tags: [registry, versioning, approvals]
related: [card-container-image, guide-build, guide-deploy]
stage: 5
inputs: [a tested image]
outputs: [a stored, named version ready to deploy]
---

# Release

## Goal

Turn a tested image into a named, stored version that can be deployed, and later redeployed, exactly.

## Inputs and outputs

**Inputs**

- An image that passed all checks

**Outputs**

- The image in a private registry under an immutable tag
- An approval record when one is required

## Steps

1. Push the image to a **private registry** in the same region as where it will run.
2. Tag it with the commit SHA. Optionally add a human-readable version tag (`v1.4.0`) on releases.
3. Treat tags as immutable: never overwrite an existing tag with different contents.
4. CI signs in to the registry with **OIDC federation**, never with a stored password.
5. For production, require an **approval**: a named person confirms before deploy continues
   (in GitHub Actions, a protected *environment* with required reviewers).
6. Write release notes from the merged pull requests.
7. Add a retention rule that removes old, unused images.

## Files to copy

- `starters/azure/workflows/build-push.yml` (planned)

## Done when

- [ ] Image in the registry, tagged by commit SHA
- [ ] CI uses OIDC to push
- [ ] Production deploys wait for an approval
- [ ] Old images are cleaned up automatically

## Common mistakes

- Rebuilding the image for each environment. Build once, promote the same image.
- Overwriting tags, so a rollback deploys something different.
- Registry in a different region, adding cost and pull time.

## Using an AI agent

**Delegate:** writing the push workflow, release notes, retention rules.

**Review yourself:** who can approve production, and that no long-lived credentials are stored in CI.
