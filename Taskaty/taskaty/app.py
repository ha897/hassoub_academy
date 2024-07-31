#تخليه يعمل بسطر الاوامر 
from argparse import ArgumentParser
from .TaskController import TaskController
def main():
    controler = TaskController("tasks.txt")
    perser = ArgumentParser(description="Simple CLI Task Manager")
    subparsers = perser.add_subparsers()
    add_task = subparsers.add_parser('add',help="Add the given task")

    add_task.add_argument("title", help="Title of the task", type=str)
    add_task.add_argument("-d","--description", help="Show description of the task", type=str, default=None)
    add_task.add_argument('-s', '--start_date', help='Date to begin the task', type=str, default=None)
    add_task.add_argument('-e', '--end_date', help='Date to end the task', type=str, default=None)
    add_task.add_argument('--done', help='Check whether the task is done or not', default=False)
    #ما استخدمنا اسهم ()لان ما نبغا استدعائه بهذي النقطة
    add_task.set_defaults(func = controler.add_task)

    list_tasks = subparsers.add_parser('list', help='List unfinished tasks')
    list_tasks.add_argument('-a', '--all', help='List all the tasks', action='store_false')
    list_tasks.set_defaults(func = controler.display)


    remove = subparsers.add_parser('remove', help='Remove a task')
    remove.add_argument('-t', '--task', help='The task to be removed (Number)', type=int)
    remove.set_defaults(func = controler.remove)

    reset = subparsers.add_parser("reset",help="Remove all tasks")
    reset.set_defaults(func = controler.reset)

    args = perser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()