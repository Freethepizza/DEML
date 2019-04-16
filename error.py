#
#    .___             .__
#  __| _/____   _____ |  |
# / __ |/ __ \ /     \|  |
#/ /_/ \  ___/|  Y Y  \  |__
#\____ |\___  >__|_|  /____/
#     \/    \/      \/
#
#Error handler
from dictionary import Stack_A,Stack_C

def CheckIntegrity_A():
    if len(Stack_A) is not len(Stack_C):
        print("\nTAG ERROR,CHECK YOUR OPEN/CLOSED TAGS")

def FinalStack_Error():
    print("FATAL ERROR:CONTROL STACK IS DIFFERENT FROM GENERALSTACK")
