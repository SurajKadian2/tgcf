"""Declare all global constants."""

COMMANDS = {
    "start": "Check whether I am alive",
    "batch": "[SRC]Bulk download",
    "cancel": "[SRC]Cancel batch",
    "forward": "[TGCF]Set a new forward",
    "style": "[TGCF]Font style",
    "remove": "[TGCF]Remove an existing forward",
    "help": "link to developers",
 
}

REGISTER_COMMANDS = True

KEEP_LAST_MANY = 10000

CONFIG_FILE_NAME = "tgcf.config.json"
CONFIG_ENV_VAR_NAME = "TGCF_CONFIG"

MONGO_DB_NAME = "tgcf-config"
MONGO_COL_NAME = "tgcf-instance-0"
