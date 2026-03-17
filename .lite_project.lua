local config = require "core.config"

config.plugins.build.targets = {
  { name = "main", type = "shell", runner = "python3", command = "tools/build.py", args_clean = {"-c"}},
}

