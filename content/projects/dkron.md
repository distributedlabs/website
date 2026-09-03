+++
title = "Dkron"
description = "A distributed, fault-tolerant job scheduling system built for cloud-native environments."
weight = 1

[extra]
thumbnail = "images/projects/dkron.svg"
year = "2015—present"
services = ["Distributed systems", "Product engineering", "Open source"]
project_url = "https://dkron.io/"
+++

## The brief

Scheduled jobs are critical infrastructure, but traditional cron concentrates responsibility on a single machine. Dkron was created to bring workload automation into distributed environments without giving up cron's focused, understandable model.

## The approach

Dkron coordinates scheduled work across a cluster. Raft provides consensus and leader election, while a lightweight gossip protocol supports node communication and failure detection. If the leader becomes unavailable, another node takes over so scheduled work can continue without a single point of failure.

The product pairs that distributed core with practical operating surfaces: a web interface, a JSON API, execution history, logs, retries, job dependencies, concurrency controls, and tag-based node selection.

## The result

An open-source scheduler written in Go that scales from a small cluster to thousands of nodes while remaining straightforward to install and operate. Dkron is available for Linux, macOS, and Windows, with free and commercial editions for different operational requirements.

[Visit dkron.io](https://dkron.io/) · [View the source on GitHub](https://github.com/dkron-io/dkron)
