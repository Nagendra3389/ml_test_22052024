from ml_flow_22052024.config.configuration import ConfigurationManager
from ml_flow_22052024.components.model_trainig import Model_trainig
from pathlib import Path
from ml_flow_22052024 import logger


Stage_name = 'model traing'
class Model_trainig_Pipeline:
    def __init__(self):
        pass

    def main(self):

        try:
            with open(Path('artifacts\data_validation\status.txt'),"r") as f:
                status = f.read().split(" ")[-1]
            if status == 'True':

                config = ConfigurationManager()
                model_training_config = config.get_model_training_config()
                model_trainig = Model_trainig(config=model_training_config)
                model_trainig.train()
            else:
                raise Exception("Your data schema is not Valid!!!")
            
        except Exception as e:
            print(e)


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {Stage_name} started <<<<<<")
        obj = Model_trainig_Pipeline()
        obj.main()
        logger.info(f">>>>>> stage {Stage_name} completed <<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e

