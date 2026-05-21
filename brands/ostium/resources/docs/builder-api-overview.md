> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ostium.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Builder API Overview

> Use the Builder API directly for live prices, candles, and streaming, or consume the same data through the Builder SDK.

Base URL:

```text theme={null}
https://builder.ostium.io
```

Direct endpoints:

* `GET /v1/prices`
* `POST /v1/ohlc`
* `WS /v1/prices/stream`

SDK wrappers:

* `getAllPrices()`
* `getCandles()`
* `streamPrices()`
