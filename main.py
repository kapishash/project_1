from src.project_1 import logger 
from src.project_1.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.project_1.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.project_1.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.project_1.pipeline.model_trainer_pipeline import ModelTrainerTrainingPipeline
from src.project_1.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline


STAGE_NAME="Data Ingestion Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<") 
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.initiate_data_ingestion()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
    except Exception as e:  
        logger.exception(e)
        raise e
    
STAGE_NAME="Data Validation Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        data_validation = DataValidationTrainingPipeline()
        data_validation.initiate_data_validation()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME="Data Transformation Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e

    
STAGE_NAME="Model Training Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.initiate_model_training()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME="Model Evaluation Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.initiate_model_evaluation()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
