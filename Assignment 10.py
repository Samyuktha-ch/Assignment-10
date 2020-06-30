
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "@@What is Python language?                                                \n",
      "-Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.\n",
      "-Its design philosophy emphasizes code readability, and its syntax allows programmers to express\n",
      " concepts in fewer lines of code than possible in languages such as C++ or Java. \n",
      "-Python supports multiple programming paradigms, including object-oriented, imperative and \n",
      " functional programming or procedural styles. It features a dynamic type system and automatic \n",
      " memory management and has a large and comprehensive standard library.\n",
      "-The best way we learn anything is by practice and exercise questions.\n"
     ]
    }
   ],
   "source": [
    "def file_read(fname):                          #Python program to read an entire text file\n",
    "        txt = open(fname)\n",
    "        print(txt.read())\n",
    "file_read('test.txt')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the No.Of lines to be read:4\n",
      "@@What is Python language?                                                \n",
      "\n",
      "-Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.\n",
      "\n",
      "-Its design philosophy emphasizes code readability, and its syntax allows programmers to express\n",
      "\n",
      " concepts in fewer lines of code than possible in languages such as C++ or Java. \n",
      "\n"
     ]
    }
   ],
   "source": [
    "def file_read_from_head(fname, nlines):        #Python program to read first n lines of a file\n",
    "        from itertools import islice\n",
    "        with open(fname) as f:\n",
    "                for line in islice(f, nlines):\n",
    "                        print(line)\n",
    "a=int(input(\"Enter the No.Of lines to be read:\"))\n",
    "file_read_from_head('test.txt',a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "It's Everything about Python Exercises\n",
      "Hence the line is appended in the file\n"
     ]
    }
   ],
   "source": [
    "def file_read(fname):                         #Python program to read first n lines of a file\n",
    "        from itertools import islice\n",
    "        with open(fname, \"w\") as myfile:\n",
    "                myfile.write(\"It's Everything about Python Exercises\\n\")\n",
    "                myfile.write(\"Hence the line is appended in the file\")\n",
    "        txt = open(fname)\n",
    "        print(txt.read())\n",
    "file_read('test.txt')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the No.Of last lines to be read:3\n",
      " functional programming or procedural styles. It features a dynamic type system and automatic \n",
      " memory management and has a large and comprehensive standard library.\n",
      "-The best way we learn anything is by practice and exercise questions."
     ]
    }
   ],
   "source": [
    "def LastNlines(fname, N):                   #Python program to read last n lines of a file\n",
    "    with open(fname) as file:\n",
    "        for line in (file.readlines() [-N:]):\n",
    "            print(line, end ='')\n",
    "if __name__=='__main__': \n",
    "    fname='Test.txt'\n",
    "    N=int(input(\"Enter the No.Of last lines to be read:\"))\n",
    "    try: \n",
    "        LastNlines(fname, N) \n",
    "    except: \n",
    "        print('File not found')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['@@What is Python language?                                                \\n', '-Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.\\n', '-Its design philosophy emphasizes code readability, and its syntax allows programmers to express\\n', ' concepts in fewer lines of code than possible in languages such as C++ or Java. \\n', '-Python supports multiple programming paradigms, including object-oriented, imperative and \\n', ' functional programming or procedural styles. It features a dynamic type system and automatic \\n', ' memory management and has a large and comprehensive standard library.\\n', '-The best way we learn anything is by practice and exercise questions.']\n"
     ]
    }
   ],
   "source": [
    "def file_read(fname):                         #Python program to read a file line by line store it into a variable\n",
    "        with open (fname, \"r\") as myfile:\n",
    "                data=myfile.readlines()\n",
    "                print(data)\n",
    "file_read('test.txt')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['@@What is Python language?                                                \\n']\n",
      "['@@What is Python language?                                                \\n', '-Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.\\n']\n",
      "['@@What is Python language?                                                \\n', '-Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.\\n', '-Its design philosophy emphasizes code readability, and its syntax allows programmers to express\\n']\n",
      "['@@What is Python language?                                                \\n', '-Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.\\n', '-Its design philosophy emphasizes code readability, and its syntax allows programmers to express\\n', ' concepts in fewer lines of code than possible in languages such as C++ or Java. \\n']\n",
      "['@@What is Python language?                                                \\n', '-Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.\\n', '-Its design philosophy emphasizes code readability, and its syntax allows programmers to express\\n', ' concepts in fewer lines of code than possible in languages such as C++ or Java. \\n', '-Python supports multiple programming paradigms, including object-oriented, imperative and \\n']\n",
      "['@@What is Python language?                                                \\n', '-Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.\\n', '-Its design philosophy emphasizes code readability, and its syntax allows programmers to express\\n', ' concepts in fewer lines of code than possible in languages such as C++ or Java. \\n', '-Python supports multiple programming paradigms, including object-oriented, imperative and \\n', ' functional programming or procedural styles. It features a dynamic type system and automatic \\n']\n",
      "['@@What is Python language?                                                \\n', '-Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.\\n', '-Its design philosophy emphasizes code readability, and its syntax allows programmers to express\\n', ' concepts in fewer lines of code than possible in languages such as C++ or Java. \\n', '-Python supports multiple programming paradigms, including object-oriented, imperative and \\n', ' functional programming or procedural styles. It features a dynamic type system and automatic \\n', ' memory management and has a large and comprehensive standard library.\\n']\n",
      "['@@What is Python language?                                                \\n', '-Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.\\n', '-Its design philosophy emphasizes code readability, and its syntax allows programmers to express\\n', ' concepts in fewer lines of code than possible in languages such as C++ or Java. \\n', '-Python supports multiple programming paradigms, including object-oriented, imperative and \\n', ' functional programming or procedural styles. It features a dynamic type system and automatic \\n', ' memory management and has a large and comprehensive standard library.\\n', '-The best way we learn anything is by practice and exercise questions.']\n"
     ]
    }
   ],
   "source": [
    "def file_read(fname):                          #Python program to read a file line by line store it into an array\n",
    "        content_array = []\n",
    "        with open(fname) as f:\n",
    "            for line in f:\n",
    "                content_array.append(line)\n",
    "                print(content_array)\n",
    "file_read('test.txt')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Number of lines in the file are: 8\n"
     ]
    }
   ],
   "source": [
    "file=open(\"test.txt\",\"r\")                      #Python program to count the number of lines in a text file\n",
    "Count=0\n",
    "Content=file.read() \n",
    "CoList=Content.split(\"\\n\") \n",
    "for i in CoList: \n",
    "    if i: \n",
    "        Count=Count+1          \n",
    "print(\"Number of lines in the file are:\",Count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "File size in bytes of a plain file:  686\n"
     ]
    }
   ],
   "source": [
    "def file_size(fname):                         #Python program to get the file size of a plain file\n",
    "        import os\n",
    "        statinfo = os.stat(fname)\n",
    "        return statinfo.st_size\n",
    "print(\"File size in bytes of a plain file: \",file_size(\"test.txt\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The file will be copied to a new file named abc.txt\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'abc.txt'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "                                             #Python program to copy the contents of a file to another file\n",
    "print(\"The file will be copied to a new file named abc.txt\")\n",
    "from shutil import copyfile\n",
    "copyfile('test.txt','abc.txt')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['@@What is Python language?                                                \\n', '-Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.\\n', '-Its design philosophy emphasizes code readability, and its syntax allows programmers to express\\n', ' concepts in fewer lines of code than possible in languages such as C++ or Java. \\n', '-Python supports multiple programming paradigms, including object-oriented, imperative and \\n', ' functional programming or procedural styles. It features a dynamic type system and automatic \\n', ' memory management and has a large and comprehensive standard library.\\n', '-The best way we learn anything is by practice and exercise questions.']\n"
     ]
    }
   ],
   "source": [
    "def file_read(fname):                       #Python program to read a file line by line and store it into a list\n",
    "        with open(fname) as f:     \n",
    "                content_list = f.readlines()\n",
    "                print(content_list)\n",
    "file_read('test.txt')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}