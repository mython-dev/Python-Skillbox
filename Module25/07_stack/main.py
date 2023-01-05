# TODO здесь писать код


class Stack():
    def __init__(self) -> None:
        self.__st = []

    def __str__(self) -> str:
        return '; '.join(self.__st)
        # return str(self.__st)

    def push(self, elem):
        self.__st.append(elem)

    def pop(self):
        if len(self.__st) == 0:
            return None
        
        else:
            return self._st.pop

my_st = Stack()

for i in range(5):
    my_st.push(i)

print(my_st)

for _ in range(3):
    my_st.pop()

print(my_st)

class TaskManager:
    def __init__(self) -> None:
        self.task = dict()

    def __str__(self) -> str:
        display = []
        if self.task:
            for i_priority in sorted(self.task.keys()):
                display.append('{prior} {task}'.format(
                    prior  = str(i_priority),
                    task = self.task[i_priority],

                ))

            return ''.join(display)


    def new_task(self, task, priority):
        if priority not in self.task:
            self.task[priority] = Stack()
        self.task[priority].push(task)

manager  = TaskManager()

manager.new_task('Сделать уборку', 4)

manager.new_task('помыть посуду', 4)

manager.new_task('отдахнуть', 1)

manager.new_task('поесть', 2)

manager.new_task('сделать дз', 2)

print(manager)
