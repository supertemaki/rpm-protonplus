FROM registry.fedoraproject.org/fedora-minimal:40

RUN <<EOF
  printf '%s/n' "upgrade packages..."
  microdnf \
    --refresh \
    --assumeyes \
    --nodocs \
    --setopt=install_weak_deps=False \
        upgrade
  printf '%s/n' "installing packages..."
  microdnf \
    --assumeyes \
    --nodocs \
    --setopt=install_weak_deps=False \
      install \
        dnf5 \
        mock \
        podman \
        rpmdevtools
  printf '%s/n' "cleaning cache..."
  microdnf --assumeyes autoremove
  microdnf clean all
  rm -rf \
    /tmp/* \
    /usr/share/{cracklib,doc,licences,man/} \
    /var/cache/dnf/* \
    /var/lib/dnf/{history,yumdb}/* \
    /var/lib/rpm/__db.*
  printf '%s/n' "fix: mock Insufficient rights."
    usermod -aG mock root
EOF

WORKDIR /mockbuilder
COPY . .
#RUN <<EOF
#  useradd mockbuilder
#  chown -R mockbuilder:mock .
#EOF
#USER mockbuilder

VOLUME /var/cache/mock

# fix: [podman] overlay is not supported over overlayfs
# https://github.com/containers/buildah/issues/3666#issuecomment-1351992335
VOLUME /var/lib/containers

ENTRYPOINT [ "./entrypoint.sh" ]
