from ml_flow_22052024 import logger
from ml_flow_22052024.pipeline.stage01_data_ingetion import Dataingetionpipeline
from ml_flow_22052024.pipeline.stage02_data_validation import DataValidationPipeline

Stage_name = " stage01 Data ingetion "

if __name__ == '__main__':
    try:
        logger.info(f"<<<<<<<< Stage {Stage_name} is started >>>>>>>")
        obj = Dataingetionpipeline()
        obj.main()
        logger.info(f"<<<<<<<< Stage {Stage_name} is Completed >>>>>>>")
    except Exception as e:
        logger.exception(e)
        raise e
    

Stage_name = 'Data validation'

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>stage {Stage_name} is strted <<<<<<<<<<<<<<")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>stage {Stage_name} is Completed <<<<<<<<<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e