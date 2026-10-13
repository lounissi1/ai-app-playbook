---
id: guide-build
type: guide
title: Build
status: draft
updated: 2026-10-13
tags: [docker, images, ci]
related: [card-container-image, guide-code, guide-test, guide-release]
stage: 3
inputs: [merged code, a Dockerfile]
outputs: [one container image per commit]
---

# Build

## Goal

Turn every merged commit into one container image, built by CI, that runs the same everywhere.

## Inputs and outputs

**Inputs**

- Code on `main`
- A Dockerfile for each deployable part of the application

**Outputs**

- One container image per deployable part, tagged with the commit SHA

## Steps

1. Write one Dockerfile per deployable part (for example web, API, worker). One image may serve
   several roles with different start commands.
2. Use a **multi-stage build**: a build stage with compilers and dev tools, and a small runtime
   stage that copies only what production needs.
3. Start from an official slim base image with a pinned version.
4. Run as a **non-root** user.
5. Order instructions from least to most frequently changing (dependencies before source code) so
   layers cache well.
6. Add a `.dockerignore` to keep tests, local data and secrets out of the image.
7. Add a `docker-compose.yml` that runs the whole app locally with its database and cache.
8. In CI, build the image on every push to `main`, tag it with the commit SHA, and cache layers
   between runs.

## Files to copy

- `starters/azure/docker/` (planned: Python API and Node web app Dockerfiles)
- `starters/azure/workflows/build-push.yml` (planned)

## Done when

- [ ] `docker compose up` runs the full application locally
- [ ] Image runs as non-root
- [ ] Image contains no tests, local data or secrets
- [ ] CI builds the image and tags it with the commit SHA
- [ ] Image size recorded; obvious bloat removed

## Common mistakes

- Using only the `latest` tag; you can no longer tell what is running.
- Installing GPU or development packages in a CPU-only production image.
- Copying the whole repository before installing dependencies, which breaks layer caching.
- Building release images on a laptop. Only CI builds what gets deployed.

## Using an AI agent

**Delegate:** writing Dockerfiles and compose files, shrinking image size, explaining build errors.

**Review yourself:** the base image and its version, the user the container runs as, and the
`.dockerignore` contents.
