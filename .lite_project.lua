local config = require "core.config"

config.plugins.build.targets = {
  { name = "main", type = "shell", runner = "python", command = "make.py", args_clean = {"-c"}},
}

