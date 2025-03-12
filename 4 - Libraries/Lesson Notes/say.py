import sys

from sayings import hello # type: ignore

if len(sys.argv) == 2:
    hello(sys.argv[1])

print(__name__)