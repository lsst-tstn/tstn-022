
:tocdepth: 1

.. Please do not modify tocdepth; will be fixed when a new Sphinx theme is shipped.

.. sectnum::

.. note::

   While analyzing data taken during campaigns in late 2019 and early 2020 with the LATISS instrument in the Auxiliary Telescope, we noticed that the sky position angle on the headers had inconsistent results, compared with object catalogs.
   At the same time we noticed that some data taken with longer exposure times and subsequent data taken on the same field showed signs of rotation.
   After analysis of the data we discover that the issue was due to the pointing component having the wrong direction for the rotator.
   This tech-note documents our findings.

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

Data Analysis
=============

The analysis focused on two different datasets; a group of exposures of well known easy to match targets and a long (>300s) exposure.
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
    | 2020-03-13 |   131  |      -94.6 |    -198.6 |  390.0    | HD 98993 | 11:23:12 | -36:09:53 |
    +------------+--------+------------+-----------+-----------+----------+----------+-----------+










.. Add content here.
.. Do not include the document title (it's automatically added from metadata.yaml).

.. .. rubric:: References

.. Make in-text citations with: :cite:`bibkey`.

.. .. bibliography:: local.bib lsstbib/books.bib lsstbib/lsst.bib lsstbib/lsst-dm.bib lsstbib/refs.bib lsstbib/refs_ads.bib
..    :style: lsst_aa
