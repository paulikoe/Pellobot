import subprocess

'''
Bylo potřeba stáhnout celý soubor yolov5 z colabu, poté nastavit váhy, bez nich to nešlo. 
Byl problém, že Windows tento soubor nezvládá, proto do souboru detect, byly přidány řádky s úpravou (viz detect.py)
best.py jsou zatím moje nejlepší váhy
'''

def run_yolov5_detection():
    # Define the command to run
    command = ["python", "yolov5/detect.py", "--weights","yolov5/runs/train/exp3/weights\\best.pt","--save-txt",
    "--save-conf","--source", "path_to_input_image_or_video"]

    # Run the command
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Wait for the process to finish and capture output
    stdout, stderr = process.communicate()
    
    # Check if there was an error
    if process.returncode != 0:
        print("Error occurred while running YOLOv5 detection:")
        print(stderr.decode("utf-8"))
    else:
        print("YOLOv5 detection completed successfully.")
        print(stdout.decode("utf-8"))

# Call the function to run YOLOv5 detection
#run_yolov5_detection()
