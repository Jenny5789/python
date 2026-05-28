##############################################################################
#######################       배열  구조 리스트        #######################
##############################################################################

class ADT_list:
    def __init__(self):
        self.list = []

    #--------------------------------        상태확인      -------------------------
    #--------------------------------    isempty(), isfull()   ---------------------
    ## 리스트가 비어있는지 확인
    def isempty(self):
        size = len(self.list) == 0
        return size


    ## 리스트는 사이즈가 정해져 있는 것이 아니므로 가득 찰 수 없다.
    def isfull(self):
        return False


    #--------------------------------    insert(pos, e)    -------------------------
    ## pos 위치에 새로운 요소 e를 삽입
    def insert(self, pos, e):
        ## 'pos'의 범위가  '0 <= pos <= 리스트 길이' 인 경우 ----> 삽입 가능
        if 0 <= pos <= len(self.list):
            self.list.append(None)
            
             ## insert pos 기준 우측으로 한 칸씩 index를 이동
            for i in range(len(self.list) - 1, pos, -1):      
                self.list[i] = self.list[i - 1]  
   
            self.list[pos] = e

            return True

        return False

    #--------------------------------    delete(pos)    ---------------------------
    ## pos 위치에 있는 요소를 삭제
    def delete(self, pos):
        ## 'pos'의 범위가  '0 <= pos < 리스트 길이' ----> 삭제 가능
        if 0 <= pos < len(self.list):

            ## delete pos 기준 좌측으로 한 칸씩 index를 이동
            for i in range(pos,len(self.list) - 1, 1):      
                self.list[i] = self.list[i + 1]
            
            self.list.pop()

            return True

        return False

    #--------------------------------    getEntry(pos)    --------------------------
    ## 해당 인덱스에 위치한 텍스트 반환
    def getEntry(self, pos):
        ## 'pos'의 범위가  '0 <= pos < 리스트 길이' ----> 반환 가능
        if 0 <= pos < len(self.list):
            return self.list[pos]
        
        return None

    #--------------------------------    size()    ----------------------------------
    ## 리스트 안의 요소 개수 반환
    def size(self):
        return len(self.list)
    
    #--------------------------------    clear()    ---------------------------------
    ## 리스트를 초기화
    def clear(self):
        self.list = []

    #--------------------------------    find(item)    ------------------------------
    ## 리스트에서 item이 있는지 찾아 인덱스를 반환
    def find(self, item):

        for i in range(len(self.list)):
            if self.list[i] == item:
                return i
            
        return -1
    
    #--------------------------------    replace(pos, item)    ----------------------
    ## pos에 위치한 요소를 item으로 교체
    def replace(self, pos, item):

        ## 'pos'의 범위가  '0 <= pos < 리스트 길이' ----> 교체 가능
        if 0 <= pos < len(self.list):
            self.list[pos] = item
            return True

        return False


    #--------------------------------    display()    -------------------------------
    ## 화면에 내용 출력
    def display(self):

        if len(self.list) == 0:
            print("리스트가 비어있습니다.")
        else:
            print("리스트가 비어있지 않습니다. 현재리스트: ", self.list)


    #--------------------------------    append()    -------------------------------
    ## 리스트의 맨 뒤에 새로운 항목을 추가
    def append(self, e):
            cur_len = len(self.list)
            self.list.append(None)
            self.list[cur_len] = e

            return True
    



########################################################################################
############################       연결된 구조 리스트       ############################ 
########################################################################################

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length
    

    #-------------------------------    isempty(), isfull()   ---------------------
    ## 리스트가 비어있는지 확인
    """
    before: head -> [1| ] -> [2| ] -> [3|None]   => False
    before: head -> None                          => True
    """
    def isempty(self):
        return self.length == 0
    

    ## 연결 구조 리스트는 계속 이어 붙일 수 있으므로 가득 찰 수 없다.
    """
    head -> [1| ] -> [2| ] -> [3| ] -> [4| ] -> ... => 항상 False
    """
    def isfull(self):
        return False
    

    #--------------------------------   appendleft(x)     -------------------------
    ## 연결 리스트의 맨 앞에 x를 추가, head에 추가
    """
    before: head -> [1| ] -> [2| ] -> [3|None]
    after:  head -> [0| ] -> [1| ] -> [2| ] -> [3|None]
    """
  
    def appendleft(self, data):
       
        node = Node(data)
        node.next = self.head  # 새 노드를 기존 head에 연결
        self.head = node       # head를 새 노드로 이동
        self.length += 1


    #--------------------------------   append(x)     -----------------------------
    ## 연결 리스트의 맨 끝에 x를 추가, tail에 추가
    """
    before: head -> [1| ] -> [2| ] -> [3|None]
                                        ↑
                                여기까지 찾아와 연결
    after:  head -> [1| ] -> [2| ] -> [3| ] -> [4|None]
    """

    def append(self, data):
        if self.head is None:
            self.head = Node(data)

        else:
        ## 마지막 노드 까지 순회
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = Node(data)  # 마지막 노드에 새 노드 연결
        self.length += 1


    #--------------------------------   popleft(x)     ---------------------------
    ## 연결 리스트의 첫 번째 노드의 값을 반환하고, 해당 노드를 삭제
    """
    before: head -> [1| ] -> [2| ] -> [3|None]
    after:  head -> [2| ] -> [3|None]   [1|None] <- 제거
    """

    def popleft(self):
        if self.head is None:
            return None
        node = self.head
        self.head = self.head.next
        self.length -= 1
        return node.data


    #--------------------------------   pop(x)     -----------------------------
    ## 연결 리스트의 마지막 노드의 값을 반환하고, 해당 노드를 삭제
    """
    before: head -> [1| ] -> [2| ] -> [3|None]
    after:  head -> [1| ] -> [2|None]   [3|None] <- 제거
    """
    def pop(self):
        if self.head is None:
            return None
        
        if self.head.next is None:
            node = self.head
            self.head = None
            self.length -= 1
            return node.data
        
        prev = None
        node = self.head
        while node.next is not None:
            prev = node
            node = node.next

        prev.next = None
        self.length -= 1
        return node.data


    #--------------------------------   remove(x)     -----------------------------
    ## 값이 x인 노드를 찾아 삭제
    """
    before: head -> [1| ] -> [2| ] -> [3|None]
    after:  head -> [1| ] -> [3|None]   [2|None] <- 제거
    """
    def remove(self, target):
        node = self.head
        while node is not None and node.data != target:
            prev = node
            node = node.next

        # target이 없을 때
        if node is None:
            return False
        
        # 첫 번째 노드일 때
        if node == self.head:
            self.head = self.head.next

        # 이전 노드를 다음 노드로 연결
        else:
            prev.next = node.next
        self.length -= 1
        return True


    #--------------------------------   insert(x)     -----------------------------
    ## 연결 리스트의 i번 인덱스 위치에 x 를 삽입
    """
    before: head -> [1| ] -> [2| ] -> [3|None]
    after:  head -> [1| ] -> [9| ] -> [2| ] -> [3|None]
    """
    def insert(self, i, data):
        
        if i <= 0:
            # 맨 앞에 삽입
            self.appendleft(data)

        elif i >= self.length:
            # 맨 뒤에 삽입
            self.append(data)

        else:
            node = self.head
            for _ in range(i - 1):
                node = node.next
            new_node = Node(data)
            # 새 노드를 다음 노드에 연결
            new_node.next = node.next
            # 이전 노드를 새 노드에 연결
            node.next = new_node
            self.length += 1



    #--------------------------------   reverse()     -----------------------------
    ## 연결 리스트의 순서를 뒤집기
    """
    before: head -> [1| ] -> [2| ] -> [3|None]
    after:  head -> [3| ] -> [2| ] -> [1|None]
    """
    def reverse(self):
        if self.length < 2:
            return
        
        prev = None
        ahead = self.head.next

        while ahead:
            self.head.next = prev
            prev = self.head
            self.head = ahead
            ahead = ahead.next
        self.head.next = prev
