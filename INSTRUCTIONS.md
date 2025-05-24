The original Restormer repository can be found at https://github.com/swz30/Restormer/tree/main.

Follow the instructions in INSTALL.md from the Restormer repository to install the necessary dependencies for the project.

Download the pretrained models for motion deblurring and single-image defocus deblurring with the links in the README.md files in the folders for each task.

You can place images you would like to resize in My_Code/to_resize then run my resize_images.py script to resize the images. Alter the amount of resize in the script if you wish.

You can find the resized images in the newly created resized/ directory.

Place the resized images in either my_images/motion or my_images/defocus depending on the task.

Run the run_on_my_images.sh script to run the demo.py script from the Restormer repository to process the images.

The commands in the script are from the tile option command in the demo.py file since I had problems with Gebru not having enough memory.
Also, I slightly modified demo.py to run on a specific GPU on Gebru using a line from Project 3.

The result images can be found in result_images.
