# Index Builder Performance

`tests/test_build_indexes.py` creates 1,000 valid atomic Markdown documents in a temporary `docs/` tree and runs the public `scripts/build_indexes.py --build` command.

The test fails when the command takes 10 seconds or more, directly enforcing RNF02 in CI. It does not modify repository content and runs with the PyYAML version pinned by the workflow.

The same suite also proves idempotence by running `--build` twice and comparing every generated `INDEX.md` plus `llms.txt` byte-for-byte.
