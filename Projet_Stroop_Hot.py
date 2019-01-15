import expyriment
import random
import glob
from  expyriment.stimuli import FixCross, BlankScreen

exp = expyriment.design.Experiment(name="Hot Stroop")
expyriment.control.initialize(exp)
kb = expyriment.io.Keyboard()


consigne = """Vous allez voir apparaitre à l'écran un visage exprimant une émotion ainsi qu'un mot signifiant une émotion.
L'objectif de cette tâche est de dénommer l'émotion exprimée par le visage (et non pas par le mot).
Vous devez répondre le plus rapidement possible avec le moins d'erreurs possible.
Pour répondre vous utiliserez le clavier de l'ordinateur avec les 4 touches suivantes :
C = colère
V = joie
B = peur
N = tristesse
Pour commencer appuyer sur la barre espace du clavier."""

#présentation de la consigne
consigne = expyriment.stimuli.TextScreen("Consigne",
                                              text=consigne)
consigne.preload()
expyriment.control.start()
consigne.present()
kb.wait_char(' ')

#présentation croix de fixation
target = FixCross(size=(25, 25), line_width=4)
target.present()
exp.clock.wait(2000)

#présentation du stimulus
visage_joie = expyriment.stimuli.Picture('Joie.png',(40,200))
visage_joie.present()
kb.wait_char('v')
target.present()
exp.clock.wait(2000)
visage_peur = expyriment.stimuli.Picture('Peur.png', (40,200))
visage_peur.present()
kb.wait_char('b')


expyriment.control.end()
