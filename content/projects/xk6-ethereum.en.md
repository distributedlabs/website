+++
title = "xk6 Ethereum"
description = "A k6 extension for performance testing EVM-compatible blockchains and smart contracts."
weight = 2

[extra]
thumbnail = "images/projects/xk6-ethereum.svg"
year = "2022"
services = ["Blockchain", "Performance engineering", "Open source"]
project_url = "https://github.com/distributedlabs/xk6-ethereum"
+++

## The brief

Conventional load-testing tools understand HTTP requests, but blockchain performance depends on protocol-specific behavior: gas prices, nonces, transaction submission, mining, receipts, contract calls, and changing chain state. Testing an EVM network effectively requires those concepts to be native to the workload.

## The approach

xk6 Ethereum extends k6 with a JavaScript API backed by a Go Ethereum client. Test scenarios can query balances and blocks, estimate gas, send transactions, wait for receipts, deploy contracts, and call existing contracts without rebuilding that protocol layer for every benchmark.

The extension also exposes blockchain-specific measurements alongside k6's standard output, including request duration, mined transactions per second, chain progress, and time to mine. Included Grafana and InfluxDB configuration makes local benchmark runs observable from the first test.

## The result

An MIT-licensed toolkit for expressing reproducible Ethereum load scenarios in JavaScript while retaining k6's execution model and reporting ecosystem. Teams can exercise EVM nodes and contracts with workloads that describe real blockchain activity rather than generic transport traffic.

[View the source on GitHub](https://github.com/distributedlabs/xk6-ethereum)
