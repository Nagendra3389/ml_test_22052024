from ml_flow_22052024 import logger
from ml_flow_22052024.config.configuration import ConfigurationManager
from ml_flow_22052024.components.data_validation import DataValiadtion

Stage_name = 'Data validation'

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>stage {Stage_name} is strted <<<<<<<<<<<<<<")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>stage {Stage_name} is Completed <<<<<<<<<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e