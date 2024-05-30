from ml_flow_22052024.config.configuration import ConfigurationManager
from ml_flow_22052024.components.data_transfermation import DataTransformation
from ml_flow_22052024 import logger

Stage_name = 'Data Transfermation'

class DataTransfermationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transfermation_config = config.get_data_transfermation_config()
        data_transfermation = DataTransformation(config=data_transfermation_config)
        data_transfermation.train_test_spliting()


if __name__ == '__main__':
    try:
        logger.info(f'>>>>>>>>>>> stage {Stage_name} is started <<<<<<<<<<<<<')
        obj = DataTransfermationPipeline()
        obj.main()
        logger.info(f'>>>>>>>>>>> stage {Stage_name} is completed <<<<<<<<<<<<<')

    except Exception as e:
        logger.exception(e)
        raise e

