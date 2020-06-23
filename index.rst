
:tocdepth: 1

.. Please do not modify tocdepth; will be fixed when a new Sphinx theme is shipped.

.. sectnum::

.. note::

   While analyzing data taken during campaigns in late 2019 and early 2020 with the LATISS instrument in the Auxiliary Telescope, we noticed that the sky position angle on the headers had inconsistent results, compared with object catalogs.
   At the same time we noticed that some data taken with longer exposure times and subsequent data taken on the same field showed signs of rotation.
   After analysis of the data we discover that the issue was due to the pointing component having the wrong direction for the rotator.
   This tech-note documents our findings.

.. _section-introduction:

Introduction
============

The LSST Atmospheric Transmission and Slitless Spectrograph (LATISS) Instrument was integrated with the Auxiliary Telescope in late 2019 followed by a series of observing runs.
The initial observing runs where mainly dedicated to integration and commissioning tests, such as acquiring data for pointing model and building lookup tables for optical alignment.
Furthermore, a couple runs where also dedicated to taking initial datasets for pipeline testing.

Over the course of analyzing the dataset taken over these runs, we realized that the WCS information in the header did not match the expected field orientation.
Further attempts to refine the WCS with matching algorithms where unsuccessful, suggesting that the information in the header where wrong by a considerable amount.
Analysis of longer exposures (300s) and sequence of exposures of the same field showed clear signs of field rotation.
At the same time, analysis of mount telemetry showed no sign of induced jitter.

After consulting with Observatory Sciences, the pointing component vendors, it was acknowledged that it was possible that the Nasmyth rotation angles could have been setup incorrectly.
We then proceeded to investigate this possibility.
Using the time when the images where taken and the length of the exposure we queried the EFD for the mount telemetry data and pointing information.
The data was used to compute the expected sky position angle for a group of exposures (considering that the rotator was in the wrong direction) and the data was verified by eye first and later by catalog matching.
We also used a long exposure, taken by accident during one of the earliest runs, to verify this hypothesis.
We confirmed that the arcs formed by stars in the field are consistent with the expected arc-size if the rotator is moving in the wrong direction.

Following is a description of the analysis performed in the data to demonstrate that the AT Nasmyth rotator is being commanded by the pointing component in the wrong direction.
The pointing component will be updated to fix the issue.

.. _section-data-analysis:

Data Analysis
=============

The analysis focused on two different datasets; a group of exposures of well known easy-to-match targets and a long (>300s) exposure.
:numref:`table-dataset` contains a summary of the data used for this analysis.

.. _table-dataset:

.. table:: Journal of observations used for the rotator analysis.

    +------------+--------+------------+-----------+-----------+----------+----------+-----------+
    | dayObs     | seqNum | Sky Angle  | Sky Angle | Exp. time |  Object  | RA       |  Dec      |
    +------------+--------+------------+-----------+-----------+----------+----------+-----------+
    |            |        | Original   | Computed  | (sec)     |          | hh:mm:ss |  dd:mm:ss |
    +============+========+============+===========+===========+==========+==========+===========+
    | 2020-03-12 |   197  |      126.1 |     -10.7 |  2.0      | HD 68450 |  8:11:01 | -37:17:32 |
    +------------+--------+------------+-----------+-----------+----------+----------+-----------+
    | 2020-03-12 |   208  |      212.9 |      84.5 |  2.0      | HD 68450 |  8:11:01 | -37:17:32 |
    +------------+--------+------------+-----------+-----------+----------+----------+-----------+
    | 2020-03-13 |   130  |      -94.6 |    -198.6 |  5.0      | HD 98993 | 11:23:12 | -36:09:53 |
    +------------+--------+------------+-----------+-----------+----------+----------+-----------+
    | 2020-03-13 |   131  |      -94.6 |    -198.6 |  390.0    | HD 98993 | 11:23:12 | -36:09:53 |
    +------------+--------+------------+-----------+-----------+----------+----------+-----------+
    | 2020-03-13 |   132  |      -94.6 |    -198.6 |   30.0    | HD 98993 | 11:23:12 | -36:09:53 |
    +------------+--------+------------+-----------+-----------+----------+----------+-----------+

The equation to compute the sky position angle is as follows:

.. math:: \mathrm{rot\_sky} = \mathrm{PA} - \mathrm{El} - \mathrm{rot\_angle}.
   :label: math-rotsky-1

If the rotator has the inverse orientation, the corrected angle should be computed as:

.. math:: \mathrm{rot\_sky} = \mathrm{PA} - \mathrm{El} + \mathrm{rot\_angle}
   :label: math-rotsky-2

where ``rot_sky`` is the angle eastward of north between camera y-axis and north, ``PA`` is the Parallactic Angle, ``El`` is the target elevation in the local coordinate system and ``rot_angle`` is the Rotator/Nasmyth angle.

.. _section-HD98993:

HD 98993
--------

This is probably the best dataset to show that the rotator is moving in the wrong direction.
We have a short discovery exposure (``visitId = 2020031300130``), followed by a long 390s exposure (``visitId = 2020031300130``) and a subsequent 30s exposure (``visitId = 2020031300132``).
The :ref:`long exposure <figure-2020031300131>` clearly shows arc-like star trails, which is consistent with rotator drift.
The size of the arcs can be easily estimated since we know the plate scale of the images and, be compared to the expected arc-size in case the rotator is rotating in the wrong direction.
Visits ``2020031300130`` and ``2020031300132``, although do not show any sign of image streak (due to the shorter exposure times) can be used to validate that the streaks in ``2020031300131`` are continuous and not jitter during the exposure.

In :numref:`figure-2020031300131` we show visit ``2020031300131`` with rulers showing the arc length and its distance to the apparent center of rotation.
The measurement values are :math:`0.003\deg` and :math:`0.062\deg`, which translates to an angle of :math:`2.77\deg`.
If we compute the variation in the rotator position from the start to finish of that exposure, we obtain a variation of :math:`2.14\deg`, which is consistent with what we get from the arc-length above.

.. figure:: /_static/HD98993_131.png
   :name: figure-2020031300131
   :target: ../_images/HD98993_131.png
   :alt: HD 98993 390s exposure

   A long (390s) exposure of HD 98993 that clearly shows the rotator direction issue.

:numref:`figure-stackall` shows an inset of a stack of the three images.
The images are combined in pixel space to highlight the effect and arbitrarily scaled to highlight the effect.
The reference star from the first and last images are marked for reference along with the arc from the long exposure.
It is quite clear that the images rotates with the expected rate as if the rotator was moving in the wrong direction.

.. figure:: /_static/HD98993_stack.png
   :name: figure-stackall
   :target: ../_images/HD98993_stack.png
   :alt: HD 98993 stack

   Stacked images of HD 98993 showing the effect of rotation over the three test images, a short 5s exposure followed by long a 390s and a 30s exposure.
   The images are arbitrarily scaled to highlight the effect.


.. _section-HD68450:

HD 68450
--------

After performing the analysis on :ref:`HD 98993 <section-HD98993>` and we are confident that the rotator is moving in the wrong direction, we should be able to verify it using observations of different targets at different times with different requested sky rotation angles.

The analysis shown here was repeated in a number of different targets but we choose ``HD 68450`` because it is easy to identify the field rotation.
In :numref:`figure-HD68450` we show a finding chart with the field orientation (direction of North and East axis) and the images taken with the Auxiliary Telescope on the left and right-hand side, respectively.
Visits ``2020031200197`` and ``2020031200208`` are shown at the top and bottom, respectively, with two different orientations.
Images in the middle (labeled "original orientation") are shown with the sky angle taken from the commanded position.
The right-most images (labeled "computed orientation") are shown with the sky angle computed from the data available in the EFD.
The calculation is done by taking the time when the exposure starts and ends and querying for the telescope azimuth, elevation and nasmyth angle.
Then, assuming the rotator has the reversed direction, we compute the expected sky angle.
It is clear, from visual inspection, that the computed sky angle should be close to the correct sky angle orientation.
We then, assuming this angle as a starting point, calibrated the WCS from the images, and matched the resulting WCS with GAIA catalog.
In all cases we manage to confirm that the nasmyth rotator is rotating in the reverse direction.

.. figure:: /_static/HD68450.png
   :name: figure-HD68450
   :target: ../_images/HD68450.png
   :alt: HD 68450

   Comparison of HD 68450 observations taken with the Auxiliary Telescope and the field finding chart.
   The left hand panel shows the finding chart of the field with roughly the same FoV of the instrument.
   In the right hand panels we show the images of HD 68450 taken with the Auxiliary Telescope, with two different orientations.
   The original orientation (as sent to the pointing component) is shown in the middle panel and the computed orientation, considering that the rotator has the wrong orientation, is shown in the right.
   Values for the angles are shown in :numref:`table-dataset`.




.. Add content here.
.. Do not include the document title (it's automatically added from metadata.yaml).

.. .. rubric:: References

.. Make in-text citations with: :cite:`bibkey`.

.. .. bibliography:: local.bib lsstbib/books.bib lsstbib/lsst.bib lsstbib/lsst-dm.bib lsstbib/refs.bib lsstbib/refs_ads.bib
..    :style: lsst_aa
