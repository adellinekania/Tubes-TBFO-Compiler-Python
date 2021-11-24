# Python Compiler
## Tugas Besar - IF2124 Formal Language Theory and Automata
Kelompok 4 - K2 - Bandung Institute of Technology

| NIM       | Nama                     |
| --------- | ------------------------ |
| 13520066  | Putri Nurhaliza          |
| 13520072  | Jova Andres Riski Sirait |
| 13520084  | Adelline Kania Setiyawan |

## General Information
This is a python compiler using Context-Free Grammar (CFG) which is then simplified into Chomsy Normal Form (CNF) as the basis for syntax validity and Finite Automata (FA) to handle variable names. This program is implemented with the CYK (Cocke-Younger-Kasami) algorithm.

#### Important Files
| File            |  Content                                   |
|----------------------|--------------------------------------------|
| `/doc`               | Laporan                                    |
| `cfg.txt`             | Context-Free Grammar G(V,T,P,S)                   |
| `cnf.txt`      | Chomsky-Normal Form G(V,T,P,S)                         |
| `CFGtoCNF.py`       | Converter CFG to CNF                          |
| `helper.py`              | Helper for converter                 |
| `cyk.py`              | Main program               |
| `fa.py`           | Finite Automata Implementation |


### Supported Syntax
| | | | | | |
|-------|--------|--------|--------|-------|--------|
| False | class | is | return | None | continue |
| for | True | def | from | while | and |
| not | with | as | elif | if | else |
| or | import | pass | break | raise | in |

## Technologies Used
- [Python 3.9.0](https://www.python.org/) (This version is the minimum requirement)
## How To Use


* Clone this repository:

  ```
  $ git clone https://github.com/adellinekania/Tubes-TBFO-Compiler-Python.git
  ```
* To get the latest cnf.txt, run this command in the terminal:
  ```
  python CFGtoCNF.py cfg.txt
  ```
* Write the program you want to compile in txt file
* To compile the program in txt file, run this command in the terminal:
  ```
  python cyk.py
  ```
  then input your txt filename, for example 
  ```
  input.txt
  ```
  or you can also supply arguments on the command line
  ```
  python cyk.py test.txt
  (Write path to the file)
  ```
  the command depends on the python command your computer is using (py, python, python3)
* DONE! this compiler will tell whether your input program compiles successfully or not
