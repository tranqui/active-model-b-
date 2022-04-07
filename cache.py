#!/usr/bin/env python3

# Use @lru_cache decorator for caching directly in memory without disk.
from functools import lru_cache

# # Create directory in the temp folder for caching to the disk.
# from pathlib import Path
# import tempfile
# source_path = Path(__file__).resolve()
# source_dir = source_path.parent
# source_project = source_dir.parts[-1]
# cachedir = Path('%s/%s' % (tempfile.gettempdir(), source_project))

# # Use @disk.memory decorator for caching to disk.
# from joblib import Memory
# disk = Memory(cachedir, verbose=0)
disk = None
