## Quick tutorial for Opentrons-2 protocol creation and running

*If you are only interested in running OP2 protocols, go to section 2*

### 1. Install the opentrons Python library

This part covers the instalation of the opentrons library on your (Mac or Linux) machine. It is not mandatory to do that if you only want to run the scripts of this repo on your machine. This step is only needed if you want to test your own code and want to contribute to the page. 

This guide follows the same instructions as [here](https://support.opentrons.com/ot-2/getting-started-software-setup/installing-the-opentrons-api-on-your-computer), but explained step by step for slow people like me.
The first step is to install __pipenv__ on your machine. If you are in Mac, and you have Homebrew installed, you can just type:

```
brew install pipenv
```

This will install pipenv on your computer and will allow you to create the Python environment needed to test the scripts. 

The next step is to clone the git repository to your own computer. Note that the following command will clone the opentrons repo in actual path you are in when you type this on your terminal.

```
git clone https://github.com/Opentrons/opentrons
```

Next, you have to go to the *api* folder inside *opentrons* folder:

```
cd opentrons\api
```
Once there, you have to install the package with the following command:

```
make install
```

After a while (it could take a little bit long), and if no warnings have arised, you will have your library installed on your computer. You can run the tests to see that everything is running properly:

```
make test
```

After all this, and if everything is working properly, you have to be in the *api* directory and then start a Python environment through pipenv with the following command:

```
pipenv shell
```

If everything is correct, you should have this kind of promt in your terminal, *api* followed by a bunch of characters like this:
> api-De4ySai-

Start a Python sesion typing *python* into the terminal, and then try to load some functions from the opentrons package by typing: 

```
from opentrons import labware, instruments
```
If no warnings or errors arises, then, everything should be fine!

### 2. What you will find in this repo

This repo is intended to have a collection of the protocols that we use in our laboratory, written for the Opentrons-2 machine. There are several folders:
- **tests**: scripts to test your machine with very simple instructions like moving tips between positions in the tip rack, pipetting liquid between specific positions, and so on
- **oficial**: some official scripts downloaded from the OP2 website
- **protocols**: our own protocol codes

### 3. Recommended actions!!

For a proper functioning of the OP2, please READ:

- Be sure that your machine is connected to your computer (turn on and off the lights, for example).
- **Always** check that the labware is in the correct positions. And that it is the appropriate labware. 
- **Always** make the *labware calibration* between different protocols, even if it is the same protocol it would be highly recommendable to do so.
- Tip calibration is not always needed, but surely it should be made between huge protocols or between different days.
- **Always** review what the OP2 is going to do before clicking *Run protocol*, surprises are not always good. If there is something wrong, either the script is not valid, or you are using an invalid protocol.
- It would be good that, if you don't know the protocol you are about to run (because it is the first time or you have edited the script), **stop and see** what it does once it starts. May be you want to press the *Cancel run* button before you unlock the (l)a(b)pocalypsis.
- If you have followed all these points, everything should be OK and you can do the fun stuff while the OP2 does the boring and repetitive actions. 
- *Bonus track: be sure that your machine always follows the [laws of robotics](https://en.wikipedia.org/wiki/Three_Laws_of_Robotics)*

## Calibration

Due to my experience the machine is buggy sometimes and it will break tips in the calibration step for some unknown reason. Because of this, I would recommend some steps to calibrate the machine without breaking half of your lab stuff:

- Have always *testing* labware with which you can work. 
- Calibrate the OP2 with this *testing* labware to avoid destroying your experiments
- As sometimes has happened to me, OP2 has a taste for breaking tips because it does not know where to stop. For this, have a cutted tip which you should place on the pipette once you start calibrating. Move the pipette to your labware and let it go down. Then, move it upwards and replace the cutted tip with a proper one, and then, calibrate it. Repeat this process with all the labware you have for the current protocol. 
