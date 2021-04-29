Brainlit Project <br>
NeuroData Design (2020-2021) <br>
Advisors: Tommy Athey and Professor Joshua Vogelstein <br><br>
Prerna's original cell detection scripts: https://github.com/prernasingh11/CLARITY


Files:
  - `CNN_soma_detection.ipynb`: final project/script for testing Brainlit data on pre-trained model
  - `crossvalidation4.pt`: pre-trained model
  - `paths.png`: list of paths for training data if desired (did not use)
  - `requirements.txt`: used to create python environment
  - `compareSubvols` : used to run the model through a set of 12x12x12 subvolumes
  
Folders
  - `brainlit` and `cloud-volume`: exisiting packages used to pull Brain1 data from the cloud
  - `output`: NCRs and ROIs produced from `CNN_soma_detection.ipynb`
  - `TigerGPU`:   
    - `slurm1.sh` : runs `wholeBrain.py` on TigerGPU
    - `testenv.yml` : reproduce brainlit environment
    - `wholeBrain.py` : loop through entire brain, output all 12x12x12 subvolumes and their coordinates
