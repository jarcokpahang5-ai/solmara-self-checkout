#!/usr/bin/env python3
"""Entry point for the self-checkout one-liner.

The joke itself lives in entry_text; this file only fetches it
through the module and puts it on standard output, nothing more.
"""

import entry_text


def main():
    print(entry_text.LINE)


if __name__ == "__main__":
    main()
