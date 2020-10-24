from .settings import DIR_ROOT
import json

class SquadPath:
    @staticmethod
    def of(tag, version):
        return "%sSQuAD%s/%s-v%s.json" % (DIR_ROOT, version, tag, version)
    
class SquadLoader:
    @staticmethod
    def load(tag, version):
        """Loads specified suqad dataset json object.

        Args:
            tag (str): 'train' or 'dev'; the tag of the squad dataset to load.
            version (float): 1.1 or 2.0; the version of the squad dataset to load.

        Returns:
            A json object of the specified squad dataset.

        """
        path = SquadPath.of(tag, version)
    
        with open(path, 'r', encoding='utf-8') as file:
            squad_json = "".join(file.readlines())
        return json.loads(squad_json)