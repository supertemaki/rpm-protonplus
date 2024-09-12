#!/usr/bin/env sh

set -eux

#podman build \
#   --tag mockbuilder \
#   "${PWD}"
mkdir build_dir
podman --transient-store run \
  --rm \
  --cap-add=SYS_ADMIN \
  --image-volume=tmpfs \
  --volume mock_cache:/var/cache/mock \
  --volume "${PWD}"/build_dir/:/mockbuilder/build_dir \
  mockbuilder:latest

#useradd mockbuilder
#chown -R mockbuilder:mockbuilder ./*
#usermod -aG mock mockbuilder
