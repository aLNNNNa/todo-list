tasks = []
while True:
    print("\n=====待办清单=====")
    print("1. 添加任务")
    print("2. 查看所有任务")
    print("3.删除任务")
    print("4. 退出")
    choice = input("请选择操作（1-4）：")
    match choice:
        case "1":
            task = input("请输入任务内容：")
            tasks.append(task)
            print(f"已添加任务：{task}")
        case"2":
            if len(tasks) == 0:
                print("目前没有任务，添加一个吧！")
            else:
                print("待办任务列表：")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        case"3":
            if len(tasks) == 0:
                print("目前没有任务可删除，添加一个吧！")
            else:
                print("当前任务列表：")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    index = int(input("请输入要删除的任务编号："))
                    if 1 <= index <= len(tasks):
                        removed = tasks.pop(index - 1)
                        print(f"已删除任务：{removed}")
                    else:
                        print("无效的编号，请重新输入。")
                except ValueError:
                    print("请输入一个有效的数字。")
        case"4":
            print("感谢使用，再见！")
            break
        case _:
            print("无效的选择，请重新输入。")
