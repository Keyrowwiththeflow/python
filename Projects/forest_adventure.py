choice = input("""You are walking alone in the woods on a narrow pathway. It's a warm summer evening and the sun is just going down. Tall trees cast dark shadows on the path that get darker with the setting sun.

You come up to a fork in the path that has three choices. The right path leads downhill and the path gets darker with more bushes on each side. The center path has some sort of rustling sound you can hear faintly. The left path has the outline of some sort of building that you can see through the trees. Which path do you take?""")
if choice == "left":
    print("""You walk to the building. On the way there,you get the feeling that someone is watching you. 

As you enter the building, you hear a heavy footstep behind you. That's the last sound you hear before a hand covers your mouth and a knife meets your throat.""")
elif choice == "center":
    print("""You decide that you will continue going straight despite the faint rustling sound.

As you walk down the path, you hear the sound get louder before it completely stops, leaving an eerie silence in its wake. You initially think nothing of it and keep walking.

After a few minutes of complete silence, save for your own footsteps, you see a deer lying in the middle of the path. It's dead and blood is pooling around it, signaling that it was killed recently.

Suddenly, you hear the rustling sound again, but this time, it isn't faint. It sounds like it's coming from your left, but it also sounds like it's coming from your right as well as behind you. You freeze. 

You hear a growl coming from the nearby bushes, but you can't see much due to the darkness. You look to the right and see a pair of eyes staring at you. You look to your left and see the same thing. You don't look behind you because you can't—one of the creatures, a wolf perhaps, has jumped out at you and has grabbed your arm. The other has grabbed your ankle. The one behind you bites your neck.

You die and end up just like that deer you saw—a lifeless corpse in the middle of the road as blood pools around it.""")
elif choice == "right":
    print("""You take the the right path. Nothing seems to be odd about it except for the bushes and the darkness. The bushes seem to be making the path smaller and smaller with each step.

Eventually, after a few minutes of walking, you realize that the bushes have completely covered the trail—and you're standing in the middle of them. Scratches cover your body. You look behind you. You have made it far into this path. The shortest way out is to continue going forward.

You continue pushing through the bushes, ignoring the pain of the thorns, and you almost make it out, but life has never been kind to you.

There was a hidden root on the ground and you, true to your unlucky nature, tripped on it. Now, your face is covered in scratches. You have closed your eyes to avoid your eyes getting impaled by thorns. You struggle to get up, but after a few minutes of immense effort, you manage to stand up just enough to walk out of the bushes. 

You survived, but the consequences of surviving have left you with many, many injuries that will probably get infected if you don't reach the village soon.""")
else:
    print("Invalid answer. Please choose a valid answer (left, center, right).")