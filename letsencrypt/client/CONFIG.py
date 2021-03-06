"""Config for Let's Encrypt."""
import os.path


ACME_SERVER = "letsencrypt-demo.org"
"""CA hostname.

If you create your own server... change this line

Note: the server certificate must be trusted in order to avoid
further modifications to the client."""

SERVER_ROOT = "/etc/apache2/"
"""Apache server root directory"""

CONFIG_DIR = "/etc/letsencrypt/"
"""Configuration file directory for letsencrypt"""

WORK_DIR = "/var/lib/letsencrypt/"
"""Working directory for letsencrypt"""

BACKUP_DIR = os.path.join(WORK_DIR, "backups/")
"""Directory where configuration backups are stored"""

TEMP_CHECKPOINT_DIR = os.path.join(WORK_DIR, "temp_checkpoint/")
"""Replaces MODIFIED_FILES, directory where temp checkpoint is created"""

IN_PROGRESS_DIR = os.path.join(BACKUP_DIR, "IN_PROGRESS/")
"""Directory used before a permanent checkpoint is finalized"""

CERT_KEY_BACKUP = os.path.join(WORK_DIR, "keys-certs/")
"""Directory where all certificates/keys are stored.

Used for easy revocation"""

KEY_DIR = os.path.join(SERVER_ROOT, "ssl/")
"""Where all keys should be stored"""

CERT_DIR = os.path.join(SERVER_ROOT, "certs/")
"""Certificate storage"""

OPTIONS_SSL_CONF = os.path.join(CONFIG_DIR, "options-ssl.conf")
"""Contains standard Apache SSL directives"""

LE_VHOST_EXT = "-le-ssl.conf"
"""Let's Encrypt SSL vhost configuration extension"""

APACHE_CHALLENGE_CONF = os.path.join(CONFIG_DIR, "le_dvsni_cert_challenge.conf")
"""Temporary file for challenge virtual hosts"""

S_SIZE = 32
"""Byte size of S"""

NONCE_SIZE = 16
"""byte size of Nonce"""

RSA_KEY_SIZE = 2048
"""Key size"""

DIFFICULTY = 23
"""bits of hashcash to generate"""

CERT_PATH = CERT_DIR + "cert-letsencrypt.pem"
"""Let's Encrypt cert file."""

CHAIN_PATH = CERT_DIR + "chain-letsencrypt.pem"
"""Let's Encrypt chain file."""

INVALID_EXT = ".acme.invalid"
"""Invalid Extension"""

CHALLENGE_PREFERENCES = ["dvsni", "recoveryToken"]
"""Challenge Preferences Dict for currently supported challenges"""

EXCLUSIVE_CHALLENGES = [frozenset(["dvsni", "simpleHttps"])]
"""Mutually Exclusive Challenges - only solve 1"""

CONFIG_CHALLENGES = frozenset(["dvsni", "simpleHttps"])
"""These are challenges that must be solved by a Configurator object"""

REWRITE_HTTPS_ARGS = [
    "^.*$", "https://%{SERVER_NAME}%{REQUEST_URI}", "[L,R=permanent]"]
"""Rewrite rule arguments used for redirections to https vhost"""
