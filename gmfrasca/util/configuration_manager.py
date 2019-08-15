import logging
import yaml
import os


class ConfigurationManager(object):

    def __init__(self, config_path, autoreload=False):
        self._logger = logging.getLogger(self.__class__.__name__)
        self.config_file_path = config_path
        self.autoreload = autoreload
        self.loaded_config = None

    @property
    def config(self):
        if self.loaded_config is None or self.autoreload is True:
            self.loaded_config = self._load_config(self.config_file_path)
        return self.loaded_config

    def _load_config(self, config_path):
        self._logger.debug("Loading config from {}".format(config_path))
        with open(config_path) as f:
            loaded = self._update_with_envvars(
                yaml.load(f, Loader=yaml.FullLoader))
        self._logger.debug("Loaded config:\n{}".format(loaded))
        return loaded

    def _update_with_envvars(self, config):
        if isinstance(config, dict):
            for k, v in config.copy().items():
                if k.endswith("_env") and isinstance(v, str):
                    config.update({k[:-4]: os.environ.get(v)})
                else:
                    config[k] = self._update_with_envvars(v)
            return config
        elif isinstance(config, list):
            return [self._update_with_envvars(x) for x in config]
        return config
