## Quick tutorial for Opentrons-2 protocol creation and running

### Install the opentrons Python library

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
