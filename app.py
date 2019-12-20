import json
import tkinter as tk
from tkinter import filedialog
from watson_developer_cloud import VisualRecognitionV3

# User Input
#------------
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

# Watson VR Instance Creation with API Credentials
#-------------------------------------------------
visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='u1jn0cC6uwwq0zMlVNRGB1Vy0EPULS--5z7RsFC4jIyE')

# Request API Service with the Selected user Input
#--------------------------------------------------
with open(file_path, 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.6',
    classifier_ids='ProductCatalogService_735746673').get_result()

output_json = json.loads(json.dumps(classes, indent=2))

# Extract the Class from JSON output
#------------------------------------
class_identified = output_json['images'][0]['classifiers'][0]['classes'][0]['class']

print('This falls in category :',class_identified)





