import yaml


class YamlParser(object):

    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    def load_file(self):
        data = {}

        with open(self.yaml_file, "r") as stream:
            try:
                data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        return data

    def save_dict_to_yaml(self, dict_data: dict):
        with open(self.yaml_file, 'w') as file:
            file.write(yaml.dump(dict_data, allow_unicode=True, sort_keys=False))
        return self.yaml_file

    def load_yaml_to_dict(self):
        with open(self.yaml_file) as file:
            dict_data = yaml.load(file.read(), Loader=yaml.FullLoader)
            return dict_data

