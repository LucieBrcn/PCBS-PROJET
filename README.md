# PCBS-PROJET : Tâche du Stroop "Hot"

### Sommaire #
**1. Introduction**

**2. Stimuli**

**3. Procédure**

**4. Résultats**

**5. Conclusion du projet**


### 1. Introduction #

Le but de ce projet était d'adapter la tâche de stroop classique (Stroop, 1935) ou l'on présente au sujet des mots ("rouge", "jaune", "vert" et "bleu") écris dans une certaine couleur ("rouge", "jaune", "vert" et "bleu"). Le but de l'expérience est de dénomer la couleur de l'encre sans lire le mot qui lui est associé. Cette tâche permet de rendre compte des capactiés d'inhibition d'un sujet. L'inhibition se définit comme la capacité à resister aux automatismes (ici la lecture du mot). Par conséquent on devra inhiber la lecture du mot (automatique) pour activer la réponse correcte, à savoir dénomer la couleur de l'encre (non automatique). Cette tâche est dite "froide" dans le sens ou elle ne fait pas intervenir les émotions (les stimuli étant neutres). Ce qui est intéressant c'est de voir quelle influence un contexte émotionnel peut avoir sur les capacités d'inhibition. Pour cela j'ai adpaté cette tâche de stroop "cool" (froide) en une tâche de stroop "hot" (permettant de rendre compte des capacités d'inhibition chaude).   

Hypothèse : on suppose que le contexte émotionnel aura un impact sur les capacités d'inhibition. C'est à dire que les temps de réponses (TR) seront différents selon la tâche (stroop froid et stroop chaud)  


### 2. Stimuli #

Pour cela, j'ai utilisé 4 images exprimant des émotions ("Colère", "Joie", "Peur" et "Tristesse")  

![Stimuli visages](/Users/luciebracon/Desktop/COGMASTER/M1/AE_Programmation/PCBS-PROJET_BRACON/Ekmanfaces.png)

Ainsi que 4 mots exprimant les même émotions.  
Je les ai ensuite combiné afin de créer des items "congruents" (lorsque l'émotion du visage concorde avec l'émotion exprimée par le mot) et des items "incongruents" (lorsque l'émotion du visage est différente de l'émotion exprimée par le mot)  
Par exemple : item congruent = Visage Joie / mot Joie
              item incongruent = Visage Joie / mot Colere

Pour cela, j'ai créé deux dictionnaires :

Le premier est un dictionnaire contenant les paires (mot/visage) qui sont congruentes. 

    motspics_congruents = {
    "JOIE": "emotion_joie.png",
    "TRISTESSE": "emotion_tristesse.png",
    "COLERE": "emotion_colere.png",
    "PEUR": "emotion_peur.png"
    }


Le deuxième contient les paires qui sont incongruentes.

    motspics_incongruents = {
    "JOIE": ["emotion_tristesse.png", "emotion_peur.png", "emotion_colere.png"],
    "COLERE": ["emotion_tristesse.png", "emotion_peur.png", "emotion_joie.png"],
    "PEUR": ["emotion_tristesse.png", "emotion_colere.png", "emotion_joie.png"],
    "TRISTESSE": ["emotion_peur.png", "emotion_colere.png", "emotion_joie.png"]
    }
    

### 3. Procédure #

La tâche est composée de 30 essais comprenant 15 essais congruents et 15 essais incongruents. Le but étant de générer aléatoirement des essais congruents et incongruents. Pour cela il a fallut randomsier les différents essais à l'aide d'une boucle générant aléatoirement ces essais. 

    trial_is_congruent = [True] * NCONG + [False] * NINCONG
    random.shuffle(trial_is_congruent)
    

    for i in range(NTRIALS):
    is_congruent = trial_is_congruent[i]
    stim = generate_stimulus(is_congruent)
    
Par la suite, j'ai défni une fonction permettant de générer ces différents essais. A l'aide de la fonction 'canvas', les deux stimuli (visage et mot) apparaissent en même temps sur l'écran. 

Entre cahque présentation des stimuli une croix de fixation apparait pendant 2 secondes à l'écran. 

Lorsque les stimuli apparaissent, le sujet doit répondre à l'aide de son clavier par les touches "c" pour colère, "v" pour joie, "b" pour peur et "n" pour tristesse. J'ai choisi de prendre ces 4 touches la, car dans l'idéal il fallait des touches rapprochés sur le clavier (afin d'éviter que le sujet ne cherche la lettre, ce qui aurait un impact sur le temps de réponse). Afin d'éviter toute confusion, il est préférable de recourvir ces 4 touches du clavier par les lettres correspndantes (à savoir C pour colère, J pour joie, P pour peur et T pour tristesse). 

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
    
    
### 4. Résultats #

Pour cette tâche l'interet est de recueillir les TR à chaque essais, afin de comparer la moyenne des TR pour les essais congruents et les TR des essais incongruents. Cela nous permet d'obtenir le score d'interférence (i.e. TR des items incongruents - TR des items congruents). Ce score d'interférence permet de rendre compte des capacités d'inhibition d'un sujet. En effet on sait que plus le score d'interférence sera faible (i.e. la différence entre les TR incongruents et les TR congruents sera faible), plus les capcités d'inhibition seront élévées. 

Suite à l'obtention des résultats à la tâche du stroop chaud (celle de ce projet), il pourrait être intéressant de comparer ces résultats à ceux de la tâche du stroop froid. Par conséquence, voir si le contexte émotionnel a un impact sur nos capacités d'inhibition (i.e. comparer les scores d'interférences du stroop chaud à ceux du stroop froid)

### 5. Conclusion du projet # 

Avant de commencer ce cours je n'avais jamais programmé. J'avais qu'une très vague idée de ce que pouvait être "la programmation", mais je n'avais pour autant jamais codé, ni même ouvert le terminal de mon ordinateur. Ce cours a été pour moi la découverte d'un outils qui me semble indispensable dans le domaine que j'étudie (psychologie). J'ai appris beaucoup de choses durant ce cours, même si j'ai eu quelques difficultés à assimiler tous ces nouveaux concepts. Pour ce projet j'ai essayé d'utiliser différents outils que l'on avait pu voir en cours. 
Je pense que la tâche que j'ai programmé pourrait encore être perfectionnée.

Comme discuté lors du dernier cours, de part la disparité des niveaux, il pourrait être intéressant que chacun construise son projet tout au long du semestre, en ayant des cours de "soutien" si nécessaire. Cependant, je pense qu'il est important de commencer ce cours par un tour d'horizon des outils de bases indispendables à la programmation (du moins pour les novices comme moi !). 
    
  





