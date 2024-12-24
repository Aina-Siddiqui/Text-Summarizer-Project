from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.logging import logger
from src.textSummarizer.components.data_validation import DataValidation

class DataValidationPipeline(DataValidation):
    def __init__(self):
        pass
    def main(self):
        config=ConfigurationManager()
        data_validation_config=config.get_data_validation()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.validate_all_files_exist()
