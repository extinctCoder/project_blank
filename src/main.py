from log_x import log_arbiter
from pathlib import Path
from os.path import join
from hydra import main as config_parser
from omegaconf import DictConfig, OmegaConf

# @config_parser(version_base=None, config_path=str(join(Path(__file__).resolve().parent.parent, 'conf')), config_name="config")
# def main_app(cfg: DictConfig) -> None:
#     '''Main entry point of the project. Only prints hello world to the console.
#
#     Returns:
#         None: Returns Nothing
#     '''
#     print(OmegaConf.to_object(cfg)['app']['development'])
#     return None


@config_parser(version_base=None, config_path=str(join(Path(__file__).resolve().parent.parent, 'conf')), config_name='config')
def main_app(cfg: DictConfig) -> None:
    '''Main entry point of the project. Only prints hello world to the console.
    Returns:
        None: Returns Nothing
    '''
    logger = log_arbiter(logger_name=__name__, cfg=cfg)
    print(logger)
    # logger = logger.log_arbiter()
    # logger.info('hello world')
    return None


if __name__ == '__main__':
    main_app()
