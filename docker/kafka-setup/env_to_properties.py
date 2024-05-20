import os
import re


def env_to_properties(env_prefix: str, properties_file: str):
    pattern = re.compile('(?<=[^_])_(?=[^_])')
    props = {}

    for (env_name, val) in os.environ.items():
        if env_name.startswith(env_prefix):
            raw_name = env_name[len(env_prefix):].lower()
            prop_dot = '.'.join(pattern.split(raw_name))
            props[prop_dot] = val

    with open(properties_file, 'r') as f:
        for k, v in props.items():
            f.writelines(f'{k}={v}\n')
