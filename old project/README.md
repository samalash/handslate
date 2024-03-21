# *HandSlate*  by deSigners

***deSigners team members***:

**Maanav Rao** - maarao
**Jasnoor Saini** - JasSaini101
**Andrew Crispino** - Drew-Crispino
**Mateo Torres** - MateoT659

  
  

## Inspiration

With the surgency of Artificial Intelligence in recent years, we felt it is our duty as computer scientists to harness this power for good use. One of those uses being providing accessibility to the less fortunate such as the Deaf community. We wanted to create a program that would allow better communication via video call between ASL speakers and people that do not speak the language.

  

## What it does

HandSlate seamlessly captures real-time footage from the user's webcam as they sign a letter in American Sign Language (ASL). It then swiftly translates the signed letter into English and elegantly displays it on the screen.

  

## How we built it

We developed HandSlate around a Flask framework, which efficiently transfers frames from the client-side video to the server-side backend. Once a frame is received, it undergoes processing through our Python functions that use OpenCV for computer vision. These functions leverage a neural network model trained on TensorFlow to  predict the signed letter within the frame to its corresponding representation in American Sign Language 

  

## Challenges we ran into
- Small dataset resulting to inaccurate predictions by the neural network
- Persistent errors stemming from communication breakdowns between our frontend and backend systems
- Passing stream for processing to the backend


  

## Accomplishments that we're proud of
- Orchestrating the development of a fully operational full-stack application.
- Custom generating a Neural Network to subvert having a small dataset
- Integrating the essential video call streaming functionality.

  
## What we learned

- Overseeing comprehensive full-stack development processes
- Conducting neural network training methodologies
- Managing file creation and deletion within the backend infrastructure
- Implementing real-time frontend updates seamlessly

  
  

## What's next for HandSlate?

- Incorporating a dynamic text-to-speech feature
- Scaling up model training using an expanded dataset, encompassing words for improved accuracy.
- Enabling Rolling Letter Recognition functionality, empowering clients to spell out words.
- And MORE!!!