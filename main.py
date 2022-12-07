from multiprocessing import Process, Queue

def queuePut(arrayOfNumbers, start, end, queue):
    queue.put(sum(arrayOfNumbers[start:end]))


def sumArray():
        arrayOfNumbers = [10, 2, -5, 1, 5, 76, 44, 2, -5]
        summary = 0
        nproc = 4
        bsize = (len(arrayOfNumbers) // nproc) + 1
        procs = [None] * nproc
        queue = Queue()
        for i in range(nproc):
            start = i * bsize
            end = min((i + 1) * bsize, len(arrayOfNumbers))
            p = Process(target=queuePut, args=(arrayOfNumbers, start, end, queue))
            p.start()
            procs[i] = p

        for i in range(nproc):
            summary += queue.get()

        print(f"Suma wszystkich liczb z tablicy wynosi: {summary}")

def minNumber():
    arrayOfNumbers = [118, 551, 883, -199, 754, 794, 351, -546, -887, -412, 901, -130, -348, 511, 622, 986, 111, 984,
                      -488, -113, 217, 795, 617, 51, 531, -937, -62, -362, -5, 509, 994, 119, 9, -129, -536, -195, 577,
                      -819, 307, 855, -702, -854, 434, -476, -96, 922, 498, 850, -464, -803, 481, -447, -489, 925, 706,
                      690, -207, -978, -66, 180, -409, 908, 999, -661, 58, -485, -808, 335, -992, -668, 502, -51, 446,
                      893, 667, -264, 250, -882, -598, -878, 455, -183, 438, 380, 304, 169, 354, 289, 236, -162, 715,
                      287, 123, 930, -86, 780, -793, 162, -846, -855]
    min = arrayOfNumbers[0]
    for number in arrayOfNumbers:
        if number < min:
            min = number
    print(f"Najmniejszą liczą w zbiorze jest: {min}")

def countVowels():
    count = 0
    arrayOfVowels = ['a', 'e', 'i', 'o', 'u', 'y']
    text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    for letter in text:
        for vowel in arrayOfVowels:
            if vowel == letter:
                count += 1
    print(f"Liczba samogłosek w tekście wynosi: {count}")

if __name__ == '__main__':
    sumArray()
    minNumber()
    countVowels()
