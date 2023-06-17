import json
import os

from jinja2 import Environment, FileSystemLoader


class VocabularyBuilder:
    """
    The VocabularyBuilder 
    """
    def __init__(self):
        pass

    @staticmethod
    def build() -> dict:
        """
        Builds the vocabulary

        :return: A dictionary of prefix: URI relations
        """
        file_loader = FileSystemLoader('')
        env = Environment(loader=file_loader)
        template = env.get_template('src/resources/vocabulary.json')
        context = template.render(base_kwg_url=os.environ.get('base_address'))
        return json.loads(context)
