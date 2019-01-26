import expyriment
import random

from  expyriment.stimuli import FixCross, BlankScreen

exp = expyriment.design.Experiment(name="Hot Stroop")
expyriment.control.initialize(exp)
kb = expyriment.io.Keyboard()

NCONG = 15
NINCONG = 15
NTRIALS = NCONG + NINCONG
MAXDURATION = 2000
target = FixCross(size=(25, 25), line_width=4)
blankscreen = BlankScreen()


expyriment.control.start()
response_device = exp.keyboard

# Consigne
consigne = """Vous allez voir apparaitre à l'écran un visage exprimant une émotion ainsi qu'un mot signifiant une émotion.
L'objectif de cette tâche est de dénommer l'émotion exprimée par le visage (et non pas par le mot).
Vous devez répondre le plus rapidement possible avec le moins d'erreurs possible.
Pour répondre vous utiliserez le clavier de l'ordinateur avec les 4 touches suivantes :
C = colère
V = joie
B = peur
N = tristesse
Pour commencer appuyer sur la barre espace du clavier."""

# Dictionnaire de paires (mots/images) qui sont congruentes
motspics_congruents = {
    "JOIE": "emotion_joie.png",
    "TRISTESSE": "emotion_tristesse.png",
    "COLERE": "emotion_colere.png",
    "PEUR": "emotion_peur.png"
    }

# Dictionnaire de paires (mots/images) qui sont incongruentes
motspics_incongruents = {
    "JOIE": ["emotion_tristesse.png", "emotion_peur.png", "emotion_colere.png"],
    "COLERE": ["emotion_tristesse.png", "emotion_peur.png", "emotion_joie.png"],
    "PEUR": ["emotion_tristesse.png", "emotion_colere.png", "emotion_joie.png"],
    "TRISTESSE": ["emotion_peur.png", "emotion_colere.png", "emotion_joie.png"]
}

# Affichage de la consigne
consigne = expyriment.stimuli.TextScreen("Consigne",
                                              text=consigne).present()
kb.wait_char(' ')
target.present()
exp.clock.wait(2000)


# Fonction permettant de générer les stimuli (congruents et incongruents)
mots_possibles = list(motspics_congruents.keys())

clock = expyriment.misc.Clock()
reactiontimes = []

def generate_stimulus(is_congruent):

    canvas = expyriment.stimuli.Canvas((500,500))
    mot = random.choice(mots_possibles)
    if is_congruent:
        imgpath = motspics_congruents[mot]
    else:
        imgpath = random.choice(motspics_incongruents[mot])
    pictures = expyriment.stimuli.Picture(imgpath,(40,200))
    pictures.plot(canvas)
    mot_afficher = expyriment.stimuli.TextLine(mot)
    mot_afficher.plot(canvas)
    canvas.preload()
    canvas.present()
    rt = exp.keyboard.wait([expyriment.misc.constants.K_c, expyriment.misc.constants.K_v, expyriment.misc.constants.K_b, expyriment.misc.constants.K_n])
    stim = kb.wait_char(['c', 'v', 'b', 'n'])
    exp.data.add([rt])
    target.present()
    exp.clock.wait(2000)
    #return stim

exp.data_variable_names = ["RT"]

# Boucle permettant de randomiser les essais congruents / incongruents
trial_is_congruent = [True] * NCONG + [False] * NINCONG
random.shuffle(trial_is_congruent)

for i in range(NTRIALS):
    is_congruent = trial_is_congruent[i]
    stim = generate_stimulus(is_congruent)


expyriment.control.end(goodbye_text="Merci d'avoir participé !", goodbye_delay=3000)
