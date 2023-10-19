<?xml version="1.0"?>
<!--
   14x28 fullbody detector (see the detailed description below). 

//////////////////////////////////////////////////////////////////////////
| Contributors License Agreement
| IMPORTANT: READ BEFORE DOWNLOADING, COPYING, INSTALLING OR USING.
|   By downloading, copying, installing or using the software you agree 
|   to this license.
|   If you do not agree to this license, do not download, install,
|   copy or use the software.
|
| Copyright (c) 2004, Hannes Kruppa and Bernt Schiele (ETH Zurich, Switzerland).
|  All rights reserved.
|
| Redistribution and use in source and binary forms, with or without
| modification, are permitted provided that the following conditions are
| met:
|
|    * Redistributions of source code must retain the above copyright
|       notice, this list of conditions and the following disclaimer.
|    * Redistributions in binary form must reproduce the above
|      copyright notice, this list of conditions and the following
|      disclaimer in the documentation and/or other materials provided
|      with the distribution.  
|    * The name of Contributor may not used to endorse or promote products 
|      derived from this software without specific prior written permission.
|
| THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
| "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
| LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
| A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
| CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
| EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
| PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
| PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
| LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
| NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
| SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.  Back to
| Top
//////////////////////////////////////////////////////////////////////////

"Haar"-based Detectors For Pedestrian Detection
===============================================
by Hannes Kruppa and Bernt Schiele, ETH Zurich, Switzerland

This archive provides the following three detectors:
- upper body detector (most fun, useful in many scenarios!)
- lower body detector
- full body detector

These detectors have been successfully applied to pedestrian detection
in still images. They can be directly passed as parameters to the
program HaarFaceDetect.
NOTE: These detectors deal with frontal and backside views but not
with side views (also see "Known limitations" below).

RESEARCHERS:
If you are using any of the detectors or involved ideas please cite
this paper (available at www.vision.ethz.ch/publications/):

@InProceedings{Kruppa03-bmvc,
  author =       "Hannes Kruppa, Modesto Castrillon-Santana and Bernt Schiele",
  title =        "Fast and Robust Face Finding via Local Context."
  booktitle =    "Joint IEEE International Workshop on Visual Surveillance and Performance Evaluation of Tracking and Surveillance"
  year =         "2003",
  month =        "October"
}

COMMERCIAL:
If you have any commercial interest in this work please contact 
hkruppa@inf.ethz.ch


ADDITIONAL INFORMATION 
====================== 
Check out the demo movie, e.g. using mplayer or any (Windows/Linux-) player
that can play back .mpg movies.
Under Linux that's:
> ffplay demo.mpg
or:
> mplayer demo.mpg

The movie shows a person walking towards the camera in a realistic
indoor setting. Using ffplay or mplayer you can pause and continue the
movie by pressing the space bar.

Detections coming from the different detectors are visualized using
different line styles: 
upper body : dotted line
lower body : dashed line
full body  : solid line

You will notice that successful detections containing the target do
not sit tightly on the body but also include some of the background
left and right.  This is not a bug but accurately reflects the
employed training data which also includes portions of the background
to ensure proper silhouette representation. If you want to get a
feeling for the training data check out the CBCL data set:
http://www.ai.mit.edu/projects/cbcl/software-datasets/PedestrianData.html

There is also a small number of false alarms in this sequence.  
NOTE: This is per frame detection, not tracking (which is also one of
the reasons why it is not mislead by the person's shadow on the back
wall). 

On an Intel Xeon 1.7GHz machine the detectors operate at something
between 6Hz to 14 Hz (on 352 x 288 frames per second) depending on the
detector. The detectors work as well on much lower image resolutions
which is always an interesting possibility for speed-ups or
"coarse-to-fine" search strategies.

Additional information e.g. on training parameters, detector
combination, detecting other types of objects (e.g. cars) etc. is
available in my PhD thesis report (available end of June). Check out
www.vision.ethz.ch/kruppa/


KNOWN LIMITATIONS
==================
1) the detectors only support frontal and back views but not sideviews.
   Sideviews are trickier and it makes a lot of sense to include additional
   modalities for their detection, e.g. motion information. I recommend
   Viola and Jones' ICCV 2003 paper if this further interests you.

2) dont expect these detectors to be as accurate as a frontal face detector.
   A frontal face as a pattern is pretty distinct with respect to other
   patterns occuring in the world (i.e. image "background"). This is not so
   for upper, lower and especially full bodies, because they have to rely
   on fragile silhouette information rather than internal (facial) features.
   Still, we found especially the upper body detector to perform amazingly well.
   In contrast to a face detector these detectors will also work at very low
   image resolutions 

Acknowledgements
================
Thanks to Martin Spengler, ETH Zurich, for providing the demo movie.
-->
<opencv_storage>
<cascade type_id="opencv-cascade-classifier"><stageType>BOOST</stageType>
  <featureType>HAAR</featureType>
  <height>28</height>
  <width>14</width>
  <stageParams>
    <maxWeakCount>107</maxWeakCount></stageParams>
  <featureParams>
    <maxCatCount>0</maxCatCount></featureParams>
  <stageNum>30</stageNum>
  <stages>
    <_>
      <maxWeakCount>9</maxWeakCount>
      <stageThreshold>-1.2288980484008789e+00</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 0 -5.5820569396018982e-02</internalNodes>
          <leafValues>
            5.8697921037673950e-01 -6.2811422348022461e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1 -3.8861181586980820e-02</internalNodes>
          <leafValues>
            -7.0916819572448730e-01 2.6821210980415344e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 2 -2.6740878820419312e-01</internalNodes>
          <leafValues>
            8.3082962036132812e-01 -2.2599589824676514e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 3 9.6419736742973328e-02</internalNodes>
          <leafValues>
            -1.1697849631309509e-01 8.7254559993743896e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 4 -1.0798710398375988e-02</internalNodes>
          <leafValues>
            -5.7219749689102173e-01 2.5325658917427063e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 5 1.1365639977157116e-02</internalNodes>
          <leafValues>
            1.9650830328464508e-01 -7.2744637727737427e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 6 -5.0216919044032693e-04</internalNodes>
          <leafValues>
            2.4435159564018250e-01 -5.1973581314086914e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 7 -2.8462480753660202e-02</internalNodes>
          <leafValues>
            -8.3607292175292969e-01 1.1158040165901184e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 8 1.3473170110955834e-03</internalNodes>
          <leafValues>
            -3.8406538963317871e-01 2.6767989993095398e-01</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>15</maxWeakCount>
      <stageThreshold>-1.0969949960708618e+00</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 9 -1.0743220336735249e-02</internalNodes>
          <leafValues>
            4.7747328877449036e-01 -6.2392932176589966e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 10 -1.3188569573685527e-03</internalNodes>
          <leafValues>
            2.1242660284042358e-01 -2.4162709712982178e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 11 -5.5571161210536957e-03</internalNodes>
          <leafValues>
            3.6147859692573547e-01 -3.7251719832420349e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 12 -1.3893410563468933e-01</internalNodes>
          <leafValues>
            -6.7900502681732178e-01 1.1280310153961182e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 13 2.6465829461812973e-02</internalNodes>
          <leafValues>
            1.2474969774484634e-01 -8.2852339744567871e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 14 -8.9386843144893646e-02</internalNodes>
          <leafValues>
            7.4271762371063232e-01 -1.7019319534301758e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 15 -2.1335419267416000e-02</internalNodes>
          <leafValues>
            -7.1750187873840332e-01 1.5566180646419525e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 16 5.5709101259708405e-02</internalNodes>
          <leafValues>
            -1.5310040116310120e-01 7.1804767847061157e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 17 -6.9709950685501099e-01</internalNodes>
          <leafValues>
            8.1154191493988037e-01 -1.0886389762163162e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 18 2.0205999910831451e-01</internalNodes>
          <leafValues>
            7.6398417353630066e-02 -7.3011511564254761e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 19 -7.1882657706737518e-02</internalNodes>
          <leafValues>
            -7.1488589048385620e-01 1.6517649590969086e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 20 -1.9228760153055191e-02</internalNodes>
          <leafValues>
            -3.9868369698524475e-01 4.0557239204645157e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 21 1.1500229593366385e-03</internalNodes>
          <leafValues>
            -3.8260778784751892e-01 3.1855079531669617e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 22 2.3252779617905617e-02</internalNodes>
          <leafValues>
            5.4390400648117065e-02 -7.0669990777969360e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 23 -3.2618120894767344e-04</internalNodes>
          <leafValues>
            2.2610600292682648e-01 -4.0709879994392395e-01</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>14</maxWeakCount>
      <stageThreshold>-1.2285970449447632e+00</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 24 -1.2910200655460358e-01</internalNodes>
          <leafValues>
            7.6003128290176392e-01 -2.3405790328979492e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 25 6.7449256777763367e-02</internalNodes>
          <leafValues>
            1.7179529368877411e-01 -8.4364777803421021e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 26 1.2663270346820354e-02</internalNodes>
          <leafValues>
            2.2913210093975067e-01 -7.3072457313537598e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 27 -4.2741331271827221e-03</internalNodes>
          <leafValues>
            6.2420479953289032e-02 -4.0985938906669617e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 28 -2.3143950849771500e-02</internalNodes>
          <leafValues>
            -8.3971828222274780e-01 2.0115749537944794e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 29 -5.5371038615703583e-04</internalNodes>
          <leafValues>
            1.5369419753551483e-01 -4.4038110971450806e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 30 -9.5239803194999695e-03</internalNodes>
          <leafValues>
            -6.3186800479888916e-01 1.6250230371952057e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 31 2.8307670727372169e-02</internalNodes>
          <leafValues>
            -7.2599969804286957e-02 3.7919989228248596e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 32 -4.5148018747568130e-02</internalNodes>
          <leafValues>
            7.4493628740310669e-01 -1.5581710636615753e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 33 1.0014739632606506e-01</internalNodes>
          <leafValues>
            1.7949639260768890e-01 -6.4644080400466919e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 34 7.3245721869170666e-03</internalNodes>
          <leafValues>
            1.7763899266719818e-01 -5.7654058933258057e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 35 1.1875670403242111e-02</internalNodes>
          <leafValues>
            -3.1129720807075500e-01 1.6321399807929993e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 36 -2.5479039177298546e-02</internalNodes>
          <leafValues>
            6.2692481279373169e-01 -1.1333750188350677e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 37 -7.9196523874998093e-03</internalNodes>
          <leafValues>
            -7.7624428272247314e-01 1.5427610278129578e-01</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>22</maxWeakCount>
      <stageThreshold>-1.1200269460678101e+00</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 38 -8.5809278488159180e-01</internalNodes>
          <leafValues>
            7.8796839714050293e-01 -2.2135549783706665e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 39 -1.6491119749844074e-03</internalNodes>
          <leafValues>
            2.5673401355743408e-01 -4.3194240331649780e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 40 -2.5882309302687645e-02</internalNodes>
          <leafValues>
            -8.7551230192184448e-01 8.8385626673698425e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 41 -4.7666151076555252e-03</internalNodes>
          <leafValues>
            -4.7022369503974915e-01 2.2800800204277039e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 42 -8.3729699254035950e-02</internalNodes>
          <leafValues>
            6.3385730981826782e-01 -1.4888319373130798e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 43 -4.0685739368200302e-02</internalNodes>
          <leafValues>
            -9.3931788206100464e-01 1.0598939843475819e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 44 -5.0759920850396156e-03</internalNodes>
          <leafValues>
            -4.5554420351982117e-01 1.7864370346069336e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 45 2.3427829146385193e-03</internalNodes>
          <leafValues>
            -2.1434280276298523e-01 1.5531420707702637e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 46 2.7649151161313057e-04</internalNodes>
          <leafValues>
            -3.3348160982131958e-01 2.2780239582061768e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 47 1.6941839829087257e-02</internalNodes>
          <leafValues>
            7.4140816926956177e-02 -5.6262052059173584e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 48 4.7558981180191040e-01</internalNodes>
          <leafValues>
            -1.0861130058765411e-01 8.2985258102416992e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 49 5.8000627905130386e-03</internalNodes>
          <leafValues>
            1.3249030709266663e-01 -5.1620399951934814e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 50 -7.4477560818195343e-02</internalNodes>
          <leafValues>
            -5.5545568466186523e-01 1.2344320118427277e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 51 -3.5143009154126048e-04</internalNodes>
          <leafValues>
            6.8190753459930420e-02 -1.3616859912872314e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 52 7.3454021476209164e-03</internalNodes>
          <leafValues>
            1.3678510487079620e-01 -5.3645122051239014e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 53 -1.5471279621124268e-02</internalNodes>
          <leafValues>
            2.6180639863014221e-01 -1.0545810312032700e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 54 5.6055500172078609e-03</internalNodes>
          <leafValues>
            -2.5746351480484009e-01 2.8795930743217468e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 55 -2.4552858667448163e-04</internalNodes>
          <leafValues>
            1.0099930316209793e-01 -2.6119679212570190e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 56 -3.3138900995254517e-02</internalNodes>
          <leafValues>
            -8.3779567480087280e-01 1.1327689886093140e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 57 3.5591889172792435e-02</internalNodes>
          <leafValues>
            8.2336090505123138e-02 -6.2505662441253662e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 58 2.0834030210971832e-01</internalNodes>
          <leafValues>
            6.9524437189102173e-02 -8.6881148815155029e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 59 -2.8165400028228760e-02</internalNodes>
          <leafValues>
            -5.9799849987030029e-01 8.0329902470111847e-02</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>25</maxWeakCount>
      <stageThreshold>-1.0664960145950317e+00</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 60 -2.6740709319710732e-02</internalNodes>
          <leafValues>
            3.8912421464920044e-01 -4.9827679991722107e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 61 -1.2516999850049615e-03</internalNodes>
          <leafValues>
            1.3123430311679840e-01 -3.6368998885154724e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 62 -4.1634511202573776e-02</internalNodes>
          <leafValues>
            5.7444751262664795e-01 -1.3932879269123077e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 63 1.0096579790115356e-02</internalNodes>
          <leafValues>
            9.9073797464370728e-02 -2.2956989705562592e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 64 -1.9090399146080017e-02</internalNodes>
          <leafValues>
            -5.5153107643127441e-01 1.5110069513320923e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 65 -3.1481068581342697e-02</internalNodes>
          <leafValues>
            -4.5884269475936890e-01 1.7579549551010132e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 66 -1.7687549814581871e-02</internalNodes>
          <leafValues>
            4.4711831212043762e-01 -1.5292930603027344e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 67 -4.3685659766197205e-03</internalNodes>
          <leafValues>
            1.2185490131378174e-01 -1.6688570380210876e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 68 8.9326845481991768e-03</internalNodes>
          <leafValues>
            -1.3333690166473389e-01 6.3753342628479004e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 69 -5.0706309266388416e-03</internalNodes>
          <leafValues>
            -1.1220289766788483e-01 6.9824352860450745e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 70 -5.9803090989589691e-03</internalNodes>
          <leafValues>
            -5.1842898130416870e-01 1.6099199652671814e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 71 2.9967839363962412e-03</internalNodes>
          <leafValues>
            4.1065338999032974e-02 -1.9455850124359131e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 72 3.8641549181193113e-03</internalNodes>
          <leafValues>
            1.6673240065574646e-01 -4.3569779396057129e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 73 6.8349428474903107e-03</internalNodes>
          <leafValues>
            -1.7162640392780304e-01 1.4818060398101807e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 74 4.3158490210771561e-02</internalNodes>
          <leafValues>
            8.3203509449958801e-02 -7.7821850776672363e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 75 7.6560080051422119e-03</internalNodes>
          <leafValues>
            8.4740802645683289e-02 -4.9738150835037231e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 76 -3.1110988929867744e-03</internalNodes>
          <leafValues>
            2.5827148556709290e-01 -2.5552031397819519e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 77 1.1870309710502625e-01</internalNodes>
          <leafValues>
            -9.0944238007068634e-02 7.2286212444305420e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 78 1.6875969246029854e-02</internalNodes>
          <leafValues>
            1.2629170715808868e-01 -5.5205297470092773e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 79 -1.0887029930017889e-04</internalNodes>
          <leafValues>
            8.1648796796798706e-02 -1.6937020421028137e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 80 2.8222990222275257e-03</internalNodes>
          <leafValues>
            1.6411300003528595e-01 -3.5218268632888794e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 81 -5.2425849437713623e-01</internalNodes>
          <leafValues>
            4.8906171321868896e-01 -1.2674759328365326e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 82 3.6927509307861328e-01</internalNodes>
          <leafValues>
            8.6115993559360504e-02 -6.7184638977050781e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 83 -1.6883780062198639e-01</internalNodes>
          <leafValues>
            -8.4915691614151001e-01 5.4833348840475082e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 84 -1.9279260188341141e-02</internalNodes>
          <leafValues>
            -7.8011512756347656e-01 6.2202680855989456e-02</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>22</maxWeakCount>
      <stageThreshold>-1.2319500446319580e+00</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 85 -2.0901350677013397e-01</internalNodes>
          <leafValues>
            6.9808167219161987e-01 -3.4573590755462646e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 86 -4.8061009147204459e-04</internalNodes>
          <leafValues>
            2.0923900604248047e-01 -2.4147640168666840e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 87 -2.4844119325280190e-03</internalNodes>
          <leafValues>
            2.7636009454727173e-01 -4.1990399360656738e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 88 -2.1536289714276791e-03</internalNodes>
          <leafValues>
            2.4710460007190704e-01 -3.0677899718284607e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 89 5.8911990374326706e-02</internalNodes>
          <leafValues>
            -7.0834763348102570e-02 7.1133142709732056e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 90 -2.3095219512470067e-04</internalNodes>
          <leafValues>
            1.7148600518703461e-01 -3.6168378591537476e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 91 -3.1396400183439255e-02</internalNodes>
          <leafValues>
            -8.0131882429122925e-01 1.0042560100555420e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 92 -3.5601970739662647e-03</internalNodes>
          <leafValues>
            9.9432766437530518e-02 -1.4848260581493378e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 93 -4.3389322236180305e-03</internalNodes>
          <leafValues>
            -5.6621241569519043e-01 1.4096799492835999e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 94 2.1326710283756256e-01</internalNodes>
          <leafValues>
            4.8158209770917892e-02 -7.4858909845352173e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 95 1.0042529553174973e-02</internalNodes>
          <leafValues>
            1.0428400337696075e-01 -5.5387377738952637e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 96 -2.6825280860066414e-02</internalNodes>
          <leafValues>
            5.7281607389450073e-01 -8.2537978887557983e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 97 8.3760882262140512e-04</internalNodes>
          <leafValues>
            -2.5626900792121887e-01 2.5898420810699463e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 98 -7.6051978394389153e-03</internalNodes>
          <leafValues>
            -5.8677357435226440e-01 5.1210779696702957e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 99 -1.1935640126466751e-01</internalNodes>
          <leafValues>
            -4.5530828833580017e-01 1.2570330500602722e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 100 6.6083478741347790e-03</internalNodes>
          <leafValues>
            -1.6316379606723785e-01 4.6659541130065918e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 101 1.7303509637713432e-02</internalNodes>
          <leafValues>
            -1.2391400337219238e-01 5.9755408763885498e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 102 5.4382272064685822e-03</internalNodes>
          <leafValues>
            1.3838729262351990e-01 -5.5069202184677124e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 103 2.4591449182480574e-03</internalNodes>
          <leafValues>
            -3.9927339553833008e-01 1.5387089550495148e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 104 3.5056238994002342e-03</internalNodes>
          <leafValues>
            -1.6146700084209442e-01 1.6086600720882416e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 105 -2.3172689543571323e-04</internalNodes>
          <leafValues>
            1.7059360444545746e-01 -3.5409420728683472e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 106 1.1914529837667942e-02</internalNodes>
          <leafValues>
            1.6265639662742615e-01 -4.1463181376457214e-01</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>18</maxWeakCount>
      <stageThreshold>-1.1912549734115601e+00</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 107 -4.5429700985550880e-03</internalNodes>
          <leafValues>
            4.2964971065521240e-01 -5.6915849447250366e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 108 4.6804840676486492e-03</internalNodes>
          <leafValues>
            -1.0380080342292786e-01 2.5453719496726990e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 109 3.5870380233973265e-03</internalNodes>
          <leafValues>
            -3.6577078700065613e-01 3.9343339204788208e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 110 -3.4428331255912781e-01</internalNodes>
          <leafValues>
            7.3125761747360229e-01 -1.5060240030288696e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 111 3.3054459840059280e-02</internalNodes>
          <leafValues>
            1.7657589912414551e-01 -5.1060509681701660e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 112 -2.1190310362726450e-03</internalNodes>
          <leafValues>
            8.6859323084354401e-02 -1.7733760178089142e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 113 1.3780740089714527e-02</internalNodes>
          <leafValues>
            -1.2247169762849808e-01 6.6472941637039185e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 114 2.4847950786352158e-02</internalNodes>
          <leafValues>
            2.3976799845695496e-01 -3.2456618547439575e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 115 -1.3126630336046219e-02</internalNodes>
          <leafValues>
            4.9461808800697327e-01 -2.0954379439353943e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 116 -1.6886189579963684e-02</internalNodes>
          <leafValues>
            -1.3973990082740784e-01 7.5013160705566406e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 117 -5.2776751108467579e-03</internalNodes>
          <leafValues>
            -3.8919359445571899e-01 1.8921519815921783e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 118 -2.0325549412518740e-03</internalNodes>
          <leafValues>
            2.4965450167655945e-01 -1.7960360646247864e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 119 -1.8056800588965416e-02</internalNodes>
          <leafValues>
            -5.3683072328567505e-01 1.0615479946136475e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 120 -2.8815109282732010e-02</internalNodes>
          <leafValues>
            5.3303200006484985e-01 -7.8712686896324158e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 121 -6.0971658676862717e-02</internalNodes>
          <leafValues>
            -8.5663092136383057e-01 8.1721447408199310e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 122 -6.2022160738706589e-02</internalNodes>
          <leafValues>
            -6.7228960990905762e-01 8.2316987216472626e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 123 -6.2961759977042675e-03</internalNodes>
          <leafValues>
            2.7192309498786926e-01 -2.3713490366935730e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 124 4.9608140252530575e-03</internalNodes>
          <leafValues>
            -1.4295519888401031e-01 2.9380369186401367e-01</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>30</maxWeakCount>
      <stageThreshold>-1.1750839948654175e+00</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 125 -8.7001353502273560e-02</internalNodes>
          <leafValues>
            6.3087427616119385e-01 -2.6264131069183350e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 126 -4.5627020299434662e-03</internalNodes>
          <leafValues>
            1.4641839265823364e-01 -5.2321881055831909e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 127 -4.1381991468369961e-03</internalNodes>
          <leafValues>
            2.1747599542140961e-01 -3.2107940316200256e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 128 -1.9443330529611558e-04</internalNodes>
          <leafValues>
            1.4305000007152557e-01 -4.4748461246490479e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 129 -2.6125069707632065e-03</internalNodes>
          <leafValues>
            -3.5936230421066284e-01 2.0934499800205231e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 130 -3.5238351672887802e-02</internalNodes>
          <leafValues>
            -5.5879557132720947e-01 1.1818339675664902e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 131 2.3880550637841225e-02</internalNodes>
          <leafValues>
            -1.2345419824123383e-01 6.4505738019943237e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 132 -3.5878319758921862e-03</internalNodes>
          <leafValues>
            2.3340910673141479e-01 -2.9905730485916138e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 133 -3.4388148784637451e-01</internalNodes>
          <leafValues>
            6.3334107398986816e-01 -8.6101479828357697e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 134 -2.5634190533310175e-03</internalNodes>
          <leafValues>
            -3.0992001295089722e-01 8.8213436305522919e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 135 4.7002349048852921e-02</internalNodes>
          <leafValues>
            7.3533393442630768e-02 -7.5965261459350586e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 136 7.1428148075938225e-03</internalNodes>
          <leafValues>
            -1.6981430351734161e-01 4.1982281208038330e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 137 -3.7736629601567984e-03</internalNodes>
          <leafValues>
            -5.5664837360382080e-01 1.0060050338506699e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 138 2.2179849445819855e-02</internalNodes>
          <leafValues>
            -7.6009899377822876e-02 6.3711041212081909e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 139 2.9807379178237170e-05</internalNodes>
          <leafValues>
            -2.7143061161041260e-01 2.1503789722919464e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 140 -1.4308329809864517e-05</internalNodes>
          <leafValues>
            1.3090610504150391e-01 -2.8089499473571777e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 141 -1.1500260233879089e-01</internalNodes>
          <leafValues>
            -7.1986222267150879e-01 7.6884172856807709e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 142 -2.5318590924143791e-02</internalNodes>
          <leafValues>
            4.5250499248504639e-01 -9.0481691062450409e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 143 -4.8698320984840393e-02</internalNodes>
          <leafValues>
            -7.4177128076553345e-01 6.7692406475543976e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 144 -5.0045289099216461e-03</internalNodes>
          <leafValues>
            1.3680170476436615e-01 -1.1860919743776321e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 145 7.5120502151548862e-03</internalNodes>
          <leafValues>
            9.1260991990566254e-02 -5.6960678100585938e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 146 -5.4631778039038181e-03</internalNodes>
          <leafValues>
            1.1702360212802887e-01 -1.4761230349540710e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 147 1.5256009995937347e-02</internalNodes>
          <leafValues>
            -1.0768359899520874e-01 6.4716261625289917e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 148 -2.1900620311498642e-02</internalNodes>
          <leafValues>
            -6.0776418447494507e-01 6.4449213445186615e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 149 2.1267218980938196e-03</internalNodes>
          <leafValues>
            -2.3115469515323639e-01 2.1813300251960754e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 150 -3.1501919031143188e-02</internalNodes>
          <leafValues>
            -1.3678109645843506e-01 6.6003270447254181e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 151 1.8107969313859940e-02</internalNodes>
          <leafValues>
            1.0865720361471176e-01 -4.4673460721969604e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 152 -1.1059570312500000e-01</internalNodes>
          <leafValues>
            4.6954178810119629e-01 -1.1268380284309387e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 153 2.2349569480866194e-03</internalNodes>
          <leafValues>
            -2.9884970188140869e-01 1.8147529661655426e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 154 4.6504188328981400e-02</internalNodes>
          <leafValues>
            1.2846769392490387e-01 -2.6609849929809570e-01</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>27</maxWeakCount>
      <stageThreshold>-1.1861419677734375e+00</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 155 -4.8820599913597107e-02</internalNodes>
          <leafValues>
            4.2807990312576294e-01 -5.5154949426651001e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 156 1.4779040357097983e-03</internalNodes>
          <leafValues>
            -1.8688060343265533e-01 1.9038289785385132e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 157 -1.0012290440499783e-02</internalNodes>
          <leafValues>
            3.8451421260833740e-01 -2.1723049879074097e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 158 -5.1000278443098068e-02</internalNodes>
          <leafValues>
            -7.6136952638626099e-01 1.3625900261104107e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 159 5.2959132008254528e-03</internalNodes>
          <leafValues>
            -2.3021429777145386e-01 2.8536239266395569e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 160 -4.8654139041900635e-02</internalNodes>
          <leafValues>
            7.0992070436477661e-01 -4.9203149974346161e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 161 8.8448636233806610e-03</internalNodes>
          <leafValues>
            -3.1505361199378967e-01 2.0899020135402679e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 162 1.0062800347805023e-01</internalNodes>
          <leafValues>
            6.6908989101648331e-03 6.7013871669769287e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 163 -7.0256260223686695e-03</internalNodes>
          <leafValues>
            -3.9408329129219055e-01 1.7433549463748932e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 164 -2.1224319934844971e-03</internalNodes>
          <leafValues>
            1.6996310651302338e-01 -3.0237409472465515e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 165 9.9532064050436020e-03</internalNodes>
          <leafValues>
            -1.4202840626239777e-01 4.5167461037635803e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 166 1.2565069831907749e-02</internalNodes>
          <leafValues>
            7.3175877332687378e-02 -6.1700421571731567e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 167 -1.7854310572147369e-03</internalNodes>
          <leafValues>
            1.4909860491752625e-01 -3.2865241169929504e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 168 -4.0306518785655499e-03</internalNodes>
          <leafValues>
            -4.5713710784912109e-01 1.0815720260143280e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 169 -7.3099560104310513e-03</internalNodes>
          <leafValues>
            -6.5592771768569946e-01 6.5615788102149963e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 170 -3.3843431621789932e-02</internalNodes>
          <leafValues>
            5.0412368774414062e-01 -6.1626069247722626e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 171 3.8319290615618229e-04</internalNodes>
          <leafValues>
            -2.5153478980064392e-01 2.0271340012550354e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 172 -2.6169361080974340e-03</internalNodes>
          <leafValues>
            2.2497959434986115e-01 -2.1958619356155396e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 173 -4.5606079511344433e-03</internalNodes>
          <leafValues>
            -4.6598041057586670e-01 1.2348009645938873e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 174 1.0822789743542671e-02</internalNodes>
          <leafValues>
            -9.6618972718715668e-02 4.6412429213523865e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 175 -5.3171347826719284e-03</internalNodes>
          <leafValues>
            -5.5634248256683350e-01 9.4623282551765442e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 176 -9.3140971148386598e-04</internalNodes>
          <leafValues>
            1.0143929719924927e-01 -1.0564240068197250e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 177 8.4296840941533446e-04</internalNodes>
          <leafValues>
            -1.3243100047111511e-01 3.5351079702377319e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 178 -2.7806960046291351e-02</internalNodes>
          <leafValues>
            -6.5050601959228516e-01 3.3153589814901352e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 179 6.9245469057932496e-04</internalNodes>
          <leafValues>
            -2.6702880859375000e-01 2.1129630506038666e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 180 -1.2787230312824249e-02</internalNodes>
          <leafValues>
            2.1593640744686127e-01 -8.6767077445983887e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 181 -6.1678601196035743e-04</internalNodes>
          <leafValues>
            1.6959980130195618e-01 -2.9248940944671631e-01</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>21</maxWeakCount>
      <stageThreshold>-1.0550270080566406e+00</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 182 -5.1706928759813309e-02</internalNodes>
          <leafValues>
            4.6942698955535889e-01 -5.1280671358108521e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 183 5.5232150480151176e-03</internalNodes>
          <leafValues>
            -2.4982389807701111e-01 6.3005810976028442e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 184 -9.2110745608806610e-03</internalNodes>
          <leafValues>
            3.7530669569969177e-01 -2.2910380363464355e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 185 4.1729960590600967e-02</internalNodes>
          <leafValues>
            -1.1262010037899017e-01 6.7508697509765625e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 186 4.5255841687321663e-03</internalNodes>
          <leafValues>
            -2.6939728856086731e-01 2.4889509379863739e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 187 -8.5208792006596923e-04</internalNodes>
          <leafValues>
            2.0098550617694855e-01 -2.3001730442047119e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 188 -3.4569639246910810e-03</internalNodes>
          <leafValues>
            -3.6372348666191101e-01 2.7142500877380371e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 189 -8.8200360536575317e-02</internalNodes>
          <leafValues>
            -7.5951957702636719e-01 -7.2166309691965580e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 190 -2.3253160179592669e-04</internalNodes>
          <leafValues>
            1.4738219976425171e-01 -4.2548701167106628e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 191 1.9258400425314903e-02</internalNodes>
          <leafValues>
            -8.4830872714519501e-02 5.9487771987915039e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 192 -3.1915740109980106e-03</internalNodes>
          <leafValues>
            -4.2638280987739563e-01 1.3357159495353699e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 193 -2.2229040041565895e-02</internalNodes>
          <leafValues>
            -4.2298269271850586e-01 3.6127958446741104e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 194 -5.3123440593481064e-03</internalNodes>
          <leafValues>
            2.9349780082702637e-01 -2.2197869420051575e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 195 5.6796981953084469e-03</internalNodes>
          <leafValues>
            8.0412790179252625e-02 -1.9725289940834045e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 196 3.2511178869754076e-03</internalNodes>
          <leafValues>
            -1.6628390550613403e-01 3.3107280731201172e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 197 2.5559039786458015e-03</internalNodes>
          <leafValues>
            6.7350171506404877e-02 -2.4642370641231537e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 198 3.1239999458193779e-02</internalNodes>
          <leafValues>
            -6.7393511533737183e-02 8.2851767539978027e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 199 -4.4333371333777905e-03</internalNodes>
          <leafValues>
            -3.8048321008682251e-01 1.4248619973659515e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 200 -3.9497618563473225e-03</internalNodes>
          <leafValues>
            -3.5660448670387268e-01 1.8685440719127655e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 201 -1.4043290168046951e-02</internalNodes>
          <leafValues>
            5.3222888708114624e-01 -7.8980803489685059e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 202 4.2212791740894318e-03</internalNodes>
          <leafValues>
            -1.9841830432415009e-01 3.1367298960685730e-01</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>43</maxWeakCount>
      <stageThreshold>-1.1214250326156616e+00</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 203 -1.5278789401054382e-01</internalNodes>
          <leafValues>
            5.4140037298202515e-01 -1.8756979703903198e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 204 -7.0655636489391327e-02</internalNodes>
          <leafValues>
            3.4003350138664246e-01 -1.4459669589996338e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 205 -2.1033229306340218e-02</internalNodes>
          <leafValues>
            -5.5878472328186035e-01 1.1598149687051773e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 206 -9.5666358247399330e-03</internalNodes>
          <leafValues>
            1.0890080034732819e-01 -2.0365689694881439e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 207 -4.2720541357994080e-02</internalNodes>
          <leafValues>
            -9.4030022621154785e-01 6.3606321811676025e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 208 -4.5477859675884247e-03</internalNodes>
          <leafValues>
            3.4227019548416138e-01 -1.7053720355033875e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 209 3.7029080558568239e-03</internalNodes>
          <leafValues>
            8.3720892667770386e-02 -4.6139541268348694e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 210 -1.1458870023488998e-01</internalNodes>
          <leafValues>
            6.0027849674224854e-01 -1.7764480784535408e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 211 5.7319342158734798e-03</internalNodes>
          <leafValues>
            -2.5590109825134277e-01 2.0062319934368134e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 212 -7.0237793028354645e-02</internalNodes>
          <leafValues>
            2.5359788537025452e-01 -2.9503619298338890e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 213 1.3983179815113544e-02</internalNodes>
          <leafValues>
            1.1456400156021118e-01 -3.9683538675308228e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 214 1.8175759911537170e-01</internalNodes>
          <leafValues>
            5.0749950110912323e-02 -8.3061927556991577e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 215 3.0185490846633911e-02</internalNodes>
          <leafValues>
            -2.6683610677719116e-01 1.4070799946784973e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 216 7.5633287429809570e-01</internalNodes>
          <leafValues>
            -4.1416618973016739e-02 9.0957278013229370e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 217 -8.5228988900780678e-03</internalNodes>
          <leafValues>
            1.6142499446868896e-01 -2.7549099922180176e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 218 -4.9996669404208660e-03</internalNodes>
          <leafValues>
            -1.1666730046272278e-01 6.0298819094896317e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 219 -5.9932802105322480e-04</internalNodes>
          <leafValues>
            1.3015550374984741e-01 -3.1072840094566345e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 220 -9.6063673496246338e-02</internalNodes>
          <leafValues>
            -8.5259348154067993e-01 1.5970790758728981e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 221 -7.0154820568859577e-03</internalNodes>
          <leafValues>
            -4.5490509271621704e-01 7.7178090810775757e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 222 -8.7620541453361511e-03</internalNodes>
          <leafValues>
            4.8034501075744629e-01 -8.1306837499141693e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 223 -3.9868508465588093e-03</internalNodes>
          <leafValues>
            2.2495600581169128e-01 -2.0447289943695068e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 224 -5.7335309684276581e-02</internalNodes>
          <leafValues>
            -5.6859737634658813e-01 5.2798101678490639e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 225 1.9260890549048781e-03</internalNodes>
          <leafValues>
            1.4920340478420258e-01 -3.1059908866882324e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 226 2.1118070930242538e-02</internalNodes>
          <leafValues>
            4.1174301877617836e-03 -5.2401381731033325e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 227 -1.1973599903285503e-03</internalNodes>
          <leafValues>
            2.3353399336338043e-01 -2.0193660259246826e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 228 4.5973812229931355e-03</internalNodes>
          <leafValues>
            5.9917010366916656e-02 -1.1878310143947601e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 229 2.8869660571217537e-02</internalNodes>
          <leafValues>
            -9.4110779464244843e-02 4.5966941118240356e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 230 -3.7549799308180809e-03</internalNodes>
          <leafValues>
            1.2161179631948471e-01 -1.4811019599437714e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 231 4.2033549398183823e-03</internalNodes>
          <leafValues>
            1.0903070122003555e-01 -3.8700520992279053e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 232 7.2994068264961243e-02</internalNodes>
          <leafValues>
            -3.4046798944473267e-02 3.0610039830207825e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 233 1.6667179763317108e-02</internalNodes>
          <leafValues>
            1.3168589770793915e-01 -3.8485860824584961e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 234 -2.8268690221011639e-03</internalNodes>
          <leafValues>
            6.4782157540321350e-02 -2.2371709346771240e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 235 3.7736070808023214e-03</internalNodes>
          <leafValues>
            -1.5592969954013824e-01 2.5413069128990173e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 236 -3.6936940159648657e-03</internalNodes>
          <leafValues>
            2.5576528906822205e-01 -1.5768060088157654e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 237 -6.6801063716411591e-02</internalNodes>
          <leafValues>
            -7.4346089363098145e-01 5.4915640503168106e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 238 1.5752790495753288e-02</internalNodes>
          <leafValues>
            -9.8638102412223816e-02 4.3119820952415466e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 239 9.0647127944976091e-04</internalNodes>
          <leafValues>
            1.1339239776134491e-01 -4.1574460268020630e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 240 -2.1695699542760849e-02</internalNodes>
          <leafValues>
            4.6949240565299988e-01 -5.5732611566781998e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 241 -1.4639029977843165e-03</internalNodes>
          <leafValues>
            -3.0617880821228027e-01 1.4398169517517090e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 242 -1.7810560762882233e-02</internalNodes>
          <leafValues>
            3.0411729216575623e-01 -4.6758800745010376e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 243 -5.6027648970484734e-03</internalNodes>
          <leafValues>
            -5.2942901849746704e-01 7.8287117183208466e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 244 1.9500569906085730e-03</internalNodes>
          <leafValues>
            -9.5949448645114899e-02 1.9031670689582825e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 245 1.0641569644212723e-01</internalNodes>
          <leafValues>
            4.7288440167903900e-02 -8.6525350809097290e-01</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>21</maxWeakCount>
      <stageThreshold>-1.1566660404205322e+00</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 246 1.8256990239024162e-02</internalNodes>
          <leafValues>
            -5.5564939975738525e-01 4.3546560406684875e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 247 -1.1249440163373947e-01</internalNodes>
          <leafValues>
            6.1800277233123779e-01 -2.1641810238361359e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 248 2.0443440880626440e-03</internalNodes>
          <leafValues>
            -3.1379559636116028e-01 2.6424890756607056e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 249 6.2505697133019567e-04</internalNodes>
          <leafValues>
            -2.3659600317478180e-01 2.1169990301132202e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 250 1.3297300320118666e-03</internalNodes>
          <leafValues>
            -3.1339448690414429e-01 3.0449068546295166e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 251 -4.6840369701385498e-02</internalNodes>
          <leafValues>
            5.3759092092514038e-01 -1.8081139773130417e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 252 -6.4874291419982910e-01</internalNodes>
          <leafValues>
            6.6768437623977661e-01 -9.1247849166393280e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 253 9.6183530986309052e-03</internalNodes>
          <leafValues>
            1.4733779430389404e-01 -3.2193028926849365e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 254 2.2117879707366228e-03</internalNodes>
          <leafValues>
            1.5755419433116913e-01 -3.6799180507659912e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 255 4.9280291423201561e-03</internalNodes>
          <leafValues>
            -8.3405740559101105e-02 6.8260177969932556e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 256 1.3977079652249813e-02</internalNodes>
          <leafValues>
            -1.0702060163021088e-01 4.8326531052589417e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 257 -1.0333389946026728e-04</internalNodes>
          <leafValues>
            1.3645449280738831e-01 -3.1777021288871765e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 258 -2.2287340834736824e-03</internalNodes>
          <leafValues>
            2.1791179478168488e-01 -1.9923299551010132e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 259 -3.2301511615514755e-02</internalNodes>
          <leafValues>
            3.3135131001472473e-01 -2.0617039874196053e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 260 2.3240039125084877e-02</internalNodes>
          <leafValues>
            5.9672571718692780e-02 -6.4993959665298462e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 261 3.5599120892584324e-03</internalNodes>
          <leafValues>
            -1.4818920195102692e-01 2.9893338680267334e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 262 1.5469759702682495e-02</internalNodes>
          <leafValues>
            -7.5569599866867065e-02 5.2314680814743042e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 263 -1.6372289974242449e-04</internalNodes>
          <leafValues>
            1.0446730256080627e-01 -2.0943340659141541e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 264 -2.9369019903242588e-03</internalNodes>
          <leafValues>
            -4.3197739124298096e-01 1.0765810310840607e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 265 -7.8579207183793187e-04</internalNodes>
          <leafValues>
            -2.4614779651165009e-01 2.1554739773273468e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 266 1.1156699620187283e-02</internalNodes>
          <leafValues>
            -8.1820882856845856e-02 6.7338067293167114e-01</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>49</maxWeakCount>
      <stageThreshold>-1.0953630208969116e+00</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 267 -1.8473519384860992e-01</internalNodes>
          <leafValues>
            5.4758828878402710e-01 -2.2319069504737854e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 268 -2.8615030460059643e-03</internalNodes>
          <leafValues>
            1.9264279305934906e-01 -2.2989100217819214e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 269 1.7970189452171326e-01</internalNodes>
          <leafValues>
            -6.4573682844638824e-02 8.0322009325027466e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 270 -5.2812729030847549e-02</internalNodes>
          <leafValues>
            2.8784981369972229e-01 -8.8289387524127960e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 271 6.9000339135527611e-03</internalNodes>
          <leafValues>
            1.0979209840297699e-01 -4.8886889219284058e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 272 4.0469530969858170e-02</internalNodes>
          <leafValues>
            6.1697468161582947e-02 -7.2907817363739014e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 273 4.5191249810159206e-03</internalNodes>
          <leafValues>
            -2.7972379326820374e-01 1.7065159976482391e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 274 -3.8400939665734768e-03</internalNodes>
          <leafValues>
            -2.8329300880432129e-01 1.1611709743738174e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 275 -7.1505218511447310e-04</internalNodes>
          <leafValues>
            1.5870480239391327e-01 -2.8253421187400818e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 276 3.0127899721264839e-02</internalNodes>
          <leafValues>
            -3.6236338317394257e-02 5.3369390964508057e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 277 -1.9907640293240547e-02</internalNodes>
          <leafValues>
            -3.2229989767074585e-01 1.4933170378208160e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 278 -3.1435668468475342e-02</internalNodes>
          <leafValues>
            2.0812889933586121e-01 -9.6762210130691528e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 279 -1.9912680611014366e-02</internalNodes>
          <leafValues>
            -3.2928928732872009e-01 1.2732729315757751e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 280 4.0626749396324158e-02</internalNodes>
          <leafValues>
            1.6985720023512840e-02 -5.2226179838180542e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 281 1.6589110018685460e-03</internalNodes>
          <leafValues>
            -2.3795670270919800e-01 2.0775599777698517e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 282 1.9869199022650719e-03</internalNodes>
          <leafValues>
            -1.3493759930133820e-01 1.2050859630107880e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 283 -4.1985820978879929e-02</internalNodes>
          <leafValues>
            4.4601130485534668e-01 -7.6145969331264496e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 284 7.0260182023048401e-02</internalNodes>
          <leafValues>
            1.5833569690585136e-02 -3.8182300329208374e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 285 -1.7992800101637840e-02</internalNodes>
          <leafValues>
            -3.6973980069160461e-01 1.0451599955558777e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 286 -1.0420969873666763e-01</internalNodes>
          <leafValues>
            5.1836878061294556e-01 -2.2372400388121605e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 287 5.3277369588613510e-02</internalNodes>
          <leafValues>
            7.4715927243232727e-02 -5.8489412069320679e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 288 9.6819162368774414e-02</internalNodes>
          <leafValues>
            -7.8130746260285378e-03 -9.0531897544860840e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 289 -2.2317610681056976e-01</internalNodes>
          <leafValues>
            4.7848999500274658e-01 -8.9570246636867523e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 290 1.3523760251700878e-02</internalNodes>
          <leafValues>
            6.5158583223819733e-02 -1.4030559360980988e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 291 -7.1465343236923218e-02</internalNodes>
          <leafValues>
            -8.8997572660446167e-01 3.8111008703708649e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 292 2.4734560400247574e-02</internalNodes>
          <leafValues>
            -3.2858259975910187e-02 3.5368600487709045e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 293 -4.2641810141503811e-03</internalNodes>
          <leafValues>
            1.2885729968547821e-01 -2.7788180112838745e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 294 4.3246541172266006e-02</internalNodes>
          <leafValues>
            -2.6344619691371918e-02 3.3333760499954224e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 295 5.2720978856086731e-03</internalNodes>
          <leafValues>
            9.6122108399868011e-02 -3.8203689455986023e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 296 -6.4102048054337502e-03</internalNodes>
          <leafValues>
            1.6924449801445007e-01 -7.5236052274703979e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 297 1.7747100442647934e-02</internalNodes>
          <leafValues>
            -6.5126739442348480e-02 5.3720867633819580e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 298 1.6466729342937469e-01</internalNodes>
          <leafValues>
            2.6764029636979103e-02 -6.9506132602691650e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 299 -7.6354909688234329e-03</internalNodes>
          <leafValues>
            1.7261630296707153e-01 -2.0242890715599060e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 300 -7.6648168265819550e-02</internalNodes>
          <leafValues>
            2.2567149996757507e-01 -3.5044141113758087e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 301 2.9634330421686172e-03</internalNodes>
          <leafValues>
            1.0679820179939270e-01 -3.0704519152641296e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 302 -1.8968040123581886e-02</internalNodes>
          <leafValues>
            -6.5349531173706055e-01 4.5328449457883835e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 303 6.2272930145263672e-01</internalNodes>
          <leafValues>
            2.9418470337986946e-02 -7.7416032552719116e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 304 3.1170540023595095e-03</internalNodes>
          <leafValues>
            -1.9263580441474915e-01 1.0082499682903290e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 305 -1.0179740190505981e-01</internalNodes>
          <leafValues>
            5.0667291879653931e-01 -7.5845532119274139e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 306 -8.7539367377758026e-02</internalNodes>
          <leafValues>
            -8.0127829313278198e-01 3.9741981774568558e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 307 -4.0089199319481850e-03</internalNodes>
          <leafValues>
            1.5867359936237335e-01 -2.0390710234642029e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 308 -1.7252740263938904e-01</internalNodes>
          <leafValues>
            -4.8556509613990784e-01 6.6162437200546265e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 309 2.2747491020709276e-03</internalNodes>
          <leafValues>
            1.0839290171861649e-01 -2.6120510697364807e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 310 8.7025731801986694e-02</internalNodes>
          <leafValues>
            -4.5612849295139313e-02 3.0642318725585938e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 311 3.3302091062068939e-02</internalNodes>
          <leafValues>
            9.8511956632137299e-02 -4.0321010351181030e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 312 -5.5495370179414749e-03</internalNodes>
          <leafValues>
            6.7809469997882843e-02 -1.9448509812355042e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 313 -7.5916801579296589e-03</internalNodes>
          <leafValues>
            -3.3229979872703552e-01 1.0552299767732620e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 314 -5.4776940494775772e-02</internalNodes>
          <leafValues>
            3.1344750523567200e-01 -9.2561431229114532e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 315 1.7293309792876244e-02</internalNodes>
          <leafValues>
            -1.0366520285606384e-01 4.5732820034027100e-01</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>40</maxWeakCount>
      <stageThreshold>-1.0216970443725586e+00</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 316 -2.2501630708575249e-02</internalNodes>
          <leafValues>
            5.2293592691421509e-01 -1.7968380451202393e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 317 -1.8166720867156982e-02</internalNodes>
          <leafValues>
            1.4281089603900909e-01 -3.0268448591232300e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 318 3.1680259853601456e-02</internalNodes>
          <leafValues>
            1.5708820521831512e-01 -3.2303369045257568e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 319 -2.3476250469684601e-02</internalNodes>
          <leafValues>
            -4.5576000213623047e-01 1.0300090163946152e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 320 4.5688278973102570e-02</internalNodes>
          <leafValues>
            6.7873537540435791e-02 -7.4623328447341919e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 321 -7.4609883129596710e-02</internalNodes>
          <leafValues>
            2.0548540353775024e-01 -1.0097859799861908e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 322 -4.5903101563453674e-02</internalNodes>
          <leafValues>
            6.6662758588790894e-01 -6.9071657955646515e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 323 -5.7763070799410343e-04</internalNodes>
          <leafValues>
            1.1386449635028839e-01 -1.2278319895267487e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 324 -4.1800830513238907e-04</internalNodes>
          <leafValues>
            1.9999989867210388e-01 -2.2372670471668243e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 325 2.4581039324402809e-03</internalNodes>
          <leafValues>
            1.0073749721050262e-01 -3.6323159933090210e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 326 6.7467048764228821e-02</internalNodes>
          <leafValues>
            5.4200690239667892e-02 -6.0347068309783936e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 327 -3.8971859961748123e-02</internalNodes>
          <leafValues>
            4.0277591347694397e-01 -1.1299470067024231e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 328 1.6628159582614899e-01</internalNodes>
          <leafValues>
            4.8290308564901352e-02 -8.1269222497940063e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 329 5.5140322074294090e-03</internalNodes>
          <leafValues>
            6.0484610497951508e-02 -5.4575890302658081e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 330 1.2837080284953117e-03</internalNodes>
          <leafValues>
            -2.8150710463523865e-01 1.2785549461841583e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 331 3.3840160816907883e-02</internalNodes>
          <leafValues>
            -6.1925090849399567e-02 5.4461580514907837e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 332 1.4224560000002384e-02</internalNodes>
          <leafValues>
            -8.3702072501182556e-02 5.5404889583587646e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 333 -1.4315280714072287e-04</internalNodes>
          <leafValues>
            1.5318620204925537e-01 -2.8312870860099792e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 334 -1.3604390434920788e-02</internalNodes>
          <leafValues>
            -6.3229328393936157e-01 5.6792028248310089e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 335 -1.7952319979667664e-01</internalNodes>
          <leafValues>
            -7.7471101284027100e-01 -1.2696949997916818e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 336 -6.3834888860583305e-03</internalNodes>
          <leafValues>
            1.2864939868450165e-01 -3.1159159541130066e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 337 -1.8140509724617004e-01</internalNodes>
          <leafValues>
            -7.0704931020736694e-01 3.0992519110441208e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 338 3.4940429031848907e-03</internalNodes>
          <leafValues>
            1.0192289948463440e-01 -3.3393231034278870e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 339 4.0861740708351135e-02</internalNodes>
          <leafValues>
            3.1267888844013214e-02 -4.3739050626754761e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 340 3.6993999034166336e-02</internalNodes>
          <leafValues>
            -6.2453608959913254e-02 5.7605278491973877e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 341 -7.7690118923783302e-03</internalNodes>
          <leafValues>
            -6.0737371444702148e-01 6.9758452475070953e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 342 7.1885702200233936e-03</internalNodes>
          <leafValues>
            -1.4034010469913483e-01 2.4509570002555847e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 343 -3.0558679252862930e-02</internalNodes>
          <leafValues>
            -2.6109099388122559e-01 2.0893760025501251e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 344 -1.3949500396847725e-02</internalNodes>
          <leafValues>
            -4.5984518527984619e-01 7.2996988892555237e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 345 -1.7439149320125580e-01</internalNodes>
          <leafValues>
            2.7917501330375671e-01 -7.0309691131114960e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 346 -5.6514460593461990e-03</internalNodes>
          <leafValues>
            -5.8335387706756592e-01 4.8543170094490051e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 347 -5.6718150153756142e-03</internalNodes>
          <leafValues>
            -2.0645590126514435e-01 5.9949990361928940e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 348 -2.9772339985356666e-05</internalNodes>
          <leafValues>
            1.6627080738544464e-01 -1.8144470453262329e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 349 -6.2705092132091522e-03</internalNodes>
          <leafValues>
            2.5829210877418518e-01 -1.3548080623149872e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 350 -5.2028051577508450e-03</internalNodes>
          <leafValues>
            -2.9585519433021545e-01 1.0223600268363953e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 351 -3.6721840500831604e-02</internalNodes>
          <leafValues>
            1.1443459987640381e-01 -1.5670689940452576e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 352 7.8717432916164398e-02</internalNodes>
          <leafValues>
            2.9407389461994171e-02 -8.9653927087783813e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 353 9.0856212377548218e-01</internalNodes>
          <leafValues>
            -5.6400269269943237e-02 6.9543528556823730e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 354 -5.2952598780393600e-03</internalNodes>
          <leafValues>
            1.8282440304756165e-01 -2.0518480241298676e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 355 -5.2672341465950012e-02</internalNodes>
          <leafValues>
            -6.8133538961410522e-01 3.6046069115400314e-02</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>51</maxWeakCount>
      <stageThreshold>-1.0450960397720337e+00</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 356 -2.1731309592723846e-01</internalNodes>
          <leafValues>
            5.9716808795928955e-01 -2.2432699799537659e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 357 -3.4627959132194519e-01</internalNodes>
          <leafValues>
            5.3741937875747681e-01 -8.7782189249992371e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 358 1.0713579831644893e-03</internalNodes>
          <leafValues>
            -3.5920229554176331e-01 1.5685929358005524e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 359 -6.1267141252756119e-02</internalNodes>
          <leafValues>
            -7.1003252267837524e-01 2.0527899265289307e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 360 3.1281840056180954e-02</internalNodes>
          <leafValues>
            -7.4646763503551483e-02 5.9689122438430786e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 361 -1.2337400112301111e-03</internalNodes>
          <leafValues>
            1.5949830412864685e-01 -2.7181199193000793e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 362 -3.4508139360696077e-03</internalNodes>
          <leafValues>
            2.0255160331726074e-01 -1.9399139285087585e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 363 -7.0481761358678341e-03</internalNodes>
          <leafValues>
            -5.5100089311599731e-01 7.0738323032855988e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 364 2.2950200736522675e-01</internalNodes>
          <leafValues>
            -8.7573416531085968e-02 6.0446268320083618e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 365 -2.2578560747206211e-03</internalNodes>
          <leafValues>
            -8.5306502878665924e-02 1.0997729748487473e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 366 -9.7562908194959164e-04</internalNodes>
          <leafValues>
            9.7412303090095520e-02 -3.6251759529113770e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 367 5.3088109940290451e-02</internalNodes>
          <leafValues>
            -3.5328660160303116e-03 -6.0694789886474609e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 368 1.5448880149051547e-03</internalNodes>
          <leafValues>
            -2.2419139742851257e-01 1.7832720279693604e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 369 1.2375700287520885e-02</internalNodes>
          <leafValues>
            -3.5778950899839401e-02 2.9557931423187256e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 370 5.9611927717924118e-03</internalNodes>
          <leafValues>
            -7.3603026568889618e-02 4.8699569702148438e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 371 8.3732418715953827e-03</internalNodes>
          <leafValues>
            9.5786556601524353e-02 -3.9222580194473267e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 372 -7.9954452812671661e-03</internalNodes>
          <leafValues>
            -2.9597011208534241e-01 1.3246519863605499e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 373 1.7624149098992348e-02</internalNodes>
          <leafValues>
            1.1629760265350342e-02 -3.7594190239906311e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 374 -8.1538967788219452e-04</internalNodes>
          <leafValues>
            1.8403179943561554e-01 -2.1106949448585510e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 375 6.5910838544368744e-02</internalNodes>
          <leafValues>
            3.8050938397645950e-02 -8.7356221675872803e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 376 -8.1749828532338142e-03</internalNodes>
          <leafValues>
            -3.0115619301795959e-01 8.1345446407794952e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 377 -3.8275010883808136e-02</internalNodes>
          <leafValues>
            3.8238960504531860e-01 -5.5969979614019394e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 378 3.2501420937478542e-03</internalNodes>
          <leafValues>
            -2.1520890295505524e-01 1.3417840003967285e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 379 5.6356219574809074e-03</internalNodes>
          <leafValues>
            -9.1598346829414368e-02 2.6930230855941772e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 380 -5.1177428103983402e-03</internalNodes>
          <leafValues>
            -3.0092298984527588e-01 1.0440470278263092e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 381 -6.0195129364728928e-02</internalNodes>
          <leafValues>
            1.8512830138206482e-01 -6.3004150986671448e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 382 4.6473558992147446e-02</internalNodes>
          <leafValues>
            3.7559378892183304e-02 -8.1117790937423706e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 383 2.2262150887399912e-03</internalNodes>
          <leafValues>
            -1.2262800335884094e-01 8.3288192749023438e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 384 1.6670780256390572e-02</internalNodes>
          <leafValues>
            -5.2774429321289062e-02 5.4887998104095459e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 385 -6.3093528151512146e-02</internalNodes>
          <leafValues>
            -7.4702072143554688e-01 2.7049509808421135e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 386 -7.7139958739280701e-04</internalNodes>
          <leafValues>
            9.2177063226699829e-02 -2.9994431138038635e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 387 -8.9107893407344818e-02</internalNodes>
          <leafValues>
            -3.8937440514564514e-01 2.9831759631633759e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 388 -1.7469590238761157e-04</internalNodes>
          <leafValues>
            1.6117650270462036e-01 -2.0639100670814514e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 389 -2.1986931096762419e-03</internalNodes>
          <leafValues>
            1.4286069571971893e-01 -1.2366549670696259e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 390 2.1864708978682756e-03</internalNodes>
          <leafValues>
            -1.7435190081596375e-01 1.6586010158061981e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 391 1.2738450430333614e-02</internalNodes>
          <leafValues>
            4.8340078443288803e-02 -8.1297926604747772e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 392 -1.2383400462567806e-02</internalNodes>
          <leafValues>
            -3.7464460730552673e-01 8.1205978989601135e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 393 -1.2094350159168243e-01</internalNodes>
          <leafValues>
            -9.1908979415893555e-01 1.7007840797305107e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 394 4.8902980983257294e-02</internalNodes>
          <leafValues>
            -7.0619069039821625e-02 5.1363438367843628e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 395 -1.9585320260375738e-03</internalNodes>
          <leafValues>
            9.9808372557163239e-02 -1.0681519657373428e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 396 -2.9645320773124695e-01</internalNodes>
          <leafValues>
            -9.1213762760162354e-01 3.2292358577251434e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 397 1.0741979628801346e-01</internalNodes>
          <leafValues>
            -2.3814958985894918e-03 -7.1836417913436890e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 398 -4.2040441185235977e-02</internalNodes>
          <leafValues>
            3.0848339200019836e-01 -9.9647372961044312e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 399 6.8270778283476830e-03</internalNodes>
          <leafValues>
            8.3302132785320282e-02 -3.6433839797973633e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 400 -1.1072089895606041e-02</internalNodes>
          <leafValues>
            -2.5886499881744385e-01 1.2579409778118134e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 401 -1.6399029642343521e-02</internalNodes>
          <leafValues>
            3.0191990733146667e-01 -4.9352090805768967e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 402 -2.0852450688835233e-04</internalNodes>
          <leafValues>
            1.2508730590343475e-01 -2.1993610262870789e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 403 -3.0174860730767250e-02</internalNodes>
          <leafValues>
            -6.5353047847747803e-01 1.0185699909925461e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 404 -3.9148568175733089e-03</internalNodes>
          <leafValues>
            -2.0781719684600830e-01 1.2460950016975403e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 405 -2.7260989882051945e-03</internalNodes>
          <leafValues>
            1.2443950027227402e-01 -1.5540640056133270e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 406 1.7432900145649910e-02</internalNodes>
          <leafValues>
            -5.9761889278888702e-02 4.9430638551712036e-01</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>45</maxWeakCount>
      <stageThreshold>-9.2809242010116577e-01</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 407 -2.1454410254955292e-01</internalNodes>
          <leafValues>
            5.1646298170089722e-01 -2.2012180089950562e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 408 1.3796210289001465e-02</internalNodes>
          <leafValues>
            5.0541419535875320e-02 -2.3305070400238037e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 409 9.6883601509034634e-04</internalNodes>
          <leafValues>
            -2.4793210625648499e-01 2.0536769926548004e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 410 -6.6670728847384453e-03</internalNodes>
          <leafValues>
            -2.2546489536762238e-01 6.4493361860513687e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 411 2.1733778994530439e-03</internalNodes>
          <leafValues>
            -2.1164029836654663e-01 2.1819859743118286e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 412 -1.2321940157562494e-03</internalNodes>
          <leafValues>
            6.7792296409606934e-02 -1.1661940068006516e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 413 -5.9950752183794975e-03</internalNodes>
          <leafValues>
            -4.2384910583496094e-01 1.3204540312290192e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 414 2.6942830532789230e-02</internalNodes>
          <leafValues>
            -1.0161910206079483e-01 4.8092079162597656e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 415 6.6907003521919250e-02</internalNodes>
          <leafValues>
            -8.4552347660064697e-02 4.9274548888206482e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 416 -1.6729519702494144e-03</internalNodes>
          <leafValues>
            9.2197872698307037e-02 -2.2954310476779938e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 417 1.3808730058372021e-02</internalNodes>
          <leafValues>
            -6.0905098915100098e-02 5.8490061759948730e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 418 -2.3627160117030144e-02</internalNodes>
          <leafValues>
            -8.8347977399826050e-01 9.7397705540060997e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 419 -1.3927640393376350e-02</internalNodes>
          <leafValues>
            -6.5309441089630127e-01 5.2886508405208588e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 420 3.6122989840805531e-03</internalNodes>
          <leafValues>
            -2.6369398832321167e-01 1.0595279932022095e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 421 -5.2949450910091400e-02</internalNodes>
          <leafValues>
            -7.3409342765808105e-01 4.7014039009809494e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 422 1.7414819449186325e-02</internalNodes>
          <leafValues>
            1.7683740705251694e-02 -5.8782297372817993e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 423 -3.2427799305878580e-04</internalNodes>
          <leafValues>
            1.3886380195617676e-01 -3.0609750747680664e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 424 -4.3613791465759277e-02</internalNodes>
          <leafValues>
            5.4857110977172852e-01 -6.7348852753639221e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 425 -9.3427510000765324e-04</internalNodes>
          <leafValues>
            1.8392640352249146e-01 -1.7492470145225525e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 426 7.9606421291828156e-02</internalNodes>
          <leafValues>
            4.5652151107788086e-02 -6.3910657167434692e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 427 -2.5120750069618225e-02</internalNodes>
          <leafValues>
            1.0046990215778351e-01 -2.7824568748474121e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 428 3.2976910471916199e-02</internalNodes>
          <leafValues>
            -5.9311199933290482e-02 6.5328377485275269e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 429 -3.7845480255782604e-03</internalNodes>
          <leafValues>
            -2.4190320074558258e-01 1.3097280263900757e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 430 9.4495685771107674e-03</internalNodes>
          <leafValues>
            -9.3100033700466156e-02 2.3785820603370667e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 431 2.5168890133500099e-03</internalNodes>
          <leafValues>
            1.3604310154914856e-01 -2.8159540891647339e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 432 2.6242460589855909e-03</internalNodes>
          <leafValues>
            8.9834272861480713e-02 -3.7729039788246155e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 433 -4.4626198709011078e-02</internalNodes>
          <leafValues>
            3.8320839405059814e-01 -9.6285469830036163e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 434 1.4027470024302602e-04</internalNodes>
          <leafValues>
            -1.7261759936809540e-01 1.6574309766292572e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 435 3.9115909487009048e-02</internalNodes>
          <leafValues>
            7.8652113676071167e-02 -3.5689839720726013e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 436 -6.6682003438472748e-02</internalNodes>
          <leafValues>
            -8.8001507520675659e-01 9.0465601533651352e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 437 6.3860351219773293e-03</internalNodes>
          <leafValues>
            -7.5936213135719299e-02 3.8622769713401794e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 438 4.3549899011850357e-02</internalNodes>
          <leafValues>
            -2.5680009275674820e-02 7.4085921049118042e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 439 1.8360930262133479e-03</internalNodes>
          <leafValues>
            1.1183869838714600e-01 -3.3362200856208801e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 440 1.6189280431717634e-03</internalNodes>
          <leafValues>
            1.8969060853123665e-02 -1.5130129456520081e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 441 2.8807038906961679e-03</internalNodes>
          <leafValues>
            9.4285592436790466e-02 -3.1100749969482422e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 442 -3.2489649951457977e-02</internalNodes>
          <leafValues>
            -2.1908520162105560e-01 1.1370900273323059e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 443 -3.8253709673881531e-02</internalNodes>
          <leafValues>
            3.7908008694648743e-01 -6.8298138678073883e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 444 -1.8478769809007645e-02</internalNodes>
          <leafValues>
            2.9623249173164368e-01 -6.0682911425828934e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 445 1.5569750219583511e-02</internalNodes>
          <leafValues>
            8.5731290280818939e-02 -3.3175340294837952e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 446 -1.7486449796706438e-03</internalNodes>
          <leafValues>
            1.2554299831390381e-01 -1.9797539710998535e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 447 9.0995557606220245e-02</internalNodes>
          <leafValues>
            -6.7590013146400452e-02 5.2676147222518921e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 448 -6.0815969482064247e-03</internalNodes>
          <leafValues>
            2.1883159875869751e-01 -1.5794619917869568e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 449 1.3633850030601025e-02</internalNodes>
          <leafValues>
            1.2463530153036118e-01 -2.3396529257297516e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 450 -3.2046619057655334e-01</internalNodes>
          <leafValues>
            4.5808508992195129e-01 -2.7573259547352791e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 451 -3.6630940157920122e-03</internalNodes>
          <leafValues>
            -2.4003350734710693e-01 1.2256260216236115e-01</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>46</maxWeakCount>
      <stageThreshold>-8.5974782705307007e-01</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 452 -1.5901359915733337e-01</internalNodes>
          <leafValues>
            4.3535038828849792e-01 -1.7064349353313446e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 453 -8.1815905869007111e-03</internalNodes>
          <leafValues>
            -4.6280708909034729e-01 8.8514603674411774e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 454 -7.1978997766564135e-06</internalNodes>
          <leafValues>
            1.6246670484542847e-01 -3.1899040937423706e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 455 1.4128180220723152e-02</internalNodes>
          <leafValues>
            4.3259881436824799e-02 -5.9328877925872803e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 456 -9.5496661961078644e-03</internalNodes>
          <leafValues>
            -6.3987672328948975e-01 4.6203929930925369e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 457 -2.4156800936907530e-03</internalNodes>
          <leafValues>
            2.6009899377822876e-01 -1.7099030315876007e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 458 4.4057718478143215e-03</internalNodes>
          <leafValues>
            -2.2679199278354645e-01 1.6393969953060150e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 459 -3.3825438469648361e-02</internalNodes>
          <leafValues>
            -7.2834062576293945e-01 5.1699958741664886e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 460 2.9628010466694832e-02</internalNodes>
          <leafValues>
            3.4399930387735367e-02 -6.9400608539581299e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 461 1.2294690310955048e-01</internalNodes>
          <leafValues>
            3.3281920477747917e-03 -7.6602149009704590e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 462 -9.8816171288490295e-02</internalNodes>
          <leafValues>
            3.1439980864524841e-01 -1.0131180286407471e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 463 -3.3952430821955204e-03</internalNodes>
          <leafValues>
            3.3362209796905518e-02 -1.3168929517269135e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 464 2.4586699903011322e-02</internalNodes>
          <leafValues>
            -6.5227553248405457e-02 6.8169701099395752e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 465 7.8804800286889076e-03</internalNodes>
          <leafValues>
            1.2926100194454193e-01 -4.3783390522003174e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 466 -9.1016880469396710e-04</internalNodes>
          <leafValues>
            1.3692790269851685e-01 -1.9827769696712494e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 467 1.6178259626030922e-02</internalNodes>
          <leafValues>
            9.9287502467632294e-02 -3.4090539813041687e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 468 -1.0527680069208145e-01</internalNodes>
          <leafValues>
            -9.1738772392272949e-01 3.2674968242645264e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 469 -3.7090498954057693e-02</internalNodes>
          <leafValues>
            4.2047971487045288e-01 -7.1002766489982605e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 470 3.8721140474081039e-02</internalNodes>
          <leafValues>
            -7.3284432291984558e-02 4.8204809427261353e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 471 -3.4923329949378967e-03</internalNodes>
          <leafValues>
            -2.8713211417198181e-01 1.0397130250930786e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 472 -1.1214460246264935e-02</internalNodes>
          <leafValues>
            -5.1632231473922729e-01 5.4384410381317139e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 473 -2.2951549908611923e-04</internalNodes>
          <leafValues>
            -1.6355240345001221e-01 7.7216558158397675e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 474 2.5744609534740448e-02</internalNodes>
          <leafValues>
            -5.7303100824356079e-02 4.9525278806686401e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 475 3.7998620420694351e-02</internalNodes>
          <leafValues>
            2.7654580771923065e-02 -4.8470789194107056e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 476 2.3906941059976816e-03</internalNodes>
          <leafValues>
            -2.0106680691242218e-01 1.6209079325199127e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 477 -1.2891319394111633e-01</internalNodes>
          <leafValues>
            -6.9726997613906860e-01 1.7226759344339371e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 478 9.4630720559507608e-04</internalNodes>
          <leafValues>
            -2.7104228734970093e-01 1.0894539952278137e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 479 3.2807278912514448e-03</internalNodes>
          <leafValues>
            -4.1949510574340820e-02 8.2179002463817596e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 480 5.1204498857259750e-02</internalNodes>
          <leafValues>
            4.8180408775806427e-02 -6.6344922780990601e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 481 -4.5751508325338364e-02</internalNodes>
          <leafValues>
            1.9350789487361908e-01 -3.7223301827907562e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 482 1.4391579665243626e-02</internalNodes>
          <leafValues>
            1.0828830301761627e-01 -2.3524640500545502e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 483 -7.6694227755069733e-03</internalNodes>
          <leafValues>
            7.7429883182048798e-02 -4.6658441424369812e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 484 -4.9375209957361221e-02</internalNodes>
          <leafValues>
            3.5604238510131836e-01 -8.1731930375099182e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 485 4.9358978867530823e-02</internalNodes>
          <leafValues>
            5.0106838345527649e-02 -5.9273171424865723e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 486 5.3014289587736130e-02</internalNodes>
          <leafValues>
            3.3155430108308792e-02 -7.0783668756484985e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 487 -1.2086739763617516e-02</internalNodes>
          <leafValues>
            1.4943680167198181e-01 -1.8973240256309509e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 488 -1.3579580187797546e-01</internalNodes>
          <leafValues>
            4.5863440632820129e-01 -7.1998342871665955e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 489 1.9633909687399864e-03</internalNodes>
          <leafValues>
            -1.0420600324869156e-01 1.8465609848499298e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 490 9.3589266762137413e-03</internalNodes>
          <leafValues>
            5.3957458585500717e-02 -4.7337940335273743e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 491 4.3361759744584560e-03</internalNodes>
          <leafValues>
            -5.7173401117324829e-02 5.0958871841430664e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 492 8.5009206086397171e-03</internalNodes>
          <leafValues>
            9.4076819717884064e-02 -2.9265969991683960e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 493 -1.9089920446276665e-02</internalNodes>
          <leafValues>
            3.5426521301269531e-01 -5.5876109749078751e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 494 -1.6061830101534724e-03</internalNodes>
          <leafValues>
            1.6634060442447662e-01 -1.5939429402351379e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 495 -7.8830653801560402e-03</internalNodes>
          <leafValues>
            -2.6064670085906982e-01 5.5236898362636566e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 496 -3.2838371116667986e-03</internalNodes>
          <leafValues>
            -2.4924349784851074e-01 1.4288279414176941e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 497 1.9204219803214073e-02</internalNodes>
          <leafValues>
            -2.6132659986615181e-02 3.2939550280570984e-01</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>55</maxWeakCount>
      <stageThreshold>-8.6706262826919556e-01</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 498 -1.0141430050134659e-01</internalNodes>
          <leafValues>
            4.7197818756103516e-01 -1.8123960494995117e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 499 -7.6708722114562988e-01</internalNodes>
          <leafValues>
            4.3214419484138489e-01 -1.0705640166997910e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 500 8.0198869109153748e-03</internalNodes>
          <leafValues>
            8.4858916699886322e-02 -5.0163632631301880e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 501 4.2173888534307480e-02</internalNodes>
          <leafValues>
            4.3612729758024216e-02 -6.5135252475738525e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 502 4.0101539343595505e-03</internalNodes>
          <leafValues>
            -2.4151140451431274e-01 1.7029179632663727e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 503 -1.3389269588515162e-03</internalNodes>
          <leafValues>
            -1.8421310186386108e-01 9.2217013239860535e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 504 3.3321550581604242e-03</internalNodes>
          <leafValues>
            -1.6709089279174805e-01 1.9239999353885651e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 505 1.5524900518357754e-03</internalNodes>
          <leafValues>
            1.1113339662551880e-01 -3.1200349330902100e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 506 2.3809259757399559e-02</internalNodes>
          <leafValues>
            -6.4096599817276001e-02 5.6162089109420776e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 507 2.8085429221391678e-02</internalNodes>
          <leafValues>
            -2.2390459477901459e-01 1.6832110285758972e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 508 -4.7726151533424854e-03</internalNodes>
          <leafValues>
            -4.6150028705596924e-01 4.9433000385761261e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 509 1.0531850159168243e-01</internalNodes>
          <leafValues>
            3.4683290868997574e-02 -6.4283651113510132e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 510 -7.2594000957906246e-03</internalNodes>
          <leafValues>
            -4.0418758988380432e-01 6.0901068150997162e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 511 8.7005542591214180e-03</internalNodes>
          <leafValues>
            -7.5832478702068329e-02 8.9484892785549164e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 512 -5.3671520203351974e-02</internalNodes>
          <leafValues>
            7.3710972070693970e-01 -4.0993150323629379e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 513 3.4521210938692093e-02</internalNodes>
          <leafValues>
            -1.3731540180742741e-02 2.7299648523330688e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 514 -7.2156880050897598e-03</internalNodes>
          <leafValues>
            1.2723149359226227e-01 -2.3329609632492065e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 515 1.7666360363364220e-03</internalNodes>
          <leafValues>
            5.7977691292762756e-02 -2.0036549866199493e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 516 3.8101759273558855e-03</internalNodes>
          <leafValues>
            7.3866911232471466e-02 -3.0780071020126343e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 517 -2.5019630789756775e-02</internalNodes>
          <leafValues>
            4.3502670526504517e-01 -4.8294428735971451e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 518 9.7328815609216690e-03</internalNodes>
          <leafValues>
            -8.3063952624797821e-02 3.0008700489997864e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 519 -3.3074519596993923e-03</internalNodes>
          <leafValues>
            1.3591299951076508e-01 -2.2476670145988464e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 520 -1.9178609549999237e-01</internalNodes>
          <leafValues>
            -8.7936902046203613e-01 2.7915079146623611e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 521 6.0892169130966067e-04</internalNodes>
          <leafValues>
            -2.2891379892826080e-01 1.0236170142889023e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 522 -7.7072591520845890e-03</internalNodes>
          <leafValues>
            -2.4917750060558319e-01 9.4315156340599060e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 523 -1.0916110128164291e-01</internalNodes>
          <leafValues>
            5.5664068460464478e-01 -4.7419041395187378e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 524 -6.3703782856464386e-02</internalNodes>
          <leafValues>
            -2.1503069996833801e-01 1.0655879974365234e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 525 -2.6704160496592522e-02</internalNodes>
          <leafValues>
            3.3017820119857788e-01 -9.3569032847881317e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 526 -2.7289129793643951e-03</internalNodes>
          <leafValues>
            8.6531341075897217e-02 -2.6623091101646423e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 527 -1.0575050115585327e-01</internalNodes>
          <leafValues>
            -1. 5.9039499610662460e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 528 1.8904829397797585e-02</internalNodes>
          <leafValues>
            -6.2077309936285019e-02 4.7796338796615601e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 529 -1.6396720707416534e-01</internalNodes>
          <leafValues>
            -1. 1.0493510402739048e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 530 1.0453710332512856e-02</internalNodes>
          <leafValues>
            1.2688960134983063e-01 -2.0351530611515045e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 531 1.3724270462989807e-01</internalNodes>
          <leafValues>
            9.6491426229476929e-03 -3.7908729910850525e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 532 -5.0359591841697693e-03</internalNodes>
          <leafValues>
            -2.5936231017112732e-01 1.1745890229940414e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 533 6.5677291713654995e-03</internalNodes>
          <leafValues>
            -6.0465291142463684e-02 1.5637819468975067e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 534 -3.0346989631652832e-02</internalNodes>
          <leafValues>
            3.8403400778770447e-01 -6.1477359384298325e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 535 1.7546329647302628e-02</internalNodes>
          <leafValues>
            2.8643229976296425e-02 -4.7679468989372253e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 536 -4.5566740445792675e-03</internalNodes>
          <leafValues>
            -3.1261089444160461e-01 1.0885629802942276e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 537 -6.9851092994213104e-02</internalNodes>
          <leafValues>
            -7.0994102954864502e-01 1.8536770716309547e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 538 -1.4962710338295437e-05</internalNodes>
          <leafValues>
            1.0287140309810638e-01 -2.2921159863471985e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 539 -7.2705000638961792e-02</internalNodes>
          <leafValues>
            4.2520120739936829e-01 -2.8236340731382370e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 540 3.7338290363550186e-02</internalNodes>
          <leafValues>
            -7.6630033552646637e-02 3.2374149560928345e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 541 2.8690960258245468e-02</internalNodes>
          <leafValues>
            3.0029499903321266e-02 -8.4007978439331055e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 542 1.0019769892096519e-02</internalNodes>
          <leafValues>
            -7.9071857035160065e-02 3.4019070863723755e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 543 -3.9540659636259079e-03</internalNodes>
          <leafValues>
            -2.4449679255485535e-01 1.1845660209655762e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 544 -8.2879550755023956e-03</internalNodes>
          <leafValues>
            1.0628750175237656e-01 -2.2044150531291962e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 545 -3.4582480788230896e-02</internalNodes>
          <leafValues>
            -7.1333628892898560e-01 2.9727920889854431e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 546 -1.4701869804412127e-03</internalNodes>
          <leafValues>
            1.2630669772624969e-01 -1.8260860443115234e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 547 -1.8792560324072838e-02</internalNodes>
          <leafValues>
            4.4159510731697083e-01 -6.2980100512504578e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 548 -1.9830280914902687e-02</internalNodes>
          <leafValues>
            -2.8308698534965515e-01 9.2180028557777405e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 549 -1.6321459412574768e-01</internalNodes>
          <leafValues>
            -4.1355830430984497e-01 1.1562050320208073e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 550 7.5624987483024597e-02</internalNodes>
          <leafValues>
            2.2105440497398376e-02 -9.1430252790451050e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 551 -2.2491789422929287e-03</internalNodes>
          <leafValues>
            9.1926686465740204e-02 -1.0633769631385803e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 552 -6.3310638070106506e-02</internalNodes>
          <leafValues>
            -7.7100628614425659e-01 2.7047479525208473e-02</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>60</maxWeakCount>
      <stageThreshold>-8.9544051885604858e-01</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 553 -1.7043270170688629e-01</internalNodes>
          <leafValues>
            4.7425061464309692e-01 -1.8581479787826538e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 554 2.7967130765318871e-02</internalNodes>
          <leafValues>
            -8.6291179060935974e-02 5.3257989883422852e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 555 2.0941249385941774e-04</internalNodes>
          <leafValues>
            -2.7199700474739075e-01 1.3615070283412933e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 556 -3.3637240529060364e-02</internalNodes>
          <leafValues>
            2.8299760818481445e-01 -2.2356469184160233e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 557 -4.5356429181993008e-03</internalNodes>
          <leafValues>
            1.6135759651660919e-01 -2.0162500441074371e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 558 3.3124668989330530e-03</internalNodes>
          <leafValues>
            -7.9677619040012360e-02 1.4375239610671997e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 559 -5.4888740181922913e-02</internalNodes>
          <leafValues>
            6.6563862562179565e-01 -5.3526669740676880e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 560 5.3796600550413132e-03</internalNodes>
          <leafValues>
            -9.6400886774063110e-02 9.3223050236701965e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 561 -6.0283239930868149e-02</internalNodes>
          <leafValues>
            -5.4325622320175171e-01 5.4515969008207321e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 562 8.4590855985879898e-03</internalNodes>
          <leafValues>
            5.0189521163702011e-02 -3.7638399004936218e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 563 2.8549430426210165e-03</internalNodes>
          <leafValues>
            1.3105809688568115e-01 -2.4903079867362976e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 564 -2.0608250051736832e-02</internalNodes>
          <leafValues>
            -4.3393260240554810e-01 6.0918930917978287e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 565 -1.0088419541716576e-02</internalNodes>
          <leafValues>
            2.9433688521385193e-01 -1.0092660039663315e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 566 -5.9431340545415878e-02</internalNodes>
          <leafValues>
            -9.0102052688598633e-01 2.7330689132213593e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 567 -2.4024050217121840e-03</internalNodes>
          <leafValues>
            1.2758029997348785e-01 -1.9134059548377991e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 568 -2.7372820302844048e-02</internalNodes>
          <leafValues>
            -2.8051578998565674e-01 1.0892979800701141e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 569 -7.3817551136016846e-02</internalNodes>
          <leafValues>
            3.6636620759963989e-01 -7.1261473000049591e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 570 -6.9365866482257843e-02</internalNodes>
          <leafValues>
            4.4759741425514221e-01 -3.5112198442220688e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 571 -1.2530760141089559e-03</internalNodes>
          <leafValues>
            1.0481069982051849e-01 -2.5331568717956543e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 572 -3.2429681159555912e-03</internalNodes>
          <leafValues>
            -2.1083809435367584e-01 8.9755013585090637e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 573 1.6115259379148483e-02</internalNodes>
          <leafValues>
            -5.8019161224365234e-02 5.5759441852569580e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 574 6.2562932725995779e-04</internalNodes>
          <leafValues>
            -2.1611200273036957e-01 1.2215120345354080e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 575 -7.6641827821731567e-01</internalNodes>
          <leafValues>
            -6.3647639751434326e-01 3.3915121108293533e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 576 -7.4419458542251959e-06</internalNodes>
          <leafValues>
            9.5346711575984955e-02 -2.3950740694999695e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 577 -3.7739300751127303e-04</internalNodes>
          <leafValues>
            1.4481280744075775e-01 -1.8476490676403046e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 578 7.6729603111743927e-02</internalNodes>
          <leafValues>
            1.1742720380425453e-02 -9.6213918924331665e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 579 -4.4697099365293980e-03</internalNodes>
          <leafValues>
            -2.3385390639305115e-01 1.0464339703321457e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 580 7.5911812484264374e-02</internalNodes>
          <leafValues>
            6.7219119518995285e-03 -4.2311188578605652e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 581 -8.3202589303255081e-03</internalNodes>
          <leafValues>
            3.2122060656547546e-01 -8.3661839365959167e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 582 -3.7233818322420120e-02</internalNodes>
          <leafValues>
            1.1662390083074570e-01 -2.3976010084152222e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 583 -2.1381198894232512e-03</internalNodes>
          <leafValues>
            8.4755808115005493e-02 -2.5149530172348022e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 584 -4.4315438717603683e-03</internalNodes>
          <leafValues>
            -1.0990399867296219e-01 6.6713362932205200e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 585 -1.0959600098431110e-02</internalNodes>
          <leafValues>
            2.8818470239639282e-01 -7.7696867287158966e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 586 3.4907169640064240e-02</internalNodes>
          <leafValues>
            -1.1712339706718922e-02 3.9965820312500000e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 587 -1.3335079886019230e-02</internalNodes>
          <leafValues>
            -4.9896249175071716e-01 5.3193040192127228e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 588 -3.7070110440254211e-02</internalNodes>
          <leafValues>
            -5.9346628189086914e-01 1.2502389959990978e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 589 -9.1118857264518738e-02</internalNodes>
          <leafValues>
            -6.0664188861846924e-01 3.0223639681935310e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 590 -6.7527957260608673e-02</internalNodes>
          <leafValues>
            3.2593071460723877e-01 -3.2810360193252563e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 591 -2.6317719370126724e-02</internalNodes>
          <leafValues>
            -7.6599878072738647e-01 2.5263689458370209e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 592 3.7877839058637619e-02</internalNodes>
          <leafValues>
            1.7415969632565975e-03 -9.1090667247772217e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 593 1.6833839472383261e-03</internalNodes>
          <leafValues>
            -6.4769007265567780e-02 3.5946249961853027e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 594 -4.2451170884305611e-05</internalNodes>
          <leafValues>
            6.2228899449110031e-02 -8.5069350898265839e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 595 2.7713281451724470e-04</internalNodes>
          <leafValues>
            -1.7252549529075623e-01 1.2511169910430908e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 596 -3.0400960240513086e-03</internalNodes>
          <leafValues>
            1.5032739937305450e-01 -1.4423249661922455e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 597 -5.4823148995637894e-02</internalNodes>
          <leafValues>
            3.4711471199989319e-01 -6.3294216990470886e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 598 1.4232549583539367e-03</internalNodes>
          <leafValues>
            7.3755688965320587e-02 -2.7084198594093323e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 599 -3.3660030458122492e-03</internalNodes>
          <leafValues>
            -2.3144030570983887e-01 8.8216871023178101e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 600 -1.1405759723857045e-03</internalNodes>
          <leafValues>
            1.5687429904937744e-01 -1.3379560410976410e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 601 3.7445020861923695e-03</internalNodes>
          <leafValues>
            -1.2132400274276733e-01 2.2723269462585449e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 602 1.6585510224103928e-02</internalNodes>
          <leafValues>
            5.4631579667329788e-02 -1.0117000341415405e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 603 -2.9970710165798664e-03</internalNodes>
          <leafValues>
            1.7258630692958832e-01 -1.4288370311260223e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 604 -3.0509869102388620e-03</internalNodes>
          <leafValues>
            1.0889530181884766e-01 -1.2865459918975830e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 605 -2.7037179097533226e-02</internalNodes>
          <leafValues>
            -2.1809040009975433e-01 1.0335580259561539e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 606 -1.4020490460097790e-02</internalNodes>
          <leafValues>
            1.7013829946517944e-01 -4.6483799815177917e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 607 4.0001110173761845e-03</internalNodes>
          <leafValues>
            6.1452940106391907e-02 -3.5107728838920593e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 608 1.1888570152223110e-02</internalNodes>
          <leafValues>
            -6.5659493207931519e-02 3.4128171205520630e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 609 1.0041910223662853e-02</internalNodes>
          <leafValues>
            1.0645069926977158e-01 -2.3905399441719055e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 610 -8.3469128003343940e-04</internalNodes>
          <leafValues>
            1.1359920352697372e-01 -1.2456230074167252e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 611 -8.4286198019981384e-02</internalNodes>
          <leafValues>
            4.4472348690032959e-01 -4.6677689999341965e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 612 -1.2084700167179108e-02</internalNodes>
          <leafValues>
            -3.1389999389648438e-01 8.1864818930625916e-02</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>69</maxWeakCount>
      <stageThreshold>-8.5815817117691040e-01</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 613 -6.6878342628479004e-01</internalNodes>
          <leafValues>
            4.1411510109901428e-01 -1.8810300529003143e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 614 3.4350738860666752e-04</internalNodes>
          <leafValues>
            -1.5680180490016937e-01 1.0782240331172943e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 615 2.6565280277282000e-03</internalNodes>
          <leafValues>
            -2.2030730545520782e-01 2.1439610421657562e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 616 -1.9296359270811081e-02</internalNodes>
          <leafValues>
            4.2026680707931519e-01 -6.8671546876430511e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 617 -6.6540208645164967e-03</internalNodes>
          <leafValues>
            -2.3488819599151611e-01 1.6749989986419678e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 618 1.5521990135312080e-02</internalNodes>
          <leafValues>
            1.9785670563578606e-02 -3.9180341362953186e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 619 8.0317907035350800e-02</internalNodes>
          <leafValues>
            -1.9278699532151222e-02 5.8520817756652832e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 620 -1.0220059752464294e-01</internalNodes>
          <leafValues>
            -8.1461167335510254e-01 8.9545976370573044e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 621 -1.0618870146572590e-02</internalNodes>
          <leafValues>
            1.8044769763946533e-01 -2.1122869849205017e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 622 9.8658069968223572e-02</internalNodes>
          <leafValues>
            -4.9179349094629288e-02 2.1871259808540344e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 623 -6.6758222877979279e-02</internalNodes>
          <leafValues>
            -2.6649540662765503e-01 1.0707940161228180e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 624 -2.9256459325551987e-02</internalNodes>
          <leafValues>
            -7.8809207677841187e-01 5.6176739744842052e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 625 -1.2126189656555653e-02</internalNodes>
          <leafValues>
            1.0218500345945358e-01 -2.2899429500102997e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 626 -5.4919619113206863e-02</internalNodes>
          <leafValues>
            -5.3647202253341675e-01 1.4213330112397671e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 627 -4.0985811501741409e-03</internalNodes>
          <leafValues>
            -3.1650361418724060e-01 7.6794192194938660e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 628 -6.2581077218055725e-02</internalNodes>
          <leafValues>
            -4.8726239800453186e-01 9.1610476374626160e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 629 4.9834471195936203e-02</internalNodes>
          <leafValues>
            -7.5687482953071594e-02 2.9998108744621277e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 630 1.0333029925823212e-01</internalNodes>
          <leafValues>
            3.3387999981641769e-02 -5.6652718782424927e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 631 -2.6153959333896637e-02</internalNodes>
          <leafValues>
            4.4663658738136292e-01 -5.7146150618791580e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 632 6.8949297070503235e-02</internalNodes>
          <leafValues>
            6.6676470451056957e-03 -9.9968850612640381e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 633 2.1299200598150492e-03</internalNodes>
          <leafValues>
            -1.8253549933433533e-01 1.2543450295925140e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 634 -4.4991839677095413e-02</internalNodes>
          <leafValues>
            -5.6401151418685913e-01 3.7286750972270966e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 635 2.2533860057592392e-02</internalNodes>
          <leafValues>
            -4.2648501694202423e-02 5.9839051961898804e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 636 1.9274459779262543e-01</internalNodes>
          <leafValues>
            3.0479490756988525e-02 -8.4564548730850220e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 637 -9.2559499898925424e-04</internalNodes>
          <leafValues>
            -2.0614519715309143e-01 1.1016649752855301e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 638 -3.6584408953785896e-03</internalNodes>
          <leafValues>
            9.1432936489582062e-02 -8.2888223230838776e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 639 3.3741090446710587e-03</internalNodes>
          <leafValues>
            8.0734901130199432e-02 -3.0495160818099976e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 640 -5.1757801324129105e-02</internalNodes>
          <leafValues>
            -8.0067127943038940e-01 2.8978339396417141e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 641 1.0498389601707458e-03</internalNodes>
          <leafValues>
            -1.8396970629692078e-01 1.3429929316043854e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 642 7.5232777744531631e-03</internalNodes>
          <leafValues>
            -3.1206240877509117e-02 1.2124940007925034e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 643 -7.1075286541599780e-05</internalNodes>
          <leafValues>
            8.4017656743526459e-02 -2.5043961405754089e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 644 1.1362830176949501e-02</internalNodes>
          <leafValues>
            -7.6280519366264343e-02 2.0559790730476379e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 645 -2.4097480345517397e-03</internalNodes>
          <leafValues>
            -1.5042850375175476e-01 1.6493639349937439e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 646 2.4056989699602127e-02</internalNodes>
          <leafValues>
            1.4566550031304359e-02 -9.0886771678924561e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 647 -2.3983620107173920e-02</internalNodes>
          <leafValues>
            3.9107671380043030e-01 -5.4178200662136078e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 648 -2.1438319236040115e-02</internalNodes>
          <leafValues>
            -4.8545840382575989e-01 4.0402751415967941e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 649 1.5210740268230438e-02</internalNodes>
          <leafValues>
            3.4481588751077652e-02 -5.4406332969665527e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 650 1.1712989769876003e-02</internalNodes>
          <leafValues>
            -6.5206751227378845e-02 4.1007021069526672e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 651 6.3996820244938135e-04</internalNodes>
          <leafValues>
            -1.4772899448871613e-01 1.5154249966144562e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 652 -3.4567480906844139e-03</internalNodes>
          <leafValues>
            6.3351117074489594e-02 -1.4297829568386078e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 653 -1.2475489638745785e-03</internalNodes>
          <leafValues>
            -1.8521060049533844e-01 1.3410830497741699e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 654 6.6904430277645588e-03</internalNodes>
          <leafValues>
            1.4112530648708344e-01 -1.8778939545154572e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 655 -6.9181032478809357e-02</internalNodes>
          <leafValues>
            3.4451478719711304e-01 -8.4655232727527618e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 656 -6.7893281579017639e-02</internalNodes>
          <leafValues>
            -7.0076942443847656e-01 2.3327259346842766e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 657 -8.5538747953251004e-04</internalNodes>
          <leafValues>
            9.2393256723880768e-02 -2.1416470408439636e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 658 1.7967769503593445e-01</internalNodes>
          <leafValues>
            2.9103670269250870e-02 -7.8690862655639648e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 659 -2.9843579977750778e-03</internalNodes>
          <leafValues>
            1.6117380559444427e-01 -1.2868699431419373e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 660 1.9973449409008026e-02</internalNodes>
          <leafValues>
            3.6350231617689133e-02 -5.9400641918182373e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 661 -8.3998020272701979e-04</internalNodes>
          <leafValues>
            1.1332140117883682e-01 -1.9175720214843750e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 662 5.0804121419787407e-03</internalNodes>
          <leafValues>
            5.3663559257984161e-02 -2.7940011024475098e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 663 7.3341121897101402e-03</internalNodes>
          <leafValues>
            -1.6792379319667816e-01 1.2119220197200775e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 664 7.6924441382288933e-03</internalNodes>
          <leafValues>
            -6.9076187908649445e-02 1.8550349771976471e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 665 2.0062309340573847e-04</internalNodes>
          <leafValues>
            -2.0654049515724182e-01 9.7337253391742706e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 666 2.6919560506939888e-02</internalNodes>
          <leafValues>
            -2.3648599162697792e-02 6.4873528480529785e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 667 -2.7951570227742195e-03</internalNodes>
          <leafValues>
            -2.0725600421428680e-01 1.0188090056180954e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 668 7.8026622533798218e-02</internalNodes>
          <leafValues>
            8.9439805597066879e-03 -3.9990609884262085e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 669 -1.0000459849834442e-01</internalNodes>
          <leafValues>
            3.7361750006675720e-01 -5.5814821273088455e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 670 -1.4978240430355072e-01</internalNodes>
          <leafValues>
            3.8677608966827393e-01 -5.5641401559114456e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 671 3.3566348254680634e-02</internalNodes>
          <leafValues>
            7.5311936438083649e-02 -3.2007390260696411e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 672 -2.1213890612125397e-01</internalNodes>
          <leafValues>
            -5.9270721673965454e-01 4.9450621008872986e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 673 -1.4402889646589756e-02</internalNodes>
          <leafValues>
            3.2471069693565369e-01 -5.8492168784141541e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 674 -1.8413169309496880e-02</internalNodes>
          <leafValues>
            -9.6801750361919403e-02 1.0343659669160843e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 675 1.6228349879384041e-02</internalNodes>
          <leafValues>
            -6.0577668249607086e-02 3.1738010048866272e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 676 -6.7683439701795578e-03</internalNodes>
          <leafValues>
            -1.9742150604724884e-01 2.7996420860290527e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 677 -1.9165309146046638e-02</internalNodes>
          <leafValues>
            -2.5684070587158203e-01 8.3432748913764954e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 678 2.8667549486272037e-04</internalNodes>
          <leafValues>
            -1.5241080522537231e-01 1.4404779672622681e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 679 9.4157401472330093e-03</internalNodes>
          <leafValues>
            -7.3207639157772064e-02 3.3655610680580139e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 680 2.3321900516748428e-02</internalNodes>
          <leafValues>
            -6.1898268759250641e-02 8.3489909768104553e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 681 -1.1910670436918736e-02</internalNodes>
          <leafValues>
            -1.9628530740737915e-01 9.6807330846786499e-02</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>63</maxWeakCount>
      <stageThreshold>-7.2787708044052124e-01</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 682 -9.4191312789916992e-02</internalNodes>
          <leafValues>
            4.7028279304504395e-01 -1.4449509978294373e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 683 -6.9314462598413229e-04</internalNodes>
          <leafValues>
            1.7749489843845367e-01 -1.8127989768981934e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 684 -1.2782390415668488e-01</internalNodes>
          <leafValues>
            2.9733940958976746e-01 -1.0098580271005630e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 685 -2.5297680404037237e-03</internalNodes>
          <leafValues>
            1.0854879766702652e-01 -1.3471469283103943e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 686 -2.5406670756638050e-03</internalNodes>
          <leafValues>
            -2.7025818824768066e-01 1.0289029777050018e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 687 -1.5717690112069249e-03</internalNodes>
          <leafValues>
            1.7058460414409637e-01 -1.0923519730567932e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 688 1.4790190383791924e-02</internalNodes>
          <leafValues>
            2.3690680041909218e-02 -5.1412177085876465e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 689 -1.1837840080261230e-02</internalNodes>
          <leafValues>
            1.5754750370979309e-01 -2.7252310886979103e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 690 -3.8180808769538999e-04</internalNodes>
          <leafValues>
            1.0274309664964676e-01 -2.1815380454063416e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 691 5.0768889486789703e-02</internalNodes>
          <leafValues>
            7.3335068300366402e-03 -8.5053902864456177e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 692 2.2738629952073097e-02</internalNodes>
          <leafValues>
            -4.3974649161100388e-02 5.0167572498321533e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 693 7.3323072865605354e-04</internalNodes>
          <leafValues>
            -9.8431721329689026e-02 1.1515360325574875e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 694 1.1889509623870254e-03</internalNodes>
          <leafValues>
            -2.2443179786205292e-01 1.0813289880752563e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 695 -3.2934029586613178e-03</internalNodes>
          <leafValues>
            7.1840867400169373e-02 -8.0868020653724670e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 696 -3.0113169923424721e-03</internalNodes>
          <leafValues>
            -2.9698678851127625e-01 7.9700268805027008e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 697 -1.5521480236202478e-03</internalNodes>
          <leafValues>
            1.8694180250167847e-01 -1.1467470228672028e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 698 -1.0300680063664913e-02</internalNodes>
          <leafValues>
            -2.9109370708465576e-01 6.7836336791515350e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 699 -2.6368349790573120e-03</internalNodes>
          <leafValues>
            1.1284109950065613e-01 -7.3468528687953949e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 700 -3.2815459417179227e-04</internalNodes>
          <leafValues>
            8.1921890377998352e-02 -2.4893359839916229e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 701 -3.4514568746089935e-02</internalNodes>
          <leafValues>
            4.2230990529060364e-01 -3.4608390182256699e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 702 2.1102999744471163e-04</internalNodes>
          <leafValues>
            -1.9479750096797943e-01 1.1572039872407913e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 703 -4.4254157692193985e-03</internalNodes>
          <leafValues>
            -1.9316120445728302e-01 5.8137431740760803e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 704 -1.7686230130493641e-03</internalNodes>
          <leafValues>
            -1.7518809437751770e-01 1.4515039324760437e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 705 -3.3355921041220427e-03</internalNodes>
          <leafValues>
            2.2621470689773560e-01 -1.0195499658584595e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 706 4.5241121202707291e-02</internalNodes>
          <leafValues>
            3.3572640269994736e-02 -6.6535997390747070e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 707 -2.7708040550351143e-02</internalNodes>
          <leafValues>
            -4.7514501214027405e-01 1.6605619341135025e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 708 -6.0042630881071091e-02</internalNodes>
          <leafValues>
            2.7002659440040588e-01 -7.5283601880073547e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 709 9.3657420948147774e-03</internalNodes>
          <leafValues>
            -5.2090760320425034e-02 3.4359771013259888e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 710 2.2545119747519493e-02</internalNodes>
          <leafValues>
            4.5823760330677032e-02 -5.3111177682876587e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 711 -6.6756099462509155e-02</internalNodes>
          <leafValues>
            5.1867592334747314e-01 -1.0766089893877506e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 712 4.3578571639955044e-03</internalNodes>
          <leafValues>
            -1.6680300235748291e-01 1.3410590589046478e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 713 -3.6338180303573608e-02</internalNodes>
          <leafValues>
            -5.4825192689895630e-01 1.8291600048542023e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 714 -4.5509558171033859e-02</internalNodes>
          <leafValues>
            3.9119181036949158e-01 -5.4338268935680389e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 715 6.2883161008358002e-03</internalNodes>
          <leafValues>
            9.5495186746120453e-02 -2.4893720448017120e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 716 1.5809159958735108e-03</internalNodes>
          <leafValues>
            -1.6792270541191101e-01 1.1553759872913361e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 717 -1.5780210494995117e-01</internalNodes>
          <leafValues>
            -6.9598740339279175e-01 3.1015299260616302e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 718 -5.0400748848915100e-02</internalNodes>
          <leafValues>
            -6.1013418436050415e-01 2.5600189343094826e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 719 -8.3708087913691998e-04</internalNodes>
          <leafValues>
            6.3689701259136200e-02 -3.2572910189628601e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 720 5.2259840071201324e-02</internalNodes>
          <leafValues>
            -5.2639529109001160e-02 4.3018800020217896e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 721 6.6796218743547797e-04</internalNodes>
          <leafValues>
            8.0761440098285675e-02 -2.5092118978500366e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 722 -3.6306399852037430e-02</internalNodes>
          <leafValues>
            7.2837859392166138e-01 -2.8703549876809120e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 723 -7.5823411345481873e-02</internalNodes>
          <leafValues>
            -7.6045262813568115e-01 1.3166300021111965e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 724 -5.5567082017660141e-03</internalNodes>
          <leafValues>
            1.1258409917354584e-01 -1.9850979745388031e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 725 3.1275521032512188e-03</internalNodes>
          <leafValues>
            -1.0436189919710159e-01 1.0283000022172928e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 726 2.7931319549679756e-02</internalNodes>
          <leafValues>
            4.7023560851812363e-02 -4.7727531194686890e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 727 1.5156970359385014e-02</internalNodes>
          <leafValues>
            -4.9909379333257675e-02 2.1705010533332825e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 728 6.8009081296622753e-03</internalNodes>
          <leafValues>
            1.1713290214538574e-01 -2.2082920372486115e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 729 -4.3796948157250881e-03</internalNodes>
          <leafValues>
            1.7191199958324432e-01 -8.9668810367584229e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 730 -6.9269728846848011e-03</internalNodes>
          <leafValues>
            8.8258482515811920e-02 -2.6454809308052063e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 731 -2.0586250722408295e-01</internalNodes>
          <leafValues>
            -5.0262999534606934e-01 4.0832251310348511e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 732 -1.1398729839129373e-04</internalNodes>
          <leafValues>
            1.0535170137882233e-01 -1.9488720595836639e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 733 3.6993779242038727e-02</internalNodes>
          <leafValues>
            -5.4779630154371262e-02 2.2932989895343781e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 734 4.7788480296730995e-03</internalNodes>
          <leafValues>
            9.1294333338737488e-02 -2.4968950450420380e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 735 1.1999059934169054e-03</internalNodes>
          <leafValues>
            -9.2685289680957794e-02 1.1050710082054138e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 736 2.0830740686506033e-03</internalNodes>
          <leafValues>
            -1.0583080351352692e-01 1.7405270040035248e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 737 2.7166489511728287e-02</internalNodes>
          <leafValues>
            1.1538780294358730e-02 -1.0000569820404053e+00</leafValues></_>
        <_>
          <internalNodes>
            0 -1 738 -4.3531907722353935e-03</internalNodes>
          <leafValues>
            -2.6105979084968567e-01 7.8109443187713623e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 739 -1.6676170751452446e-02</internalNodes>
          <leafValues>
            -6.3766658306121826e-01 1.2807319872081280e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 740 -1.7588710179552436e-03</internalNodes>
          <leafValues>
            1.5328720211982727e-01 -1.4830219745635986e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 741 -1.3470610138028860e-03</internalNodes>
          <leafValues>
            1.1022730171680450e-01 -1.1166580021381378e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 742 -7.7226730063557625e-03</internalNodes>
          <leafValues>
            2.6749759912490845e-01 -8.4375701844692230e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 743 2.4557989090681076e-02</internalNodes>
          <leafValues>
            1.1705229990184307e-02 -6.9936311244964600e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 744 -4.1882451623678207e-03</internalNodes>
          <leafValues>
            -2.0845660567283630e-01 1.1073870211839676e-01</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>67</maxWeakCount>
      <stageThreshold>-7.7944219112396240e-01</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 745 -3.0925211310386658e-01</internalNodes>
          <leafValues>
            3.1520840525627136e-01 -1.6629250347614288e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 746 3.8660250604152679e-02</internalNodes>
          <leafValues>
            -5.7934600859880447e-02 4.5278790593147278e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 747 -1.8853870034217834e-01</internalNodes>
          <leafValues>
            -8.2013928890228271e-01 3.0941359698772430e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 748 7.1423681220039725e-04</internalNodes>
          <leafValues>
            1.0280930250883102e-01 -2.4902869760990143e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 749 -7.2074443101882935e-02</internalNodes>
          <leafValues>
            3.3171579241752625e-01 -7.3685511946678162e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 750 9.4616664573550224e-03</internalNodes>
          <leafValues>
            3.2647788524627686e-02 -3.6112511157989502e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 751 -4.6513080596923828e-02</internalNodes>
          <leafValues>
            -4.7550851106643677e-01 5.6877400726079941e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 752 -3.4777458757162094e-02</internalNodes>
          <leafValues>
            -6.3515567779541016e-01 3.1314119696617126e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 753 -1.4840300427749753e-03</internalNodes>
          <leafValues>
            9.2628233134746552e-02 -2.5283080339431763e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 754 8.3039281889796257e-03</internalNodes>
          <leafValues>
            3.3991388976573944e-02 -1.8357479572296143e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 755 2.7342209592461586e-02</internalNodes>
          <leafValues>
            -5.1393941044807434e-02 5.5958998203277588e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 756 5.8637421578168869e-02</internalNodes>
          <leafValues>
            -5.7350661605596542e-02 1.4842259883880615e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 757 -3.7032511085271835e-02</internalNodes>
          <leafValues>
            -4.0602868795394897e-01 6.6790133714675903e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 758 8.9913606643676758e-03</internalNodes>
          <leafValues>
            -1.9094319641590118e-01 5.9438090771436691e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 759 -5.9351198375225067e-02</internalNodes>
          <leafValues>
            -8.7097257375717163e-01 2.1483449265360832e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 760 3.7055540084838867e-01</internalNodes>
          <leafValues>
            -4.0396090596914291e-02 6.0631322860717773e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 761 -8.4517069626599550e-04</internalNodes>
          <leafValues>
            1.3660719990730286e-01 -1.5541790425777435e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 762 1.0664479807019234e-02</internalNodes>
          <leafValues>
            3.4129761159420013e-02 -2.3508089780807495e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 763 3.7040449678897858e-03</internalNodes>
          <leafValues>
            1.1293920129537582e-01 -1.5596470236778259e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 764 2.3328550159931183e-02</internalNodes>
          <leafValues>
            3.6770980805158615e-02 -1.6631129384040833e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 765 2.0906640216708183e-02</internalNodes>
          <leafValues>
            -7.3391966521739960e-02 3.2708668708801270e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 766 2.0865180995315313e-03</internalNodes>
          <leafValues>
            9.6375763416290283e-02 -2.1638840436935425e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 767 1.2039430439472198e-03</internalNodes>
          <leafValues>
            -1.7018699645996094e-01 1.0815030336380005e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 768 3.3848760649561882e-03</internalNodes>
          <leafValues>
            -1.0820890218019485e-01 9.0751953423023224e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 769 -1.5309279784560204e-02</internalNodes>
          <leafValues>
            -6.2071442604064941e-01 3.1353730708360672e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 770 2.1820720285177231e-02</internalNodes>
          <leafValues>
            -5.7232249528169632e-02 2.9141768813133240e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 771 5.8554150164127350e-03</internalNodes>
          <leafValues>
            5.5810708552598953e-02 -3.4557789564132690e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 772 -8.8380590081214905e-02</internalNodes>
          <leafValues>
            -5.8971607685089111e-01 3.2257869839668274e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 773 -3.6303598433732986e-02</internalNodes>
          <leafValues>
            6.7906290292739868e-01 -3.1298439949750900e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 774 6.7714422941207886e-02</internalNodes>
          <leafValues>
            2.8151830658316612e-02 -7.5963890552520752e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 775 -1.7487880541011691e-03</internalNodes>
          <leafValues>
            1.3521270453929901e-01 -1.4939880371093750e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 776 5.7627420872449875e-02</internalNodes>
          <leafValues>
            1.4716790057718754e-02 -6.4088898897171021e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 777 4.8004398122429848e-03</internalNodes>
          <leafValues>
            5.7510860264301300e-02 -3.0728340148925781e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 778 1.5568589791655540e-02</internalNodes>
          <leafValues>
            -2.6860829442739487e-02 3.9390829205513000e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 779 -9.9650640040636063e-03</internalNodes>
          <leafValues>
            3.2090151309967041e-01 -5.8974441140890121e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 780 -9.1902203857898712e-03</internalNodes>
          <leafValues>
            -3.8006910681724548e-01 3.5807169973850250e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 781 3.0834939330816269e-02</internalNodes>
          <leafValues>
            4.0354121476411819e-02 -5.0782901048660278e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 782 -6.4900278812274337e-04</internalNodes>
          <leafValues>
            9.5597133040428162e-02 -1.8812850117683411e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 783 -3.9334357716143131e-03</internalNodes>
          <leafValues>
            -2.0279949903488159e-01 1.0514850169420242e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 784 -2.1477680653333664e-02</internalNodes>
          <leafValues>
            -3.2985571026802063e-01 3.5263378173112869e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 785 -2.7516249567270279e-02</internalNodes>
          <leafValues>
            3.4558650851249695e-01 -7.2544910013675690e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 786 -7.2914459742605686e-03</internalNodes>
          <leafValues>
            1.0051680356264114e-01 -1.3560770452022552e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 787 -5.6135728955268860e-02</internalNodes>
          <leafValues>
            4.0078470110893250e-01 -5.1991838961839676e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 788 1.3679620623588562e-01</internalNodes>
          <leafValues>
            -1.6432780772447586e-02 5.6100088357925415e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 789 -2.4549920111894608e-02</internalNodes>
          <leafValues>
            -1.8187479674816132e-01 1.4125369489192963e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 790 4.6405121684074402e-03</internalNodes>
          <leafValues>
            -1.6500659286975861e-01 1.4912450313568115e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 791 -2.1023359149694443e-02</internalNodes>
          <leafValues>
            -1.9611929357051849e-01 9.9226936697959900e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 792 -4.8856949433684349e-03</internalNodes>
          <leafValues>
            1.1330509930849075e-01 -8.0172486603260040e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 793 -1.7337809503078461e-01</internalNodes>
          <leafValues>
            -8.3458930253982544e-01 2.3691669106483459e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 794 -9.2903972836211324e-04</internalNodes>
          <leafValues>
            8.5904203355312347e-02 -1.0580120235681534e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 795 -1.0562090203166008e-02</internalNodes>
          <leafValues>
            2.6989871263504028e-01 -6.7542143166065216e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 796 1.5071259811520576e-02</internalNodes>
          <leafValues>
            5.8657489717006683e-02 -3.2436290383338928e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 797 -1.8616430461406708e-02</internalNodes>
          <leafValues>
            3.5660719871520996e-01 -5.3099378943443298e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 798 8.4412463009357452e-02</internalNodes>
          <leafValues>
            1.7715929076075554e-02 -4.5803558826446533e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 799 5.1138769835233688e-02</internalNodes>
          <leafValues>
            1.7407679930329323e-02 -9.4110202789306641e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 800 -1.0613460093736649e-02</internalNodes>
          <leafValues>
            -6.0632371902465820e-01 3.0793670564889908e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 801 1.8357619643211365e-02</internalNodes>
          <leafValues>
            -7.7268190681934357e-02 2.9780578613281250e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 802 -8.4444461390376091e-04</internalNodes>
          <leafValues>
            7.8023009002208710e-02 -2.5017648935317993e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 803 -6.2388968653976917e-03</internalNodes>
          <leafValues>
            -4.8017698526382446e-01 3.9185639470815659e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 804 -3.5363171249628067e-02</internalNodes>
          <leafValues>
            -1. 9.3268742784857750e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 805 -7.3558121919631958e-02</internalNodes>
          <leafValues>
            -7.7895337343215942e-01 1.8441500142216682e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 806 -8.7034203112125397e-02</internalNodes>
          <leafValues>
            4.3624061346054077e-01 -1.7716599628329277e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 807 -8.0721646547317505e-02</internalNodes>
          <leafValues>
            2.7296718955039978e-01 -6.6346958279609680e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 808 1.0344590246677399e-01</internalNodes>
          <leafValues>
            9.0693607926368713e-03 -6.6438651084899902e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 809 9.3807540833950043e-03</internalNodes>
          <leafValues>
            7.1242772042751312e-02 -2.7381658554077148e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 810 -7.1806147694587708e-02</internalNodes>
          <leafValues>
            -9.1222041845321655e-01 8.0809993669390678e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 811 -1.9418599549680948e-03</internalNodes>
          <leafValues>
            1.8472340703010559e-01 -1.1344549804925919e-01</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>68</maxWeakCount>
      <stageThreshold>-7.3019427061080933e-01</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 812 3.0328959226608276e-02</internalNodes>
          <leafValues>
            -1.7539510130882263e-01 3.6945340037345886e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 813 -8.2631781697273254e-02</internalNodes>
          <leafValues>
            2.2216479480266571e-01 -8.7577551603317261e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 814 2.5548380799591541e-03</internalNodes>
          <leafValues>
            -1.5091089904308319e-01 1.4608770608901978e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 815 -1.4431839808821678e-03</internalNodes>
          <leafValues>
            6.2405250966548920e-02 -1.8302099406719208e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 816 4.3006289750337601e-02</internalNodes>
          <leafValues>
            8.5711486637592316e-02 -4.4278779625892639e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 817 -1.7748139798641205e-01</internalNodes>
          <leafValues>
            -6.7308551073074341e-01 2.1622380241751671e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 818 9.9723696708679199e-02</internalNodes>
          <leafValues>
            -4.2775660753250122e-02 6.9088941812515259e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 819 -1.7957199364900589e-02</internalNodes>
          <leafValues>
            8.8784933090209961e-02 -2.9352998733520508e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 820 5.8914110995829105e-03</internalNodes>
          <leafValues>
            2.6884179562330246e-02 -3.9257821440696716e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 821 -1.2439199490472674e-03</internalNodes>
          <leafValues>
            8.3695329725742340e-02 -1.3524650037288666e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 822 -6.3109956681728363e-02</internalNodes>
          <leafValues>
            6.8365001678466797e-01 -1.1174580082297325e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 823 5.3107268176972866e-03</internalNodes>
          <leafValues>
            7.3095791041851044e-02 -3.3228519558906555e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 824 -9.6346868667751551e-04</internalNodes>
          <leafValues>
            9.3923456966876984e-02 -2.6014220714569092e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 825 -2.0377680659294128e-02</internalNodes>
          <leafValues>
            2.3682409524917603e-01 -5.1811341196298599e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 826 -1.5610749833285809e-02</internalNodes>
          <leafValues>
            -4.8465269804000854e-01 4.2128730565309525e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 827 4.5497290790081024e-02</internalNodes>
          <leafValues>
            5.7874252088367939e-03 -5.2637368440628052e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 828 -1.2244869954884052e-02</internalNodes>
          <leafValues>
            3.0523040890693665e-01 -7.9311266541481018e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 829 -5.5875871330499649e-03</internalNodes>
          <leafValues>
            7.2504900395870209e-02 -1.0300940275192261e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 830 -1.3237710110843182e-02</internalNodes>
          <leafValues>
            -2.1259979903697968e-01 1.4112070202827454e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 831 -1.6236070543527603e-02</internalNodes>
          <leafValues>
            -3.6822131276130676e-01 1.6904499381780624e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 832 8.7341741891577840e-04</internalNodes>
          <leafValues>
            -1.7513209581375122e-01 1.1717790365219116e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 833 7.8164516016840935e-03</internalNodes>
          <leafValues>
            -4.0935669094324112e-02 3.8136309385299683e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 834 1.4803799786022864e-05</internalNodes>
          <leafValues>
            -1.1581300199031830e-01 1.8054120242595673e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 835 3.6272540688514709e-02</internalNodes>
          <leafValues>
            1.5196749940514565e-02 -4.6037960052490234e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 836 -3.8026720285415649e-03</internalNodes>
          <leafValues>
            1.3440360128879547e-01 -1.6124980151653290e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 837 -1.4585750177502632e-02</internalNodes>
          <leafValues>
            -2.8331491351127625e-01 7.4682116508483887e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 838 1.4677370199933648e-03</internalNodes>
          <leafValues>
            -1.3493220508098602e-01 1.4244909584522247e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 839 -1.3981569558382034e-02</internalNodes>
          <leafValues>
            2.1735540032386780e-01 -5.2886679768562317e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 840 -6.3076039077714086e-04</internalNodes>
          <leafValues>
            1.4901949465274811e-01 -1.3620099425315857e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 841 -1.4475540257990360e-02</internalNodes>
          <leafValues>
            -1.9180099666118622e-01 1.0607130080461502e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 842 -3.2217580825090408e-02</internalNodes>
          <leafValues>
            2.8091669082641602e-01 -8.5046291351318359e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 843 3.4460560418665409e-03</internalNodes>
          <leafValues>
            7.4571870267391205e-02 -2.7108609676361084e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 844 -4.3949890881776810e-02</internalNodes>
          <leafValues>
            4.4002100825309753e-01 -4.5509129762649536e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 845 -1.1966270394623280e-02</internalNodes>
          <leafValues>
            6.3286870718002319e-02 -1.9805380702018738e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 846 -4.3486028909683228e-01</internalNodes>
          <leafValues>
            -7.6205497980117798e-01 2.1508129313588142e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 847 3.9887550473213196e-01</internalNodes>
          <leafValues>
            8.0703729763627052e-03 -8.4284877777099609e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 848 -4.4802378863096237e-02</internalNodes>
          <leafValues>
            -6.8417382240295410e-01 2.2474979981780052e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 849 -1.0935150086879730e-01</internalNodes>
          <leafValues>
            2.1119509637355804e-01 -3.9731640368700027e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 850 3.0923409387469292e-02</internalNodes>
          <leafValues>
            4.4779401272535324e-02 -3.5875031352043152e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 851 1.3285979628562927e-02</internalNodes>
          <leafValues>
            -4.8151660710573196e-02 3.7119218707084656e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 852 -3.9830091409385204e-03</internalNodes>
          <leafValues>
            1.2781530618667603e-01 -1.9959120452404022e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 853 1.4184620231389999e-02</internalNodes>
          <leafValues>
            -3.9896048605442047e-02 2.4085929989814758e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 854 1.6680279513821006e-03</internalNodes>
          <leafValues>
            -1.8107059597969055e-01 9.3981906771659851e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 855 -2.2055890411138535e-02</internalNodes>
          <leafValues>
            -2.8798168897628784e-01 3.0038369819521904e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 856 -6.0371801257133484e-02</internalNodes>
          <leafValues>
            2.9529640078544617e-01 -6.4714096486568451e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 857 5.9291448444128036e-02</internalNodes>
          <leafValues>
            8.4209917113184929e-03 -5.8830922842025757e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 858 3.2637149095535278e-02</internalNodes>
          <leafValues>
            3.2118339091539383e-02 -5.1192921400070190e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 859 -9.8897633142769337e-04</internalNodes>
          <leafValues>
            1.3382619619369507e-01 -1.1545710265636444e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 860 -3.5560440272092819e-02</internalNodes>
          <leafValues>
            -1.5159629285335541e-01 1.0519140213727951e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 861 9.8722549155354500e-03</internalNodes>
          <leafValues>
            9.3462042510509491e-02 -2.5988951325416565e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 862 7.1953269653022289e-03</internalNodes>
          <leafValues>
            -8.6937829852104187e-02 2.8372770547866821e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 863 2.4437099695205688e-02</internalNodes>
          <leafValues>
            -3.9930108934640884e-02 3.9243239164352417e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 864 5.2195340394973755e-03</internalNodes>
          <leafValues>
            4.9804110080003738e-02 -3.1846821308135986e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 865 2.3442960809916258e-03</internalNodes>
          <leafValues>
            -5.4469950497150421e-02 3.3718121051788330e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 866 4.7694300301373005e-03</internalNodes>
          <leafValues>
            7.1476787328720093e-02 -3.1018280982971191e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 867 -1.4517470262944698e-02</internalNodes>
          <leafValues>
            7.8642480075359344e-02 -1.4538839459419250e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 868 4.4710729271173477e-02</internalNodes>
          <leafValues>
            -2.5051780045032501e-02 6.4730519056320190e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 869 1.6867399215698242e-02</internalNodes>
          <leafValues>
            2.9088959097862244e-02 -3.9030238986015320e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 870 -9.0343318879604340e-04</internalNodes>
          <leafValues>
            8.7722577154636383e-02 -1.6588549315929413e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 871 -8.2187339663505554e-02</internalNodes>
          <leafValues>
            -8.4238857030868530e-01 9.8376423120498657e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 872 1.8525390187278390e-03</internalNodes>
          <leafValues>
            -1.2251490354537964e-01 1.2000189721584320e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 873 -9.3228723853826523e-03</internalNodes>
          <leafValues>
            7.8422851860523224e-02 -1.3231949508190155e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 874 2.2730689495801926e-02</internalNodes>
          <leafValues>
            -3.3696789294481277e-02 4.4383940100669861e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 875 1.0286659747362137e-01</internalNodes>
          <leafValues>
            1.7917430028319359e-02 -5.8341610431671143e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 876 -9.9547371268272400e-02</internalNodes>
          <leafValues>
            -9.5365560054779053e-01 1.2582040391862392e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 877 1.6412759199738503e-02</internalNodes>
          <leafValues>
            1.6067119315266609e-02 -4.1402378678321838e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 878 -2.5932409334927797e-03</internalNodes>
          <leafValues>
            5.2763499319553375e-02 -3.0404600501060486e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 879 9.5953093841671944e-03</internalNodes>
          <leafValues>
            8.3528086543083191e-02 -1.1780069768428802e-01</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>66</maxWeakCount>
      <stageThreshold>-6.8558442592620850e-01</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 880 -3.5430109500885010e-01</internalNodes>
          <leafValues>
            3.1792920827865601e-01 -1.8512800335884094e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 881 -1.4761329628527164e-02</internalNodes>
          <leafValues>
            3.4065079689025879e-01 -8.6621738970279694e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 882 -1.1580450087785721e-01</internalNodes>
          <leafValues>
            -7.2353202104568481e-01 3.4404840320348740e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 883 -4.4705160689773038e-05</internalNodes>
          <leafValues>
            8.2497082650661469e-02 -2.1311110258102417e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 884 -5.8883379097096622e-05</internalNodes>
          <leafValues>
            1.0809300094842911e-01 -1.8269860744476318e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 885 3.7944849580526352e-02</internalNodes>
          <leafValues>
            -2.4756550788879395e-02 4.5866918563842773e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 886 -2.1807940211147070e-03</internalNodes>
          <leafValues>
            1.5783859789371490e-01 -1.7752459645271301e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 887 -4.5430101454257965e-02</internalNodes>
          <leafValues>
            -3.7249541282653809e-01 5.7393261231482029e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 888 1.9972559530287981e-03</internalNodes>
          <leafValues>
            -1.9175310432910919e-01 1.1995170265436172e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 889 -2.2458820239990018e-05</internalNodes>
          <leafValues>
            9.1529168188571930e-02 -1.3080990314483643e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 890 -3.7994279991835356e-03</internalNodes>
          <leafValues>
            -2.0454970002174377e-01 1.4146579802036285e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 891 -2.7970419614575803e-04</internalNodes>
          <leafValues>
            1.1078160256147385e-01 -1.8713960051536560e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 892 -3.9631421677768230e-03</internalNodes>
          <leafValues>
            -3.7749990820884705e-01 5.6935790926218033e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 893 -1.4290240360423923e-03</internalNodes>
          <leafValues>
            -1.9449859857559204e-01 9.8834916949272156e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 894 2.1182179450988770e-02</internalNodes>
          <leafValues>
            -8.7030410766601562e-02 2.8888610005378723e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 895 8.7332521798089147e-04</internalNodes>
          <leafValues>
            -1.1729159951210022e-01 1.2506540119647980e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 896 2.6135759428143501e-02</internalNodes>
          <leafValues>
            -3.9572428911924362e-02 6.2252640724182129e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 897 4.3046330101788044e-03</internalNodes>
          <leafValues>
            1.1582309752702713e-01 -1.9618239998817444e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 898 1.5224959934130311e-03</internalNodes>
          <leafValues>
            -1.8586060404777527e-01 1.1688389629125595e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 899 -7.4201932875439525e-04</internalNodes>
          <leafValues>
            9.8724737763404846e-02 -2.5791341066360474e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 900 -2.5593061000108719e-03</internalNodes>
          <leafValues>
            1.7307940125465393e-01 -1.2067069858312607e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 901 -9.5563217997550964e-02</internalNodes>
          <leafValues>
            3.4646418690681458e-01 -1.3142139650881290e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 902 1.3280790299177170e-02</internalNodes>
          <leafValues>
            1.2056879699230194e-01 -2.0627740025520325e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 903 1.8245529383420944e-02</internalNodes>
          <leafValues>
            -6.7242950201034546e-02 4.6858128160238266e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 904 -6.1288971453905106e-02</internalNodes>
          <leafValues>
            -6.6364967823028564e-01 2.9319150373339653e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 905 -2.6133419945836067e-02</internalNodes>
          <leafValues>
            2.0848380029201508e-01 -2.7202930301427841e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 906 -3.2300818711519241e-02</internalNodes>
          <leafValues>
            -6.2726408243179321e-01 3.0091879889369011e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 907 5.0284489989280701e-02</internalNodes>
          <leafValues>
            1.5047290362417698e-03 -5.9630411863327026e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 908 -1.8137119710445404e-02</internalNodes>
          <leafValues>
            2.9262909293174744e-01 -6.9213449954986572e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 909 1.0980300139635801e-03</internalNodes>
          <leafValues>
            1.0316859930753708e-01 -1.6558070480823517e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 910 3.9596110582351685e-03</internalNodes>
          <leafValues>
            -5.7063579559326172e-02 3.3744910359382629e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 911 3.1622028909623623e-03</internalNodes>
          <leafValues>
            8.8302358984947205e-02 -2.7917590737342834e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 912 8.4337368607521057e-03</internalNodes>
          <leafValues>
            8.6311057209968567e-02 -2.5153660774230957e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 913 2.3408479988574982e-02</internalNodes>
          <leafValues>
            -3.7011519074440002e-02 2.5571560859680176e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 914 -1.9710899796336889e-03</internalNodes>
          <leafValues>
            1.4960870146751404e-01 -1.3213759660720825e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 915 -3.1434781849384308e-02</internalNodes>
          <leafValues>
            2.7072909474372864e-01 -2.4784140288829803e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 916 -2.0984669681638479e-03</internalNodes>
          <leafValues>
            -2.2842940688133240e-01 9.2392489314079285e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 917 -1.0477580130100250e-01</internalNodes>
          <leafValues>
            1.3740949332714081e-01 -5.8604940772056580e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 918 1.2558500282466412e-02</internalNodes>
          <leafValues>
            9.4428263604640961e-02 -2.3187640309333801e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 919 2.6465631090104580e-03</internalNodes>
          <leafValues>
            -2.0493589341640472e-01 9.2889577150344849e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 920 2.8069379925727844e-01</internalNodes>
          <leafValues>
            4.0848400443792343e-02 -4.6177521347999573e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 921 -4.5882318168878555e-02</internalNodes>
          <leafValues>
            -7.1715551614761353e-01 9.1696027666330338e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 922 -1.3070689747110009e-03</internalNodes>
          <leafValues>
            1.6250529885292053e-01 -1.1437030136585236e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 923 6.8374760448932648e-03</internalNodes>
          <leafValues>
            -6.7564792931079865e-02 2.1927219629287720e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 924 -5.8329561725258827e-03</internalNodes>
          <leafValues>
            -3.5843908786773682e-01 5.7467628270387650e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 925 -4.0936999022960663e-02</internalNodes>
          <leafValues>
            -5.5129498243331909e-01 1.3819620013237000e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 926 1.8727440387010574e-02</internalNodes>
          <leafValues>
            -5.2844639867544174e-02 3.4427130222320557e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 927 1.0303989984095097e-03</internalNodes>
          <leafValues>
            -9.4872146844863892e-02 1.1235869675874710e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 928 -2.6228028582409024e-04</internalNodes>
          <leafValues>
            6.3875511288642883e-02 -3.0397358536720276e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 929 -2.6861110702157021e-02</internalNodes>
          <leafValues>
            1.7592920362949371e-01 -6.2506988644599915e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 930 3.1061280518770218e-02</internalNodes>
          <leafValues>
            -7.2171129286289215e-02 3.1532520055770874e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 931 -7.1269841864705086e-03</internalNodes>
          <leafValues>
            -1.2540310621261597e-01 1.0068179666996002e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 932 -2.7709340676665306e-02</internalNodes>
          <leafValues>
            -8.0085551738739014e-01 2.5742180645465851e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 933 4.2209450155496597e-02</internalNodes>
          <leafValues>
            2.7846070006489754e-02 -5.6140202283859253e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 934 6.2995860353112221e-03</internalNodes>
          <leafValues>
            1.0806919634342194e-01 -2.0114520192146301e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 935 2.0048789680004120e-02</internalNodes>
          <leafValues>
            -5.8164618909358978e-02 1.8885469436645508e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 936 -7.8481709351763129e-05</internalNodes>
          <leafValues>
            8.2995712757110596e-02 -2.1331989765167236e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 937 -8.9945547282695770e-02</internalNodes>
          <leafValues>
            -7.9307717084884644e-01 7.8350491821765900e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 938 7.7181761153042316e-03</internalNodes>
          <leafValues>
            4.1435040533542633e-02 -3.7721860408782959e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 939 5.3638177923858166e-03</internalNodes>
          <leafValues>
            -9.3567937612533569e-02 1.4666350185871124e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 940 1.4555330388247967e-02</internalNodes>
          <leafValues>
            -5.6989211589097977e-02 3.4367969632148743e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 941 1.0583730041980743e-01</internalNodes>
          <leafValues>
            3.0579300597310066e-02 -5.8684998750686646e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 942 2.7123570907860994e-04</internalNodes>
          <leafValues>
            8.5480518639087677e-02 -2.2808749973773956e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 943 -7.3196433484554291e-02</internalNodes>
          <leafValues>
            -5.1212561130523682e-01 9.6583841368556023e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 944 8.3729642210528255e-04</internalNodes>
          <leafValues>
            -1.7978319525718689e-01 1.4117470383644104e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 945 1.9459549803286791e-03</internalNodes>
          <leafValues>
            8.7605938315391541e-02 -2.0442050695419312e-01</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>78</maxWeakCount>
      <stageThreshold>-3.0717300415039062e+01</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 946 -8.5505366325378418e-02</internalNodes>
          <leafValues>
            2.6714649796485901e-01 -1.8152849376201630e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 947 -3.7014279514551163e-02</internalNodes>
          <leafValues>
            3.7405461072921753e-01 -7.0312701165676117e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 948 1.6834780573844910e-02</internalNodes>
          <leafValues>
            8.9160107076168060e-02 -2.4566100537776947e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 949 9.7268886747770011e-05</internalNodes>
          <leafValues>
            -1.9830940663814545e-01 1.4981469511985779e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 950 5.2984068170189857e-03</internalNodes>
          <leafValues>
            -1.5779909491539001e-01 1.7095419764518738e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 951 -2.3770859465003014e-02</internalNodes>
          <leafValues>
            -2.5096279382705688e-01 3.2790731638669968e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 952 -1.4852959662675858e-02</internalNodes>
          <leafValues>
            2.7263158559799194e-01 -7.2188302874565125e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 953 -8.2722969353199005e-02</internalNodes>
          <leafValues>
            -6.6801771521568298e-02 1.3384120166301727e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 954 6.4472708618268371e-04</internalNodes>
          <leafValues>
            -1.9309680163860321e-01 1.3628469407558441e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 955 -4.3215509504079819e-04</internalNodes>
          <leafValues>
            5.7426910847425461e-02 -7.2983436286449432e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 956 -7.5133621066925116e-06</internalNodes>
          <leafValues>
            1.2174469977617264e-01 -1.8166640400886536e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 957 2.0493609830737114e-02</internalNodes>
          <leafValues>
            -6.1657600104808807e-02 3.8570550084114075e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 958 -5.9959441423416138e-03</internalNodes>
          <leafValues>
            -1.8091249465942383e-01 1.1791180074214935e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 959 -9.3910521268844604e-01</internalNodes>
          <leafValues>
            3.1374409794807434e-01 -5.9216298162937164e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 960 -2.4341490119695663e-02</internalNodes>
          <leafValues>
            -3.7053358554840088e-01 5.5251110345125198e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 961 -7.6796777546405792e-02</internalNodes>
          <leafValues>
            1.3754889369010925e-01 -5.8201938867568970e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 962 -8.2179326564073563e-03</internalNodes>
          <leafValues>
            -2.5679248571395874e-01 9.9195696413516998e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 963 -5.1702618598937988e-02</internalNodes>
          <leafValues>
            -5.2937638759613037e-01 2.7275180444121361e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 964 6.3065597787499428e-03</internalNodes>
          <leafValues>
            -1.0400679707527161e-01 2.0388899743556976e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 965 3.6337040364742279e-02</internalNodes>
          <leafValues>
            1.3178840279579163e-02 -3.8717061281204224e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 966 -2.7929339557886124e-03</internalNodes>
          <leafValues>
            1.2351000308990479e-01 -2.0460779964923859e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 967 -1.4435379765927792e-02</internalNodes>
          <leafValues>
            -5.0111377239227295e-01 3.7262540310621262e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 968 6.4411992207169533e-03</internalNodes>
          <leafValues>
            -6.0557190328836441e-02 3.0578470230102539e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 969 -1.2598140165209770e-03</internalNodes>
          <leafValues>
            5.3200751543045044e-02 -1.6916200518608093e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 970 -6.9105648435652256e-03</internalNodes>
          <leafValues>
            -3.6398649215698242e-01 4.2843151837587357e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 971 -5.2663110196590424e-02</internalNodes>
          <leafValues>
            4.4169178605079651e-01 -3.2096829265356064e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 972 -4.0925059467554092e-02</internalNodes>
          <leafValues>
            -5.5673360824584961e-01 2.9191689565777779e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 973 -2.1683140657842159e-03</internalNodes>
          <leafValues>
            6.6585853695869446e-02 -1.1715179681777954e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 974 1.7480919137597084e-02</internalNodes>
          <leafValues>
            -6.7747853696346283e-02 3.4224361181259155e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 975 1.3032980263233185e-01</internalNodes>
          <leafValues>
            1.0853439569473267e-02 -5.9894740581512451e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 976 5.1362451631575823e-04</internalNodes>
          <leafValues>
            -1.8810969591140747e-01 1.0938909649848938e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 977 -3.8764420896768570e-02</internalNodes>
          <leafValues>
            -2.6928341388702393e-01 2.0156569778919220e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 978 -4.8952922224998474e-03</internalNodes>
          <leafValues>
            -2.3670850694179535e-01 7.0693537592887878e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 979 8.4380611777305603e-02</internalNodes>
          <leafValues>
            -6.1777111142873764e-02 1.5130819380283356e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 980 -5.4832860827445984e-02</internalNodes>
          <leafValues>
            -4.9945160746574402e-01 3.5915810614824295e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 981 -5.4148300550878048e-03</internalNodes>
          <leafValues>
            8.2116909325122833e-02 -1.3672749698162079e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 982 1.2813720107078552e-01</internalNodes>
          <leafValues>
            -3.9755281060934067e-02 6.0340911149978638e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 983 -4.4217561371624470e-03</internalNodes>
          <leafValues>
            -7.4642613530158997e-02 1.0235700011253357e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 984 -7.1978997766564135e-06</internalNodes>
          <leafValues>
            7.4595592916011810e-02 -2.9046559333801270e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 985 7.3321886360645294e-02</internalNodes>
          <leafValues>
            -2.1364469081163406e-02 6.9809699058532715e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 986 -2.2566469386219978e-02</internalNodes>
          <leafValues>
            -5.3714770078659058e-01 3.6509968340396881e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 987 -2.9338080435991287e-02</internalNodes>
          <leafValues>
            1.0626199841499329e-01 -3.1652290374040604e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 988 1.3684090226888657e-02</internalNodes>
          <leafValues>
            -5.7709541171789169e-02 3.0355650186538696e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 989 -8.2646618830040097e-04</internalNodes>
          <leafValues>
            1.2958580255508423e-01 -1.3603089749813080e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 990 3.9828647859394550e-03</internalNodes>
          <leafValues>
            5.0734668970108032e-02 -3.3896729350090027e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 991 -2.0535979419946671e-02</internalNodes>
          <leafValues>
            2.6028490066528320e-01 -7.2259396314620972e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 992 -1.4932189881801605e-01</internalNodes>
          <leafValues>
            -5.4172599315643311e-01 4.4534388929605484e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 993 -1.7894789576530457e-02</internalNodes>
          <leafValues>
            4.7149929404258728e-01 -3.0801070854067802e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 994 4.7443818766623735e-04</internalNodes>
          <leafValues>
            -1.9686989486217499e-01 1.2433020025491714e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 995 -4.0598851628601551e-03</internalNodes>
          <leafValues>
            1.4028669893741608e-01 -4.7751329839229584e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 996 -1.1755799874663353e-02</internalNodes>
          <leafValues>
            -2.6237910985946655e-01 5.9933070093393326e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 997 -1.8559649586677551e-02</internalNodes>
          <leafValues>
            1.0493250191211700e-01 -3.2159261405467987e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 998 3.4838409628719091e-03</internalNodes>
          <leafValues>
            7.9499892890453339e-02 -2.0486010611057281e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 999 -6.2133308500051498e-02</internalNodes>
          <leafValues>
            -3.5091090202331543e-01 1.2265560217201710e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1000 -4.4008668512105942e-02</internalNodes>
          <leafValues>
            2.6838389039039612e-01 -8.8284887373447418e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1001 3.0750890728086233e-03</internalNodes>
          <leafValues>
            -4.5581929385662079e-02 1.9343300163745880e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1002 -8.9865371584892273e-02</internalNodes>
          <leafValues>
            -4.8605358600616455e-01 4.5101881027221680e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1003 -1.6210540197789669e-03</internalNodes>
          <leafValues>
            8.7722256779670715e-02 -1.6689349710941315e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1004 -2.9370939359068871e-02</internalNodes>
          <leafValues>
            -4.2794701457023621e-01 4.5566789805889130e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1005 -8.5921816527843475e-02</internalNodes>
          <leafValues>
            -6.9077378511428833e-01 1.5122929587960243e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1006 6.7258282797411084e-04</internalNodes>
          <leafValues>
            -1.1166089773178101e-01 1.5630759298801422e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1007 1.7752440180629492e-03</internalNodes>
          <leafValues>
            -4.5409418642520905e-02 7.7933087944984436e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1008 1.5036190234241076e-05</internalNodes>
          <leafValues>
            -1.6349479556083679e-01 1.0864420235157013e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1009 1.8150300020352006e-03</internalNodes>
          <leafValues>
            9.6329912543296814e-02 -1.1818060278892517e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1010 -6.7588366568088531e-02</internalNodes>
          <leafValues>
            2.2657020390033722e-01 -9.0492926537990570e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1011 1.8347490578889847e-02</internalNodes>
          <leafValues>
            1.6350140795111656e-02 -4.4877880811691284e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1012 -1.0822510346770287e-02</internalNodes>
          <leafValues>
            -4.9622350931167603e-01 4.0703330188989639e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1013 1.7427999526262283e-02</internalNodes>
          <leafValues>
            -3.5475689917802811e-02 3.0856430530548096e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1014 -7.8753121197223663e-02</internalNodes>
          <leafValues>
            -6.7144078016281128e-01 2.6170469820499420e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1015 7.3261657962575555e-04</internalNodes>
          <leafValues>
            -1.0309589654207230e-01 6.4503982663154602e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1016 2.8185009956359863e-02</internalNodes>
          <leafValues>
            -5.5124811828136444e-02 3.1133919954299927e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1017 -1.5536470338702202e-02</internalNodes>
          <leafValues>
            -8.5527300834655762e-02 4.9024209380149841e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1018 -2.6290729641914368e-02</internalNodes>
          <leafValues>
            -6.5267199277877808e-01 2.4495759978890419e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1019 -6.8586082197725773e-03</internalNodes>
          <leafValues>
            -5.8548830449581146e-02 2.8735989332199097e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1020 -3.0750960577279329e-03</internalNodes>
          <leafValues>
            8.6425736546516418e-02 -2.2627249360084534e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1021 5.6799430400133133e-02</internalNodes>
          <leafValues>
            2.9048459604382515e-02 -3.6798200011253357e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1022 3.7182599306106567e-02</internalNodes>
          <leafValues>
            -3.5062279552221298e-02 4.5094621181488037e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1023 -3.5590359475463629e-03</internalNodes>
          <leafValues>
            -1.7892469465732574e-01 6.8459518253803253e-02</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>77</maxWeakCount>
      <stageThreshold>-3.0740200042724609e+01</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 1024 -5.8595160953700542e-03</internalNodes>
          <leafValues>
            2.0132589340209961e-01 -2.6587140560150146e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1025 -5.9507137537002563e-01</internalNodes>
          <leafValues>
            3.6134061217308044e-01 -1.2203159928321838e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1026 4.1726600378751755e-02</internalNodes>
          <leafValues>
            -5.2889000624418259e-02 3.9082470536231995e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1027 4.7253750264644623e-02</internalNodes>
          <leafValues>
            1.4923909679055214e-02 -5.0544148683547974e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1028 9.8612194415181875e-04</internalNodes>
          <leafValues>
            -2.0337739586830139e-01 1.1030670255422592e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1029 -7.2683179751038551e-03</internalNodes>
          <leafValues>
            -2.0899240672588348e-01 1.4733150601387024e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1030 -2.9695410281419754e-02</internalNodes>
          <leafValues>
            6.6190290451049805e-01 -6.7257620394229889e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1031 -1.3097229599952698e-01</internalNodes>
          <leafValues>
            1.7485789954662323e-01 -8.1029571592807770e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1032 1.7316760495305061e-02</internalNodes>
          <leafValues>
            -4.8908680677413940e-02 4.6843668818473816e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1033 -1.0221409797668457e-01</internalNodes>
          <leafValues>
            -2.2275149822235107e-01 7.7479638159275055e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1034 2.9453460592776537e-03</internalNodes>
          <leafValues>
            3.9738278836011887e-02 -2.8107449412345886e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1035 -4.5425590127706528e-02</internalNodes>
          <leafValues>
            2.4193780124187469e-01 1.3621949590742588e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1036 2.2699350956827402e-03</internalNodes>
          <leafValues>
            -1.6247589886188507e-01 1.6063609719276428e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1037 1.1421869695186615e-01</internalNodes>
          <leafValues>
            1.5750480815768242e-02 -5.7382887601852417e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1038 -4.1054069995880127e-02</internalNodes>
          <leafValues>
            3.0522629618644714e-01 -5.5898960679769516e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1039 1.1980540119111538e-02</internalNodes>
          <leafValues>
            1.7477169632911682e-02 -4.0707069635391235e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1040 1.2105259811505675e-03</internalNodes>
          <leafValues>
            -1.7840960621833801e-01 1.0353209823369980e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1041 -2.2351980209350586e-02</internalNodes>
          <leafValues>
            -4.7567600011825562e-01 3.7311390042304993e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1042 2.2135479375720024e-02</internalNodes>
          <leafValues>
            -5.4137628525495529e-02 4.2861071228981018e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1043 -1.5875579789280891e-02</internalNodes>
          <leafValues>
            6.6373616456985474e-02 -1.6455489397048950e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1044 6.0371369123458862e-02</internalNodes>
          <leafValues>
            3.8663931190967560e-02 -4.6496200561523438e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1045 -5.1881238818168640e-02</internalNodes>
          <leafValues>
            -5.6141299009323120e-01 5.4471958428621292e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1046 1.9330360228195786e-03</internalNodes>
          <leafValues>
            -1.3475979864597321e-01 1.3747330009937286e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1047 -4.3940469622612000e-03</internalNodes>
          <leafValues>
            -9.3405917286872864e-02 3.5123821347951889e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1048 -5.2314151078462601e-02</internalNodes>
          <leafValues>
            7.5311762094497681e-01 -2.9210770502686501e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1049 -5.6897811591625214e-02</internalNodes>
          <leafValues>
            -9.1858989000320435e-01 2.8862420469522476e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1050 -2.1614639461040497e-01</internalNodes>
          <leafValues>
            -1. 6.9490820169448853e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1051 1.8479259312152863e-01</internalNodes>
          <leafValues>
            -8.8357992470264435e-02 1.9002689421176910e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1052 -5.6834658607840538e-03</internalNodes>
          <leafValues>
            -1.7791560292243958e-01 9.8286077380180359e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1053 -8.2448042929172516e-02</internalNodes>
          <leafValues>
            -3.4058651328086853e-01 1.5612719580531120e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1054 -7.5926659628748894e-03</internalNodes>
          <leafValues>
            2.5929468870162964e-01 -6.9370441138744354e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1055 -2.9748380184173584e-03</internalNodes>
          <leafValues>
            5.4534178227186203e-02 -1.2630839645862579e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1056 -1.6377970576286316e-01</internalNodes>
          <leafValues>
            -8.3725690841674805e-01 2.2446790710091591e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1057 -3.8845320232212543e-03</internalNodes>
          <leafValues>
            -2.1008059382438660e-01 9.1814376413822174e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1058 -5.5496331304311752e-02</internalNodes>
          <leafValues>
            5.2739220857620239e-01 -3.8561638444662094e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1059 4.5041809789836407e-03</internalNodes>
          <leafValues>
            3.8907989859580994e-02 -2.1077489852905273e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1060 5.7516310364007950e-02</internalNodes>
          <leafValues>
            -5.4442461580038071e-02 3.4977319836616516e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1061 -5.4960879497230053e-03</internalNodes>
          <leafValues>
            1.0459329932928085e-01 -2.2956989705562592e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1062 5.8753142366185784e-04</internalNodes>
          <leafValues>
            7.4045538902282715e-02 -2.3731130361557007e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1063 1.1216119676828384e-01</internalNodes>
          <leafValues>
            -2.5916000828146935e-02 1.1389470100402832e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1064 2.1753750741481781e-01</internalNodes>
          <leafValues>
            1.9727870821952820e-02 -9.6220922470092773e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1065 -1.4632700476795435e-03</internalNodes>
          <leafValues>
            -9.4052821397781372e-02 6.4389176666736603e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1066 -8.6313979700207710e-03</internalNodes>
          <leafValues>
            2.5036060810089111e-01 -7.2234652936458588e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1067 -1.9858509302139282e-02</internalNodes>
          <leafValues>
            -1.2698090076446533e-01 7.9051487147808075e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1068 -1.3804109767079353e-04</internalNodes>
          <leafValues>
            1.4466640353202820e-01 -1.1444070190191269e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1069 2.6781240478157997e-02</internalNodes>
          <leafValues>
            1.7647750675678253e-02 -8.3157891035079956e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1070 1.9331119954586029e-02</internalNodes>
          <leafValues>
            -4.5500081032514572e-02 5.0110948085784912e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1071 4.1692070662975311e-02</internalNodes>
          <leafValues>
            2.2502349689602852e-02 -3.8992220163345337e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1072 1.1296980082988739e-01</internalNodes>
          <leafValues>
            -3.2494839280843735e-02 5.3929620981216431e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1073 3.1683610286563635e-03</internalNodes>
          <leafValues>
            -1.7195589840412140e-01 9.3619801104068756e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1074 5.3966748528182507e-03</internalNodes>
          <leafValues>
            5.7677630335092545e-02 -3.0436149239540100e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1075 -1.3829180598258972e-01</internalNodes>
          <leafValues>
            -5.2158790826797485e-01 1.8444910645484924e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1076 -1.2594119645655155e-02</internalNodes>
          <leafValues>
            2.2748909890651703e-01 -6.9325000047683716e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1077 -1.6514480113983154e-02</internalNodes>
          <leafValues>
            1.6279229521751404e-01 -3.4446150064468384e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1078 -1.6392849385738373e-02</internalNodes>
          <leafValues>
            -1.4277680218219757e-01 1.6290099918842316e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1079 -3.4606490284204483e-02</internalNodes>
          <leafValues>
            -4.0356379747390747e-01 8.3033805713057518e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1080 -6.8894061259925365e-03</internalNodes>
          <leafValues>
            2.6890090107917786e-01 -6.9450862705707550e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1081 -1.1879400350153446e-02</internalNodes>
          <leafValues>
            2.1395209431648254e-01 -2.0930450409650803e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1082 -1.9165100529789925e-03</internalNodes>
          <leafValues>
            6.8464219570159912e-02 -3.1453219056129456e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1083 1.3729350175708532e-03</internalNodes>
          <leafValues>
            -6.0340028256177902e-02 2.7572840452194214e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1084 2.4278028868138790e-03</internalNodes>
          <leafValues>
            -2.3944500088691711e-01 8.4658838808536530e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1085 2.1290169097483158e-03</internalNodes>
          <leafValues>
            8.6938478052616119e-02 -2.8218480944633484e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1086 -5.2569470426533371e-05</internalNodes>
          <leafValues>
            1.3682359457015991e-01 -1.1980649828910828e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1087 1.5957899391651154e-02</internalNodes>
          <leafValues>
            -3.9610300213098526e-02 2.4825170636177063e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1088 8.9294081553816795e-03</internalNodes>
          <leafValues>
            8.1123508512973785e-02 -2.6561570167541504e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1089 4.9925308674573898e-02</internalNodes>
          <leafValues>
            1.5018629841506481e-02 -3.6647871136665344e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1090 -1.7374839633703232e-02</internalNodes>
          <leafValues>
            3.3971020579338074e-01 -5.4494149982929230e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1091 -7.8357063233852386e-02</internalNodes>
          <leafValues>
            -4.9435839056968689e-01 8.4990533068776131e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1092 -8.9894477277994156e-03</internalNodes>
          <leafValues>
            -2.3209859430789948e-01 7.1379087865352631e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1093 -1.5932919923216105e-03</internalNodes>
          <leafValues>
            8.2504719495773315e-02 -9.3123182654380798e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1094 2.6272730901837349e-03</internalNodes>
          <leafValues>
            -1.3213430345058441e-01 1.3099829852581024e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1095 -5.9108160436153412e-02</internalNodes>
          <leafValues>
            -3.7229761481285095e-01 4.5574661344289780e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1096 3.5086690913885832e-03</internalNodes>
          <leafValues>
            8.9478462934494019e-02 -1.8543410301208496e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1097 1.5465220436453819e-02</internalNodes>
          <leafValues>
            -3.0604820698499680e-02 2.0754580199718475e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1098 -1.1749019846320152e-02</internalNodes>
          <leafValues>
            3.9200168848037720e-01 -4.1100859642028809e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1099 4.8413608223199844e-02</internalNodes>
          <leafValues>
            3.7391050718724728e-03 -8.5701841115951538e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1100 -1.1499889660626650e-03</internalNodes>
          <leafValues>
            -2.2441549599170685e-01 7.1305088698863983e-02</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>89</maxWeakCount>
      <stageThreshold>-3.0760700225830078e+01</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 1101 -3.2420051097869873e-01</internalNodes>
          <leafValues>
            4.1447758674621582e-01 -1.0684230178594589e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1102 -2.1065689623355865e-01</internalNodes>
          <leafValues>
            2.3302809894084930e-01 -9.4695799052715302e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1103 -2.1540550515055656e-02</internalNodes>
          <leafValues>
            -2.8891721367835999e-01 7.0666067302227020e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1104 5.9726871550083160e-03</internalNodes>
          <leafValues>
            -9.0559490025043488e-02 2.2989599406719208e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1105 2.6468100026249886e-02</internalNodes>
          <leafValues>
            -5.0254050642251968e-02 3.9346438646316528e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1106 -7.2531126439571381e-02</internalNodes>
          <leafValues>
            -3.9421468973159790e-01 7.5547359883785248e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1107 -4.3684918433427811e-02</internalNodes>
          <leafValues>
            -5.7553547620773315e-01 5.1893319934606552e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1108 1.1670660227537155e-01</internalNodes>
          <leafValues>
            -2.5791339576244354e-03 -8.2597649097442627e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1109 -8.2381166517734528e-02</internalNodes>
          <leafValues>
            7.5818961858749390e-01 -2.6576930657029152e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1110 -2.3157079704105854e-03</internalNodes>
          <leafValues>
            6.6858686506748199e-02 -3.0407869815826416e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1111 -1.6678189858794212e-02</internalNodes>
          <leafValues>
            3.8525319099426270e-01 -4.8842679709196091e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1112 -3.0678999610245228e-03</internalNodes>
          <leafValues>
            -2.7150988578796387e-01 6.4561262726783752e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1113 -8.3884904161095619e-03</internalNodes>
          <leafValues>
            -2.8267300128936768e-01 7.0778891444206238e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1114 2.1357910707592964e-02</internalNodes>
          <leafValues>
            -6.6106483340263367e-02 3.1867539882659912e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1115 -4.0636979974806309e-03</internalNodes>
          <leafValues>
            1.1739840358495712e-01 -1.5105929970741272e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1116 -1.1475679930299520e-03</internalNodes>
          <leafValues>
            6.4262896776199341e-02 -7.4472077190876007e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1117 1.8145689740777016e-02</internalNodes>
          <leafValues>
            -5.6946009397506714e-02 4.2107149958610535e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1118 5.0288350321352482e-03</internalNodes>
          <leafValues>
            8.3866670727729797e-02 -3.3929398655891418e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1119 -5.7916361838579178e-02</internalNodes>
          <leafValues>
            4.5170179009437561e-01 -4.3198868632316589e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1120 3.1025299802422523e-02</internalNodes>
          <leafValues>
            2.8000740334391594e-02 -1.6818940639495850e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1121 8.2134291529655457e-02</internalNodes>
          <leafValues>
            1.9999530166387558e-02 -7.6910507678985596e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1122 7.3666572570800781e-02</internalNodes>
          <leafValues>
            -1.2391459895297885e-03 -1.0004559755325317e+00</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1123 1.5681830700486898e-04</internalNodes>
          <leafValues>
            -1.2154590338468552e-01 1.3561969995498657e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1124 4.5130930840969086e-02</internalNodes>
          <leafValues>
            4.7123869881033897e-03 -2.9671049118041992e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1125 -5.1468348829075694e-04</internalNodes>
          <leafValues>
            1.4606890082359314e-01 -1.3600480556488037e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1126 -1.4981119893491268e-02</internalNodes>
          <leafValues>
            -1.7933659255504608e-01 5.3928699344396591e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1127 -2.7151789516210556e-02</internalNodes>
          <leafValues>
            -6.7529010772705078e-01 2.3046780377626419e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1128 -6.6578023135662079e-02</internalNodes>
          <leafValues>
            -6.5586429834365845e-01 4.7667929902672768e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1129 -3.3119178842753172e-03</internalNodes>
          <leafValues>
            1.2255000323057175e-01 -1.6333930194377899e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1130 -1.5811180695891380e-02</internalNodes>
          <leafValues>
            -4.4731178879737854e-01 8.9029967784881592e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1131 -5.6757620768621564e-05</internalNodes>
          <leafValues>
            1.4944350719451904e-01 -1.0686829686164856e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1132 1.0602490045130253e-02</internalNodes>
          <leafValues>
            2.1685829386115074e-02 -3.2208129763603210e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1133 2.1245649550110102e-03</internalNodes>
          <leafValues>
            -2.0425739884376526e-01 8.2330957055091858e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1134 4.7638580203056335e-02</internalNodes>
          <leafValues>
            -3.2728441059589386e-02 4.4726258516311646e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1135 -1.1300199665129185e-02</internalNodes>
          <leafValues>
            2.5546020269393921e-01 -6.9969899952411652e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1136 -1.1472209589555860e-03</internalNodes>
          <leafValues>
            4.7467790544033051e-02 -2.2220790386199951e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1137 1.8008640035986900e-02</internalNodes>
          <leafValues>
            -6.0860209167003632e-02 2.9082441329956055e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1138 -1.1634260416030884e-02</internalNodes>
          <leafValues>
            -3.1474921107292175e-01 8.3630897104740143e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1139 6.5580541267991066e-03</internalNodes>
          <leafValues>
            -1.2121830135583878e-01 1.3124500215053558e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1140 -2.3253620602190495e-03</internalNodes>
          <leafValues>
            -8.7138622999191284e-02 7.0476517081260681e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1141 2.1486220881342888e-02</internalNodes>
          <leafValues>
            -3.5936549305915833e-02 4.3737021088600159e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1142 1.2589399516582489e-01</internalNodes>
          <leafValues>
            1.2443150393664837e-02 -9.2822617292404175e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1143 -2.2191529569681734e-04</internalNodes>
          <leafValues>
            6.9798342883586884e-02 -3.2106238603591919e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1144 -5.8175198733806610e-02</internalNodes>
          <leafValues>
            -7.7025629580020905e-02 9.6747986972332001e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1145 -4.5887380838394165e-04</internalNodes>
          <leafValues>
            1.1412449926137924e-01 -1.4719170331954956e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1146 -4.0837019681930542e-02</internalNodes>
          <leafValues>
            4.7654581069946289e-01 -4.9737568944692612e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1147 -9.7786840051412582e-03</internalNodes>
          <leafValues>
            -2.0513780415058136e-01 8.4468983113765717e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1148 2.7964261174201965e-01</internalNodes>
          <leafValues>
            -3.0034869909286499e-02 6.9526249170303345e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1149 -8.8869117200374603e-02</internalNodes>
          <leafValues>
            2.4081839621067047e-01 -7.0576377213001251e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1150 -1.4095460064709187e-02</internalNodes>
          <leafValues>
            -1.0456439852714539e-01 4.6604979783296585e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1151 2.6836670003831387e-03</internalNodes>
          <leafValues>
            6.0495968908071518e-02 -2.5784969329833984e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1152 8.7051279842853546e-02</internalNodes>
          <leafValues>
            -2.4173669517040253e-02 2.4043059349060059e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1153 -1.0178039781749249e-02</internalNodes>
          <leafValues>
            2.5469788908958435e-01 -9.2890508472919464e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1154 -9.0314531698822975e-03</internalNodes>
          <leafValues>
            -2.6343479752540588e-01 7.0848807692527771e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1155 -6.7082298919558525e-03</internalNodes>
          <leafValues>
            2.3313470184803009e-01 -7.6271809637546539e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1156 -6.7614473402500153e-02</internalNodes>
          <leafValues>
            -5.2013260126113892e-01 1.3785160146653652e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1157 -3.9636880159378052e-01</internalNodes>
          <leafValues>
            -7.6267188787460327e-01 2.0686520263552666e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1158 1.2813470093533397e-03</internalNodes>
          <leafValues>
            -1.4046239852905273e-01 1.2711919844150543e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1159 8.4416065365076065e-03</internalNodes>
          <leafValues>
            7.4712827801704407e-02 -2.5663131475448608e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1160 1.4749030015082099e-05</internalNodes>
          <leafValues>
            -1.4015120267868042e-01 1.5210489928722382e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1161 -4.5073211193084717e-02</internalNodes>
          <leafValues>
            -6.4262861013412476e-01 2.5925450026988983e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1162 7.7068619430065155e-03</internalNodes>
          <leafValues>
            3.2485689967870712e-02 -2.0377029478549957e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1163 5.9383822372183204e-04</internalNodes>
          <leafValues>
            -1.2950329482555389e-01 1.6219380497932434e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1164 -1.3042639475315809e-03</internalNodes>
          <leafValues>
            8.6318843066692352e-02 -1.9224709272384644e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1165 6.4417850226163864e-03</internalNodes>
          <leafValues>
            -7.1506053209304810e-02 3.0627349019050598e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1166 -1.5630330890417099e-02</internalNodes>
          <leafValues>
            4.9515549093484879e-02 -1.4840349555015564e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1167 1.1395620182156563e-02</internalNodes>
          <leafValues>
            6.3355296850204468e-02 -2.5576409697532654e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1168 4.7544430941343307e-02</internalNodes>
          <leafValues>
            4.8167328350245953e-03 -7.8987777233123779e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1169 8.3856023848056793e-03</internalNodes>
          <leafValues>
            -4.3012011796236038e-02 4.1108319163322449e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1170 -1.6369849909096956e-03</internalNodes>
          <leafValues>
            8.2473292946815491e-02 -7.8956812620162964e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1171 -1.6513109207153320e-02</internalNodes>
          <leafValues>
            -5.0692492723464966e-01 3.9071910083293915e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1172 1.0358359664678574e-01</internalNodes>
          <leafValues>
            2.0772270858287811e-02 -6.9371747970581055e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1173 3.3361840993165970e-02</internalNodes>
          <leafValues>
            -4.4479008764028549e-02 4.6392819285392761e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1174 -2.8664430603384972e-02</internalNodes>
          <leafValues>
            -4.5883670449256897e-01 3.5676170140504837e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1175 -1.1209170043002814e-04</internalNodes>
          <leafValues>
            8.4344513714313507e-02 -2.1555650234222412e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1176 1.7690200358629227e-02</internalNodes>
          <leafValues>
            9.7461966797709465e-03 -8.5261541604995728e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1177 -2.1878469735383987e-02</internalNodes>
          <leafValues>
            2.6345950365066528e-01 -7.0220641791820526e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1178 -1.2424430251121521e-01</internalNodes>
          <leafValues>
            -2.8659409284591675e-01 2.1816140040755272e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1179 6.5736092627048492e-02</internalNodes>
          <leafValues>
            2.3600580170750618e-02 -7.0263791084289551e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1180 -4.4633701443672180e-02</internalNodes>
          <leafValues>
            -9.5776432752609253e-01 3.5877549089491367e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1181 -6.4271576702594757e-02</internalNodes>
          <leafValues>
            6.0099518299102783e-01 -2.8557619079947472e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1182 5.6516240874771029e-05</internalNodes>
          <leafValues>
            -1.3485489785671234e-01 1.1080929636955261e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1183 1.3419260503724217e-03</internalNodes>
          <leafValues>
            9.8325006663799286e-02 -1.6883499920368195e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1184 -2.1889729425311089e-02</internalNodes>
          <leafValues>
            -2.1880550682544708e-01 2.9620679095387459e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1185 -1.9670790061354637e-03</internalNodes>
          <leafValues>
            9.7642809152603149e-02 -1.8062870204448700e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1186 -7.6196521520614624e-02</internalNodes>
          <leafValues>
            -8.6387622356414795e-01 7.3730680160224438e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1187 -7.9841358819976449e-04</internalNodes>
          <leafValues>
            1.5353679656982422e-01 -1.2105809897184372e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1188 -8.2246732199564576e-04</internalNodes>
          <leafValues>
            4.0794339030981064e-02 -1.3737790286540985e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1189 -3.0324649997055531e-03</internalNodes>
          <leafValues>
            1.2088210135698318e-01 -1.4088730514049530e-01</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>107</maxWeakCount>
      <stageThreshold>-3.0838300704956055e+01</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 1190 -5.2718650549650192e-02</internalNodes>
          <leafValues>
            2.5985679030418396e-01 -1.5721979737281799e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1191 5.1614670082926750e-03</internalNodes>
          <leafValues>
            -1.0271859914064407e-01 5.9346981346607208e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1192 6.7699067294597626e-02</internalNodes>
          <leafValues>
            -7.7311262488365173e-02 2.8602010011672974e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1193 -3.3822011202573776e-02</internalNodes>
          <leafValues>
            -5.6999057531356812e-01 4.0684528648853302e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1194 -5.3746398538351059e-02</internalNodes>
          <leafValues>
            -4.7421398758888245e-01 6.2751591205596924e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1195 -3.0559560284018517e-02</internalNodes>
          <leafValues>
            7.1638780832290649e-01 -1.7423950135707855e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1196 -3.3822011202573776e-02</internalNodes>
          <leafValues>
            -6.7283177375793457e-01 -1.2177439639344811e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1197 2.7876009698957205e-04</internalNodes>
          <leafValues>
            -7.0205226540565491e-02 1.1648730188608170e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1198 -2.5016230065375566e-03</internalNodes>
          <leafValues>
            1.2915210425853729e-01 -1.3576079905033112e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1199 9.0835839509963989e-02</internalNodes>
          <leafValues>
            4.1303969919681549e-03 4.0111660957336426e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1200 -2.5603260844945908e-02</internalNodes>
          <leafValues>
            -1.0059480369091034e-01 1.8819159269332886e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1201 -5.2134461700916290e-02</internalNodes>
          <leafValues>
            2.5282728672027588e-01 -1.1447659879922867e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1202 3.8462068885564804e-02</internalNodes>
          <leafValues>
            5.5828869342803955e-02 -5.7635480165481567e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1203 -1.4195869443938136e-03</internalNodes>
          <leafValues>
            4.5769099146127701e-02 -1.6001120209693909e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1204 -7.6488167047500610e-02</internalNodes>
          <leafValues>
            -5.2531337738037109e-01 5.2011650055646896e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1205 1.2786199804395437e-03</internalNodes>
          <leafValues>
            7.6051406562328339e-02 -2.5104090571403503e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1206 -1.2661969522014260e-03</internalNodes>
          <leafValues>
            -1.2411650270223618e-01 1.6375949978828430e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1207 -9.0841390192508698e-03</internalNodes>
          <leafValues>
            2.2613930702209473e-01 -5.4559618234634399e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1208 7.4418167059775442e-05</internalNodes>
          <leafValues>
            -1.6488799452781677e-01 1.0864400118589401e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1209 -2.5643699336796999e-03</internalNodes>
          <leafValues>
            -1.8933239579200745e-01 1.0298830270767212e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1210 -3.4997228533029556e-02</internalNodes>
          <leafValues>
            2.3746269941329956e-01 -8.2390688359737396e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1211 -1.9422829151153564e-02</internalNodes>
          <leafValues>
            -9.9691540002822876e-02 4.0376558899879456e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1212 -5.9601478278636932e-02</internalNodes>
          <leafValues>
            -9.1162431240081787e-01 1.8367420881986618e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1213 3.4046408534049988e-01</internalNodes>
          <leafValues>
            6.0519641265273094e-03 -4.4584161043167114e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1214 6.5878271125257015e-03</internalNodes>
          <leafValues>
            -9.5767751336097717e-02 1.8087559938430786e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1215 5.3841830231249332e-03</internalNodes>
          <leafValues>
            5.2658561617136002e-02 -4.5202389359474182e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1216 7.9094972461462021e-03</internalNodes>
          <leafValues>
            3.8064301013946533e-02 -4.5984381437301636e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1217 -1.7566539347171783e-02</internalNodes>
          <leafValues>
            1.1139140278100967e-01 -2.9564509168267250e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1218 -1.1352599831297994e-03</internalNodes>
          <leafValues>
            1.0825510323047638e-01 -1.8355409801006317e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1219 1.4237280189990997e-01</internalNodes>
          <leafValues>
            -3.1995229423046112e-02 3.8099318742752075e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1220 -1.0024409741163254e-01</internalNodes>
          <leafValues>
            -7.7461862564086914e-01 2.3992599919438362e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1221 -1.2453799694776535e-01</internalNodes>
          <leafValues>
            2.1255059540271759e-01 -9.1748759150505066e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1222 1.9641380012035370e-01</internalNodes>
          <leafValues>
            3.3028271049261093e-02 -6.0223150253295898e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1223 -4.1467338800430298e-02</internalNodes>
          <leafValues>
            -8.8264447450637817e-01 1.3399540446698666e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1224 -3.0020199716091156e-02</internalNodes>
          <leafValues>
            5.8158951997756958e-01 -3.9801310747861862e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1225 1.9002150744199753e-02</internalNodes>
          <leafValues>
            -2.4508230388164520e-02 3.2259100675582886e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1226 -1.0837280191481113e-02</internalNodes>
          <leafValues>
            -2.5428688526153564e-01 7.3384523391723633e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1227 -2.4493860080838203e-02</internalNodes>
          <leafValues>
            1.4883559942245483e-01 -3.6729950457811356e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1228 4.7652618959546089e-03</internalNodes>
          <leafValues>
            1.2693640589714050e-01 -1.9157619774341583e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1229 -1.2438010424375534e-02</internalNodes>
          <leafValues>
            7.1727007627487183e-02 -2.5421911478042603e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1230 2.1275319159030914e-02</internalNodes>
          <leafValues>
            -4.9392588436603546e-02 5.2715432643890381e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1231 -6.7369833588600159e-02</internalNodes>
          <leafValues>
            -4.6891281008720398e-01 4.2881548404693604e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1232 -1.0925510432571173e-03</internalNodes>
          <leafValues>
            1.1250150203704834e-01 -1.3688379526138306e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1233 -9.7863428294658661e-02</internalNodes>
          <leafValues>
            -8.5167092084884644e-01 7.9745445400476456e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1234 -2.0980979315936565e-03</internalNodes>
          <leafValues>
            7.2556197643280029e-02 -2.1253560483455658e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1235 4.4975668191909790e-02</internalNodes>
          <leafValues>
            -6.4254011958837509e-03 6.7334640026092529e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1236 -2.0970530807971954e-02</internalNodes>
          <leafValues>
            -1.5341369807720184e-01 1.1229439824819565e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1237 7.1862142067402601e-04</internalNodes>
          <leafValues>
            -1.3690039515495300e-01 1.2323109805583954e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1238 1.1921999976038933e-02</internalNodes>
          <leafValues>
            -5.2036911249160767e-02 3.5095539689064026e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1239 -1.2956890277564526e-02</internalNodes>
          <leafValues>
            8.7813578546047211e-02 -2.8173919767141342e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1240 -2.7972649782896042e-02</internalNodes>
          <leafValues>
            -5.9018450975418091e-01 2.4770129472017288e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1241 -6.0088839381933212e-03</internalNodes>
          <leafValues>
            -6.5963357686996460e-02 3.6277290433645248e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1242 -4.0854439139366150e-03</internalNodes>
          <leafValues>
            1.8211939930915833e-01 -8.9567668735980988e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1243 6.3200960867106915e-03</internalNodes>
          <leafValues>
            2.3888850584626198e-02 -1.0606460273265839e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1244 2.0633619278669357e-02</internalNodes>
          <leafValues>
            -3.8176801055669785e-02 5.2134162187576294e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1245 -2.5221719406545162e-03</internalNodes>
          <leafValues>
            4.6510368585586548e-02 -9.3957871198654175e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1246 -4.6648699790239334e-03</internalNodes>
          <leafValues>
            -2.3734979331493378e-01 8.0608420073986053e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1247 2.5844529736787081e-03</internalNodes>
          <leafValues>
            -2.4275559931993484e-02 2.2888250648975372e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1248 -1.4966880371503066e-05</internalNodes>
          <leafValues>
            9.9380202591419220e-02 -1.9830170273780823e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1249 6.2676537781953812e-03</internalNodes>
          <leafValues>
            -7.4367232620716095e-02 2.2790339589118958e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1250 2.6347549632191658e-02</internalNodes>
          <leafValues>
            1.9285459071397781e-02 -8.8683319091796875e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1251 -6.0268949717283249e-02</internalNodes>
          <leafValues>
            1.2562690675258636e-01 -3.3716868609189987e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1252 -3.8371770642697811e-03</internalNodes>
          <leafValues>
            -1.7735309898853302e-01 8.8588736951351166e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1253 -3.5063549876213074e-03</internalNodes>
          <leafValues>
            -8.7100908160209656e-02 5.6650858372449875e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1254 -8.1536881625652313e-03</internalNodes>
          <leafValues>
            2.5863811373710632e-01 -5.9690609574317932e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1255 3.8574129343032837e-02</internalNodes>
          <leafValues>
            8.4148198366165161e-03 -4.3409061431884766e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1256 -3.9269659668207169e-02</internalNodes>
          <leafValues>
            3.5469511151313782e-01 -4.3248169124126434e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1257 -1.7512469785287976e-03</internalNodes>
          <leafValues>
            8.6816087365150452e-02 -9.6924632787704468e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1258 -8.4061250090599060e-02</internalNodes>
          <leafValues>
            -6.5256571769714355e-01 2.4765320122241974e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1259 -4.3417539447546005e-02</internalNodes>
          <leafValues>
            -5.6205427646636963e-01 9.8713487386703491e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1260 -1.3643169775605202e-02</internalNodes>
          <leafValues>
            2.4562139809131622e-01 -6.0552708804607391e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1261 1.6490360721945763e-02</internalNodes>
          <leafValues>
            3.8866888731718063e-02 -2.7715849876403809e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1262 -1.4422900043427944e-02</internalNodes>
          <leafValues>
            -2.2820469737052917e-01 5.9026841074228287e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1263 2.7178740128874779e-03</internalNodes>
          <leafValues>
            -1.1887180060148239e-01 1.2192229926586151e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1264 6.3701239414513111e-03</internalNodes>
          <leafValues>
            -1.7167779803276062e-01 9.9555417895317078e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1265 8.1290200352668762e-02</internalNodes>
          <leafValues>
            -2.2509740665555000e-02 2.4472869932651520e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1266 -1.4793650188948959e-04</internalNodes>
          <leafValues>
            8.0845691263675690e-02 -2.1680369973182678e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1267 -6.9097941741347313e-04</internalNodes>
          <leafValues>
            6.2281239777803421e-02 -1.4082409441471100e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1268 -1.1455359868705273e-02</internalNodes>
          <leafValues>
            -1.1722529679536819e-01 1.5948510169982910e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1269 -1.6334399580955505e-01</internalNodes>
          <leafValues>
            -3.4727150201797485e-01 1.1003250256180763e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1270 -6.8652302026748657e-02</internalNodes>
          <leafValues>
            2.5441581010818481e-01 -7.8778758645057678e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1271 6.9226641207933426e-03</internalNodes>
          <leafValues>
            -2.9800569638609886e-02 2.0455279946327209e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1272 -1.0851600021123886e-01</internalNodes>
          <leafValues>
            -4.7375029325485229e-01 4.0704440325498581e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1273 5.8868151158094406e-02</internalNodes>
          <leafValues>
            1.3014429714530706e-03 -1.0001180171966553e+00</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1274 1.5332780312746763e-03</internalNodes>
          <leafValues>
            -1.6441990435123444e-01 9.9495269358158112e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1275 -2.5576220359653234e-03</internalNodes>
          <leafValues>
            8.1458933651447296e-02 -9.0945683419704437e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1276 3.6009950563311577e-03</internalNodes>
          <leafValues>
            8.6760893464088440e-02 -1.9872209429740906e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1277 1.0986080393195152e-02</internalNodes>
          <leafValues>
            -4.8230320215225220e-02 1.9264499843120575e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1278 -4.4403300853446126e-04</internalNodes>
          <leafValues>
            2.0115670561790466e-01 -8.3059810101985931e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1279 2.9464240651577711e-04</internalNodes>
          <leafValues>
            -1.2808699905872345e-01 6.6652536392211914e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1280 -4.1320081800222397e-02</internalNodes>
          <leafValues>
            -5.3510922193527222e-01 2.9578590765595436e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1281 8.1929996609687805e-02</internalNodes>
          <leafValues>
            -1.6939610242843628e-02 7.6524221897125244e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1282 1.4758399687707424e-02</internalNodes>
          <leafValues>
            2.7206780388951302e-02 -6.2607800960540771e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1283 -1.7577099800109863e-01</internalNodes>
          <leafValues>
            1.0328330099582672e-01 -5.1863618195056915e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1284 -1.0492449626326561e-02</internalNodes>
          <leafValues>
            -1.9424819946289062e-01 8.5835307836532593e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1285 -5.6793028488755226e-03</internalNodes>
          <leafValues>
            1.6252349317073822e-01 -1.1607410013675690e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1286 -7.7026091516017914e-02</internalNodes>
          <leafValues>
            -1.6585369408130646e-01 1.0487639904022217e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1287 8.8255241513252258e-02</internalNodes>
          <leafValues>
            -4.2857029475271702e-03 1.0002230405807495e+00</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1288 -2.5600788649171591e-04</internalNodes>
          <leafValues>
            1.3218410313129425e-01 -1.4754749834537506e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1289 3.4532468765974045e-02</internalNodes>
          <leafValues>
            -4.7874059528112411e-02 2.7708581089973450e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1290 1.0978250205516815e-01</internalNodes>
          <leafValues>
            -2.1606300026178360e-02 8.5059100389480591e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1291 3.6717768758535385e-02</internalNodes>
          <leafValues>
            1.6276430338621140e-02 -8.9000707864761353e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1292 -6.1206728219985962e-02</internalNodes>
          <leafValues>
            5.4838019609451294e-01 -3.1625121831893921e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1293 2.9046889394521713e-03</internalNodes>
          <leafValues>
            4.1483800858259201e-02 -8.6054533720016479e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1294 6.9003179669380188e-02</internalNodes>
          <leafValues>
            -2.6552880182862282e-02 6.0647368431091309e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1295 7.0049421628937125e-04</internalNodes>
          <leafValues>
            -1.9934299588203430e-01 7.5443200767040253e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1296 3.4873239696025848e-02</internalNodes>
          <leafValues>
            3.9036870002746582e-02 -4.2251279950141907e-01</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>71</maxWeakCount>
      <stageThreshold>-3.0640199661254883e+01</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 1297 5.4466608911752701e-02</internalNodes>
          <leafValues>
            -1.3182820379734039e-01 2.7660441398620605e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1298 -2.1856650710105896e-02</internalNodes>
          <leafValues>
            2.5475510954856873e-01 -8.4045611321926117e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1299 6.6198781132698059e-03</internalNodes>
          <leafValues>
            7.1489393711090088e-02 -2.6304081082344055e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1300 8.8211596012115479e-03</internalNodes>
          <leafValues>
            -1.3396710157394409e-01 1.4222930371761322e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1301 -2.3251229524612427e-01</internalNodes>
          <leafValues>
            -3.4628748893737793e-01 5.6767478585243225e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1302 2.8472349047660828e-01</internalNodes>
          <leafValues>
            8.6089121177792549e-03 -1.0012650489807129e+00</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1303 4.2303521186113358e-02</internalNodes>
          <leafValues>
            -9.1637752950191498e-02 1.9090470671653748e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1304 4.9781981855630875e-02</internalNodes>
          <leafValues>
            2.9709989205002785e-02 -3.5961869359016418e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1305 -4.8924300819635391e-02</internalNodes>
          <leafValues>
            -3.8387179374694824e-01 5.5182989686727524e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1306 -7.7399803558364511e-05</internalNodes>
          <leafValues>
            -1.2758800387382507e-01 9.4793520867824554e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1307 -2.4455290287733078e-02</internalNodes>
          <leafValues>
            4.6911829710006714e-01 -5.1782071590423584e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1308 2.5210820138454437e-02</internalNodes>
          <leafValues>
            4.4035088270902634e-02 -1.7653049528598785e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1309 -4.7570910304784775e-02</internalNodes>
          <leafValues>
            -5.3332722187042236e-01 4.6693909913301468e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1310 -1.4046980440616608e-01</internalNodes>
          <leafValues>
            3.2798460125923157e-01 -6.5607719123363495e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1311 -1.0932429879903793e-01</internalNodes>
          <leafValues>
            -5.9276747703552246e-01 3.0543249100446701e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1312 -9.8567470908164978e-02</internalNodes>
          <leafValues>
            3.6753898859024048e-01 -6.6568426787853241e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1313 -7.6861098408699036e-02</internalNodes>
          <leafValues>
            -1.3722559809684753e-01 1.7806069552898407e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1314 -2.1035360172390938e-02</internalNodes>
          <leafValues>
            4.3632039427757263e-01 -2.9524799436330795e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1315 1.3428479433059692e-03</internalNodes>
          <leafValues>
            -2.4420669674873352e-01 1.1969459801912308e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1316 -3.4433171153068542e-02</internalNodes>
          <leafValues>
            2.7110278606414795e-01 -7.5950436294078827e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1317 1.7944410210475326e-03</internalNodes>
          <leafValues>
            -1.7997020483016968e-01 1.3508750498294830e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1318 -9.6644267439842224e-02</internalNodes>
          <leafValues>
            -7.6689988374710083e-01 1.5435869805514812e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1319 2.5092919822782278e-03</internalNodes>
          <leafValues>
            -1.2506179511547089e-01 1.8814159929752350e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1320 -2.2511319257318974e-03</internalNodes>
          <leafValues>
            7.8268818557262421e-02 -7.2636753320693970e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1321 -7.4670952017186210e-06</internalNodes>
          <leafValues>
            7.6933227479457855e-02 -2.6148709654808044e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1322 2.6573959738016129e-02</internalNodes>
          <leafValues>
            2.2534679621458054e-02 -1.6299429535865784e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1323 1.7086470499634743e-02</internalNodes>
          <leafValues>
            -5.8232828974723816e-02 3.6095941066741943e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1324 3.0147018842399120e-03</internalNodes>
          <leafValues>
            1.2817589938640594e-01 -1.8230159580707550e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1325 9.4206426292657852e-03</internalNodes>
          <leafValues>
            8.9825786650180817e-02 -2.6877298951148987e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1326 7.5143040157854557e-04</internalNodes>
          <leafValues>
            8.8295407593250275e-02 -2.3304849863052368e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1327 -1.0687969624996185e-02</internalNodes>
          <leafValues>
            3.0612778663635254e-01 -6.5760366618633270e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1328 7.5001686811447144e-02</internalNodes>
          <leafValues>
            4.3955240398645401e-03 -7.5094991922378540e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1329 5.0849020481109619e-02</internalNodes>
          <leafValues>
            2.0524559542536736e-02 -8.3406442403793335e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1330 2.3555630818009377e-02</internalNodes>
          <leafValues>
            3.6320169456303120e-03 -8.8322782516479492e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1331 -1.6827480867505074e-02</internalNodes>
          <leafValues>
            -6.5697771310806274e-01 2.3138659074902534e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1332 1.9977349787950516e-02</internalNodes>
          <leafValues>
            -2.3847330361604691e-02 3.2636478543281555e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1333 3.1397528946399689e-02</internalNodes>
          <leafValues>
            -3.6343611776828766e-02 4.4792640209197998e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1334 -9.3282759189605713e-02</internalNodes>
          <leafValues>
            -5.2942079305648804e-01 6.3824458047747612e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1335 -7.7012612018734217e-04</internalNodes>
          <leafValues>
            1.5420450270175934e-01 -1.5751419961452484e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1336 4.6891491860151291e-02</internalNodes>
          <leafValues>
            1.1802299879491329e-02 -7.3092728853225708e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1337 -3.4607138950377703e-03</internalNodes>
          <leafValues>
            1.1565960198640823e-01 -1.7568419873714447e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1338 -3.3493418246507645e-02</internalNodes>
          <leafValues>
            -6.8049472570419312e-01 5.1433579064905643e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1339 -5.5793918669223785e-02</internalNodes>
          <leafValues>
            -5.3908890485763550e-01 3.2008830457925797e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1340 5.1339478231966496e-03</internalNodes>
          <leafValues>
            -6.6114626824855804e-02 3.1760030984878540e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1341 3.0386429280042648e-03</internalNodes>
          <leafValues>
            8.1462718546390533e-02 -2.4291920661926270e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1342 -3.1149981077760458e-04</internalNodes>
          <leafValues>
            4.6723391860723495e-02 -8.4542676806449890e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1343 1.8326110439375043e-03</internalNodes>
          <leafValues>
            -1.2830300629138947e-01 1.5127150714397430e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1344 -2.5878880172967911e-02</internalNodes>
          <leafValues>
            -2.1160699427127838e-01 2.9811259359121323e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1345 -1.3985199620947242e-03</internalNodes>
          <leafValues>
            1.9801080226898193e-01 -1.0368689894676208e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1346 2.4663188960403204e-03</internalNodes>
          <leafValues>
            2.4554869160056114e-02 -1.0830429941415787e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1347 -1.3155230553820729e-03</internalNodes>
          <leafValues>
            -2.1984469890594482e-01 9.3965977430343628e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1348 -1.0562440007925034e-01</internalNodes>
          <leafValues>
            -7.9747790098190308e-01 8.9689819142222404e-03</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1349 -3.0508160125464201e-03</internalNodes>
          <leafValues>
            1.3266490399837494e-01 -1.3734680414199829e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1350 2.9857279732823372e-02</internalNodes>
          <leafValues>
            9.6069881692528725e-03 -3.0116540193557739e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1351 3.0972119420766830e-02</internalNodes>
          <leafValues>
            3.0091350898146629e-02 -5.7279831171035767e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1352 1.0772749781608582e-01</internalNodes>
          <leafValues>
            -1.1804240057244897e-03 -9.9987578392028809e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1353 -5.1501881331205368e-02</internalNodes>
          <leafValues>
            2.7181380987167358e-01 -6.8161502480506897e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1354 -2.5288289412856102e-02</internalNodes>
          <leafValues>
            4.5067310333251953e-01 -1.6520980745553970e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1355 -4.2859618552029133e-03</internalNodes>
          <leafValues>
            3.7213888764381409e-01 -4.9761738628149033e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1356 -2.3194460198283195e-02</internalNodes>
          <leafValues>
            -2.0697650313377380e-01 4.1071210056543350e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1357 1.6878530383110046e-02</internalNodes>
          <leafValues>
            5.6408129632472992e-02 -3.7614488601684570e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1358 -2.9601169750094414e-02</internalNodes>
          <leafValues>
            2.7207991480827332e-01 -7.3090076446533203e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1359 -1.0797269642353058e-01</internalNodes>
          <leafValues>
            -4.9193540215492249e-01 3.6118570715188980e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1360 2.5317850708961487e-01</internalNodes>
          <leafValues>
            8.8794529438018799e-03 -3.4746390581130981e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1361 -7.5927868485450745e-02</internalNodes>
          <leafValues>
            -5.2568101882934570e-01 3.0029149726033211e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1362 3.5496079362928867e-03</internalNodes>
          <leafValues>
            6.1817318201065063e-02 -2.3450049757957458e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1363 -1.0419470258057117e-02</internalNodes>
          <leafValues>
            9.5470182597637177e-02 -1.9764930009841919e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1364 -1.6242120414972305e-02</internalNodes>
          <leafValues>
            3.5856780409812927e-01 -5.2510499954223633e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1365 -1.4503370039165020e-03</internalNodes>
          <leafValues>
            -1.8003490567207336e-01 9.5208331942558289e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1366 1.9696209579706192e-02</internalNodes>
          <leafValues>
            3.7537660449743271e-02 -4.8065909743309021e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1367 3.4964820370078087e-03</internalNodes>
          <leafValues>
            -9.7187377512454987e-02 1.7569050192832947e-01</leafValues></_></weakClassifiers></_>
    <_>
      <maxWeakCount>96</maxWeakCount>
      <stageThreshold>-3.0804899215698242e+01</stageThreshold>
      <weakClassifiers>
        <_>
          <internalNodes>
            0 -1 1368 -1.4011229574680328e-01</internalNodes>
          <leafValues>
            3.5787770152091980e-01 -1.2125530093908310e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1369 -1.0008949786424637e-02</internalNodes>
          <leafValues>
            2.6330929994583130e-01 -8.9008018374443054e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1370 -1.1394180357456207e-02</internalNodes>
          <leafValues>
            4.3228828907012939e-01 -5.0159178674221039e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1371 2.3134359717369080e-01</internalNodes>
          <leafValues>
            6.3841762021183968e-03 -7.0292097330093384e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1372 1.2646619975566864e-01</internalNodes>
          <leafValues>
            4.2768001556396484e-02 -4.3919000029563904e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1373 4.6616248786449432e-02</internalNodes>
          <leafValues>
            1.9250590354204178e-02 5.4499799013137817e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1374 2.2037800401449203e-02</internalNodes>
          <leafValues>
            -8.5108749568462372e-02 3.3848780393600464e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1375 3.1345561146736145e-02</internalNodes>
          <leafValues>
            2.2690940648317337e-02 -5.1671189069747925e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1376 -2.1140639483928680e-01</internalNodes>
          <leafValues>
            2.9412490129470825e-01 -4.6479560434818268e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1377 -6.6334113478660583e-02</internalNodes>
          <leafValues>
            -1.3444049656391144e-01 1.2842020392417908e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1378 4.0738668292760849e-02</internalNodes>
          <leafValues>
            2.3405810818076134e-02 -8.0233561992645264e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1379 -4.1470870375633240e-02</internalNodes>
          <leafValues>
            1.4620569348335266e-01 -1.9590210169553757e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1380 1.8456790596246719e-02</internalNodes>
          <leafValues>
            -3.6185469478368759e-02 5.1238268613815308e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1381 3.7538509350270033e-03</internalNodes>
          <leafValues>
            -1.5587760508060455e-01 1.0312390327453613e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1382 -2.8798980638384819e-03</internalNodes>
          <leafValues>
            -1.2225770205259323e-01 1.7551769316196442e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1383 -3.2762341201305389e-02</internalNodes>
          <leafValues>
            -4.7169759869575500e-01 3.0380319803953171e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1384 -3.9022210985422134e-02</internalNodes>
          <leafValues>
            3.5106760263442993e-01 -6.6119261085987091e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1385 -4.4674798846244812e-02</internalNodes>
          <leafValues>
            -3.9958310127258301e-01 2.1066389977931976e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1386 5.3343027830123901e-03</internalNodes>
          <leafValues>
            7.9137377440929413e-02 -2.1176779270172119e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1387 1.5521169640123844e-02</internalNodes>
          <leafValues>
            3.4438930451869965e-02 -5.7202047109603882e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1388 -8.0842437455430627e-04</internalNodes>
          <leafValues>
            1.1951749771833420e-01 -1.4325830340385437e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1389 2.7754740789532661e-02</internalNodes>
          <leafValues>
            -3.2436888664960861e-02 3.0749228596687317e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1390 -3.4786630421876907e-03</internalNodes>
          <leafValues>
            1.5688750147819519e-01 -1.5649950504302979e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1391 -2.7840979397296906e-02</internalNodes>
          <leafValues>
            -1.2932580709457397e-01 1.5408019721508026e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1392 -2.0033390319440514e-04</internalNodes>
          <leafValues>
            1.0591139644384384e-01 -2.3829479515552521e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1393 6.3352532684803009e-02</internalNodes>
          <leafValues>
            -3.5057701170444489e-02 1.1119090020656586e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1394 -1.0634259879589081e-01</internalNodes>
          <leafValues>
            -6.7938178777694702e-01 2.7465900406241417e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1395 1.9035820150747895e-04</internalNodes>
          <leafValues>
            -1.1908160150051117e-01 1.1334689706563950e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1396 -1.3564240187406540e-02</internalNodes>
          <leafValues>
            2.7505800127983093e-01 -6.8315982818603516e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1397 2.1096229553222656e-02</internalNodes>
          <leafValues>
            -1.0987949557602406e-02 3.9935430884361267e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1398 -2.4880920536816120e-03</internalNodes>
          <leafValues>
            -2.1849539875984192e-01 8.9293807744979858e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1399 1.2370670214295387e-02</internalNodes>
          <leafValues>
            -9.5645450055599213e-02 5.6633960455656052e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1400 -1.2036350369453430e-01</internalNodes>
          <leafValues>
            -5.3174102306365967e-01 3.5775080323219299e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1401 -6.7138060927391052e-02</internalNodes>
          <leafValues>
            2.1456840634346008e-01 -8.7389126420021057e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1402 -1.2161920219659805e-01</internalNodes>
          <leafValues>
            -1.8160809576511383e-01 1.4573550224304199e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1403 2.0479459315538406e-02</internalNodes>
          <leafValues>
            -5.5715341120958328e-02 6.1189219355583191e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1404 2.1847079042345285e-03</internalNodes>
          <leafValues>
            -9.5258213579654694e-02 2.0591090619564056e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1405 4.0952740237116814e-03</internalNodes>
          <leafValues>
            -1.1867360025644302e-01 4.6696461737155914e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1406 -3.5035728942602873e-03</internalNodes>
          <leafValues>
            2.3321969807147980e-01 -7.5537599623203278e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1407 -1.0467019863426685e-02</internalNodes>
          <leafValues>
            -1.2448009848594666e-01 5.0595261156558990e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1408 -1.5020829625427723e-02</internalNodes>
          <leafValues>
            9.1991908848285675e-02 -2.2077399492263794e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1409 4.4499050825834274e-02</internalNodes>
          <leafValues>
            3.4101899713277817e-02 -5.3422772884368896e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1410 8.1879837671294808e-04</internalNodes>
          <leafValues>
            -1.9193440675735474e-01 1.0177730023860931e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1411 -2.9793549329042435e-02</internalNodes>
          <leafValues>
            4.1442748904228210e-01 -2.0298149436712265e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1412 1.6614329069852829e-02</internalNodes>
          <leafValues>
            1.0457099974155426e-01 -1.8352369964122772e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1413 -2.2510789334774017e-02</internalNodes>
          <leafValues>
            1.8911230564117432e-01 -3.3867038786411285e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1414 2.0407250151038170e-02</internalNodes>
          <leafValues>
            -5.8524370193481445e-02 3.5967621207237244e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1415 3.0294319149106741e-03</internalNodes>
          <leafValues>
            -1.4031639695167542e-01 5.4849781095981598e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1416 5.8518280275166035e-04</internalNodes>
          <leafValues>
            9.5523588359355927e-02 -1.9650359451770782e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1417 1.7756339162588120e-02</internalNodes>
          <leafValues>
            1.6195869073271751e-02 -5.8534300327301025e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1418 -3.2687620259821415e-03</internalNodes>
          <leafValues>
            -3.0802598595619202e-01 6.5568111836910248e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1419 3.4140530042350292e-03</internalNodes>
          <leafValues>
            -8.2502417266368866e-02 9.9890269339084625e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1420 6.3527207821607590e-03</internalNodes>
          <leafValues>
            -3.5163778811693192e-02 5.4237622022628784e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1421 2.0045090932399035e-03</internalNodes>
          <leafValues>
            -1.0081720352172852e-01 9.6935041248798370e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1422 6.9825910031795502e-03</internalNodes>
          <leafValues>
            -1.6012389957904816e-01 1.1348509788513184e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1423 4.5963011682033539e-02</internalNodes>
          <leafValues>
            6.1929170042276382e-03 -8.8551759719848633e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1424 3.7062391638755798e-02</internalNodes>
          <leafValues>
            2.0128250122070312e-02 -8.0933511257171631e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1425 -4.1522808372974396e-02</internalNodes>
          <leafValues>
            2.0597919821739197e-01 -3.1927939504384995e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1426 1.6521860659122467e-01</internalNodes>
          <leafValues>
            2.5524839758872986e-02 -6.2951612472534180e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1427 -2.3188880085945129e-01</internalNodes>
          <leafValues>
            1.3953979313373566e-01 -6.1611790210008621e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1428 -2.8150070458650589e-02</internalNodes>
          <leafValues>
            -1.3676370680332184e-01 1.1677569895982742e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1429 2.0499450620263815e-03</internalNodes>
          <leafValues>
            -1.5855039656162262e-01 1.3511709868907928e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1430 1.2636490282602608e-04</internalNodes>
          <leafValues>
            -1.5024340152740479e-01 1.3739089667797089e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1431 2.4286638945341110e-03</internalNodes>
          <leafValues>
            7.9247459769248962e-02 -2.5959441065788269e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1432 -2.1873589605093002e-02</internalNodes>
          <leafValues>
            3.5590508580207825e-01 -6.1835918575525284e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1433 -5.8419788256287575e-03</internalNodes>
          <leafValues>
            -1.0219120234251022e-01 3.9997130632400513e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1434 -2.6236099656671286e-03</internalNodes>
          <leafValues>
            1.2129990011453629e-01 -1.4861150085926056e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1435 1.4590419828891754e-01</internalNodes>
          <leafValues>
            -3.6884650588035583e-02 4.1484919190406799e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1436 -8.6298510432243347e-03</internalNodes>
          <leafValues>
            2.5522458553314209e-01 -6.9871626794338226e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1437 -3.9153471589088440e-02</internalNodes>
          <leafValues>
            -8.5533118247985840e-01 1.4639239758253098e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1438 3.8482698798179626e-01</internalNodes>
          <leafValues>
            1.7361119389533997e-02 -7.9790550470352173e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1439 -6.3598138513043523e-04</internalNodes>
          <leafValues>
            1.1518269777297974e-01 -1.4216409623622894e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1440 5.9026381932199001e-03</internalNodes>
          <leafValues>
            7.0523656904697418e-02 -2.3031190037727356e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1441 -1.1841119703603908e-04</internalNodes>
          <leafValues>
            1.0401789844036102e-01 -1.7126679420471191e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1442 8.1962659955024719e-02</internalNodes>
          <leafValues>
            2.7799099683761597e-02 -5.8331722021102905e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1443 -7.9551688395440578e-04</internalNodes>
          <leafValues>
            1.2568520009517670e-01 -1.0317719727754593e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1444 -1.5588940680027008e-01</internalNodes>
          <leafValues>
            6.2890201807022095e-01 -2.5191979482769966e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1445 -1.3456310145556927e-02</internalNodes>
          <leafValues>
            -3.2471698522567749e-01 5.5486921221017838e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1446 -2.1507199853658676e-02</internalNodes>
          <leafValues>
            2.8819179534912109e-01 -6.1176139861345291e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1447 -1.9042069092392921e-02</internalNodes>
          <leafValues>
            -6.0552909970283508e-02 8.9629061520099640e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1448 -9.1205362696200609e-04</internalNodes>
          <leafValues>
            1.2385459989309311e-01 -1.3584870100021362e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1449 3.8202628493309021e-02</internalNodes>
          <leafValues>
            1.9218420609831810e-02 -8.4488832950592041e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1450 5.1787391304969788e-02</internalNodes>
          <leafValues>
            -5.4830659180879593e-02 3.3352980017662048e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1451 -1.3860349357128143e-01</internalNodes>
          <leafValues>
            -2.7164599299430847e-01 1.0680199600756168e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1452 -3.9325959980487823e-02</internalNodes>
          <leafValues>
            -7.6043432950973511e-01 1.9320670515298843e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1453 -1.1157010449096560e-03</internalNodes>
          <leafValues>
            6.9478519260883331e-02 -2.0327170193195343e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1454 -4.2068599723279476e-03</internalNodes>
          <leafValues>
            1.6007219254970551e-01 -1.0982350260019302e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1455 3.7919029127806425e-03</internalNodes>
          <leafValues>
            -8.3800643682479858e-02 2.5154781341552734e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1456 -3.1430590897798538e-02</internalNodes>
          <leafValues>
            -5.0590312480926514e-01 3.7667378783226013e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1457 -4.3412651866674423e-03</internalNodes>
          <leafValues>
            5.8591969311237335e-02 -1.7271269857883453e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1458 -5.6401407346129417e-04</internalNodes>
          <leafValues>
            1.0131839662790298e-01 -1.6737550497055054e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1459 -1.7139960080385208e-02</internalNodes>
          <leafValues>
            4.9619451165199280e-02 -1.1812750250101089e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1460 -2.3868490010499954e-02</internalNodes>
          <leafValues>
            -9.5875509083271027e-02 1.8404319882392883e-01</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1461 -8.7408810853958130e-02</internalNodes>
          <leafValues>
            1.4144630730152130e-01 -5.7713828980922699e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1462 -3.9170090109109879e-02</internalNodes>
          <leafValues>
            -6.1036241054534912e-01 2.2308109328150749e-02</leafValues></_>
        <_>
          <internalNodes>
            0 -1 1463 5.3361579775810242e-02</internalNodes>
          <leafValues>
            1.5027640387415886e-02 -6.5409141778945923e-01</leafValues></_></weakClassifiers></_></stages>
  <features>
    <_>
      <rects>
        <_>
          1 5 12 21 -1.</_>
        <_>
          5 5 4 21 3.</_></rects></_>
    <_>
      <rects>
        <_>
          9 2 3 26 -1.</_>
        <_>
          9 15 3 13 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 4 12 23 -1.</_>
        <_>
          5 4 4 23 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 7 12 9 -1.</_>
        <_>
          4 7 6 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 12 3 16 -1.</_>
        <_>
          3 20 3 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 8 6 6 -1.</_>
        <_>
          4 11 6 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 25 12 3 -1.</_>
        <_>
          5 25 4 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 25 8 3 -1.</_>
        <_>
          6 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 2 4 12 -1.</_>
        <_>
          4 2 2 6 2.</_>
        <_>
          6 8 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 15 8 11 -1.</_>
        <_>
          5 15 4 11 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 9 6 6 -1.</_>
        <_>
          8 9 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 9 6 6 -1.</_>
        <_>
          4 9 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          8 0 5 28 -1.</_>
        <_>
          8 14 5 14 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 24 10 4 -1.</_>
        <_>
          7 24 5 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 15 8 11 -1.</_>
        <_>
          5 15 4 11 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 25 14 3 -1.</_>
        <_>
          7 25 7 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 11 12 13 -1.</_>
        <_>
          5 11 4 13 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 2 12 21 -1.</_>
        <_>
          5 9 4 7 9.</_></rects></_>
    <_>
      <rects>
        <_>
          10 0 3 28 -1.</_>
        <_>
          10 14 3 14 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 0 3 28 -1.</_>
        <_>
          1 14 3 14 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 5 6 8 -1.</_>
        <_>
          8 5 3 4 2.</_>
        <_>
          5 9 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 5 6 8 -1.</_>
        <_>
          3 5 3 4 2.</_>
        <_>
          6 9 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          10 16 4 12 -1.</_>
        <_>
          12 16 2 6 2.</_>
        <_>
          10 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 8 6 4 -1.</_>
        <_>
          4 10 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 5 8 21 -1.</_>
        <_>
          5 5 4 21 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 15 12 12 -1.</_>
        <_>
          7 15 6 6 2.</_>
        <_>
          1 21 6 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 25 12 3 -1.</_>
        <_>
          6 25 6 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 14 3 8 -1.</_>
        <_>
          8 14 3 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          0 25 8 3 -1.</_>
        <_>
          4 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 24 12 4 -1.</_>
        <_>
          5 24 6 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 18 4 6 -1.</_>
        <_>
          3 18 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 8 4 7 -1.</_>
        <_>
          8 8 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 8 4 7 -1.</_>
        <_>
          4 8 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 3 12 18 -1.</_>
        <_>
          1 3 6 18 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 20 4 8 -1.</_>
        <_>
          3 20 2 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 10 7 18 -1.</_>
        <_>
          6 19 7 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 8 3 13 -1.</_>
        <_>
          5 8 1 13 3.</_></rects></_>
    <_>
      <rects>
        <_>
          10 22 4 6 -1.</_>
        <_>
          10 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 0 12 27 -1.</_>
        <_>
          5 9 4 9 9.</_></rects></_>
    <_>
      <rects>
        <_>
          2 20 12 7 -1.</_>
        <_>
          5 20 6 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 25 10 3 -1.</_>
        <_>
          7 25 5 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 26 14 2 -1.</_>
        <_>
          0 26 7 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 15 8 9 -1.</_>
        <_>
          5 15 4 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 23 6 5 -1.</_>
        <_>
          8 23 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 26 14 2 -1.</_>
        <_>
          7 26 7 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 10 2 18 -1.</_>
        <_>
          8 19 2 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 4 4 12 -1.</_>
        <_>
          4 4 2 6 2.</_>
        <_>
          6 10 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 24 9 4 -1.</_>
        <_>
          7 24 3 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 3 12 15 -1.</_>
        <_>
          5 8 4 5 9.</_></rects></_>
    <_>
      <rects>
        <_>
          11 16 2 12 -1.</_>
        <_>
          11 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 4 7 16 -1.</_>
        <_>
          2 12 7 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 8 4 6 -1.</_>
        <_>
          8 8 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 8 8 6 -1.</_>
        <_>
          3 11 8 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 8 6 8 -1.</_>
        <_>
          10 8 2 8 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 8 6 7 -1.</_>
        <_>
          2 8 2 7 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 25 12 3 -1.</_>
        <_>
          6 25 4 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 25 12 3 -1.</_>
        <_>
          4 25 4 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 7 12 4 -1.</_>
        <_>
          1 7 6 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 2 14 12 -1.</_>
        <_>
          7 2 7 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 19 14 6 -1.</_>
        <_>
          7 19 7 3 2.</_>
        <_>
          0 22 7 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 14 12 6 -1.</_>
        <_>
          5 14 4 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 24 12 4 -1.</_>
        <_>
          5 24 6 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 1 4 14 -1.</_>
        <_>
          2 1 2 7 2.</_>
        <_>
          4 8 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          10 3 4 6 -1.</_>
        <_>
          10 3 2 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          4 3 6 4 -1.</_>
        <_>
          4 3 6 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          0 16 14 8 -1.</_>
        <_>
          0 16 7 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 16 3 12 -1.</_>
        <_>
          6 16 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 15 4 7 -1.</_>
        <_>
          7 15 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 15 4 8 -1.</_>
        <_>
          5 15 2 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 17 4 8 -1.</_>
        <_>
          9 17 2 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 17 4 8 -1.</_>
        <_>
          3 17 2 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 18 4 7 -1.</_>
        <_>
          9 18 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 18 4 7 -1.</_>
        <_>
          3 18 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 5 4 6 -1.</_>
        <_>
          7 5 2 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 5 6 4 -1.</_>
        <_>
          7 5 6 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          2 26 12 2 -1.</_>
        <_>
          2 26 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 7 3 12 -1.</_>
        <_>
          5 7 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 7 12 11 -1.</_>
        <_>
          4 7 6 11 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 13 8 4 -1.</_>
        <_>
          6 13 4 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          5 22 6 4 -1.</_>
        <_>
          5 22 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 26 14 2 -1.</_>
        <_>
          7 26 7 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 3 12 18 -1.</_>
        <_>
          5 9 4 6 9.</_></rects></_>
    <_>
      <rects>
        <_>
          0 6 9 22 -1.</_>
        <_>
          0 17 9 11 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 1 12 24 -1.</_>
        <_>
          7 1 6 12 2.</_>
        <_>
          1 13 6 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 26 12 2 -1.</_>
        <_>
          6 26 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 4 12 23 -1.</_>
        <_>
          5 4 4 23 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 22 6 5 -1.</_>
        <_>
          5 22 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 22 6 5 -1.</_>
        <_>
          6 22 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 1 4 6 -1.</_>
        <_>
          5 4 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 8 12 8 -1.</_>
        <_>
          4 8 6 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 8 5 12 -1.</_>
        <_>
          6 11 5 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 20 14 6 -1.</_>
        <_>
          0 20 7 3 2.</_>
        <_>
          7 23 7 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 9 6 6 -1.</_>
        <_>
          8 9 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 8 4 6 -1.</_>
        <_>
          7 8 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 13 12 15 -1.</_>
        <_>
          2 18 12 5 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 16 4 12 -1.</_>
        <_>
          0 16 2 6 2.</_>
        <_>
          2 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 2 2 26 -1.</_>
        <_>
          10 2 1 13 2.</_>
        <_>
          9 15 1 13 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 2 2 26 -1.</_>
        <_>
          3 2 1 13 2.</_>
        <_>
          4 15 1 13 2.</_></rects></_>
    <_>
      <rects>
        <_>
          10 22 4 6 -1.</_>
        <_>
          10 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 1 12 12 -1.</_>
        <_>
          4 5 4 4 9.</_></rects></_>
    <_>
      <rects>
        <_>
          6 15 3 12 -1.</_>
        <_>
          7 15 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 10 3 15 -1.</_>
        <_>
          6 10 1 15 3.</_></rects></_>
    <_>
      <rects>
        <_>
          10 22 4 6 -1.</_>
        <_>
          10 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 10 8 18 -1.</_>
        <_>
          0 19 8 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 16 8 12 -1.</_>
        <_>
          9 16 4 6 2.</_>
        <_>
          5 22 4 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 25 8 3 -1.</_>
        <_>
          4 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 17 14 8 -1.</_>
        <_>
          7 17 7 4 2.</_>
        <_>
          0 21 7 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 15 6 4 -1.</_>
        <_>
          5 15 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 23 9 4 -1.</_>
        <_>
          8 23 3 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 23 9 5 -1.</_>
        <_>
          3 23 3 5 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 4 12 22 -1.</_>
        <_>
          5 4 4 22 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 4 5 24 -1.</_>
        <_>
          1 10 5 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 23 12 4 -1.</_>
        <_>
          5 23 6 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 16 4 12 -1.</_>
        <_>
          5 16 2 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 17 12 11 -1.</_>
        <_>
          1 17 6 11 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 16 3 12 -1.</_>
        <_>
          6 16 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          8 17 4 6 -1.</_>
        <_>
          8 17 4 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 16 4 6 -1.</_>
        <_>
          7 16 2 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 2 4 6 -1.</_>
        <_>
          6 2 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 12 5 16 -1.</_>
        <_>
          2 20 5 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 13 3 14 -1.</_>
        <_>
          7 13 1 14 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 6 8 3 -1.</_>
        <_>
          6 6 4 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          0 8 14 6 -1.</_>
        <_>
          0 11 14 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 7 4 7 -1.</_>
        <_>
          4 7 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 8 4 6 -1.</_>
        <_>
          8 8 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 13 8 13 -1.</_>
        <_>
          5 13 4 13 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 2 4 12 -1.</_>
        <_>
          10 2 2 6 2.</_>
        <_>
          8 8 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 2 4 12 -1.</_>
        <_>
          2 2 2 6 2.</_>
        <_>
          4 8 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 24 8 3 -1.</_>
        <_>
          6 24 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 16 2 12 -1.</_>
        <_>
          4 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 21 14 6 -1.</_>
        <_>
          0 21 7 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 11 8 4 -1.</_>
        <_>
          4 11 4 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 2 12 5 -1.</_>
        <_>
          5 2 4 5 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 1 6 21 -1.</_>
        <_>
          4 8 2 7 9.</_></rects></_>
    <_>
      <rects>
        <_>
          11 16 2 12 -1.</_>
        <_>
          11 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 17 6 5 -1.</_>
        <_>
          7 17 3 5 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 16 3 12 -1.</_>
        <_>
          7 16 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 16 2 12 -1.</_>
        <_>
          2 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 13 3 12 -1.</_>
        <_>
          8 13 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 17 4 6 -1.</_>
        <_>
          6 17 2 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 8 4 6 -1.</_>
        <_>
          6 11 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 5 8 12 -1.</_>
        <_>
          1 11 8 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 13 3 12 -1.</_>
        <_>
          8 13 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 6 8 3 -1.</_>
        <_>
          6 6 4 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 14 3 12 -1.</_>
        <_>
          8 14 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 25 12 3 -1.</_>
        <_>
          4 25 4 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 17 4 8 -1.</_>
        <_>
          7 17 2 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 17 4 8 -1.</_>
        <_>
          5 17 2 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 24 6 4 -1.</_>
        <_>
          8 24 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 22 6 6 -1.</_>
        <_>
          4 22 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          8 15 5 8 -1.</_>
        <_>
          8 15 5 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 15 8 5 -1.</_>
        <_>
          6 15 4 5 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          1 8 12 7 -1.</_>
        <_>
          4 8 6 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 10 6 10 -1.</_>
        <_>
          0 15 6 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 4 4 22 -1.</_>
        <_>
          7 15 4 11 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 4 12 22 -1.</_>
        <_>
          4 4 6 22 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 3 4 12 -1.</_>
        <_>
          8 3 2 6 2.</_>
        <_>
          6 9 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 16 3 12 -1.</_>
        <_>
          6 16 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 5 6 8 -1.</_>
        <_>
          8 5 3 4 2.</_>
        <_>
          5 9 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 5 6 8 -1.</_>
        <_>
          3 5 3 4 2.</_>
        <_>
          6 9 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 4 6 4 -1.</_>
        <_>
          8 4 6 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          5 10 3 18 -1.</_>
        <_>
          5 19 3 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 6 4 6 -1.</_>
        <_>
          7 6 4 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 6 6 4 -1.</_>
        <_>
          7 6 3 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 24 8 3 -1.</_>
        <_>
          6 24 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 11 12 5 -1.</_>
        <_>
          4 11 6 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          10 22 4 6 -1.</_>
        <_>
          10 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 3 4 12 -1.</_>
        <_>
          2 3 2 6 2.</_>
        <_>
          4 9 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          10 22 4 6 -1.</_>
        <_>
          10 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 22 4 6 -1.</_>
        <_>
          2 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 15 3 12 -1.</_>
        <_>
          7 15 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 16 4 6 -1.</_>
        <_>
          7 16 2 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          4 2 6 6 -1.</_>
        <_>
          4 4 6 2 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 16 2 12 -1.</_>
        <_>
          4 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 16 2 12 -1.</_>
        <_>
          7 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 9 4 6 -1.</_>
        <_>
          7 9 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 15 2 12 -1.</_>
        <_>
          7 15 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 15 2 12 -1.</_>
        <_>
          6 15 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 25 12 2 -1.</_>
        <_>
          2 25 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 16 4 12 -1.</_>
        <_>
          3 16 2 6 2.</_>
        <_>
          5 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 24 8 3 -1.</_>
        <_>
          6 24 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 25 12 2 -1.</_>
        <_>
          6 25 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 1 6 27 -1.</_>
        <_>
          4 10 6 9 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 16 3 12 -1.</_>
        <_>
          7 16 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 21 6 4 -1.</_>
        <_>
          6 21 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 2 6 12 -1.</_>
        <_>
          4 8 6 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 0 6 4 -1.</_>
        <_>
          6 0 3 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 4 3 14 -1.</_>
        <_>
          7 4 1 14 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 8 6 6 -1.</_>
        <_>
          6 8 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 24 12 4 -1.</_>
        <_>
          6 24 4 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 24 12 4 -1.</_>
        <_>
          4 24 4 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          8 13 3 12 -1.</_>
        <_>
          9 13 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 22 4 6 -1.</_>
        <_>
          3 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 7 3 12 -1.</_>
        <_>
          8 7 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 7 3 12 -1.</_>
        <_>
          5 7 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 1 8 3 -1.</_>
        <_>
          4 1 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 4 3 23 -1.</_>
        <_>
          5 4 1 23 3.</_></rects></_>
    <_>
      <rects>
        <_>
          9 21 4 7 -1.</_>
        <_>
          9 21 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 14 3 12 -1.</_>
        <_>
          6 14 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 26 12 2 -1.</_>
        <_>
          2 26 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 26 12 2 -1.</_>
        <_>
          6 26 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 13 3 12 -1.</_>
        <_>
          9 13 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 13 3 12 -1.</_>
        <_>
          4 13 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 2 8 20 -1.</_>
        <_>
          3 7 8 10 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 18 12 8 -1.</_>
        <_>
          5 18 6 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 9 6 6 -1.</_>
        <_>
          6 9 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 18 12 8 -1.</_>
        <_>
          5 18 6 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 24 8 4 -1.</_>
        <_>
          4 24 4 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 2 2 24 -1.</_>
        <_>
          7 2 1 12 2.</_>
        <_>
          6 14 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 8 4 12 -1.</_>
        <_>
          5 8 2 6 2.</_>
        <_>
          7 14 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 3 6 6 -1.</_>
        <_>
          7 3 3 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          0 8 6 7 -1.</_>
        <_>
          2 8 2 7 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 3 6 6 -1.</_>
        <_>
          7 3 3 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          4 8 6 4 -1.</_>
        <_>
          7 8 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 7 10 19 -1.</_>
        <_>
          2 7 5 19 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 4 11 24 -1.</_>
        <_>
          0 16 11 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 1 12 21 -1.</_>
        <_>
          5 8 4 7 9.</_></rects></_>
    <_>
      <rects>
        <_>
          0 18 12 8 -1.</_>
        <_>
          3 18 6 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 17 4 8 -1.</_>
        <_>
          9 17 2 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 7 4 6 -1.</_>
        <_>
          4 10 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 7 5 9 -1.</_>
        <_>
          7 10 5 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 17 4 8 -1.</_>
        <_>
          3 17 2 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 15 3 13 -1.</_>
        <_>
          10 15 1 13 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 0 6 8 -1.</_>
        <_>
          3 0 3 4 2.</_>
        <_>
          6 4 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 18 4 10 -1.</_>
        <_>
          9 18 2 10 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 18 4 10 -1.</_>
        <_>
          3 18 2 10 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 22 2 4 -1.</_>
        <_>
          7 22 1 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 22 4 2 -1.</_>
        <_>
          7 22 4 1 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 7 5 9 -1.</_>
        <_>
          7 10 5 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 7 12 11 -1.</_>
        <_>
          4 7 6 11 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 6 3 8 -1.</_>
        <_>
          8 6 3 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          5 8 3 16 -1.</_>
        <_>
          5 12 3 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 6 3 8 -1.</_>
        <_>
          8 6 3 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 6 8 3 -1.</_>
        <_>
          6 6 4 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          2 24 12 3 -1.</_>
        <_>
          6 24 4 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 5 6 4 -1.</_>
        <_>
          3 7 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 5 6 4 -1.</_>
        <_>
          4 7 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 14 6 6 -1.</_>
        <_>
          6 14 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 11 3 13 -1.</_>
        <_>
          7 11 1 13 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 24 12 3 -1.</_>
        <_>
          4 24 4 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          9 16 2 12 -1.</_>
        <_>
          9 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 16 2 12 -1.</_>
        <_>
          4 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 16 2 12 -1.</_>
        <_>
          7 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 21 4 6 -1.</_>
        <_>
          2 21 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 16 2 12 -1.</_>
        <_>
          7 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 3 10 16 -1.</_>
        <_>
          2 3 5 8 2.</_>
        <_>
          7 11 5 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 12 6 16 -1.</_>
        <_>
          4 20 6 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 15 12 11 -1.</_>
        <_>
          4 15 6 11 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 4 6 10 -1.</_>
        <_>
          3 4 3 5 2.</_>
        <_>
          6 9 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 24 12 4 -1.</_>
        <_>
          8 24 6 2 2.</_>
        <_>
          2 26 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 24 12 4 -1.</_>
        <_>
          0 24 6 2 2.</_>
        <_>
          6 26 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 4 6 4 -1.</_>
        <_>
          8 4 6 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          1 2 12 18 -1.</_>
        <_>
          5 8 4 6 9.</_></rects></_>
    <_>
      <rects>
        <_>
          2 22 10 6 -1.</_>
        <_>
          2 22 5 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 26 12 2 -1.</_>
        <_>
          7 26 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 4 6 4 -1.</_>
        <_>
          8 4 6 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          0 12 10 4 -1.</_>
        <_>
          5 12 5 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 8 6 4 -1.</_>
        <_>
          4 10 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 1 4 12 -1.</_>
        <_>
          5 4 4 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 4 6 8 -1.</_>
        <_>
          10 4 3 4 2.</_>
        <_>
          7 8 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 18 14 4 -1.</_>
        <_>
          0 18 7 2 2.</_>
        <_>
          7 20 7 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 16 2 12 -1.</_>
        <_>
          7 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 15 3 12 -1.</_>
        <_>
          5 15 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          8 9 2 13 -1.</_>
        <_>
          8 9 1 13 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 10 4 6 -1.</_>
        <_>
          7 10 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 11 8 5 -1.</_>
        <_>
          3 11 4 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 16 2 12 -1.</_>
        <_>
          6 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 7 10 17 -1.</_>
        <_>
          5 7 5 17 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 7 8 4 -1.</_>
        <_>
          3 9 8 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 0 4 24 -1.</_>
        <_>
          5 8 4 8 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 16 9 4 -1.</_>
        <_>
          6 16 3 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 14 6 4 -1.</_>
        <_>
          7 14 3 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          5 23 9 4 -1.</_>
        <_>
          8 23 3 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 22 9 4 -1.</_>
        <_>
          3 22 3 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          9 22 4 6 -1.</_>
        <_>
          9 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 24 6 4 -1.</_>
        <_>
          4 24 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 19 8 9 -1.</_>
        <_>
          6 19 4 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 19 8 9 -1.</_>
        <_>
          4 19 4 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 22 12 4 -1.</_>
        <_>
          5 22 6 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 19 14 7 -1.</_>
        <_>
          7 19 7 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 20 6 8 -1.</_>
        <_>
          8 20 3 4 2.</_>
        <_>
          5 24 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 20 6 8 -1.</_>
        <_>
          3 20 3 4 2.</_>
        <_>
          6 24 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 1 4 14 -1.</_>
        <_>
          8 1 2 7 2.</_>
        <_>
          6 8 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 2 4 12 -1.</_>
        <_>
          2 2 2 6 2.</_>
        <_>
          4 8 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 4 6 4 -1.</_>
        <_>
          7 4 3 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 4 4 6 -1.</_>
        <_>
          7 4 4 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 3 6 5 -1.</_>
        <_>
          7 3 3 5 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 3 5 6 -1.</_>
        <_>
          7 3 5 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 3 6 4 -1.</_>
        <_>
          7 3 6 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          3 2 8 18 -1.</_>
        <_>
          3 8 8 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 15 9 12 -1.</_>
        <_>
          7 19 3 4 9.</_></rects></_>
    <_>
      <rects>
        <_>
          1 21 12 6 -1.</_>
        <_>
          7 21 6 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 18 4 8 -1.</_>
        <_>
          9 18 2 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 16 9 4 -1.</_>
        <_>
          5 16 3 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 17 10 6 -1.</_>
        <_>
          4 17 5 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 18 4 8 -1.</_>
        <_>
          3 18 2 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 3 5 6 -1.</_>
        <_>
          9 3 5 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          1 17 8 6 -1.</_>
        <_>
          5 17 4 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 19 12 9 -1.</_>
        <_>
          6 22 4 3 9.</_></rects></_>
    <_>
      <rects>
        <_>
          2 0 4 14 -1.</_>
        <_>
          2 0 2 7 2.</_>
        <_>
          4 7 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 9 10 14 -1.</_>
        <_>
          9 9 5 7 2.</_>
        <_>
          4 16 5 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 16 4 12 -1.</_>
        <_>
          0 16 2 6 2.</_>
        <_>
          2 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 24 8 4 -1.</_>
        <_>
          3 24 4 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 5 14 22 -1.</_>
        <_>
          0 16 14 11 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 13 6 8 -1.</_>
        <_>
          6 17 6 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 9 10 14 -1.</_>
        <_>
          0 9 5 7 2.</_>
        <_>
          5 16 5 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 3 9 9 -1.</_>
        <_>
          3 6 9 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 1 4 6 -1.</_>
        <_>
          5 4 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 0 12 9 -1.</_>
        <_>
          5 3 4 3 9.</_></rects></_>
    <_>
      <rects>
        <_>
          4 7 6 12 -1.</_>
        <_>
          4 7 3 6 2.</_>
        <_>
          7 13 3 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 7 6 18 -1.</_>
        <_>
          8 13 2 6 9.</_></rects></_>
    <_>
      <rects>
        <_>
          2 7 6 18 -1.</_>
        <_>
          4 13 2 6 9.</_></rects></_>
    <_>
      <rects>
        <_>
          2 22 12 4 -1.</_>
        <_>
          6 22 4 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 16 8 8 -1.</_>
        <_>
          3 16 4 4 2.</_>
        <_>
          7 20 4 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 7 6 10 -1.</_>
        <_>
          7 7 3 10 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 8 12 10 -1.</_>
        <_>
          4 8 6 10 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 16 3 12 -1.</_>
        <_>
          6 16 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 5 10 17 -1.</_>
        <_>
          4 5 5 17 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 4 14 24 -1.</_>
        <_>
          7 4 7 24 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 9 6 7 -1.</_>
        <_>
          6 9 2 7 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 20 10 8 -1.</_>
        <_>
          2 20 5 4 2.</_>
        <_>
          7 24 5 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 5 6 8 -1.</_>
        <_>
          6 7 6 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 4 4 6 -1.</_>
        <_>
          6 4 2 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 3 4 6 -1.</_>
        <_>
          6 3 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 4 4 6 -1.</_>
        <_>
          7 4 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 8 4 6 -1.</_>
        <_>
          5 8 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 3 6 6 -1.</_>
        <_>
          7 3 6 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          4 5 6 6 -1.</_>
        <_>
          4 8 6 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 12 6 14 -1.</_>
        <_>
          3 19 6 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          11 16 2 12 -1.</_>
        <_>
          11 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 22 6 6 -1.</_>
        <_>
          3 22 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 16 3 12 -1.</_>
        <_>
          7 16 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 16 3 12 -1.</_>
        <_>
          6 16 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 9 8 4 -1.</_>
        <_>
          3 11 8 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 16 2 12 -1.</_>
        <_>
          4 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 20 12 8 -1.</_>
        <_>
          5 20 6 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 20 12 8 -1.</_>
        <_>
          3 20 6 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 4 9 12 -1.</_>
        <_>
          5 10 9 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 12 10 4 -1.</_>
        <_>
          4 12 10 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          4 2 10 4 -1.</_>
        <_>
          4 2 5 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 15 12 13 -1.</_>
        <_>
          4 15 6 13 2.</_></rects></_>
    <_>
      <rects>
        <_>
          11 16 2 12 -1.</_>
        <_>
          11 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 3 3 12 -1.</_>
        <_>
          3 3 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          8 2 4 6 -1.</_>
        <_>
          8 2 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 2 4 6 -1.</_>
        <_>
          4 2 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 13 12 14 -1.</_>
        <_>
          5 13 6 14 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 16 2 12 -1.</_>
        <_>
          2 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 21 4 6 -1.</_>
        <_>
          9 21 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 21 4 6 -1.</_>
        <_>
          3 21 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 0 3 15 -1.</_>
        <_>
          10 0 1 15 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 22 4 6 -1.</_>
        <_>
          4 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 13 12 14 -1.</_>
        <_>
          5 13 6 14 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 3 4 6 -1.</_>
        <_>
          6 3 4 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          1 0 12 24 -1.</_>
        <_>
          5 8 4 8 9.</_></rects></_>
    <_>
      <rects>
        <_>
          4 2 6 8 -1.</_>
        <_>
          4 6 6 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 4 12 8 -1.</_>
        <_>
          2 6 12 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 8 12 18 -1.</_>
        <_>
          4 8 6 18 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 0 8 24 -1.</_>
        <_>
          3 8 8 8 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 21 6 6 -1.</_>
        <_>
          3 21 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 7 8 3 -1.</_>
        <_>
          5 7 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 7 8 3 -1.</_>
        <_>
          5 7 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 1 4 6 -1.</_>
        <_>
          5 4 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 6 4 6 -1.</_>
        <_>
          4 9 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          10 20 4 6 -1.</_>
        <_>
          10 20 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 1 8 21 -1.</_>
        <_>
          3 8 8 7 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 16 4 12 -1.</_>
        <_>
          9 16 2 6 2.</_>
        <_>
          7 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 25 12 3 -1.</_>
        <_>
          5 25 4 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 16 4 12 -1.</_>
        <_>
          9 16 2 6 2.</_>
        <_>
          7 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 16 4 12 -1.</_>
        <_>
          3 16 2 6 2.</_>
        <_>
          5 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 17 4 7 -1.</_>
        <_>
          7 17 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 17 4 7 -1.</_>
        <_>
          5 17 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 12 6 6 -1.</_>
        <_>
          6 12 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 8 4 15 -1.</_>
        <_>
          6 8 2 15 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 22 2 4 -1.</_>
        <_>
          7 22 1 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 22 4 2 -1.</_>
        <_>
          7 22 4 1 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          1 15 12 3 -1.</_>
        <_>
          1 15 6 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 15 6 12 -1.</_>
        <_>
          4 15 3 6 2.</_>
        <_>
          7 21 3 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 16 3 12 -1.</_>
        <_>
          8 16 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 9 4 18 -1.</_>
        <_>
          2 9 2 9 2.</_>
        <_>
          4 18 2 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 10 4 6 -1.</_>
        <_>
          8 10 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 16 4 12 -1.</_>
        <_>
          0 16 2 6 2.</_>
        <_>
          2 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 22 12 4 -1.</_>
        <_>
          6 22 4 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 24 9 4 -1.</_>
        <_>
          3 24 3 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          9 13 4 12 -1.</_>
        <_>
          9 17 4 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 10 4 6 -1.</_>
        <_>
          4 10 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 8 8 6 -1.</_>
        <_>
          4 10 8 2 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 22 12 4 -1.</_>
        <_>
          4 22 4 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 21 9 7 -1.</_>
        <_>
          7 21 3 7 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 22 4 6 -1.</_>
        <_>
          7 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 2 3 12 -1.</_>
        <_>
          10 2 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 3 3 12 -1.</_>
        <_>
          3 3 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          8 4 4 6 -1.</_>
        <_>
          8 4 2 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 4 6 4 -1.</_>
        <_>
          6 4 6 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          4 6 8 16 -1.</_>
        <_>
          8 6 4 8 2.</_>
        <_>
          4 14 4 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 6 8 16 -1.</_>
        <_>
          2 6 4 8 2.</_>
        <_>
          6 14 4 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 8 8 8 -1.</_>
        <_>
          6 8 4 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 6 12 10 -1.</_>
        <_>
          4 6 4 10 3.</_></rects></_>
    <_>
      <rects>
        <_>
          8 10 6 7 -1.</_>
        <_>
          10 12 2 7 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 10 7 6 -1.</_>
        <_>
          4 12 7 2 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          5 11 4 7 -1.</_>
        <_>
          5 11 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 11 12 16 -1.</_>
        <_>
          1 11 6 8 2.</_>
        <_>
          7 19 6 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 9 3 13 -1.</_>
        <_>
          7 9 1 13 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 9 6 4 -1.</_>
        <_>
          3 11 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 22 4 6 -1.</_>
        <_>
          9 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 9 7 4 -1.</_>
        <_>
          2 11 7 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 15 3 12 -1.</_>
        <_>
          8 15 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 15 8 3 -1.</_>
        <_>
          6 15 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 7 12 19 -1.</_>
        <_>
          4 7 6 19 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 9 4 12 -1.</_>
        <_>
          8 9 2 6 2.</_>
        <_>
          6 15 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 12 4 6 -1.</_>
        <_>
          1 15 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 22 8 6 -1.</_>
        <_>
          8 22 4 3 2.</_>
        <_>
          4 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 22 8 6 -1.</_>
        <_>
          2 22 4 3 2.</_>
        <_>
          6 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 17 4 6 -1.</_>
        <_>
          9 17 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 17 4 6 -1.</_>
        <_>
          3 17 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 5 6 4 -1.</_>
        <_>
          4 7 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 3 4 6 -1.</_>
        <_>
          7 3 2 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 24 6 4 -1.</_>
        <_>
          6 24 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 21 12 3 -1.</_>
        <_>
          5 21 4 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 17 2 7 -1.</_>
        <_>
          7 17 1 7 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 17 7 2 -1.</_>
        <_>
          7 17 7 1 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 12 3 16 -1.</_>
        <_>
          6 20 3 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 24 9 4 -1.</_>
        <_>
          5 24 3 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 25 12 2 -1.</_>
        <_>
          2 25 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 25 12 2 -1.</_>
        <_>
          6 25 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 11 6 8 -1.</_>
        <_>
          4 15 6 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 0 4 6 -1.</_>
        <_>
          7 0 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 2 10 7 -1.</_>
        <_>
          2 2 5 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 1 12 25 -1.</_>
        <_>
          3 1 6 25 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 14 12 6 -1.</_>
        <_>
          4 14 6 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 26 12 2 -1.</_>
        <_>
          6 26 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 15 3 12 -1.</_>
        <_>
          7 15 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 7 2 12 -1.</_>
        <_>
          7 7 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 9 4 6 -1.</_>
        <_>
          5 9 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 20 6 6 -1.</_>
        <_>
          6 20 3 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 10 8 4 -1.</_>
        <_>
          3 10 4 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 5 9 18 -1.</_>
        <_>
          3 11 3 6 9.</_></rects></_>
    <_>
      <rects>
        <_>
          8 8 4 6 -1.</_>
        <_>
          8 8 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 8 4 6 -1.</_>
        <_>
          4 8 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 8 4 12 -1.</_>
        <_>
          10 8 2 6 2.</_>
        <_>
          8 14 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 10 6 8 -1.</_>
        <_>
          4 10 3 4 2.</_>
        <_>
          7 14 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 15 4 6 -1.</_>
        <_>
          7 15 4 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 15 6 4 -1.</_>
        <_>
          7 15 3 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          1 9 13 15 -1.</_>
        <_>
          1 14 13 5 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 1 3 25 -1.</_>
        <_>
          6 1 1 25 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 15 3 12 -1.</_>
        <_>
          7 15 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 7 4 16 -1.</_>
        <_>
          0 7 2 8 2.</_>
        <_>
          2 15 2 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 2 6 4 -1.</_>
        <_>
          4 4 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 0 10 10 -1.</_>
        <_>
          0 5 10 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 5 6 8 -1.</_>
        <_>
          11 5 3 4 2.</_>
        <_>
          8 9 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 14 12 14 -1.</_>
        <_>
          1 14 6 7 2.</_>
        <_>
          7 21 6 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 1 6 18 -1.</_>
        <_>
          9 7 2 6 9.</_></rects></_>
    <_>
      <rects>
        <_>
          0 18 14 8 -1.</_>
        <_>
          0 18 7 4 2.</_>
        <_>
          7 22 7 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 3 8 23 -1.</_>
        <_>
          6 3 4 23 2.</_></rects></_>
    <_>
      <rects>
        <_>
          10 18 4 9 -1.</_>
        <_>
          10 18 2 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 25 8 3 -1.</_>
        <_>
          4 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 26 12 2 -1.</_>
        <_>
          2 26 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 22 4 6 -1.</_>
        <_>
          3 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 16 2 12 -1.</_>
        <_>
          6 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 14 6 14 -1.</_>
        <_>
          2 14 3 7 2.</_>
        <_>
          5 21 3 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 8 6 6 -1.</_>
        <_>
          6 8 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 18 8 6 -1.</_>
        <_>
          0 18 4 3 2.</_>
        <_>
          4 21 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 13 6 11 -1.</_>
        <_>
          9 13 2 11 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 16 12 7 -1.</_>
        <_>
          4 16 6 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 15 4 9 -1.</_>
        <_>
          7 15 2 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 15 4 9 -1.</_>
        <_>
          5 15 2 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          10 18 4 8 -1.</_>
        <_>
          10 18 2 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 7 9 6 -1.</_>
        <_>
          2 9 9 2 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 9 12 6 -1.</_>
        <_>
          1 12 12 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 5 5 12 -1.</_>
        <_>
          3 11 5 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 6 8 4 -1.</_>
        <_>
          3 8 8 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 6 6 6 -1.</_>
        <_>
          4 8 6 2 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 26 12 2 -1.</_>
        <_>
          1 26 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 7 4 6 -1.</_>
        <_>
          7 7 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 5 6 5 -1.</_>
        <_>
          7 5 3 5 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          5 9 3 13 -1.</_>
        <_>
          6 9 1 13 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 18 6 10 -1.</_>
        <_>
          8 18 3 5 2.</_>
        <_>
          5 23 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 18 6 10 -1.</_>
        <_>
          3 18 3 5 2.</_>
        <_>
          6 23 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 15 7 6 -1.</_>
        <_>
          7 15 7 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          0 23 9 5 -1.</_>
        <_>
          3 23 3 5 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 15 7 6 -1.</_>
        <_>
          7 15 7 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 15 6 7 -1.</_>
        <_>
          7 15 3 7 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 2 6 12 -1.</_>
        <_>
          10 2 3 6 2.</_>
        <_>
          7 8 3 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 5 6 4 -1.</_>
        <_>
          7 5 6 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 3 6 10 -1.</_>
        <_>
          10 3 3 5 2.</_>
        <_>
          7 8 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 3 6 10 -1.</_>
        <_>
          1 3 3 5 2.</_>
        <_>
          4 8 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 7 12 4 -1.</_>
        <_>
          1 7 6 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 1 6 4 -1.</_>
        <_>
          5 1 6 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          0 0 14 10 -1.</_>
        <_>
          0 5 14 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 8 10 18 -1.</_>
        <_>
          0 8 5 9 2.</_>
        <_>
          5 17 5 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 16 2 12 -1.</_>
        <_>
          7 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 21 8 7 -1.</_>
        <_>
          4 21 4 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 21 8 6 -1.</_>
        <_>
          5 21 4 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 10 6 8 -1.</_>
        <_>
          6 10 2 8 3.</_></rects></_>
    <_>
      <rects>
        <_>
          8 2 3 12 -1.</_>
        <_>
          9 2 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 2 3 12 -1.</_>
        <_>
          4 2 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 26 12 2 -1.</_>
        <_>
          2 26 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 25 12 3 -1.</_>
        <_>
          7 25 6 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 20 3 5 -1.</_>
        <_>
          8 21 1 5 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          3 15 8 11 -1.</_>
        <_>
          5 15 4 11 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 1 12 21 -1.</_>
        <_>
          5 8 4 7 9.</_></rects></_>
    <_>
      <rects>
        <_>
          0 22 4 6 -1.</_>
        <_>
          2 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 23 9 4 -1.</_>
        <_>
          8 23 3 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 23 9 4 -1.</_>
        <_>
          3 23 3 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 3 4 12 -1.</_>
        <_>
          8 3 2 6 2.</_>
        <_>
          6 9 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 4 2 24 -1.</_>
        <_>
          6 4 1 12 2.</_>
        <_>
          7 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 9 4 6 -1.</_>
        <_>
          5 9 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 7 4 6 -1.</_>
        <_>
          4 7 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 8 6 20 -1.</_>
        <_>
          4 18 6 10 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 16 3 12 -1.</_>
        <_>
          2 16 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          8 12 6 16 -1.</_>
        <_>
          8 16 6 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 17 4 6 -1.</_>
        <_>
          3 17 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 14 6 9 -1.</_>
        <_>
          9 14 2 9 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 14 6 9 -1.</_>
        <_>
          3 14 2 9 3.</_></rects></_>
    <_>
      <rects>
        <_>
          8 0 4 18 -1.</_>
        <_>
          10 0 2 9 2.</_>
        <_>
          8 9 2 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 0 4 18 -1.</_>
        <_>
          2 0 2 9 2.</_>
        <_>
          4 9 2 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          11 14 2 12 -1.</_>
        <_>
          11 14 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 14 2 12 -1.</_>
        <_>
          2 14 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 11 3 12 -1.</_>
        <_>
          9 11 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 7 12 6 -1.</_>
        <_>
          4 7 6 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 1 12 9 -1.</_>
        <_>
          4 1 6 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 3 12 20 -1.</_>
        <_>
          1 3 6 10 2.</_>
        <_>
          7 13 6 10 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 8 6 10 -1.</_>
        <_>
          7 8 3 5 2.</_>
        <_>
          4 13 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 5 8 3 -1.</_>
        <_>
          6 5 4 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          3 15 8 7 -1.</_>
        <_>
          5 15 4 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 14 12 12 -1.</_>
        <_>
          4 18 4 4 9.</_></rects></_>
    <_>
      <rects>
        <_>
          5 12 4 16 -1.</_>
        <_>
          5 16 4 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 21 12 6 -1.</_>
        <_>
          4 21 4 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 17 8 7 -1.</_>
        <_>
          4 17 4 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 17 8 7 -1.</_>
        <_>
          6 17 4 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 4 6 5 -1.</_>
        <_>
          7 4 3 5 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 4 5 6 -1.</_>
        <_>
          7 4 5 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          8 3 6 7 -1.</_>
        <_>
          8 3 3 7 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 3 7 6 -1.</_>
        <_>
          6 3 7 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 4 2 22 -1.</_>
        <_>
          7 4 1 22 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 4 2 22 -1.</_>
        <_>
          6 4 1 22 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 8 2 12 -1.</_>
        <_>
          7 8 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 8 2 12 -1.</_>
        <_>
          6 8 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 8 10 5 -1.</_>
        <_>
          3 8 5 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 12 6 6 -1.</_>
        <_>
          6 12 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          8 8 4 16 -1.</_>
        <_>
          10 8 2 8 2.</_>
        <_>
          8 16 2 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 8 4 16 -1.</_>
        <_>
          2 8 2 8 2.</_>
        <_>
          4 16 2 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 21 12 4 -1.</_>
        <_>
          7 21 6 2 2.</_>
        <_>
          1 23 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 2 2 12 -1.</_>
        <_>
          4 8 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 10 6 4 -1.</_>
        <_>
          4 12 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 8 10 12 -1.</_>
        <_>
          2 12 10 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 17 6 8 -1.</_>
        <_>
          7 17 3 4 2.</_>
        <_>
          4 21 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 15 4 3 -1.</_>
        <_>
          6 16 4 1 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          9 20 3 5 -1.</_>
        <_>
          10 21 1 5 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          0 18 14 6 -1.</_>
        <_>
          7 18 7 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 0 3 24 -1.</_>
        <_>
          9 6 3 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 0 3 24 -1.</_>
        <_>
          2 6 3 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 2 4 6 -1.</_>
        <_>
          6 2 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 25 12 3 -1.</_>
        <_>
          5 25 4 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 4 12 14 -1.</_>
        <_>
          4 4 6 14 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 16 3 12 -1.</_>
        <_>
          7 16 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 18 4 6 -1.</_>
        <_>
          7 18 2 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 16 3 12 -1.</_>
        <_>
          7 16 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 16 3 12 -1.</_>
        <_>
          6 16 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 4 6 4 -1.</_>
        <_>
          7 4 3 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 1 7 4 -1.</_>
        <_>
          7 1 7 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 2 6 4 -1.</_>
        <_>
          7 2 3 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          3 10 8 6 -1.</_>
        <_>
          5 10 4 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 20 8 8 -1.</_>
        <_>
          7 20 4 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 15 8 5 -1.</_>
        <_>
          6 15 4 5 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          2 7 10 6 -1.</_>
        <_>
          7 7 5 3 2.</_>
        <_>
          2 10 5 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 20 4 4 -1.</_>
        <_>
          6 21 4 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          1 24 12 4 -1.</_>
        <_>
          4 24 6 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 4 6 6 -1.</_>
        <_>
          6 4 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 4 12 24 -1.</_>
        <_>
          7 4 6 12 2.</_>
        <_>
          1 16 6 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 4 3 15 -1.</_>
        <_>
          4 9 3 5 3.</_></rects></_>
    <_>
      <rects>
        <_>
          11 3 3 8 -1.</_>
        <_>
          11 3 3 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          4 9 2 13 -1.</_>
        <_>
          5 9 1 13 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 9 4 6 -1.</_>
        <_>
          6 9 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 17 8 3 -1.</_>
        <_>
          6 17 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 11 6 8 -1.</_>
        <_>
          7 11 3 4 2.</_>
        <_>
          4 15 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 0 14 27 -1.</_>
        <_>
          0 9 14 9 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 8 4 6 -1.</_>
        <_>
          5 11 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 2 4 12 -1.</_>
        <_>
          5 5 4 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 3 4 9 -1.</_>
        <_>
          6 6 4 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 3 4 9 -1.</_>
        <_>
          4 6 4 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          9 5 4 6 -1.</_>
        <_>
          9 5 4 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          5 5 6 4 -1.</_>
        <_>
          5 5 3 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          1 1 12 21 -1.</_>
        <_>
          4 1 6 21 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 25 12 3 -1.</_>
        <_>
          5 25 4 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          9 18 4 10 -1.</_>
        <_>
          9 18 2 10 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 16 9 3 -1.</_>
        <_>
          3 17 9 1 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          9 18 4 10 -1.</_>
        <_>
          9 18 2 10 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 18 4 10 -1.</_>
        <_>
          3 18 2 10 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 10 9 4 -1.</_>
        <_>
          4 12 9 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 0 12 5 -1.</_>
        <_>
          5 0 4 5 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 9 2 18 -1.</_>
        <_>
          7 15 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 22 6 6 -1.</_>
        <_>
          2 22 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 21 6 5 -1.</_>
        <_>
          5 21 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 21 6 5 -1.</_>
        <_>
          6 21 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 21 2 5 -1.</_>
        <_>
          9 21 1 5 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          0 17 6 8 -1.</_>
        <_>
          0 17 3 4 2.</_>
        <_>
          3 21 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 0 6 6 -1.</_>
        <_>
          6 0 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 1 6 14 -1.</_>
        <_>
          2 1 3 7 2.</_>
        <_>
          5 8 3 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 8 5 6 -1.</_>
        <_>
          6 11 5 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 8 4 6 -1.</_>
        <_>
          6 8 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 6 6 6 -1.</_>
        <_>
          4 8 6 2 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 5 6 4 -1.</_>
        <_>
          3 7 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 6 4 6 -1.</_>
        <_>
          7 6 2 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          4 5 6 4 -1.</_>
        <_>
          4 7 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 1 4 21 -1.</_>
        <_>
          8 1 2 21 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 2 6 20 -1.</_>
        <_>
          4 2 2 20 3.</_></rects></_>
    <_>
      <rects>
        <_>
          9 20 3 5 -1.</_>
        <_>
          10 21 1 5 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          0 24 6 4 -1.</_>
        <_>
          3 24 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 2 6 6 -1.</_>
        <_>
          6 2 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 2 4 6 -1.</_>
        <_>
          6 2 4 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          1 4 13 2 -1.</_>
        <_>
          1 5 13 1 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 11 6 7 -1.</_>
        <_>
          7 11 3 7 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          8 16 6 4 -1.</_>
        <_>
          8 16 6 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          1 3 12 24 -1.</_>
        <_>
          5 11 4 8 9.</_></rects></_>
    <_>
      <rects>
        <_>
          2 24 12 4 -1.</_>
        <_>
          8 24 6 2 2.</_>
        <_>
          2 26 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 24 12 4 -1.</_>
        <_>
          0 24 6 2 2.</_>
        <_>
          6 26 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 4 2 24 -1.</_>
        <_>
          7 4 1 12 2.</_>
        <_>
          6 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 8 6 6 -1.</_>
        <_>
          6 8 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 6 4 9 -1.</_>
        <_>
          6 6 2 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 8 8 7 -1.</_>
        <_>
          6 8 4 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 7 10 7 -1.</_>
        <_>
          3 7 5 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 7 10 7 -1.</_>
        <_>
          6 7 5 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 1 9 12 -1.</_>
        <_>
          7 5 3 4 9.</_></rects></_>
    <_>
      <rects>
        <_>
          1 1 9 12 -1.</_>
        <_>
          4 5 3 4 9.</_></rects></_>
    <_>
      <rects>
        <_>
          4 25 8 3 -1.</_>
        <_>
          4 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 16 12 7 -1.</_>
        <_>
          3 16 6 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 17 4 7 -1.</_>
        <_>
          9 17 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 17 4 7 -1.</_>
        <_>
          3 17 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 0 4 7 -1.</_>
        <_>
          7 0 2 7 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 0 7 4 -1.</_>
        <_>
          7 0 7 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          9 3 5 6 -1.</_>
        <_>
          9 3 5 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          0 10 6 12 -1.</_>
        <_>
          0 10 3 6 2.</_>
        <_>
          3 16 3 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 3 4 12 -1.</_>
        <_>
          10 3 2 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 3 4 12 -1.</_>
        <_>
          2 3 2 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 7 10 10 -1.</_>
        <_>
          7 7 5 5 2.</_>
        <_>
          2 12 5 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 16 4 9 -1.</_>
        <_>
          5 16 2 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 11 14 11 -1.</_>
        <_>
          0 11 7 11 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 16 5 6 -1.</_>
        <_>
          4 18 5 2 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          11 20 2 6 -1.</_>
        <_>
          11 20 1 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          1 18 4 6 -1.</_>
        <_>
          3 18 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          10 14 3 6 -1.</_>
        <_>
          11 15 1 6 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          4 14 6 3 -1.</_>
        <_>
          3 15 6 1 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 20 3 5 -1.</_>
        <_>
          8 21 1 5 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          2 25 8 3 -1.</_>
        <_>
          6 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 15 3 12 -1.</_>
        <_>
          10 15 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 15 6 2 -1.</_>
        <_>
          5 15 6 1 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 18 2 7 -1.</_>
        <_>
          7 18 1 7 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 20 5 3 -1.</_>
        <_>
          6 21 5 1 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          10 16 2 10 -1.</_>
        <_>
          10 16 1 10 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          4 16 10 2 -1.</_>
        <_>
          4 16 10 1 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          1 17 12 6 -1.</_>
        <_>
          4 17 6 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 15 6 8 -1.</_>
        <_>
          4 15 3 4 2.</_>
        <_>
          7 19 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 17 6 4 -1.</_>
        <_>
          9 19 2 4 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 17 4 6 -1.</_>
        <_>
          5 19 4 2 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          1 13 12 4 -1.</_>
        <_>
          1 13 6 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 2 8 12 -1.</_>
        <_>
          0 2 4 6 2.</_>
        <_>
          4 8 4 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 2 2 16 -1.</_>
        <_>
          6 10 2 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 8 8 4 -1.</_>
        <_>
          2 10 8 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 10 4 18 -1.</_>
        <_>
          5 19 4 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 3 3 12 -1.</_>
        <_>
          0 7 3 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 22 12 4 -1.</_>
        <_>
          7 22 6 2 2.</_>
        <_>
          1 24 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 19 7 2 -1.</_>
        <_>
          2 19 7 1 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          2 26 12 2 -1.</_>
        <_>
          2 26 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 11 6 14 -1.</_>
        <_>
          0 11 3 7 2.</_>
        <_>
          3 18 3 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 3 3 10 -1.</_>
        <_>
          7 8 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 17 6 6 -1.</_>
        <_>
          2 17 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          9 16 2 12 -1.</_>
        <_>
          9 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 16 6 3 -1.</_>
        <_>
          5 17 6 1 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          8 0 6 8 -1.</_>
        <_>
          10 2 2 8 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 4 8 6 -1.</_>
        <_>
          8 6 4 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          4 7 6 21 -1.</_>
        <_>
          4 14 6 7 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 0 8 18 -1.</_>
        <_>
          3 0 4 9 2.</_>
        <_>
          7 9 4 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 6 9 10 -1.</_>
        <_>
          6 6 3 10 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 21 4 3 -1.</_>
        <_>
          6 22 4 1 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          2 23 12 5 -1.</_>
        <_>
          6 23 4 5 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 16 3 12 -1.</_>
        <_>
          5 16 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 17 2 7 -1.</_>
        <_>
          7 17 1 7 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          0 5 14 10 -1.</_>
        <_>
          0 5 7 5 2.</_>
        <_>
          7 10 7 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 10 8 4 -1.</_>
        <_>
          3 10 4 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 12 10 4 -1.</_>
        <_>
          5 12 5 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 0 6 6 -1.</_>
        <_>
          7 0 3 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          2 3 10 7 -1.</_>
        <_>
          7 3 5 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 7 4 21 -1.</_>
        <_>
          5 7 2 21 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 2 2 24 -1.</_>
        <_>
          7 2 1 12 2.</_>
        <_>
          6 14 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 4 8 16 -1.</_>
        <_>
          3 8 8 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 16 2 12 -1.</_>
        <_>
          9 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 16 2 12 -1.</_>
        <_>
          4 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 2 6 6 -1.</_>
        <_>
          5 4 6 2 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 19 4 9 -1.</_>
        <_>
          3 19 2 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 10 4 16 -1.</_>
        <_>
          10 10 2 16 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 18 5 2 -1.</_>
        <_>
          5 18 5 1 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          5 4 6 4 -1.</_>
        <_>
          5 4 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 4 6 4 -1.</_>
        <_>
          6 4 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 5 6 8 -1.</_>
        <_>
          8 5 3 4 2.</_>
        <_>
          5 9 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 5 6 8 -1.</_>
        <_>
          3 5 3 4 2.</_>
        <_>
          6 9 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 3 8 12 -1.</_>
        <_>
          10 3 4 6 2.</_>
        <_>
          6 9 4 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 10 2 12 -1.</_>
        <_>
          2 10 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 0 13 3 -1.</_>
        <_>
          1 1 13 1 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 1 4 7 -1.</_>
        <_>
          4 1 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 21 2 5 -1.</_>
        <_>
          9 21 1 5 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          2 25 8 3 -1.</_>
        <_>
          6 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 16 3 12 -1.</_>
        <_>
          7 16 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 15 8 6 -1.</_>
        <_>
          0 15 4 3 2.</_>
        <_>
          4 18 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 26 12 2 -1.</_>
        <_>
          2 26 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 26 12 2 -1.</_>
        <_>
          6 26 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 1 13 3 -1.</_>
        <_>
          1 2 13 1 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 3 14 2 -1.</_>
        <_>
          7 3 7 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 16 12 4 -1.</_>
        <_>
          8 16 6 2 2.</_>
        <_>
          2 18 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 20 12 6 -1.</_>
        <_>
          3 20 6 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 15 8 7 -1.</_>
        <_>
          6 15 4 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 10 6 12 -1.</_>
        <_>
          4 10 3 6 2.</_>
        <_>
          7 16 3 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 0 4 6 -1.</_>
        <_>
          7 0 2 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 0 6 4 -1.</_>
        <_>
          7 0 6 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 18 8 6 -1.</_>
        <_>
          10 18 4 3 2.</_>
        <_>
          6 21 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 0 8 4 -1.</_>
        <_>
          6 0 8 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          2 15 10 6 -1.</_>
        <_>
          7 15 5 3 2.</_>
        <_>
          2 18 5 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 13 4 8 -1.</_>
        <_>
          0 17 4 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 9 14 9 -1.</_>
        <_>
          0 12 14 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 24 9 4 -1.</_>
        <_>
          5 24 3 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 24 12 4 -1.</_>
        <_>
          4 24 6 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 11 10 8 -1.</_>
        <_>
          0 11 5 4 2.</_>
        <_>
          5 15 5 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 9 6 4 -1.</_>
        <_>
          5 11 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 8 4 17 -1.</_>
        <_>
          2 8 2 17 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 2 4 12 -1.</_>
        <_>
          10 2 2 6 2.</_>
        <_>
          8 8 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 2 4 12 -1.</_>
        <_>
          2 2 2 6 2.</_>
        <_>
          4 8 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          10 7 4 14 -1.</_>
        <_>
          12 7 2 7 2.</_>
        <_>
          10 14 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 7 4 14 -1.</_>
        <_>
          0 7 2 7 2.</_>
        <_>
          2 14 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 8 10 6 -1.</_>
        <_>
          4 8 5 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 6 8 3 -1.</_>
        <_>
          6 6 4 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          2 5 12 3 -1.</_>
        <_>
          2 6 12 1 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 15 9 5 -1.</_>
        <_>
          5 15 3 5 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 1 14 15 -1.</_>
        <_>
          0 6 14 5 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 1 6 18 -1.</_>
        <_>
          3 7 2 6 9.</_></rects></_>
    <_>
      <rects>
        <_>
          4 2 9 10 -1.</_>
        <_>
          4 7 9 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 12 4 6 -1.</_>
        <_>
          7 12 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 4 3 21 -1.</_>
        <_>
          7 4 1 21 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 17 6 3 -1.</_>
        <_>
          5 18 6 1 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 16 2 4 -1.</_>
        <_>
          7 16 1 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 16 4 2 -1.</_>
        <_>
          7 16 4 1 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          8 20 2 6 -1.</_>
        <_>
          8 20 1 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 20 6 2 -1.</_>
        <_>
          6 20 6 1 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 4 6 6 -1.</_>
        <_>
          8 4 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 1 3 16 -1.</_>
        <_>
          2 1 1 16 3.</_></rects></_>
    <_>
      <rects>
        <_>
          12 14 2 10 -1.</_>
        <_>
          12 14 1 10 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          2 14 10 2 -1.</_>
        <_>
          2 14 10 1 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          3 1 6 27 -1.</_>
        <_>
          5 10 2 9 9.</_></rects></_>
    <_>
      <rects>
        <_>
          6 16 3 12 -1.</_>
        <_>
          7 16 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 6 8 22 -1.</_>
        <_>
          4 6 4 22 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 6 6 13 -1.</_>
        <_>
          6 6 2 13 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 11 6 6 -1.</_>
        <_>
          5 13 6 2 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          2 26 12 2 -1.</_>
        <_>
          2 26 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 8 6 9 -1.</_>
        <_>
          6 8 2 9 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 25 8 3 -1.</_>
        <_>
          6 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 24 6 4 -1.</_>
        <_>
          6 24 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 16 8 9 -1.</_>
        <_>
          4 16 4 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 16 8 9 -1.</_>
        <_>
          6 16 4 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 5 6 6 -1.</_>
        <_>
          7 5 3 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 15 6 6 -1.</_>
        <_>
          7 15 3 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          3 13 10 12 -1.</_>
        <_>
          3 19 10 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 6 10 3 -1.</_>
        <_>
          7 6 5 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 1 8 21 -1.</_>
        <_>
          3 8 8 7 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 7 6 6 -1.</_>
        <_>
          4 9 6 2 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 10 8 4 -1.</_>
        <_>
          4 12 8 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 5 6 6 -1.</_>
        <_>
          7 5 6 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          2 8 12 10 -1.</_>
        <_>
          2 8 6 10 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 4 8 10 -1.</_>
        <_>
          5 4 4 10 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 16 8 6 -1.</_>
        <_>
          7 16 4 3 2.</_>
        <_>
          3 19 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 3 2 24 -1.</_>
        <_>
          3 3 1 12 2.</_>
        <_>
          4 15 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 16 4 12 -1.</_>
        <_>
          10 16 2 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 16 4 12 -1.</_>
        <_>
          2 16 2 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 12 3 12 -1.</_>
        <_>
          9 12 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 8 5 6 -1.</_>
        <_>
          3 11 5 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 7 10 8 -1.</_>
        <_>
          2 11 10 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 12 3 12 -1.</_>
        <_>
          4 12 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 16 4 12 -1.</_>
        <_>
          5 16 2 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 22 4 2 -1.</_>
        <_>
          7 22 4 1 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 22 8 6 -1.</_>
        <_>
          10 22 4 3 2.</_>
        <_>
          6 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 14 2 14 -1.</_>
        <_>
          2 14 1 14 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 20 3 5 -1.</_>
        <_>
          10 21 1 5 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          5 20 5 3 -1.</_>
        <_>
          4 21 5 1 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 15 2 5 -1.</_>
        <_>
          7 15 1 5 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          1 17 10 6 -1.</_>
        <_>
          1 17 5 3 2.</_>
        <_>
          6 20 5 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 3 12 3 -1.</_>
        <_>
          5 3 4 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 3 5 6 -1.</_>
        <_>
          7 3 5 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 7 3 12 -1.</_>
        <_>
          8 7 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 7 3 12 -1.</_>
        <_>
          5 7 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 11 9 13 -1.</_>
        <_>
          8 11 3 13 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 5 3 21 -1.</_>
        <_>
          6 5 1 21 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 13 9 11 -1.</_>
        <_>
          7 13 3 11 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 13 9 11 -1.</_>
        <_>
          4 13 3 11 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 18 8 10 -1.</_>
        <_>
          9 18 4 5 2.</_>
        <_>
          5 23 4 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 5 14 14 -1.</_>
        <_>
          0 5 7 7 2.</_>
        <_>
          7 12 7 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 0 3 15 -1.</_>
        <_>
          10 0 1 15 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 0 6 20 -1.</_>
        <_>
          5 0 2 20 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 4 12 2 -1.</_>
        <_>
          2 5 12 1 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 3 12 3 -1.</_>
        <_>
          0 4 12 1 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 18 14 6 -1.</_>
        <_>
          7 18 7 3 2.</_>
        <_>
          0 21 7 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 0 3 15 -1.</_>
        <_>
          3 0 1 15 3.</_></rects></_>
    <_>
      <rects>
        <_>
          8 1 6 4 -1.</_>
        <_>
          8 1 3 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          2 7 6 6 -1.</_>
        <_>
          2 9 6 2 3.</_></rects></_>
    <_>
      <rects>
        <_>
          10 22 4 6 -1.</_>
        <_>
          10 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 7 3 12 -1.</_>
        <_>
          3 7 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 25 8 3 -1.</_>
        <_>
          6 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 22 4 6 -1.</_>
        <_>
          2 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 24 6 4 -1.</_>
        <_>
          8 24 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 0 4 9 -1.</_>
        <_>
          4 3 4 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          8 3 6 4 -1.</_>
        <_>
          8 3 6 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          2 0 6 22 -1.</_>
        <_>
          2 0 3 11 2.</_>
        <_>
          5 11 3 11 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 18 8 10 -1.</_>
        <_>
          10 18 4 5 2.</_>
        <_>
          6 23 4 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 22 6 6 -1.</_>
        <_>
          2 22 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          8 13 6 6 -1.</_>
        <_>
          8 15 6 2 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 13 6 6 -1.</_>
        <_>
          0 15 6 2 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 16 6 6 -1.</_>
        <_>
          3 16 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 2 3 21 -1.</_>
        <_>
          7 9 3 7 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 14 6 3 -1.</_>
        <_>
          3 15 6 1 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 25 8 3 -1.</_>
        <_>
          6 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 3 4 6 -1.</_>
        <_>
          7 3 4 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          4 9 8 16 -1.</_>
        <_>
          4 9 4 16 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 9 8 16 -1.</_>
        <_>
          6 9 4 16 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 3 7 24 -1.</_>
        <_>
          4 9 7 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 17 4 6 -1.</_>
        <_>
          3 17 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 2 6 4 -1.</_>
        <_>
          5 4 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 2 4 6 -1.</_>
        <_>
          7 2 2 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          4 9 6 4 -1.</_>
        <_>
          4 9 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 24 6 4 -1.</_>
        <_>
          4 24 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 0 6 8 -1.</_>
        <_>
          8 0 3 4 2.</_>
        <_>
          5 4 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 26 12 2 -1.</_>
        <_>
          6 26 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 0 6 8 -1.</_>
        <_>
          8 0 3 4 2.</_>
        <_>
          5 4 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 4 4 6 -1.</_>
        <_>
          7 4 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 0 6 8 -1.</_>
        <_>
          6 2 6 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 0 8 6 -1.</_>
        <_>
          8 2 4 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 17 3 4 -1.</_>
        <_>
          8 18 1 4 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          1 20 6 8 -1.</_>
        <_>
          1 20 3 4 2.</_>
        <_>
          4 24 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 15 2 12 -1.</_>
        <_>
          9 15 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 15 2 12 -1.</_>
        <_>
          4 15 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 2 6 4 -1.</_>
        <_>
          5 2 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 3 6 4 -1.</_>
        <_>
          6 3 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 4 6 24 -1.</_>
        <_>
          7 4 3 12 2.</_>
        <_>
          4 16 3 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 13 2 12 -1.</_>
        <_>
          7 13 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 16 3 12 -1.</_>
        <_>
          7 16 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 4 2 14 -1.</_>
        <_>
          7 4 1 14 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 3 4 25 -1.</_>
        <_>
          6 3 2 25 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 4 3 21 -1.</_>
        <_>
          6 4 1 21 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 6 2 12 -1.</_>
        <_>
          7 6 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 4 4 20 -1.</_>
        <_>
          5 4 2 10 2.</_>
        <_>
          7 14 2 10 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 4 6 24 -1.</_>
        <_>
          8 12 2 8 9.</_></rects></_>
    <_>
      <rects>
        <_>
          0 1 12 24 -1.</_>
        <_>
          6 1 6 24 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 6 7 22 -1.</_>
        <_>
          7 17 7 11 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 3 4 9 -1.</_>
        <_>
          4 6 4 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          8 4 6 8 -1.</_>
        <_>
          6 6 6 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 5 6 4 -1.</_>
        <_>
          7 5 6 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          5 1 4 6 -1.</_>
        <_>
          5 4 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 0 7 10 -1.</_>
        <_>
          0 5 7 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 2 3 24 -1.</_>
        <_>
          7 8 3 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 8 4 15 -1.</_>
        <_>
          2 8 2 15 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 25 8 3 -1.</_>
        <_>
          6 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 23 12 3 -1.</_>
        <_>
          5 23 4 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 22 8 6 -1.</_>
        <_>
          10 22 4 3 2.</_>
        <_>
          6 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 22 14 6 -1.</_>
        <_>
          0 22 7 3 2.</_>
        <_>
          7 25 7 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 3 12 3 -1.</_>
        <_>
          2 4 12 1 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 2 12 9 -1.</_>
        <_>
          4 5 4 3 9.</_></rects></_>
    <_>
      <rects>
        <_>
          1 0 12 12 -1.</_>
        <_>
          5 4 4 4 9.</_></rects></_>
    <_>
      <rects>
        <_>
          1 3 12 3 -1.</_>
        <_>
          1 4 12 1 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 4 12 3 -1.</_>
        <_>
          5 4 4 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 15 2 12 -1.</_>
        <_>
          2 15 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 20 12 5 -1.</_>
        <_>
          5 20 4 5 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 15 5 4 -1.</_>
        <_>
          6 16 5 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 2 3 21 -1.</_>
        <_>
          7 9 3 7 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 2 4 12 -1.</_>
        <_>
          2 2 2 6 2.</_>
        <_>
          4 8 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 22 8 6 -1.</_>
        <_>
          7 22 4 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 1 10 6 -1.</_>
        <_>
          0 1 5 3 2.</_>
        <_>
          5 4 5 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 11 9 6 -1.</_>
        <_>
          3 13 9 2 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 7 2 19 -1.</_>
        <_>
          7 7 1 19 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 10 8 16 -1.</_>
        <_>
          7 10 4 16 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 16 3 12 -1.</_>
        <_>
          6 16 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          10 13 4 15 -1.</_>
        <_>
          10 18 4 5 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 1 10 10 -1.</_>
        <_>
          2 1 5 5 2.</_>
        <_>
          7 6 5 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 19 2 7 -1.</_>
        <_>
          7 19 1 7 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          2 14 9 6 -1.</_>
        <_>
          5 14 3 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 13 10 14 -1.</_>
        <_>
          9 13 5 7 2.</_>
        <_>
          4 20 5 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 7 12 15 -1.</_>
        <_>
          5 12 4 5 9.</_></rects></_>
    <_>
      <rects>
        <_>
          6 2 2 24 -1.</_>
        <_>
          7 2 1 12 2.</_>
        <_>
          6 14 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 3 4 12 -1.</_>
        <_>
          5 9 4 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 24 6 4 -1.</_>
        <_>
          8 24 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 24 6 4 -1.</_>
        <_>
          3 24 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 8 12 4 -1.</_>
        <_>
          4 8 6 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 5 4 9 -1.</_>
        <_>
          5 8 4 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          9 18 4 6 -1.</_>
        <_>
          9 18 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 20 8 8 -1.</_>
        <_>
          2 20 4 4 2.</_>
        <_>
          6 24 4 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          11 15 2 8 -1.</_>
        <_>
          11 15 1 8 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          3 15 8 2 -1.</_>
        <_>
          3 15 8 1 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          5 9 4 6 -1.</_>
        <_>
          5 9 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 22 4 6 -1.</_>
        <_>
          2 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 26 14 2 -1.</_>
        <_>
          0 26 7 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 20 6 8 -1.</_>
        <_>
          3 20 3 4 2.</_>
        <_>
          6 24 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 16 2 12 -1.</_>
        <_>
          7 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 13 4 12 -1.</_>
        <_>
          5 13 2 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 22 12 2 -1.</_>
        <_>
          1 22 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 24 12 4 -1.</_>
        <_>
          0 24 6 2 2.</_>
        <_>
          6 26 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 8 6 4 -1.</_>
        <_>
          5 10 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 3 12 3 -1.</_>
        <_>
          0 4 12 1 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 4 6 6 -1.</_>
        <_>
          7 4 3 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 4 6 6 -1.</_>
        <_>
          7 4 6 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          8 3 6 8 -1.</_>
        <_>
          8 3 3 8 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          0 6 6 5 -1.</_>
        <_>
          3 6 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 3 3 12 -1.</_>
        <_>
          9 3 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 0 2 22 -1.</_>
        <_>
          7 0 1 22 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 3 3 12 -1.</_>
        <_>
          9 3 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 3 3 12 -1.</_>
        <_>
          4 3 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 6 3 12 -1.</_>
        <_>
          7 6 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 15 2 12 -1.</_>
        <_>
          6 15 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 8 6 10 -1.</_>
        <_>
          8 8 3 5 2.</_>
        <_>
          5 13 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 8 10 10 -1.</_>
        <_>
          2 8 5 5 2.</_>
        <_>
          7 13 5 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 9 6 10 -1.</_>
        <_>
          10 9 3 5 2.</_>
        <_>
          7 14 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 4 12 3 -1.</_>
        <_>
          0 5 12 1 3.</_></rects></_>
    <_>
      <rects>
        <_>
          9 16 2 12 -1.</_>
        <_>
          9 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 16 2 12 -1.</_>
        <_>
          4 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 20 12 6 -1.</_>
        <_>
          6 20 4 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 10 8 8 -1.</_>
        <_>
          2 10 4 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 12 14 6 -1.</_>
        <_>
          0 15 14 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 6 12 16 -1.</_>
        <_>
          1 14 12 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 7 3 12 -1.</_>
        <_>
          8 7 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 0 14 3 -1.</_>
        <_>
          0 1 14 1 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 0 13 3 -1.</_>
        <_>
          1 1 13 1 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 17 6 7 -1.</_>
        <_>
          2 17 2 7 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 24 6 4 -1.</_>
        <_>
          6 24 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 9 6 7 -1.</_>
        <_>
          3 9 3 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 9 6 18 -1.</_>
        <_>
          10 9 3 9 2.</_>
        <_>
          7 18 3 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 22 12 5 -1.</_>
        <_>
          4 22 4 5 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 9 6 10 -1.</_>
        <_>
          10 9 3 5 2.</_>
        <_>
          7 14 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 9 6 10 -1.</_>
        <_>
          1 9 3 5 2.</_>
        <_>
          4 14 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 22 4 6 -1.</_>
        <_>
          8 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 16 6 8 -1.</_>
        <_>
          0 16 3 4 2.</_>
        <_>
          3 20 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 0 6 8 -1.</_>
        <_>
          4 2 6 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 3 4 9 -1.</_>
        <_>
          5 6 4 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          9 8 4 19 -1.</_>
        <_>
          10 8 2 19 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 8 4 6 -1.</_>
        <_>
          5 11 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 2 7 6 -1.</_>
        <_>
          7 4 7 2 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 16 2 12 -1.</_>
        <_>
          1 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          11 0 3 17 -1.</_>
        <_>
          12 0 1 17 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 0 3 17 -1.</_>
        <_>
          1 0 1 17 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 13 4 14 -1.</_>
        <_>
          5 20 4 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 15 8 4 -1.</_>
        <_>
          6 15 4 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          5 17 8 6 -1.</_>
        <_>
          7 17 4 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 17 8 6 -1.</_>
        <_>
          3 17 4 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 11 4 6 -1.</_>
        <_>
          5 11 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 13 8 13 -1.</_>
        <_>
          5 13 4 13 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 6 8 4 -1.</_>
        <_>
          3 8 8 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 5 6 4 -1.</_>
        <_>
          7 5 6 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          4 9 6 8 -1.</_>
        <_>
          7 9 3 4 2.</_>
        <_>
          4 13 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 4 2 24 -1.</_>
        <_>
          6 4 1 12 2.</_>
        <_>
          7 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 24 6 4 -1.</_>
        <_>
          7 24 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 20 5 3 -1.</_>
        <_>
          6 21 5 1 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          3 15 9 12 -1.</_>
        <_>
          6 19 3 4 9.</_></rects></_>
    <_>
      <rects>
        <_>
          1 20 8 7 -1.</_>
        <_>
          3 20 4 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          10 12 2 14 -1.</_>
        <_>
          10 12 1 14 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 12 2 14 -1.</_>
        <_>
          3 12 1 14 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 6 8 4 -1.</_>
        <_>
          3 8 8 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 9 8 8 -1.</_>
        <_>
          3 9 4 4 2.</_>
        <_>
          7 13 4 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 2 12 24 -1.</_>
        <_>
          5 10 4 8 9.</_></rects></_>
    <_>
      <rects>
        <_>
          2 8 10 3 -1.</_>
        <_>
          7 8 5 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 15 8 8 -1.</_>
        <_>
          6 15 4 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 15 4 4 -1.</_>
        <_>
          6 16 4 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          4 12 6 6 -1.</_>
        <_>
          6 12 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 16 3 12 -1.</_>
        <_>
          5 16 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 8 3 12 -1.</_>
        <_>
          8 8 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 8 3 12 -1.</_>
        <_>
          5 8 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          10 17 4 6 -1.</_>
        <_>
          10 17 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 4 2 24 -1.</_>
        <_>
          5 4 1 12 2.</_>
        <_>
          6 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 25 8 3 -1.</_>
        <_>
          6 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 17 4 6 -1.</_>
        <_>
          2 17 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 11 6 12 -1.</_>
        <_>
          11 11 3 6 2.</_>
        <_>
          8 17 3 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 7 3 10 -1.</_>
        <_>
          3 12 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 6 4 6 -1.</_>
        <_>
          7 6 4 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          1 7 10 3 -1.</_>
        <_>
          6 7 5 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 6 4 6 -1.</_>
        <_>
          7 6 4 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 6 6 4 -1.</_>
        <_>
          7 6 3 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 0 4 6 -1.</_>
        <_>
          7 3 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 6 6 8 -1.</_>
        <_>
          4 6 3 4 2.</_>
        <_>
          7 10 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 12 6 16 -1.</_>
        <_>
          8 20 6 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 4 10 3 -1.</_>
        <_>
          5 4 5 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 2 4 13 -1.</_>
        <_>
          8 2 2 13 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 1 10 14 -1.</_>
        <_>
          1 1 5 7 2.</_>
        <_>
          6 8 5 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 25 8 3 -1.</_>
        <_>
          6 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 25 8 3 -1.</_>
        <_>
          4 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 13 3 13 -1.</_>
        <_>
          7 13 1 13 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 24 6 4 -1.</_>
        <_>
          4 24 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 8 4 7 -1.</_>
        <_>
          8 8 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 7 12 3 -1.</_>
        <_>
          0 8 12 1 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 6 6 6 -1.</_>
        <_>
          4 8 6 2 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 9 7 4 -1.</_>
        <_>
          3 11 7 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 7 4 18 -1.</_>
        <_>
          5 16 4 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 1 5 26 -1.</_>
        <_>
          4 14 5 13 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 22 8 6 -1.</_>
        <_>
          10 22 4 3 2.</_>
        <_>
          6 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 22 8 6 -1.</_>
        <_>
          0 22 4 3 2.</_>
        <_>
          4 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 21 8 6 -1.</_>
        <_>
          9 21 4 3 2.</_>
        <_>
          5 24 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 0 6 4 -1.</_>
        <_>
          6 0 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 1 6 5 -1.</_>
        <_>
          6 1 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 6 4 12 -1.</_>
        <_>
          6 6 2 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 8 4 7 -1.</_>
        <_>
          8 8 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 8 4 7 -1.</_>
        <_>
          4 8 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 12 8 3 -1.</_>
        <_>
          6 12 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 11 9 5 -1.</_>
        <_>
          4 11 3 5 3.</_></rects></_>
    <_>
      <rects>
        <_>
          10 3 4 14 -1.</_>
        <_>
          12 3 2 7 2.</_>
        <_>
          10 10 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 2 4 14 -1.</_>
        <_>
          0 2 2 7 2.</_>
        <_>
          2 9 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 9 13 6 -1.</_>
        <_>
          1 11 13 2 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 17 4 2 -1.</_>
        <_>
          7 17 4 1 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          10 15 3 6 -1.</_>
        <_>
          11 16 1 6 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          4 15 6 3 -1.</_>
        <_>
          3 16 6 1 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 19 2 7 -1.</_>
        <_>
          7 19 1 7 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          0 18 12 9 -1.</_>
        <_>
          3 18 6 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 19 2 7 -1.</_>
        <_>
          7 19 1 7 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 19 7 2 -1.</_>
        <_>
          7 19 7 1 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 15 3 13 -1.</_>
        <_>
          8 15 1 13 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 16 8 7 -1.</_>
        <_>
          4 16 4 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 21 10 6 -1.</_>
        <_>
          9 21 5 3 2.</_>
        <_>
          4 24 5 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 21 10 6 -1.</_>
        <_>
          0 21 5 3 2.</_>
        <_>
          5 24 5 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 14 6 7 -1.</_>
        <_>
          10 16 2 7 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          0 20 12 4 -1.</_>
        <_>
          0 20 6 2 2.</_>
        <_>
          6 22 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 14 12 10 -1.</_>
        <_>
          4 14 6 10 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 18 6 4 -1.</_>
        <_>
          6 18 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          11 11 2 16 -1.</_>
        <_>
          11 19 2 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 10 6 14 -1.</_>
        <_>
          3 10 3 7 2.</_>
        <_>
          6 17 3 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 9 4 6 -1.</_>
        <_>
          6 9 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 16 3 12 -1.</_>
        <_>
          6 16 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 3 12 18 -1.</_>
        <_>
          6 9 4 6 9.</_></rects></_>
    <_>
      <rects>
        <_>
          3 4 6 10 -1.</_>
        <_>
          3 4 3 5 2.</_>
        <_>
          6 9 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 18 6 4 -1.</_>
        <_>
          7 18 6 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 18 4 6 -1.</_>
        <_>
          7 18 2 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          5 8 4 13 -1.</_>
        <_>
          6 8 2 13 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 6 3 12 -1.</_>
        <_>
          3 6 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 15 12 12 -1.</_>
        <_>
          5 15 6 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 15 4 12 -1.</_>
        <_>
          5 15 2 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 19 9 9 -1.</_>
        <_>
          7 19 3 9 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 16 5 4 -1.</_>
        <_>
          6 17 5 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 14 6 8 -1.</_>
        <_>
          9 14 3 4 2.</_>
        <_>
          6 18 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 14 6 8 -1.</_>
        <_>
          2 14 3 4 2.</_>
        <_>
          5 18 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 2 10 16 -1.</_>
        <_>
          8 2 5 8 2.</_>
        <_>
          3 10 5 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 15 3 12 -1.</_>
        <_>
          6 15 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          8 23 6 4 -1.</_>
        <_>
          8 23 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 2 4 14 -1.</_>
        <_>
          4 2 2 7 2.</_>
        <_>
          6 9 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 7 8 6 -1.</_>
        <_>
          7 7 4 3 2.</_>
        <_>
          3 10 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 4 4 6 -1.</_>
        <_>
          2 7 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 0 6 24 -1.</_>
        <_>
          7 6 6 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 13 6 14 -1.</_>
        <_>
          0 13 3 7 2.</_>
        <_>
          3 20 3 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 19 10 6 -1.</_>
        <_>
          9 19 5 3 2.</_>
        <_>
          4 22 5 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 19 10 6 -1.</_>
        <_>
          0 19 5 3 2.</_>
        <_>
          5 22 5 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 18 8 10 -1.</_>
        <_>
          8 18 4 5 2.</_>
        <_>
          4 23 4 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 18 8 10 -1.</_>
        <_>
          2 18 4 5 2.</_>
        <_>
          6 23 4 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 14 4 14 -1.</_>
        <_>
          5 14 2 14 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 2 10 16 -1.</_>
        <_>
          1 2 5 8 2.</_>
        <_>
          6 10 5 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 12 14 16 -1.</_>
        <_>
          0 20 14 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 3 10 6 -1.</_>
        <_>
          2 3 5 3 2.</_>
        <_>
          7 6 5 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          10 1 3 26 -1.</_>
        <_>
          10 14 3 13 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 9 4 18 -1.</_>
        <_>
          0 18 4 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 21 4 6 -1.</_>
        <_>
          8 21 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 6 9 8 -1.</_>
        <_>
          5 6 3 8 3.</_></rects></_>
    <_>
      <rects>
        <_>
          9 21 4 6 -1.</_>
        <_>
          9 21 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 0 6 8 -1.</_>
        <_>
          3 0 3 4 2.</_>
        <_>
          6 4 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 20 4 7 -1.</_>
        <_>
          9 20 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 4 10 12 -1.</_>
        <_>
          6 4 5 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 1 2 24 -1.</_>
        <_>
          6 9 2 8 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 21 4 6 -1.</_>
        <_>
          4 21 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          10 1 3 26 -1.</_>
        <_>
          10 14 3 13 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 1 3 26 -1.</_>
        <_>
          1 14 3 13 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 9 12 14 -1.</_>
        <_>
          8 9 6 7 2.</_>
        <_>
          2 16 6 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 11 6 8 -1.</_>
        <_>
          4 15 6 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 9 9 18 -1.</_>
        <_>
          5 15 9 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 0 9 4 -1.</_>
        <_>
          4 0 3 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 7 4 6 -1.</_>
        <_>
          5 10 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 7 8 4 -1.</_>
        <_>
          3 9 8 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 16 12 6 -1.</_>
        <_>
          8 16 6 3 2.</_>
        <_>
          2 19 6 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 2 8 22 -1.</_>
        <_>
          1 2 4 11 2.</_>
        <_>
          5 13 4 11 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 19 6 7 -1.</_>
        <_>
          9 19 2 7 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 7 2 18 -1.</_>
        <_>
          6 13 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 8 8 16 -1.</_>
        <_>
          5 12 8 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 20 6 2 -1.</_>
        <_>
          5 20 6 1 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          10 19 3 6 -1.</_>
        <_>
          11 20 1 6 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          1 22 12 6 -1.</_>
        <_>
          4 22 6 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 25 12 3 -1.</_>
        <_>
          2 25 6 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 19 6 3 -1.</_>
        <_>
          3 20 6 1 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 20 6 7 -1.</_>
        <_>
          9 20 2 7 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 17 12 10 -1.</_>
        <_>
          4 17 4 10 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 18 12 4 -1.</_>
        <_>
          4 18 6 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 19 6 7 -1.</_>
        <_>
          3 19 2 7 3.</_></rects></_>
    <_>
      <rects>
        <_>
          10 22 4 6 -1.</_>
        <_>
          10 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 4 2 24 -1.</_>
        <_>
          1 4 1 12 2.</_>
        <_>
          2 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          10 5 4 10 -1.</_>
        <_>
          10 5 2 10 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 5 4 10 -1.</_>
        <_>
          2 5 2 10 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 10 3 15 -1.</_>
        <_>
          9 10 1 15 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 10 3 15 -1.</_>
        <_>
          4 10 1 15 3.</_></rects></_>
    <_>
      <rects>
        <_>
          8 7 3 17 -1.</_>
        <_>
          9 7 1 17 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 7 3 17 -1.</_>
        <_>
          4 7 1 17 3.</_></rects></_>
    <_>
      <rects>
        <_>
          9 0 3 13 -1.</_>
        <_>
          10 0 1 13 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 0 3 13 -1.</_>
        <_>
          3 0 1 13 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 3 12 5 -1.</_>
        <_>
          4 3 6 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 0 7 6 -1.</_>
        <_>
          4 2 7 2 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 2 4 8 -1.</_>
        <_>
          7 2 2 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 4 2 12 -1.</_>
        <_>
          7 4 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 16 3 6 -1.</_>
        <_>
          10 17 1 6 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          5 8 4 6 -1.</_>
        <_>
          7 8 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 5 12 21 -1.</_>
        <_>
          4 5 6 21 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 3 12 18 -1.</_>
        <_>
          2 9 12 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 1 12 4 -1.</_>
        <_>
          4 1 6 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 13 3 13 -1.</_>
        <_>
          7 13 1 13 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 1 6 12 -1.</_>
        <_>
          1 1 3 6 2.</_>
        <_>
          4 7 3 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 6 6 6 -1.</_>
        <_>
          9 6 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 6 6 6 -1.</_>
        <_>
          3 6 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 2 6 13 -1.</_>
        <_>
          9 2 2 13 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 2 6 13 -1.</_>
        <_>
          3 2 2 13 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 0 6 28 -1.</_>
        <_>
          6 0 2 28 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 13 14 3 -1.</_>
        <_>
          0 14 14 1 3.</_></rects></_>
    <_>
      <rects>
        <_>
          10 20 4 7 -1.</_>
        <_>
          10 20 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 8 2 12 -1.</_>
        <_>
          6 8 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 16 4 8 -1.</_>
        <_>
          5 16 2 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 0 6 8 -1.</_>
        <_>
          3 0 3 4 2.</_>
        <_>
          6 4 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 0 6 8 -1.</_>
        <_>
          8 0 3 4 2.</_>
        <_>
          5 4 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 0 6 8 -1.</_>
        <_>
          3 0 3 4 2.</_>
        <_>
          6 4 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          10 20 4 7 -1.</_>
        <_>
          10 20 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 15 4 12 -1.</_>
        <_>
          5 15 2 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 16 4 6 -1.</_>
        <_>
          7 16 2 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          3 2 6 9 -1.</_>
        <_>
          6 2 3 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 2 12 2 -1.</_>
        <_>
          2 2 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 2 12 2 -1.</_>
        <_>
          6 2 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 1 6 4 -1.</_>
        <_>
          6 1 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 2 4 6 -1.</_>
        <_>
          0 5 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 4 8 4 -1.</_>
        <_>
          5 6 8 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 8 12 2 -1.</_>
        <_>
          1 9 12 1 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 7 6 8 -1.</_>
        <_>
          8 9 6 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 7 6 8 -1.</_>
        <_>
          0 9 6 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          11 15 2 12 -1.</_>
        <_>
          11 15 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 15 3 12 -1.</_>
        <_>
          3 15 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          11 15 2 12 -1.</_>
        <_>
          11 15 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 12 6 16 -1.</_>
        <_>
          1 12 3 8 2.</_>
        <_>
          4 20 3 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 10 10 5 -1.</_>
        <_>
          4 10 5 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 16 8 3 -1.</_>
        <_>
          3 17 8 1 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          2 25 12 3 -1.</_>
        <_>
          6 25 4 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 10 10 8 -1.</_>
        <_>
          1 10 5 4 2.</_>
        <_>
          6 14 5 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 12 14 6 -1.</_>
        <_>
          7 12 7 3 2.</_>
        <_>
          0 15 7 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 20 8 8 -1.</_>
        <_>
          2 20 4 4 2.</_>
        <_>
          6 24 4 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          12 16 2 7 -1.</_>
        <_>
          12 16 1 7 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          1 17 12 4 -1.</_>
        <_>
          4 17 6 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 9 6 14 -1.</_>
        <_>
          7 9 2 14 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 9 6 14 -1.</_>
        <_>
          5 9 2 14 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 8 9 12 -1.</_>
        <_>
          6 12 3 4 9.</_></rects></_>
    <_>
      <rects>
        <_>
          5 4 4 19 -1.</_>
        <_>
          7 4 2 19 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 5 4 19 -1.</_>
        <_>
          5 5 2 19 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 10 10 18 -1.</_>
        <_>
          2 10 5 9 2.</_>
        <_>
          7 19 5 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 3 9 15 -1.</_>
        <_>
          3 8 9 5 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 7 8 12 -1.</_>
        <_>
          3 11 8 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 9 6 8 -1.</_>
        <_>
          6 11 6 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 16 2 12 -1.</_>
        <_>
          2 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          11 3 3 18 -1.</_>
        <_>
          11 12 3 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 3 3 18 -1.</_>
        <_>
          0 12 3 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 8 10 6 -1.</_>
        <_>
          7 8 5 3 2.</_>
        <_>
          2 11 5 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 3 3 23 -1.</_>
        <_>
          1 3 1 23 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 3 6 5 -1.</_>
        <_>
          7 3 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 0 10 28 -1.</_>
        <_>
          2 14 10 14 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 17 8 6 -1.</_>
        <_>
          10 17 4 3 2.</_>
        <_>
          6 20 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 13 4 14 -1.</_>
        <_>
          4 13 2 7 2.</_>
        <_>
          6 20 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          12 7 2 12 -1.</_>
        <_>
          12 7 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 3 6 5 -1.</_>
        <_>
          4 3 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          12 7 2 12 -1.</_>
        <_>
          12 7 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 7 2 12 -1.</_>
        <_>
          1 7 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 12 6 6 -1.</_>
        <_>
          6 12 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 10 10 5 -1.</_>
        <_>
          5 10 5 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 9 12 8 -1.</_>
        <_>
          5 9 6 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 7 4 12 -1.</_>
        <_>
          2 7 2 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          11 16 3 6 -1.</_>
        <_>
          12 17 1 6 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          5 16 2 12 -1.</_>
        <_>
          6 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          11 16 3 6 -1.</_>
        <_>
          12 17 1 6 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 6 2 14 -1.</_>
        <_>
          7 6 1 14 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 2 8 11 -1.</_>
        <_>
          5 2 4 11 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 3 3 22 -1.</_>
        <_>
          6 3 1 22 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 7 4 6 -1.</_>
        <_>
          5 10 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 9 6 4 -1.</_>
        <_>
          4 11 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 25 8 3 -1.</_>
        <_>
          5 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 6 6 4 -1.</_>
        <_>
          4 8 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 5 10 8 -1.</_>
        <_>
          4 9 10 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 12 6 6 -1.</_>
        <_>
          0 15 6 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 25 8 3 -1.</_>
        <_>
          5 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 13 10 6 -1.</_>
        <_>
          0 13 5 3 2.</_>
        <_>
          5 16 5 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 7 3 15 -1.</_>
        <_>
          7 7 1 15 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 1 14 15 -1.</_>
        <_>
          0 6 14 5 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 4 8 8 -1.</_>
        <_>
          6 6 8 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 10 12 8 -1.</_>
        <_>
          0 12 12 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 1 6 6 -1.</_>
        <_>
          8 3 6 2 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 1 6 6 -1.</_>
        <_>
          0 3 6 2 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 25 8 3 -1.</_>
        <_>
          5 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 0 6 6 -1.</_>
        <_>
          6 0 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 16 12 4 -1.</_>
        <_>
          4 16 6 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 4 6 4 -1.</_>
        <_>
          8 4 6 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 4 4 6 -1.</_>
        <_>
          6 4 2 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          4 4 6 4 -1.</_>
        <_>
          4 6 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 15 7 4 -1.</_>
        <_>
          6 15 7 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          4 4 6 4 -1.</_>
        <_>
          4 6 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 4 6 4 -1.</_>
        <_>
          4 6 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 2 3 12 -1.</_>
        <_>
          9 2 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 2 3 12 -1.</_>
        <_>
          4 2 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 0 8 28 -1.</_>
        <_>
          6 0 4 28 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 0 8 28 -1.</_>
        <_>
          4 0 4 28 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 15 4 8 -1.</_>
        <_>
          8 15 2 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 22 8 6 -1.</_>
        <_>
          0 22 4 3 2.</_>
        <_>
          4 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 20 4 4 -1.</_>
        <_>
          8 21 2 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          4 15 6 6 -1.</_>
        <_>
          6 15 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 10 6 9 -1.</_>
        <_>
          6 10 2 9 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 8 4 17 -1.</_>
        <_>
          6 8 2 17 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 16 2 12 -1.</_>
        <_>
          7 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 11 2 12 -1.</_>
        <_>
          7 11 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 12 14 12 -1.</_>
        <_>
          0 12 7 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 4 4 24 -1.</_>
        <_>
          0 10 4 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 0 4 8 -1.</_>
        <_>
          8 4 4 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 24 12 4 -1.</_>
        <_>
          4 24 6 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 9 8 18 -1.</_>
        <_>
          5 18 8 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 4 3 22 -1.</_>
        <_>
          2 4 1 22 3.</_></rects></_>
    <_>
      <rects>
        <_>
          11 16 2 12 -1.</_>
        <_>
          11 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 16 2 12 -1.</_>
        <_>
          2 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 1 8 6 -1.</_>
        <_>
          8 1 4 3 2.</_>
        <_>
          4 4 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 1 8 6 -1.</_>
        <_>
          2 1 4 3 2.</_>
        <_>
          6 4 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 0 8 20 -1.</_>
        <_>
          4 10 8 10 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 5 9 6 -1.</_>
        <_>
          0 8 9 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 4 8 16 -1.</_>
        <_>
          3 8 8 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 11 6 16 -1.</_>
        <_>
          3 19 6 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 9 6 12 -1.</_>
        <_>
          7 9 3 6 2.</_>
        <_>
          4 15 3 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 20 4 3 -1.</_>
        <_>
          6 21 4 1 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          2 6 12 2 -1.</_>
        <_>
          2 7 12 1 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 2 6 4 -1.</_>
        <_>
          4 2 6 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          8 1 6 5 -1.</_>
        <_>
          8 1 3 5 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 4 4 6 -1.</_>
        <_>
          7 4 4 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          4 5 6 20 -1.</_>
        <_>
          4 10 6 10 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 8 4 13 -1.</_>
        <_>
          4 8 2 13 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 0 14 8 -1.</_>
        <_>
          7 0 7 4 2.</_>
        <_>
          0 4 7 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 0 4 6 -1.</_>
        <_>
          7 0 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 2 4 12 -1.</_>
        <_>
          6 6 4 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 14 4 7 -1.</_>
        <_>
          4 14 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 4 6 4 -1.</_>
        <_>
          5 4 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 0 8 19 -1.</_>
        <_>
          7 0 4 19 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 5 4 15 -1.</_>
        <_>
          5 5 2 15 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 11 12 3 -1.</_>
        <_>
          1 12 12 1 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 4 6 4 -1.</_>
        <_>
          5 4 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 10 5 6 -1.</_>
        <_>
          1 13 5 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 4 6 4 -1.</_>
        <_>
          5 4 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 13 13 3 -1.</_>
        <_>
          0 14 13 1 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 4 6 4 -1.</_>
        <_>
          5 4 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 4 6 4 -1.</_>
        <_>
          6 4 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 22 4 6 -1.</_>
        <_>
          8 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 22 4 6 -1.</_>
        <_>
          4 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 22 4 6 -1.</_>
        <_>
          8 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 22 4 6 -1.</_>
        <_>
          4 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 13 14 3 -1.</_>
        <_>
          0 14 14 1 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 19 7 2 -1.</_>
        <_>
          7 19 7 1 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 9 6 12 -1.</_>
        <_>
          6 13 6 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 26 12 2 -1.</_>
        <_>
          6 26 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 25 12 3 -1.</_>
        <_>
          2 25 6 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 24 14 4 -1.</_>
        <_>
          0 24 7 2 2.</_>
        <_>
          7 26 7 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          12 3 2 12 -1.</_>
        <_>
          12 3 1 12 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          3 2 4 12 -1.</_>
        <_>
          3 2 2 6 2.</_>
        <_>
          5 8 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 1 3 17 -1.</_>
        <_>
          7 1 1 17 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 6 8 7 -1.</_>
        <_>
          5 6 4 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 0 3 12 -1.</_>
        <_>
          7 0 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 0 3 12 -1.</_>
        <_>
          6 0 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 1 3 17 -1.</_>
        <_>
          7 1 1 17 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 8 8 8 -1.</_>
        <_>
          3 8 4 4 2.</_>
        <_>
          7 12 4 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 15 3 12 -1.</_>
        <_>
          9 15 1 12 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 16 10 12 -1.</_>
        <_>
          0 16 5 6 2.</_>
        <_>
          5 22 5 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 2 8 22 -1.</_>
        <_>
          10 2 4 11 2.</_>
        <_>
          6 13 4 11 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 25 12 3 -1.</_>
        <_>
          6 25 6 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 14 12 14 -1.</_>
        <_>
          2 14 6 14 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 14 8 10 -1.</_>
        <_>
          4 14 4 10 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 13 6 14 -1.</_>
        <_>
          7 13 2 14 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 13 6 14 -1.</_>
        <_>
          5 13 2 14 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 12 8 13 -1.</_>
        <_>
          6 12 4 13 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 12 8 13 -1.</_>
        <_>
          4 12 4 13 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 22 10 6 -1.</_>
        <_>
          8 22 5 3 2.</_>
        <_>
          3 25 5 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 22 10 6 -1.</_>
        <_>
          1 22 5 3 2.</_>
        <_>
          6 25 5 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 5 6 9 -1.</_>
        <_>
          8 8 6 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 8 12 6 -1.</_>
        <_>
          0 8 6 3 2.</_>
        <_>
          6 11 6 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 6 3 13 -1.</_>
        <_>
          10 6 1 13 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 2 5 24 -1.</_>
        <_>
          0 14 5 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          11 11 3 8 -1.</_>
        <_>
          11 15 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 1 3 17 -1.</_>
        <_>
          6 1 1 17 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 5 8 8 -1.</_>
        <_>
          7 5 4 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 16 2 12 -1.</_>
        <_>
          4 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 3 6 18 -1.</_>
        <_>
          8 9 2 6 9.</_></rects></_>
    <_>
      <rects>
        <_>
          4 2 4 12 -1.</_>
        <_>
          4 6 4 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 1 4 12 -1.</_>
        <_>
          5 4 4 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 0 12 12 -1.</_>
        <_>
          5 4 4 4 9.</_></rects></_>
    <_>
      <rects>
        <_>
          6 0 6 5 -1.</_>
        <_>
          6 0 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 0 6 5 -1.</_>
        <_>
          5 0 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 5 3 21 -1.</_>
        <_>
          7 5 1 21 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 0 6 24 -1.</_>
        <_>
          1 0 3 12 2.</_>
        <_>
          4 12 3 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 18 4 6 -1.</_>
        <_>
          9 19 2 6 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          3 0 6 8 -1.</_>
        <_>
          3 0 3 4 2.</_>
        <_>
          6 4 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 24 9 4 -1.</_>
        <_>
          8 24 3 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 20 8 6 -1.</_>
        <_>
          2 20 4 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 22 6 6 -1.</_>
        <_>
          9 22 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 22 6 6 -1.</_>
        <_>
          3 22 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 15 6 11 -1.</_>
        <_>
          3 15 2 11 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 6 6 4 -1.</_>
        <_>
          4 8 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 16 4 11 -1.</_>
        <_>
          2 16 2 11 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 16 6 6 -1.</_>
        <_>
          10 16 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 16 12 12 -1.</_>
        <_>
          4 20 4 4 9.</_></rects></_>
    <_>
      <rects>
        <_>
          8 10 6 18 -1.</_>
        <_>
          8 16 6 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 12 5 16 -1.</_>
        <_>
          0 20 5 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          11 12 3 16 -1.</_>
        <_>
          11 16 3 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 13 14 12 -1.</_>
        <_>
          0 13 7 6 2.</_>
        <_>
          7 19 7 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 12 10 16 -1.</_>
        <_>
          8 12 5 8 2.</_>
        <_>
          3 20 5 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 11 5 12 -1.</_>
        <_>
          3 17 5 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 0 6 18 -1.</_>
        <_>
          8 6 2 6 9.</_></rects></_>
    <_>
      <rects>
        <_>
          6 4 2 14 -1.</_>
        <_>
          6 11 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 15 8 11 -1.</_>
        <_>
          5 15 4 11 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 2 8 11 -1.</_>
        <_>
          5 2 4 11 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 4 12 5 -1.</_>
        <_>
          5 4 4 5 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 3 8 25 -1.</_>
        <_>
          5 3 4 25 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 16 6 6 -1.</_>
        <_>
          10 16 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 16 6 6 -1.</_>
        <_>
          2 16 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 13 3 14 -1.</_>
        <_>
          8 13 1 14 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 8 4 12 -1.</_>
        <_>
          2 8 2 6 2.</_>
        <_>
          4 14 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 13 3 14 -1.</_>
        <_>
          8 13 1 14 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 13 3 14 -1.</_>
        <_>
          5 13 1 14 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 3 9 6 -1.</_>
        <_>
          5 5 9 2 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 8 6 4 -1.</_>
        <_>
          3 10 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          11 3 3 12 -1.</_>
        <_>
          11 7 3 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 8 8 3 -1.</_>
        <_>
          4 8 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 13 12 8 -1.</_>
        <_>
          7 13 6 4 2.</_>
        <_>
          1 17 6 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 18 10 10 -1.</_>
        <_>
          7 18 5 10 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 8 4 6 -1.</_>
        <_>
          5 8 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 0 13 3 -1.</_>
        <_>
          0 1 13 1 3.</_></rects></_>
    <_>
      <rects>
        <_>
          8 1 6 8 -1.</_>
        <_>
          11 1 3 4 2.</_>
        <_>
          8 5 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 1 6 8 -1.</_>
        <_>
          0 1 3 4 2.</_>
        <_>
          3 5 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 18 2 7 -1.</_>
        <_>
          7 18 1 7 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          7 18 7 2 -1.</_>
        <_>
          7 18 7 1 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          4 22 9 4 -1.</_>
        <_>
          7 22 3 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 4 5 6 -1.</_>
        <_>
          0 7 5 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          11 3 3 12 -1.</_>
        <_>
          11 7 3 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 3 3 12 -1.</_>
        <_>
          0 7 3 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 0 6 8 -1.</_>
        <_>
          8 0 3 4 2.</_>
        <_>
          5 4 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 0 6 8 -1.</_>
        <_>
          3 0 3 4 2.</_>
        <_>
          6 4 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 3 2 12 -1.</_>
        <_>
          8 3 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 6 9 8 -1.</_>
        <_>
          0 8 9 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 2 6 4 -1.</_>
        <_>
          4 4 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 18 4 10 -1.</_>
        <_>
          3 18 2 10 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 18 4 6 -1.</_>
        <_>
          9 18 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 2 12 3 -1.</_>
        <_>
          1 3 12 1 3.</_></rects></_>
    <_>
      <rects>
        <_>
          9 18 4 6 -1.</_>
        <_>
          9 18 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 2 14 3 -1.</_>
        <_>
          0 3 14 1 3.</_></rects></_>
    <_>
      <rects>
        <_>
          9 19 4 6 -1.</_>
        <_>
          9 19 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 19 4 6 -1.</_>
        <_>
          3 19 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 7 3 15 -1.</_>
        <_>
          8 12 3 5 3.</_></rects></_>
    <_>
      <rects>
        <_>
          7 20 4 4 -1.</_>
        <_>
          6 21 4 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          9 3 4 6 -1.</_>
        <_>
          9 3 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 3 4 6 -1.</_>
        <_>
          3 3 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 7 3 15 -1.</_>
        <_>
          8 12 3 5 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 7 3 15 -1.</_>
        <_>
          3 12 3 5 3.</_></rects></_>
    <_>
      <rects>
        <_>
          9 12 2 12 -1.</_>
        <_>
          9 18 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 12 2 12 -1.</_>
        <_>
          3 18 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 0 5 6 -1.</_>
        <_>
          8 3 5 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 0 5 6 -1.</_>
        <_>
          1 3 5 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 6 8 8 -1.</_>
        <_>
          3 8 8 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 4 6 14 -1.</_>
        <_>
          4 4 2 14 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 10 7 16 -1.</_>
        <_>
          5 18 7 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 10 6 10 -1.</_>
        <_>
          6 10 2 10 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 10 4 12 -1.</_>
        <_>
          5 13 4 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 0 6 18 -1.</_>
        <_>
          4 6 2 6 9.</_></rects></_>
    <_>
      <rects>
        <_>
          1 11 12 4 -1.</_>
        <_>
          1 12 12 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 15 5 2 -1.</_>
        <_>
          7 15 5 1 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          4 24 6 4 -1.</_>
        <_>
          4 24 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 18 5 4 -1.</_>
        <_>
          4 19 5 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          3 1 6 25 -1.</_>
        <_>
          6 1 3 25 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 13 2 12 -1.</_>
        <_>
          6 13 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 4 2 13 -1.</_>
        <_>
          7 4 1 13 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 2 6 19 -1.</_>
        <_>
          10 2 2 19 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 2 6 19 -1.</_>
        <_>
          2 2 2 19 3.</_></rects></_>
    <_>
      <rects>
        <_>
          9 1 4 13 -1.</_>
        <_>
          10 1 2 13 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 1 4 13 -1.</_>
        <_>
          2 1 2 13 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 3 8 3 -1.</_>
        <_>
          3 3 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 5 10 18 -1.</_>
        <_>
          2 11 10 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 8 9 12 -1.</_>
        <_>
          6 12 3 4 9.</_></rects></_>
    <_>
      <rects>
        <_>
          4 4 6 4 -1.</_>
        <_>
          4 6 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 8 10 8 -1.</_>
        <_>
          9 8 5 4 2.</_>
        <_>
          4 12 5 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 8 6 6 -1.</_>
        <_>
          4 8 2 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 10 6 10 -1.</_>
        <_>
          7 10 3 5 2.</_>
        <_>
          4 15 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 9 8 14 -1.</_>
        <_>
          3 9 4 7 2.</_>
        <_>
          7 16 4 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 7 6 20 -1.</_>
        <_>
          7 7 3 10 2.</_>
        <_>
          4 17 3 10 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 0 6 8 -1.</_>
        <_>
          3 0 3 4 2.</_>
        <_>
          6 4 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 5 4 6 -1.</_>
        <_>
          7 5 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 7 8 8 -1.</_>
        <_>
          3 7 4 4 2.</_>
        <_>
          7 11 4 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 9 6 4 -1.</_>
        <_>
          5 11 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 9 4 9 -1.</_>
        <_>
          0 12 4 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          8 6 4 12 -1.</_>
        <_>
          8 10 4 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 7 10 6 -1.</_>
        <_>
          1 9 10 2 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 7 14 12 -1.</_>
        <_>
          0 10 14 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 9 6 4 -1.</_>
        <_>
          3 11 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 1 4 8 -1.</_>
        <_>
          8 1 2 8 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          2 6 4 12 -1.</_>
        <_>
          2 10 4 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          2 16 12 4 -1.</_>
        <_>
          8 16 6 2 2.</_>
        <_>
          2 18 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 20 4 4 -1.</_>
        <_>
          6 21 4 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          9 16 2 12 -1.</_>
        <_>
          9 16 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 18 5 4 -1.</_>
        <_>
          4 19 5 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          8 1 4 8 -1.</_>
        <_>
          8 1 2 8 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          2 6 9 7 -1.</_>
        <_>
          5 6 3 7 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 6 8 12 -1.</_>
        <_>
          3 9 8 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 0 9 21 -1.</_>
        <_>
          3 7 3 7 9.</_></rects></_>
    <_>
      <rects>
        <_>
          8 1 4 8 -1.</_>
        <_>
          8 1 2 8 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          2 1 5 18 -1.</_>
        <_>
          2 10 5 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 1 6 7 -1.</_>
        <_>
          8 1 3 7 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          0 3 2 16 -1.</_>
        <_>
          1 3 1 16 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 18 4 8 -1.</_>
        <_>
          9 18 2 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 18 12 9 -1.</_>
        <_>
          3 18 6 9 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 2 12 3 -1.</_>
        <_>
          5 2 4 3 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 1 7 6 -1.</_>
        <_>
          6 1 7 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 9 3 13 -1.</_>
        <_>
          7 9 1 13 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 1 6 6 -1.</_>
        <_>
          6 1 6 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          6 4 4 11 -1.</_>
        <_>
          6 4 2 11 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 4 4 11 -1.</_>
        <_>
          6 4 2 11 2.</_></rects></_>
    <_>
      <rects>
        <_>
          8 1 4 8 -1.</_>
        <_>
          8 1 2 8 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          1 20 4 8 -1.</_>
        <_>
          3 20 2 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 22 4 6 -1.</_>
        <_>
          9 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 22 4 6 -1.</_>
        <_>
          3 22 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          9 0 3 22 -1.</_>
        <_>
          10 0 1 22 3.</_></rects></_>
    <_>
      <rects>
        <_>
          3 21 8 6 -1.</_>
        <_>
          5 21 4 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 11 3 15 -1.</_>
        <_>
          7 11 1 15 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 1 8 4 -1.</_>
        <_>
          6 1 8 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          2 16 12 4 -1.</_>
        <_>
          8 16 6 2 2.</_>
        <_>
          2 18 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 16 12 4 -1.</_>
        <_>
          0 16 6 2 2.</_>
        <_>
          6 18 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 10 3 12 -1.</_>
        <_>
          6 14 3 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 13 6 14 -1.</_>
        <_>
          4 20 6 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 9 9 15 -1.</_>
        <_>
          6 14 3 5 9.</_></rects></_>
    <_>
      <rects>
        <_>
          4 10 9 4 -1.</_>
        <_>
          7 13 3 4 3.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          3 7 8 7 -1.</_>
        <_>
          3 7 4 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 9 4 6 -1.</_>
        <_>
          6 9 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 9 6 11 -1.</_>
        <_>
          6 9 2 11 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 11 4 12 -1.</_>
        <_>
          1 15 4 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          9 0 2 12 -1.</_>
        <_>
          9 0 1 12 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 4 4 16 -1.</_>
        <_>
          2 4 2 8 2.</_>
        <_>
          4 12 2 8 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 8 5 14 -1.</_>
        <_>
          5 15 5 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 0 3 22 -1.</_>
        <_>
          3 0 1 22 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 25 8 3 -1.</_>
        <_>
          6 25 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 6 8 22 -1.</_>
        <_>
          1 17 8 11 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 15 6 8 -1.</_>
        <_>
          7 15 3 4 2.</_>
        <_>
          4 19 3 4 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 13 4 14 -1.</_>
        <_>
          5 13 2 7 2.</_>
        <_>
          7 20 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          2 16 10 12 -1.</_>
        <_>
          7 16 5 6 2.</_>
        <_>
          2 22 5 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 15 8 3 -1.</_>
        <_>
          4 15 4 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          2 0 12 3 -1.</_>
        <_>
          2 1 12 1 3.</_></rects></_>
    <_>
      <rects>
        <_>
          0 5 9 22 -1.</_>
        <_>
          3 5 3 22 3.</_></rects></_>
    <_>
      <rects>
        <_>
          4 9 6 4 -1.</_>
        <_>
          4 11 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 14 6 2 -1.</_>
        <_>
          4 14 6 1 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          8 12 6 4 -1.</_>
        <_>
          8 12 3 4 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          5 16 8 4 -1.</_>
        <_>
          4 17 8 2 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          5 15 4 6 -1.</_>
        <_>
          5 15 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          5 9 2 14 -1.</_>
        <_>
          5 16 2 7 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 6 6 12 -1.</_>
        <_>
          6 10 6 4 3.</_></rects></_>
    <_>
      <rects>
        <_>
          1 20 12 6 -1.</_>
        <_>
          1 20 6 3 2.</_>
        <_>
          7 23 6 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          4 8 6 4 -1.</_>
        <_>
          4 10 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          1 6 9 6 -1.</_>
        <_>
          1 8 9 2 3.</_></rects></_>
    <_>
      <rects>
        <_>
          5 6 6 4 -1.</_>
        <_>
          5 8 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          3 3 8 6 -1.</_>
        <_>
          3 3 4 3 2.</_>
        <_>
          7 6 4 3 2.</_></rects></_>
    <_>
      <rects>
        <_>
          6 23 6 5 -1.</_>
        <_>
          6 23 3 5 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 3 12 4 -1.</_>
        <_>
          0 3 6 2 2.</_>
        <_>
          6 5 6 2 2.</_></rects></_>
    <_>
      <rects>
        <_>
          7 4 6 18 -1.</_>
        <_>
          7 10 6 6 3.</_></rects></_>
    <_>
      <rects>
        <_>
          6 12 4 6 -1.</_>
        <_>
          6 12 4 3 2.</_></rects>
      <tilted>1</tilted></_>
    <_>
      <rects>
        <_>
          2 15 12 6 -1.</_>
        <_>
          5 15 6 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          0 5 4 12 -1.</_>
        <_>
          0 5 2 6 2.</_>
        <_>
          2 11 2 6 2.</_></rects></_>
    <_>
      <rects>
        <_>
          10 4 4 16 -1.</_>
        <_>
          12 4 2 8 2.</_>
        <_>
          10 12 2 8 2.</_></rects></_></features></cascade>
</opencv_storage>