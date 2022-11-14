# Third Party Libraries/Packages can be installed using PIP and then use on our python scripts
# Let's try to use a third party package named art (https://pypi.org/project/art/) to create a text art
# Other Available third party packages can be found here : https://pypi.org/

# First Step is to install the art package. On Terminal, run 'pip3 install art'
# Pip reference here -> https://docs.python.org/3/tutorial/venv.html#managing-packages-with-pip

# Second step is to import text2art  from the art package.
from art import text2art
from os import system
system("clear")

# Finally, use the text2art function and specify the text you want to create an art from.
# Refer to the documentation of the package on how to use the other functions -> https://pypi.org/project/art/
elit = text2art("PYTHON")
print(elit)  # Output a text art

