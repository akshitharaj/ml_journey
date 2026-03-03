{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7b56d2bd-c7e4-4d20-882e-75144c5db297",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]\n"
     ]
    }
   ],
   "source": [
    "onetotwenty = list(range(1,21))\n",
    "print(onetotwenty)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a2f16913-308f-40c2-885e-3159a2d336c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "4\n",
      "6\n",
      "8\n",
      "10\n",
      "12\n",
      "14\n",
      "16\n",
      "18\n",
      "20\n"
     ]
    }
   ],
   "source": [
    "for i in range(1,20+1):\n",
    "    if i % 2 == 0:\n",
    "        print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "82b877c8-8577-4d93-99d8-4f14a8d79d94",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "4\n",
      "6\n",
      "8\n",
      "10\n",
      "12\n",
      "14\n",
      "16\n",
      "18\n",
      "20\n"
     ]
    }
   ],
   "source": [
    "a = 1\n",
    "b = 20\n",
    "for i in range(a, b+1):\n",
    "    if i % 2 == 0:\n",
    "        print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "ff41fbb5-9e82-4e07-ae7b-b03d694c91a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Jack': 95, 'Jones': 80, 'Mary': 96}\n"
     ]
    }
   ],
   "source": [
    "students = {\"Jack\" : 95, \"Jones\" : 80, \"Mary\" : 96}\n",
    "print(students)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "76bbd823-748b-44b6-8ba6-7d776238282a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def average(numbers):\n",
    "    if not numbers:\n",
    "        return 0\n",
    "    else:\n",
    "        total_sum = sum(numbers)\n",
    "        count = len(numbers)\n",
    "        average = total_sum / count\n",
    "        return average\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "60e33b31-8161-4ea6-8e6e-2a4726ed94ff",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10.5\n"
     ]
    }
   ],
   "source": [
    "print(average(onetotwenty))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a71233fa-3276-4564-a9b7-8acc9fd0bceb",
   "metadata": {},
   "outputs": [],
   "source": [
    "def variance(arr):\n",
    "    mean = sum(arr)/len(arr)\n",
    "    return sum((x - mean)**2 for x in arr)/len(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "110a6de5-88ff-48d9-8cc9-362850463e72",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "33.25\n"
     ]
    }
   ],
   "source": [
    "print(variance(onetotwenty))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "e94ab09d-78c3-4921-b0cf-b327a251845d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(5,)\n",
      "3.0\n",
      "1.4142135623730951\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "arr = np.array([1,2,3,4,5])\n",
    "print(arr.shape)\n",
    "print(arr.mean())\n",
    "print(arr.std())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "ea897f83-d88e-436c-bc17-05a0e54acb63",
   "metadata": {},
   "outputs": [],
   "source": [
    "#list vs array\n",
    "#vectorization\n",
    "#broadcasting\n",
    "#reshaping"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "4022598e-8243-4659-9930-99788881f001",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(2, 3)\n",
      "[[1 2]\n",
      " [3 4]\n",
      " [5 6]]\n"
     ]
    }
   ],
   "source": [
    "matrix = np.array([[1,2,3],[4,5,6]])\n",
    "print(matrix.shape)\n",
    "print(matrix.reshape(3,2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "41709cc2-e505-40da-b56a-999904760533",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Why Numpy is better for ML?\n",
    "# - Efficient array operations\n",
    "# - Broadcasting and Vectorization\n",
    "# - Integration with ML libraries\n",
    "# - Memory efficiency and performance\n",
    "# - Advanced Mathematical Functions\n",
    "# - Data Handling and Preprocessing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "353eafd1-ff62-4517-8901-1720201a2d16",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.14.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
