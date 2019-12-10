Kung Fu Escape

Running: install pygame via pip then simply run
python3 main.py

Main Menu controls:
arrow keys to select entry, enter to start combat with selected difficulty

Combat controls:
a - punch
s - chop
d - headbutt
space bar - block
arrow keys - move targeting reticle
escape - exits game back to main menu

This is a wave based 2D combat game with a focus on timing and decision making.

To play, navigate over the enemy you want to attack and input an attack. After an animation completes the enemy will take damage.
When an enemy finishes their attack animation you will take damage. When your hp hits 0 you will die (but be able to navigate to the main menu by hitting escape)
Negate damage by blocking. Blocked damage is converted to stamina damage.
Stamina is an important resource which is regenerated over time. You need at least 1/10th of your stamina bar in order to take any action.

Attack types:
punch: average speed, average damage, stamina cost = 10. Bread and butter attack.
chop: high speed, low damage, stamina cost = 10. High burst damage but spamming it will leave you without stamina.
headbutt: low speed, average damage, stamina cost = 10, cancels the enemy's attack. Time it right to save some HP or stamina.

Parry/riposte:
If you block within half a second of an enemy's attack (timing window indicated by a flash of blue behind the player), while targeting the attacking enemy, you will have a second long window to riposte.
The riposte timing window is represented by a flash of red; input an attack within that time frame and double the speed of the inputted attack. Comboes well with the headbutt.
Parry/riposte are a strong defensive tool but using them too often could cause you to prematurely run out of stamina.

Waves:
You will start at wave 1 and progress as you clear out all enemies and reinforcements. Number of reinforcements = waves * 3. See how many you can take out before you succumb.

Difficulty: the only thing difficulty effects is how fast reinforcements arrive, higher difficulty = faster reinforcements for enemies
