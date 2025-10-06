import os


class FileReader:
    def set_env(self):
        try:
            folder="allure-results"
            file_name="environment.properties"
            folder_path=os.path.join(os.getcwd(),folder)
            os.makedirs(folder_path,exist_ok=True)
            file_path=os.path.join(folder_path,file_name)

            with open(file_path, 'w') as f:
                f.write("Browser=Chrome\n")
                f.write("URL=https://www.cnarios.com/challenges\n")
                f.write("Tester=Anurag\n")
                f.write("Environment=QA\n")
        except Exception as e:
            print(f"Reason: {e}")