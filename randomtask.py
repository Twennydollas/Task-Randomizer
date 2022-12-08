from dice import Die
import shelve

tasks = []
die = Die()
save_file = shelve.open('data')
type(save_file)
print("Twenny's Task Randomizer")
print("Type load to load last task list.")
print("Input task:")

while True:
    task = input()
    task = task.upper()
    match task:
        case "":
            print("Not a task")
        case "LOAD":
            try:
                tasks = save_file['tasks']
                die.num_sides = len(tasks) - 1
                choice = die.roll()
                print("Today's task is : " + tasks[choice])
                break
            except KeyError:
                print("No list to load. Please input new tasks.")
        case "ROLL":
            if len(tasks) >= 2:
                die.num_sides = len(tasks) - 1
                choice = die.roll()
                print("Today's task is : " + tasks[choice])
                print("Do you want to save your list of tasks? y/n")
                save = input()
                match save:
                    case 'y':
                        save_file['tasks'] = tasks
                        print("Tasks saved and Closing.")
                    case other:
                        print("Closing.")
            else:
                print("Not enough tasks to randomize. Closing.")
            break
        case other:
            print("Task added to list.")
            print("Type roll to randomize tasks or type another task.")
            tasks.append(task)

close = input("Press enter to close")
save_file.close()
