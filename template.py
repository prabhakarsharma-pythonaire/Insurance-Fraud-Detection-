import os


#directories we need to create
directories=['application_logging', 'best_model_finder', 'data', 'DataTransformation_Prediction', 'DataTransform_Training',
    'DataTypeValidation_Insertion_Prediction', 'DataTypeValidation_Insertion_Training', 'data_ingestion',
    'data_preprocessing', 'documentation', 'EDA', 'file_operations', 'models', 'Prediction_Batch_files',
    'Prediction_Database', 'Prediction_FileFromDB', 'Prediction_Logs', 'Prediction_Output_File',
    'Prediction_Raw_Data_Validation', 'preprocessing_data', 'templates', 'TrainingArchiveBadData',
    'Training_Batch_Files', 'Training_FileFromDB', 'Training_Logs', 'Training_Raw_data_validation', '__pycache__'
]

#files to be created

files = [
'main.py', 'predictFromModel.py', 'prediction_Validation_Insertion.py', 'test.py',
    'trainingModel.py', 'training_Validation_Insertion.py', 'Procfile', 'requirements.txt', 'schema_prediction.json',
    'schema_training.json'
]


def create_directories_and_files():
    #create directories
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Directory {directory} created ")
        else:
            print(f"Directory {directory} already exists.")

    #create files
    for file in files:
        if not os.path.exists(file):
            open(file,"w").close()
            print(f"File '{file}' created")
        else:
            print(f"File '{file}' already present")

if __name__ == "__main__":
    create_directories_and_files()