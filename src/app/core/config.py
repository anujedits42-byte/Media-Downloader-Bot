import environs

env = environs.Env()
env.read_env()

class Settings:
    bot_token = env.str("BOT_TOKEN")
    bot_user_redis = env.bool("BOT_USE_REDIS", default=False)
    tg_api_server_url = env.str("TG_API_SERVER_URL", default="https://api.telegram.org")
    admins_ids = env.list("ADMINS_IDS", default=[])

db_name = env.str("POSTGRES_DB", default=None) or env.str("PGDATABASE", default="postgres")
    db_user = env.str("POSTGRES_USER", default=None) or env.str("PGUSER", default="postgres")
    db_password = env.str("POSTGRES_PASSWORD", default=None) or env.str("PGPASSWORD", default="")
    db_host = env.str("POSTGRES_HOST", default=None) or env.str("PGHOST", default="localhost")
    db_port = env.str("POSTGRES_PORT", default=None) or env.str("PGPORT", default="5432")

redis_host = env.str("REDIS_HOST", default="localhost")
    redis_db_name = env.str("REDIS_DB", default="0")

selenium_url = env.str("SELENIUM_REMOTE_URL", default="http://localhost:4444/wd/hub")

lastfm_api_key = env.str("LASTFM_API_KEY", default="")
