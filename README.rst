Promises Patterns Demo
======================

This demo shows different patterns of JS promises:

- a "chain", where AJAX calls must be made in order. For an example
  banking app, this gets the price of a product, converts that price
  into RithmCoin, then transfers that amount. These steps must happen
  in order.

- a "pool", where several AJAX calls must be made, but one does not
  depend on another. This requests the weather in 3 different zip codes,
  making those requests all at once, but only reporting back once all
  3 responses have been received.

- a "race", where several AJAX calls are made, but we only need one
  response. In this case, this uses 3 different joke-providing endpoints,
  but since any joke will do, completes once the first one returns.

Rather than relying on external APIs, this uses a Flask backend.

To demo:

1. Install Flask, either in a virtualenv or globally.

2. Start the app (``python server.py``)

3. Browse to `http://localhost:5001/static/index.html`

4. Turn on the JS console, since the demo buttons log the results :)
