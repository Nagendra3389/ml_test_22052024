from ml_flow_22052024.config.configuration import ConfigurationManager
from ml_flow_22052024.components.data_ingetion import DataIngestion
from ml_flow_22052024 import logger

Stage_name = " Data ingetion "

class Dataingetionpipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f"<<<<<<<< Stage {Stage_name} is started >>>>>>>")
        obj = Dataingetionpipeline
        obj.main()
        logger.info(f"<<<<<<<< Stage {Stage_name} is Completed >>>>>>>")
    except Exception as e:
        logger.exception(e)
        raise e