import argparse
import datetime

from mmcv import Config, DictAction
from mmdet.utils import replace_cfg_vals, update_data_root

def parse_args():
    parser = argparse.ArgumentParser(description='Train a detector')
    parser.add_argument('configs',
        nargs='+',
        help='file paths of configs used to train. If more than one, later files override config entries of earliers.'
        )
    parser.add_argument('--out',
        help='path of the output (config) file',
        default=None
        )
    parser.add_argument(
        '--cfg-options',
        nargs='+',
        action=DictAction,
        help='override some settings in the used config, the key-value pair '
        'in xxx=yyy format will be merged into config file. If the value to '
        'be overwritten is a list, it should be like key="[a,b]" or key=a,b '
        'It also allows nested list/tuple values, e.g. key="[(a,b),(c,d)]" '
        'Note that the quotation marks are necessary and that no white space '
        'is allowed.')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()

    cfg = None
    for config_path in args.configs:
        next_cfg = Config.fromfile(config_path)
        if cfg is None:
            cfg = next_cfg
        else:
            cfg.merge_from_dict(next_cfg._cfg_dict)
    cfg = replace_cfg_vals(cfg)
    update_data_root(cfg)

    if args.cfg_options is not None:
        cfg.merge_from_dict(args.cfg_options)
    
    path_out = args.out
    if path_out is None:
        today = datetime.datetime.today().strftime('%Y%m%d-%H%M')
        path_out = f'config_{today}.py'
    
    cfg.dump(path_out)

if __name__ == '__main__':
    main()
