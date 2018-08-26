
.. _l-proj_domo_auto:

Automatisation, Objets connectés, Reconnaissance
================================================

.. contents::
    :local:

Pas tout-à-fait prêt pour cette année.
Ce sujet serait pour quelques aventureux.

.. _l-tech-smart:

Application smartphone
----------------------

.. index:: kivy, smartphone

Le module `kivy <http://kivy.org/#home>`_ permet d'implémenter des
applications pour smartphone ou tablette en python.

.. _l-tech-domo:

Domotique
---------

.. index:: arduino, domotique

L'idée serait d'utiliser un module `Arduino <http://www.arduino.cc/>`_, d'y ajouter
quelques capteurs, de récupérer les données puis d'afficher quelques
graphiques avec quelques statistiques.

**Articles**

* `Arduino and Python <http://playground.arduino.cc/Interfacing/Python>`_
* `Communiquez avec votre Arduino, en Python <http://www.dad3zero.net/201207/communiquez-avec-arduino-en-python/>`_

**Modules**

* `nanpy <https://github.com/astagi/nanpy>`_
* `pyFirmata <https://github.com/tino/pyFirmata>`_
* `Python-Arduino-Command-API <https://github.com/thearn/Python-Arduino-Command-API>`_

.. _l-visage-reel:

Expressions du visages en temps réel (2017)
-------------------------------------------

L'article
`Wink Detection using Dlib and OpenCV <http://www.codesofinterest.com/2017/06/wink-detection-using-dlib-and-opencv.html>`_
donne un exemple de code qui permet de détecter si une personne cligne des yeux. Le programme
récupère les images de la caméra vidéo et détecte si les yeux sont fermés ou non.
Le code ci-dessous est extrait de l'article. L'idée du projet est de s'en servir pour
faire autre chose que le clignement des yeux avec peut-être un peu de machine learning.
Qu'arriverez-vous à détecter au cours de ce projet ?

::

     import numpy as np
     import cv2
     import dlib
     from scipy.spatial import distance as dist

     PREDICTOR_PATH = "path to your shape_predictor_68_face_landmarks.dat file"

     FULL_POINTS = list(range(0, 68))
     FACE_POINTS = list(range(17, 68))

     JAWLINE_POINTS = list(range(0, 17))
     RIGHT_EYEBROW_POINTS = list(range(17, 22))
     LEFT_EYEBROW_POINTS = list(range(22, 27))
     NOSE_POINTS = list(range(27, 36))
     RIGHT_EYE_POINTS = list(range(36, 42))
     LEFT_EYE_POINTS = list(range(42, 48))
     MOUTH_OUTLINE_POINTS = list(range(48, 61))
     MOUTH_INNER_POINTS = list(range(61, 68))

     EYE_AR_THRESH = 0.25
     EYE_AR_CONSEC_FRAMES = 3

     COUNTER_LEFT = 0
     TOTAL_LEFT = 0

     COUNTER_RIGHT = 0
     TOTAL_RIGHT = 0

     def eye_aspect_ratio(eye):
       # compute the euclidean distances between the two sets of
       # vertical eye landmarks (x, y)-coordinates
       A = dist.euclidean(eye[1], eye[5])
       B = dist.euclidean(eye[2], eye[4])

       # compute the euclidean distance between the horizontal
       # eye landmark (x, y)-coordinates
       C = dist.euclidean(eye[0], eye[3])

       # compute the eye aspect ratio
       ear = (A + B) / (2.0 * C)

       # return the eye aspect ratio
       return ear

     detector = dlib.get_frontal_face_detector()

     predictor = dlib.shape_predictor(PREDICTOR_PATH)

     # Start capturing the WebCam
     video_capture = cv2.VideoCapture(0)

     while True:
       ret, frame = video_capture.read()

       if ret:
         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

         rects = detector(gray, 0)

         for rect in rects:
           x = rect.left()
           y = rect.top()
           x1 = rect.right()
           y1 = rect.bottom()

           landmarks = np.matrix([[p.x, p.y] for p in predictor(frame, rect).parts()])

           left_eye = landmarks[LEFT_EYE_POINTS]
           right_eye = landmarks[RIGHT_EYE_POINTS]

           left_eye_hull = cv2.convexHull(left_eye)
           right_eye_hull = cv2.convexHull(right_eye)
           cv2.drawContours(frame, [left_eye_hull], -1, (0, 255, 0), 1)
           cv2.drawContours(frame, [right_eye_hull], -1, (0, 255, 0), 1)

           ear_left = eye_aspect_ratio(left_eye)
           ear_right = eye_aspect_ratio(right_eye)

           cv2.putText(frame, "E.A.R. Left : {:.2f}".format(ear_left), (300, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
           cv2.putText(frame, "E.A.R. Right: {:.2f}".format(ear_right), (300, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

           if ear_left < EYE_AR_THRESH:
             COUNTER_LEFT += 1
           else:
             if COUNTER_LEFT >= EYE_AR_CONSEC_FRAMES:
               TOTAL_LEFT += 1
               print("Left eye winked")
             COUNTER_LEFT = 0

           if ear_right < EYE_AR_THRESH:
             COUNTER_RIGHT += 1
           else:
             if COUNTER_RIGHT >= EYE_AR_CONSEC_FRAMES:
               TOTAL_RIGHT += 1
               print("Right eye winked")
             COUNTER_RIGHT = 0

         cv2.putText(frame, "Wink Left : {}".format(TOTAL_LEFT), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
         cv2.putText(frame, "Wink Right: {}".format(TOTAL_RIGHT), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

         cv2.imshow("Faces found", frame)

       ch = 0xFF & cv2.waitKey(1)

       if ch == ord('q'):
         break

     cv2.destroyAllWindows()

*Modules à installer*

* `opencv <http://opencv.org/>`_
* `dlib <https://pypi.python.org/pypi/dlib>`_

Il faudra installer ces modules le plus tôt possible car selon les systèmes
d'exploitation, ce n'est pas toujours un processus évident.

.. _l-parole-reel:

Reconnaissance de la parole en temps réel et BOT (2017)
-------------------------------------------------------

Deux exemples et deux articles pour commencer :

* `Realtime Audio Visualization in Python <http://www.swharden.com/wp/2016-07-19-realtime-audio-visualization-in-python>`_
* `Easy Speech Recognition in Python with PyAudio and Pocketsphinx <http://www.codesofinterest.com/2017/03/python-speech-recognition-pocketsphinx.html>`_

L'idée du projet est d'abord d'arriver à faire fonctionner la reconnaissance de la parole
en temps réel puis de se diriger vers l'implémentation d'un
`BOT <http://www.xavierdupre.fr/app/jupytalk/helpsphinx/2017/devoxx2017.html>`_.
Ci-dessous un exemple de code extrait du second article cité plus haut.

::

     import speech_recognition as sr

     # obtain audio from the microphone
     r = sr.Recognizer()
     with sr.Microphone() as source:
       print("Please wait. Calibrating microphone...")
       # listen for 5 seconds and create the ambient noise energy level
       r.adjust_for_ambient_noise(source, duration=5)
       print("Say something!")
       audio = r.listen(source)

     # recognize speech using Sphinx
     try:
       print("Sphinx thinks you said '" + r.recognize_sphinx(audio) + "'")
     except sr.UnknownValueError:
       print("Sphinx could not understand audio")
     except sr.RequestError as e:
       print("Sphinx error; {0}".format(e))

*Modules à installer*

* `pyaudio <https://people.csail.mit.edu/hubert/pyaudio/docs/>`_
* `pocketsphinx <https://pypi.python.org/pypi/pocketsphinx>`_
* `speechrecognition <https://pypi.python.org/pypi/SpeechRecognition/>`_

Il faudra installer ces modules le plus tôt possible car selon les systèmes
d'exploitation, ce n'est pas toujours un processus évident.
