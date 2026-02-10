import Ed

# Standard EdPy setup
Ed.EdisonVersion = Ed.V3
Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

for i in range(45):
    for i in range(360):
        Ed.Drive(Ed.FORWARD, Ed.SPEED_5, 1)
        Ed.Drive(Ed.SPIN_RIGHT, Ed.SPEED_5, 1)
    Ed.Drive(Ed.SPIN_LEFT, Ed.SPEED_5, 8)