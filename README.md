# PPE-detection-using-Deep-Learning
PPE detection using Deep Learning models optimized to run on Nvidia Jetson platforms

With technological developments in machinery and equipment, businesses
must monitor worker compliance with safety rules, such as
wearing hardhats and high visibility vests. Existing surveillance cameras
at such plants give some compliance, but regular human monitoring
is needed to detect whether a worker is wearing personal protective
equipment (PPE), such as a helmet or vest. Due to the manual nature
of the procedure, it can be hard to detect and predict dangerous
events. This research proposes three deep learning (DL) algorithms to
verify PPE compliance of workers in real-time from image/video. We
try three different approaches and compare the results. First, the DL
model detects a person, hardhat, and vest in a joint object regression.
In the second approach, DL recognises hardhat and vest-wearing personnel,
where the presence of PPE is an attribute of a single object
detector. In the third method, the primary detector model detects
just a person, then the cropped image is used by the secondary detector
model to identify if the person is wearing a hardhat and/or vest
as a second stage object detection. All three models are optimised
for efficient operation on embedded platforms such as Nvidia Jetson
Xavier NX due to the real time requirements of the project. This
paper also discusses real-world challenges such as the availability of
high-quality data-sets and the effort of labelling image samples. Furthermore,
the available data-sets are typically imbalanced and biased,
necessitating a great deal of effort and time to resolve these problems.
This research proposes a PPE detection framework that evaluates the
efficacy of each of the three DL models, considers the limitations of
practical applications, and ultimately settles on the optimal approach.
