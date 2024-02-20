# Capita Selecta of Software Engineering (2023/2024)

The repository hosts the material, developed and needed in the lab-sessions of CSSE,
at VUB Brussels. The material is developer by Johannes Härtel.

## Lab-Session 1 (21 November 2023)

This session will give a brief introduction to alternative libraries
used to represent and process data in MSR. We will discuss NumPy, Pandas, Spark, R (vectors), TensorFlow
and PyTorch. The PDF of the presentation can be found [here](session01/slides.pdf).

The second part will be a live demo of a basic data collection on a repository. The code
can be found [here](session01/src).


## Lab-Session 2 (5 December 2023)

In this session, we will take a look at models, and different ways to use them. We will explore conceptual alternatives
in how we can infer parameters. This will get relevant later when we answer our hypothesis about software development or predict bugs.

Slides can be found [here](session02/slides.pdf).
Backup code that illustrates the slides can be found [here](session02/src).

## Lab-Session 3 (12 December 2023)

Please **bring your laptop to lab-session 3** and ensure that the **code from lab-session 1 runs**.

Session 3 will be active. You can follow up on some ideas. The previous code from session 1 can be used as a starting point.
- You can follow up on resolving the problem of **comment length**. Different length comments should be reflected in our metric on comments.
- You can follow up on the idea of **watermarks**. Not all comments matter. Some are repetitive and have no true meaning. You can develop a creative solution.
- You can follow up on providing other metrics that **explain** why a class is commented. Taking a look at access modifications is a suitable option. Do you have other ideas?
- You can follow up on **blaming the developer**. This is complicated since you need to call git's blame. A potential outcome can be the developer with the highest contribution in the file. We can then check if developers have different commenting behavior.

The final program including the pull request by jbarber07, and fixed comment counting, can be found [here](session03/src/program.py).


## Lab-Session 4 (20 February 2024)

We will explore different ways of **implementing typical models** using **low to high-level** libraries.
We will implement a **linear (regression) model** with a single and many variables,
a **logistic regression**, and a **basic feed-forward neural network**.
We will use **sklearn**, **TensorFlow Core**, **Keras** and **Stan**.

The code can be found [here](session03/src). The slides can be found [here](session03/slides.pdf).

## Assignment 1

This assignment requires building a data set consisting of metrics that can be used for defect prediction.
We limit us to studying the Java files of one repository, [jwtk/jjwt](https://github.com/jwtk/jjwt).
We study the following revisions of the repository.

| SHA  | DATE        | AUTHOR                                                |
|-----|:--------------------------------------------------------|-------------|
| 529f04dd9097331220c3239bdadacee6b1dfd6de |2023-08-04 21:35:33 | lhazlewood |
| 894d6f298b6edc48bddedeaa8abd930cea744f9c |2021-02-17 19:39:11 | Dominik Dorn |
| 56db77ed7e4b9165c0440ffc451dd813c9713578 |2019-10-03 01:06:23 | sal0max |
| ba1f235bd157fd3a68fc5803de65ee4d1848d5a0 |2019-02-22 08:47:49 | Micah Silverman |
| 54ddbedbec5a2563209028d86e5b294091f8e1c4 |2018-07-20 23:23:23 | Les Hazlewood |
| a473dc4be1562476df6183edf91fffa575fda21f |2017-05-13 17:55:00 | aadrian |
| ceac032f11ebc0bf829c68961ca3c643eb85f70e |2016-06-30 23:11:08 | Les Hazlewood |
| 6a422211c8a16013592cbd88d0346ebe4ca3e788 |2015-10-13 01:07:01 | Les Hazlewood |
| 4d2080b36973314f8ed26887addda000de84809f |2015-06-26 20:34:33 | Les Hazlewood |
| 34a97add5b1fc99424ef5789a21254a77b3144b6 |2014-10-29 01:53:29 | Les Hazlewood |
| 39b456b1a37f49e35b80b464481c81500ee638c4 |2014-09-19 23:47:43 | Les Hazlewood |

For every revision `r`, compute the following metrics (ID) for all Java files in the repository at the particular revision.
The output file should be a CSV or line-delimited JSON file, with the columns or keys: *metric* (the ID of the metric), *value* (the value of the metric),
*file* (the path of the file), *revision* (the SHA of the revision).
The following metrics need to be extracted.

| ID  | Description                                                               |
|-----|:--------------------------------------------------------------------------|
| LOC | Number of lines of code in file `f` at a revision `r`. |
| CC  | Cyclomatic complexity in file `f` at a revision `r`. |
| NC1  | Number of commits changing file `f` **before** a revision `r`. |
| NC2  | Number of commits changing file `f` **after** a revision `r`.|
| BUG1 | Number of commits changing file `f` **before** revision `r` where the commit message includes a keyword (fix, bug ...) that indicates a defect in the file.|
| BUG2 | Number of commits changing file `f` **after** revision `r` where the commit message includes a keyword (fix, bug ...) that indicates a defect in the file.|
| DEV1 | Number of distinct developers who changed file `f` **before** a revision `r`.|
| DEV2 | Number of distinct developers who changed file `f` **after** a revision `r`.|

The code for analyzing a repository needs to be written in Python. You are 
encouraged to us the [gitpython](https://gitpython.readthedocs.io/en/stable/tutorial.html) library.
The library is already added the recent [environment.yml](environment.yml).
See an [example](session03/src/example_gitpython.py) from session 3.
**The submission requires the script to compute the metrics and the CSV or line-delimited JSON file. Deadline for the assignments: 21 June 2024**
