from ml_flow_22052024.constants import *
from ml_flow_22052024.utils.common import read_yaml,create_directories
from ml_flow_22052024.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig
from ml_flow_22052024.entity.config_entity import Model_trainingConfig,ModelEvaluationConfig


class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    

    def get_data_validation_config(self) -> DataValidationConfig:
            config = self.config.data_validation
            schema = self.schema.COLUMNS

            create_directories([config.root_dir])

            data_validation_config = DataValidationConfig(
                root_dir=config.root_dir,
                STATUS_FILE=config.STATUS_FILE,
                unzip_data_dir = config.unzip_data_dir,
                all_schema=schema,
            )

            return data_validation_config
    

    def get_data_transfermation_config(self) -> DataTransformationConfig:
         config = self.config.data_transformation
         create_directories([config.root_dir])

         data_transfermation_config = DataTransformationConfig(
              root_dir = config.root_dir,
              data_path = config.data_path
         )

         return data_transfermation_config
    

    def get_model_training_config(self) -> Model_trainingConfig:
         config = self.config.model_trainer
         params = self.params.ElasticNet
         schema = self.schema.TARGET_COLUMN
         create_directories([config.root_dir])

         model_training_config = Model_trainingConfig(
              root_dir = config.root_dir,
              train_data_path = config.train_data_path,
              test_data_path = config.test_data_path,
              model_name = config.model_name,
              alpha = params.alpha,
              l1_ratio = params.l1_ratio,
              target_column = schema.name
         )

         return model_training_config
    

    def get_data_model_eval_config(self) -> ModelEvaluationConfig:
         config = self.config.model_evaluation
         params = self.params.ElasticNet
         schema = self.schema.TARGET_COLUMN
         
         create_directories([config.root_dir])

         model_eval_config = ModelEvaluationConfig(
              root_dir= config.root_dir,
              test_data_path = config.test_data_path,
              model_path = config.model_path,
              metric_file_name = config.metric_file_name,
              all_params = params,
              target_column = schema.name,
              mlflow_uri = 'https://dagshub.com/pnagendra341/ml_test_22052024.mlflow'
         )

         return model_eval_config

