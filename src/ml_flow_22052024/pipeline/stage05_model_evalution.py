from ml_flow_22052024.config.configuration import ConfigurationManager
from ml_flow_22052024.components.model_evaluation import ModelEvaluation
from ml_flow_22052024 import logger

STAGE_NAME = "Model Evalution stage"

class ModelTrainerEvalutionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_data_model_eval_config()
        model_evalution = ModelEvaluation(config=model_evaluation_config)
        model_evalution.log_into_mlflow()




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerEvalutionPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e