from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

#There are currently fewer options, more options will be added in the future
DEFAULT_CONFIG = {
    "width": "100%",
    "height": 400,
    "preview_theme": "dark",
    "typewriterMode": "True",
    "mode": "ir",
    "debugger": "false",
    "value": "",
    "theme": "dark",
    "icon": "ant",
    "outline": "false",
    "sanitize":"true"
}

if settings.LANGUAGE_CODE.lower() == "zh-hans":
    DEFAULT_CONFIG["lang"] = "zh_CN"
elif settings.LANGUAGE_CODE.lower() == "ja-jp":
    DEFAULT_CONFIG["lang"] = "ja_JP"
elif settings.LANGUAGE_CODE.lower() == "ko-kr":
    DEFAULT_CONFIG["lang"] = "ko_KR"
else:
    DEFAULT_CONFIG["lang"] = "en_US"

class MDConfig(dict):
    def __init__(self, config_name = "default"):
        self.update(DEFAULT_CONFIG)
        self.set_configs(config_name)

    def set_configs(self, config_name = "default"):
        configs = getattr(settings, "VDITOR_CONFIGS", None)
        if configs:
            if isinstance(configs, dict):
                if config_name in configs:
                    config = configs[config_name]
                    if not isinstance(config, dict):
                        raise ImproperlyConfigured('VDITOR_CONFIGS["%s"] \
                                        setting must be a dictionary type.' %config_name)
                    self.update(config)
                else:
                    raise ImproperlyConfigured("No configuration named '%s' \
                                    found in your VDITOR_CONFIGS setting." %config_name)
            else:
                raise ImproperlyConfigured('VDITOR_CONFIGS setting must be a\
                                dictionary type.')
