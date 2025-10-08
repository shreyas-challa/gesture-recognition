This is a project build by shreyas challa

The goal is to use computer vision and machine learning to recognize hand gestures shown to a camera and use this correctly recogized output to perform automated tasks.

The model starts off with static detection, in a sense, each frame of the live input is passed into the recognition model using opencv, where model outputs the name of the gesture if recognized, none otherwise.

The next milestone is to turn this into dynamic detection, where we set rules to recognize the transition from one gesture to another. 
For example, going from open palm to a closed fist.
This action should map to a single task and perform it.


