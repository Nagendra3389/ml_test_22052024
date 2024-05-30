from ml_flow_22052024 import logger
from ml_flow_22052024.pipeline.stage01_data_ingetion import Dataingetionpipeline
from ml_flow_22052024.pipeline.stage02_data_validation import DataValidationPipeline
from ml_flow_22052024.pipeline.stage03_data_transfermation import DataTransfermationPipeline
from ml_flow_22052024.pipeline.stage04_model_training import Model_trainig_Pipeline
from ml_flow_22052024.pipeline.stage05_model_evalution import ModelTrainerEvalutionPipeline

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
    

Stage_name = 'Data Transfermation'


if __name__ == '__main__':
    try:
        logger.info(f'>>>>>>>>>>> stage {Stage_name} is started <<<<<<<<<<<<<')
        obj = DataTransfermationPipeline()
        obj.main()
        logger.info(f'>>>>>>>>>>> stage {Stage_name} is completed <<<<<<<<<<<<<')

    except Exception as e:
        logger.exception(e)
        raise e
    

Stage_name = 'model traing'

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
        obj = Model_trainig_Pipeline()
        obj.main()
        logger.info(f">>>>>> stage {Stage_name} completed <<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME = "Model Evalution stage"

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerEvalutionPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
