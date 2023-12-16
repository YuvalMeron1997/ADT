import copy

class ByteNode:
    def __init__(self, byte):
        """
The constructor for ByteNode class
if byte is not a string on the length byte in not 8- there will be an error
next - Indicates another ByteNode or None
        @param byte: An 8-character string variable, each character is '0' or '1'
        """
        if type(byte) != str:
            raise TypeError('Wrong Type')
        if len(byte) != 8:
            raise ValueError('The len have to be 8')
        for number in byte:
            if number != '0' and number != '1':
                raise ValueError('The number have to be 1 or 0')
        self.byte = byte
        self.next = None

    def get_byte(self):
        """
The method will return the byte field
        @return: The method will return the byte field
        """
        return self.byte

    def get_next(self):
        """
The method will return the field value next
        @return: The method will return the field value next
        """
        return self.next

    def set_next(self, next):
        """
The method will update the next field in the next parameter
        @param next: next is a Byte Node type
        """
        self.next = next

    def __repr__(self):
        """
The method will return a string representing Byte Node in the following way: [byte]=>
        @return: The method will return a string representing Byte Node in the following way: [byte]=>
        """
        return f'[{self.byte}]=>'


from functools import total_ordering


@total_ordering
class LinkedListBinaryNum:
    def __init__(self, num):
        """
A constructor for LinkedListBinaryNum class
the constructor gets number and change it to binary number
Head- ByteNode representing the first byte of the list
Size- The number of bits needed to represent the number
        @param num: int. positive integer number. otherwise it will be error
        """
        if num < 0:
            raise ValueError('The num is not positive')
        if type(num) != int:
            raise TypeError('The number is not integer')
        if num == 0:
            self.head = ByteNode('00000000')
            self.size = 1
        answer = ''
        while num != 0:
            digit = num % 2
            num = num // 2
            answer = str(digit) + answer
        if len(answer) % 8 != 0:
            rest = len(answer) % 8
            answer = '0'*(8 - rest) + answer
        for digit1 in range(len(answer)):
                self.head = ByteNode(answer[0:8])
                self.size = int(len(answer) / 8)
                break
        first = self.head
        answer = answer[8:]
        while len(answer) != 0:
            next_n = ByteNode(answer[0:8])
            first.set_next(next_n)
            first = next_n
            answer = answer[8:]

    def add_MSB(self, byte):
        """
A method that adds a ByteNode vertebra as an MSB in LinkedListBinaryNum
MSB -The leftmost byte
        @param byte: An 8-character string variable, each character is '0' or '1'
        """
        first_node = ByteNode(byte)
        first_node.set_next(self.head)
        self.head = first_node
        self.size += 1

    def __len__(self):
        """
A method that returns the link number in the linked list
        @return: A method that returns the link number in the linked list
        """
        return self.size

    def __str__(self):  # end user
        """
A method that returns a representative string for printing purposes.
Each byte will be separated by '|'. '|' will appear at the beginning and end of the string
        @return: A string that represents the object by the format
        """
        empty = ''
        first_node = str(self.head)
        sec_node = self.head.get_next()
        while sec_node != None:
            for num in first_node:
                if num == '0' or num == '1':
                    empty += num
            empty = f'{empty}|'
            first_node = str(sec_node)
            sec_node = sec_node.get_next()
        if sec_node == None:
            for num in first_node:
                if num == '0' or num == '1':
                    empty += num
        return f'|{empty}|'

    def __repr__(self):  # developer
        """
A method that returns a string that represents the number in binary representation.
The method will return a string detailing the amount of vertebrae and their voting order according to the vertebrae arrangement.
        @return: A string that represents the object by the format
        """
        if self.size == 1:
            return f'LinkedListBinaryNum with {self.size} Byte, Bytes map: {self.head}' + 'None'
        else:
            sec_node = self.head.get_next()
            empty_str = str(self.head)
            while sec_node != None:
                empty_str += str(sec_node)
                sec_node = sec_node.get_next()
            return f'LinkedListBinaryNum with {self.size} Bytes, Bytes map: {empty_str}' + 'None'

    def __getitem__(self, item):
        """
A method that receives an index and returns the right byte. For an unsuitable type of input an error will be thrown
        @param item: int
        @return: A method that receives an index and returns the right byte
        """
        empty_str = ''
        if type(item) != int:
            raise TypeError('Index have to be int')
        if item >= self.size or item <= -self.size - 1:
            raise IndexError('The index invalid')
        for num in self.__str__():
            if num == '0' or num == '1':
                empty_str += num
        for number in empty_str:
            if item == 0:
                return empty_str[0:8]
            if item > 0:
                return empty_str[(8 * item):(8 * (item + 1))]
            if item < 0:
                return empty_str[(8 * (item + (self.size))):(8 * (item + self.size + 1))]

    # Order relations:
    def __gt__(self, other):
        """
The method checks if one number is bigger from the other one
        @param other: positive and integer number
        @return: True (if it is bigger) or False (otherwise)
        """
        if type(other) != LinkedListBinaryNum:
            raise TypeError('Must be LinkedListBinaryNum type')
        empty_binary = ''
        for num in self.__str__():
            if num == '0' or num == '1':
                empty_binary += num
        decimal_number = 0
        n_digits = len(empty_binary)
        for number in range(n_digits):
            if empty_binary[number] == '1':
                decimal_number += 2 ** (n_digits - number - 1)
        binary_num = ''
        for num1 in other.__str__():
            if num1 == '0' or num1 == '1':
                binary_num += num1
        decimal_number1 = 0
        n_digits1 = len(binary_num)
        for number1 in range(n_digits1):
            if binary_num[number1] == '1':
                decimal_number1 += 2 ** (n_digits1 - number1 - 1)
        return decimal_number > decimal_number1

    def __eq__(self, other):
        """
The method checks if 2 numbers are equal
        @param other: positive and integer number
        @return: True if the numbers are equal, False otherwise
        """
        if type(other) != LinkedListBinaryNum:
            raise TypeError('Must be LinkedListBinaryNum type')
        empty_binary = ''
        for num in self.__str__():
            if num == '0' or num == '1':
                empty_binary += num
        decimal_number = 0
        n_digits = len(empty_binary)
        for number in range(n_digits):
            if empty_binary[number] == '1':
                decimal_number += 2 ** (n_digits - number - 1)
        binary_num = ''
        for num1 in other.__str__():
            if num1 == '0' or num1 == '1':
                binary_num += num1
        decimal_number1 = 0
        n_digits1 = len(binary_num)
        for number1 in range(n_digits1):
            if binary_num[number1] == '1':
                decimal_number1 += 2 ** (n_digits1 - number1 - 1)
        return decimal_number == decimal_number1

    def __add__(self, other):
        """
Addition operators that returns a new object of type LinkedListBinaryNum.
If the input is not of the LinklistBinaryNum type or int type an error will be thrown. Also if the number is integer and negative
        @param other: positive and integer
        @return: Addition operators that returns a new object of type LinkedListBinaryNum.
        """
        if type(other) != int and type(other) != LinkedListBinaryNum:
            raise TypeError('It must be LinkedListBinaryNum type or int type')
        if type(other) == int and other < 0:
            raise ValueError('Must be positive number')
        if type(other) == int and other > 0:
            other = LinkedListBinaryNum(other)
        maximum_len = max(len(str(self)), len(str(other)))
        bin_num1 = str(self).zfill(maximum_len)
        bin_num2 = str(other).zfill(maximum_len)
        result = ''
        temp = 0
        for num_index in range(maximum_len - 1, -1, -1):
            result1 = temp
            if bin_num1[num_index] == '1':
                result1 += 1
            if bin_num2[num_index] == '1':
                result1 += 1
            if result1 % 2 == 1:
                result = '1' + result
            else:
                result = '0' + result
            if result1 < 2:
                temp = 0
            else:
                temp = 1
        if temp != 0:
            result = '1' + result
        empty = ''
        for index_num in range(len(result.zfill(maximum_len))):
            if index_num % 9 != 0:
               empty += result.zfill(maximum_len)[index_num]
            if index_num % 9 == 0:
                empty += ''
        self.head = ByteNode(empty[0:8])
        self.size = int(len(empty) / 8)
        empty = empty[8:]
        first = self.head
        if self.size > 1:
            while len(empty) != 0:
                next_n = ByteNode(empty[0:8])
                first.set_next(next_n)
                first = next_n
                empty = empty[8:]
        return self


    def __sub__(self, other):
        pass

    def __radd__(self, other):
        """
Addition numbers from the right side
        @param other: positive and integer number
        @return: Addition operators that returns a new object of type LinkedListBinaryNum.
        """
        return self + other


class DoublyLinkedNode:
    def __init__(self, data):
        """
A constructor for DoublyLinkedList
The class is defined by the fields:
data - Represents the information in the link
next - Represents the pointer to the next link or None if it is the last link
prev -Represents the pointer to the previous link or None if it is the first link
        @param data: Value. Can be of any type
        """
        self.data = data
        self.prev = None
        self.next = None

    def get_data(self):
        """
A method that returns the data in the link
        @return: A method that returns the data in the link
        """
        return self.data

    def set_next(self, next):
        """
A method that updates the next link
        @param next: type- DoublyLinkedNode
        """
        self.next = next

    def get_next(self):
        """
The method returns pointer to the next link
        @return: The method returns pointer to the next link
        """
        return self.next

    def get_prev(self):
        """
The method returns pointer to the previous link
        @return: The method returns pointer to the previous link
        """
        return self.prev

    def set_prev(self, prev):
        """
A method that updates the previous link
        @param prev: type- DoublyLinkedNode
        """
        self.prev = prev

    def __repr__(self):
        """
A method that returns a string representing the link in the format =>[data]<=
        @return: A method that returns a string representing the link in the format =>[data]<=
        """
        return f'=>[{self.data}]<='


class DoublyLinkedList:
    def __init__(self):
        """
A constructor for DoublyLinkedList class
The class is defined by the following fields:
Head- Indicates the first link or None if the list is empty
Tail- Indicates the last link or None if the list is empty
Size- Contains the number of links in the list
        """
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        """
A method that returns the number of links in the linked list
        @return: A method that returns the number of links in the linked list
        """
        return self.size

    def add_at_start(self, data):
        """
A method that adds data at the beginning of the list
        @param data: The value can be of any type
        """
        if self.size == 0:
            self.size = 1
            self.head = DoublyLinkedNode(data)
            self.tail = self.head
        else:
            new = DoublyLinkedNode(data)
            new.set_next(self.head)
            self.head.set_prev(new)
            self.head = new
            self.size += 1

    def remove_from_end(self):
        """
A method that removes and returns the data from the last link in the list or a StopIteration error if the list is empty
        @return: A method that removes and returns the data from the last link in the list or a StopIteration error if the list is empty
        """
        data_tail = self.tail.get_data()
        if self.size == 0:
            raise StopIteration('The list is empty')
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size = 0
            return data_tail
        prev = self.tail.get_prev()
        prev.set_next(None)
        self.size -= 1
        self.tail = prev
        return data_tail

    def get_tail(self):
        """
A method that returns the pointer to the last link in the list
        @return: A method that returns the pointer to the last link in the list
        """
        return self.tail

    def get_head(self):
        """
A method that returns the pointer to the first link in the list
        @return: A method that returns the pointer to the first link in the list
        """
        return self.head

    def __repr__(self):
        """
A method that returns a string representing the DoublyLinkedList in the format: Head==>DoublyLinkedList<==Tail
        @return: A method that returns a string representing the DoublyLinkedList in the format: Head==>DoublyLinkedList<==Tail
        """
        if self.size == 0:
            return 'Head==><==Tail'
        else:
            first = str(self.head)
            sec = self.head.get_next()
            while sec != None:
                first += str(sec)
                sec = sec.get_next()
            return f'Head={first}=Tail'

    def is_empty(self):
        """
A method that returns whether the list is empty
        @return: True if the list is empty. False otherwise
        """
        if self.size == 0:
            return True
        else:
            return False


class DoublyLinkedListQueue:
    def __init__(self):
        """
A constructor for DoublyLinkedListQueue class
data- field from DoublyLinkedList type
        """
        self.data = DoublyLinkedList()

    def enqueue(self, val):
        """
The method adds a data to the queue (from the begining of the queue)
        @param val: The value can be of any type
        """
        self.data.add_at_start(val)

    def dequeue(self):
        """
Removing and returning a data from a queue or an error if the queue is empty
        @return: The value can be of any type
        """
        if len(self.data) == 0:
            raise StopIteration('Empty queue')
        else:
            return self.data.remove_from_end()

    def __len__(self):
        """
A method that returns the number of members in the queue
        @return: The number of members in the queue
        """
        return self.data.__len__()

    def is_empty(self):
        """
A method that returns a Boolean value that indicates whether the queue is empty
        @return: True if the queue is empty. False otherwise
        """
        if self.data.__len__() == 0:
            return True
        else:
            return False

    def __repr__(self):
        """
A method that returns a string that represents the queue
        @return: A method that returns a string that represents the queue
        """
        if self.data.__len__() == 0:
            return 'Newest=>[]<=Oldest'
        else:
            empty = ''
            for tail1 in range(self.data.__len__()):
                tail = self.data.get_tail()
                empty = str(tail)[3:-3] + ',' + empty
                self.data.remove_from_end()
                self.data.add_at_start(str(tail)[3:-3])
            return f'Newest=>[{empty[:-1]}]<=Oldest'

    def __iter__(self):
        """
A method that returns an iterator to a class
        @return: A method that returns an iterator to a class
        """
        self.deep_copy_data = copy.deepcopy(self.data)
        return self

    def __next__(self):
        """
A method that returns the data of the next link in the iteration
        @return: A method that returns the data of the next link in the iteration
        """
        if len(self.deep_copy_data) == 0:
            raise StopIteration('The length of the list is 0')
        value = self.deep_copy_data.remove_from_end()
        if value.isnumeric():
            value = int(value)
        return value



from hw8_lib import Stack
from hw8_lib import BinarySearchTree


class NumsManagment:
    def __init__(self, file_name):
        """
A constructor for NumsManagment class
        @param file_name: File name as a string
        """
        self.file_name = file_name

    def is_line_pos_int(self, st):
        """
A method that checks whether the line in the file represents an integer and a positive number
        @param st: A string read from the file
        @return: True if it is a integer positive number. False otherwise
        """
        new_str = st[:-2]
        if len(st) == 0:
            return False
        for num in new_str:
            if num != '0' and num != '1' and num != '2' and num != '3' and num != '4' and num != '5' and num != '6' and num != '7' and num != '8' and num != '9':
                return False
        return True

    def read_file_gen(self):
        """
A method that returns a generator that in each iteration will return a representation of the next correct number in the file
        """
        nm = open("nums_in_memory.txt", "r")
        read = nm.readlines()
        for line in read:
            if self.is_line_pos_int(line) == True:
                line = int(line)
                yield str(LinkedListBinaryNum(line))

    def stack_from_file(self):
        """
A method that returns a stack with all the correct numbers in the file
        @return: A stack that contains all the correct numbers in the file
        """
        stack_1 = Stack()
        for line in self.read_file_gen():
            stack_1.push(line)
        return stack_1


    def sort_stack_descending(self, s):
        pass

    def queue_from_file(self):
        pass

    def set_of_bytes(self, q_of_nums):
        pass

    def nums_bst(self):
        pass

    def bst_closest_gen(self, bst):
        pass
