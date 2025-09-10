# General information on computers

This is a brief overview of computers, with a focus on illustrating the role of application software.

**What is a computer?**

A quick look on [Wikipedia](https://en.wikipedia.org/wiki/Computer) provides a simple definition: _a computer is a machine that can be programmed to automatically carry out sequences of arithmetic or logical operations (computation)._

This can take on a variety of meanings, and of course modern computers are everywhere around us, from smart watches and cell phones to the old desktop computer buried by old exams underneath Robert's desk. For our purposes in this book we will consider the following definition of computer

```{tip}
**Our Definition of Computer**: a machine that can be configured with software to execute programs to automatically carry out operations, in particular numerical analyses and visualization. The machine can be physically present (i.e., a desktop or laptop computer), or a virtual machine (i.e., a "cloud" computer; although this is accessible over the internet and may seem like it does not exist, in reality there is always a physical computer sitting somewhere in an air-conditioned server farm processing those 1's and 0's).
```

A computer can be broken down into a number of components, for example: hardware, software and peripherals, as illustrated in the figure below.

```{figure} https://files.mude.citg.tudelft.nl/typical.svg
---
width: 95%
name: computer_typical
---
Essential components of a typical computer. In particular, we are interested in the Application Software.
```

Although it is not the focus of this book, it is important to recognize the complexity in hardware, software and components that we often take for granted in modern computers (similar diagrams can be imagined for everyday devices like your cell phone). Of all these components, our work in scientific computing generally focuses on the software part of a computer, which can be broken down into two parts: the _system_ and _application software._

The _system software_ includes the _operating system_ (OS) of a computer and the _drivers_ that allow the OS to be run on a particular set of hardware. Common examples are the Windows and Mac (Apple) OS's. ALthough the OS on your computer is critical to consider, as we will see later, our goal is to install a few tools (software) that are compatible with our OS/computer and will eventually enable us to ignore the specific OS that we are running, especially when collaborating with colleagues.

As far as this book is concerned, the _application software_ is where our true interest lies, as it is here where we will be writing programs to solve our problems of interest and collaborate with others. This is where our everyday software tools for scientific computing are categorized, for example, Python, VS Code, Matlab, our web browsers (e.g., Chrome) and much more software! As illustrated in the following figure, "we want to be" working at a relatively high level of application software (e.g., writing Python code to conduct analysis and make interesting visualizations) such that we don't have to worry about which OS we are working on. This is both to allow us to focus on our work, as well as collaborate others.


```{figure} https://files.mude.citg.tudelft.nl/apps.svg
---
width: 80%
name: computer_applications
---
Relationship between the code we write, the OS-specific tools we need to install and our computer.
```

Of course, there are times when we still need to be conscious of which OS we are running, but this is less frequent, for example, when we are installing the proper version of `conda` or Python, as well as our IDE of choice (e.g., VS Code).