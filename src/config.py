from dynaconf import Dynaconf

settings_files = ['../conf/basic.yaml',
                  '../conf/settings.yaml',
                  '../conf/development.yaml',
                  '../conf/production.yaml']

settings = Dynaconf(
    warn_dynaconf_global_settings=True,
    environments=True,
    lowercase_read=False,
    load_dotenv=True,
    envvar_prefix="APP",
    settings_files=settings_files,
)

if (settings.DEBUG):
    settings.configure(FORCE_ENV_FOR_DYNACONF='development')
else:
    settings.configure(FORCE_ENV_FOR_DYNACONF='production')
