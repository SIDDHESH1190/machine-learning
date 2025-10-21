from data_cleaning.clean_dataset import CleanDataset
import os

if __name__ == "__main__":

    # Get the absolute path of the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, '..', '..'))

    # Define file paths
    input_filepath = os.path.join(project_root, 'data', 'students_data.csv')
    output_filepath = os.path.join(project_root, 'data', 'cleaned_students.csv')

    if os.path.exists(output_filepath):
        print("Cleaned data already exists.")
    else:
        # Create a DataCleaner instance
        cleanDataset = CleanDataset(input_filepath)

        isDataCleanedAndSaved = False
        # Load the data
        if cleanDataset.load_data() is not None:
            # Analyze the data
            isAnalyzed = cleanDataset.analyze_data()

            if not isAnalyzed:
                print("Data analysis failed.")
                exit(1)
            else:
                if cleanDataset.clean_data():
                    print("\nData cleaned successfully.")
                    isDataCleanedAndSaved = cleanDataset.save_cleaned_data(output_filepath)
                else:
                    print("Data cleaning failed.")
        else:
            print("Failed to load data.")
        
        if isDataCleanedAndSaved:
            print("Cleaned data saved successfully.")
        else:
            print("Failed to save cleaned data.")

    