#!/usr/bin/env sh

set -euxo pipefail

groups
spectool -g *.spec
mock --resultdir "${PWD}" --buildsrpm --spec *.spec --sources "${PWD}"
mock --resultdir build_dir/results/ --rebuild *.src.rpm
