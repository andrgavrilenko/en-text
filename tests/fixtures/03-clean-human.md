We broke the deploy on Tuesday. Not badly, and not for long, but we broke it, and the reason is worth writing down.

The new config loader reads environment variables at import time. That is fine in production, where the variables exist. In the CI container they do not, so the import failed, the test runner never started, and the pipeline reported success because a runner that never starts also never fails. Nobody noticed for six hours.

The fix was one line: read the variables lazily. The lesson is not about config loaders. It is that a green pipeline proves only that nothing reported failure, which is not the same thing as nothing failing. We now have a test that asserts the runner ran at least one test — the smallest sanity check I have ever written, and the one I most wish we had written earlier.

If you have a pipeline you trust, go check whether it can fail silently. Ours could.
