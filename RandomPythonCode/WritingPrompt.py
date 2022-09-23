import random

WritingPrompts = [
    "Arakocra", "Aboleth", "Angels", "Animated Objects", "Ankheg", "Azer", 
    "Banshee", "Basilisk", "Behir", "Beholders", "Blights", "Bugbears", "Bulette", "Bullywug",
    "Cambion", "Carrion Crawler", "Centaur", "Chimera", "Chuul", "Cloaker", "Cockatrice", "Couatl", "Crawling Claw", "Cyclops",
    "Darkmantle", "Death Knight", "Demilich", "Demons", "Devils", "Dinosaurs", "Displacer Beast", "Doppelganger", "Dracolich", "Dragon, Shadow", "Dragons", "Dragon Turtle", "Drider", "Dryad", 'Duergar',
    'Elementals', 'Elves: Drow', 'Empyrean', 'Ettercap', 'Ettin', 
    'Faerie Dragon', 'Flameskull', 'Flumph', 'Fomorian', 'Fungi', 
    'Galeb Duhr', 'Gargoyle', 'Genies', 'Ghosts', 'Ghouls', 'Giants', 'Gibbering Mouther', 'Gith', 'Gnolls', 'Gnome, Deep(Svirfneblin)', 'Goblins', 'Golems', 'Gorgon', 'Grell', 'Griffon', 'Grimlock',
    'Hags', 'Half-Dragon', 'Harpy', 'Hell Hound', 'Helmed Horror', 'Hippogriff', 'Hobgoblins', 'Homunculus', 'Hook Horror', 'Hydra',
    'Intellect Devourer', 'Invisible Stalker',
    "Jackalwere",
    'Kenku', 'Kobolds', 'Kraken', 'Kuo-toa', 'Lamia', 'Lich', 'Lizardfolk', 'Lycanthropes',
    'Magmin', 'Manticore', 'Medusa', 'Mephits', 'Merfolk', 'Merrow', 'Mimic', 'Mind Flayer', 'Minotaur', 'Modrons', 'Mummies', 'Myconids',
    'Nagas', 'Nightmare', 'Nothic',
    'Ogres', 'Oni', 'Oozes', 'Orcs', 'Otyugh', 'Owlbear',
    'Pegasus', 'Peryton', 'Piercer', 'Pixie', 'Pseudodragon', 'Purple Worm',
    'Quaggoth',
    'Rakshasa', 'Remorhazes', 'Revenant', 'Roc', 'Roper', 'Rust Monster',
    'Sahuagin', 'Salamanders', 'Satry', 'Scarecrow', 'Shadow', 'Shambling Mound', 'Shield Guardian', 'Skeletons', 'Sladdi', 'Specter', 'Sphinxes', 'Sprite', 'Stirge', 'Succubus/Incubus',
    'Tarrasque', 'Thri-kreen', 'Treant', 'Troglodyte', 'Troll', 
    'Umber Hulk', 'Unicorn',
    'Vampires',
    'Water Weird', 'Wight', 'Will-o-wisp', 'Wraith', 'Wyvern',
    'Xorn',
    'Yetis', 'Yuan-ti', 'Yugoloths',
    'Zombies'
]

x = len(WritingPrompts)
x = str(x)

b = random.randrange(0, 152)
#print("Writing prompts left to complete: " + x)

c = WritingPrompts[b]

Creature = c

Creature = str(Creature)
print("Your creature is: " + Creature + ".")
