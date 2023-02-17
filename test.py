import sys
import os

text = "# Heading\n\n*[HTML]: Hyper Text Markup Language\n\nThe HTML specification is maintained by the W3C.\n"

sys.path.insert(0, os.path.abspath('extensions'))

import mdit_py_abbr

from markdown_it import MarkdownIt

md = MarkdownIt().use(mdit_py_abbr.abbr_plugin)

print(md.render(text))
