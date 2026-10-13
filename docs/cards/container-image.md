---
id: card-container-image
type: card
title: Container image
status: draft
updated: 2026-10-13
tags: [docker, containers, images, build]
related: [guide-build, guide-release, guide-deploy]
kind: concept
stages: [3, 5, 6]
---

# Container image

## In one sentence

A container image is a sealed, read-only package containing an application and everything it
needs to run: runtime, libraries, system packages and default settings.

## Why it exists

Software used to behave differently on each machine because each had different versions of the
language, libraries and operating system packages ("it works on my machine"). An image freezes
all of that once, so the same package runs identically on a laptop, in CI and in the cloud.

## How it works

```
Dockerfile ──docker build──▶ Image (layers) ──push──▶ Registry ──pull──▶ Container (running copy)
```

- A **Dockerfile** lists the steps: start from a base image, install dependencies, copy code,
  set the start command.
- Each step produces a **layer**. Layers are cached and shared, so rebuilding after a small code
  change only redoes the last layers.
- The finished image gets a **tag** (a movable label such as `sha-4f2c1a`) and a **digest**
  (a fixed fingerprint of its exact contents).
- A **container** is a running copy of an image. One image can start many identical containers.
- Settings that differ between environments are **not** baked in; they arrive as environment
  variables when the container starts.

## Analogy

The Dockerfile is a recipe, the image is a frozen meal made from it, and a container is that meal
heated and served. You can serve many plates from the same frozen batch, and they all taste the same.

## Key terms

| Term | Meaning |
|---|---|
| Base image | The starting image, such as an official slim Python or Node image |
| Layer | A cached filesystem change produced by one Dockerfile step |
| Multi-stage build | Build in one stage with tools, copy only the result into a small final stage |
| Tag | A human-readable, movable label for an image |
| Digest | An immutable content fingerprint (`sha256:…`) |
| Registry | A server that stores and serves images |

## Pitfalls

- Relying on `latest`: you can no longer tell which code is running.
- Baking secrets or environment-specific settings into the image.
- Huge images from development tools or GPU libraries that production does not need.
- Running as root inside the container.
- Building release images on a laptop instead of in CI.

## Provider mapping

| Azure | AWS | Google Cloud | Open source |
|---|---|---|---|
| Azure Container Registry | Amazon Elastic Container Registry (ECR) | Artifact Registry | Docker, Podman, Buildah; registries: Harbor, Docker Hub |

## Say it in an interview

> CI builds one immutable image per commit with a multi-stage Dockerfile, tags it with the commit
> SHA and pushes it to a private registry. Every environment runs that exact image; only
> environment variables and secrets differ.
