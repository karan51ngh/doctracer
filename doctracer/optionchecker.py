import sys


def optionchecker(argumentList):
    arr = [0, 0]
    if '--help' in argumentList:
        print("")
        print(" pass 1 arguments ['FILE NAME']")
        print("	options:")
        print(" 	-d | displays the complete path being travelled by the tool")
        print(" 	-c | displays the contents of the file")
        print(" 	-v | displays the version of the software")
        print("")
        print(" 	--help | displays help")
        print(" 	-version | displays the version of the software")
        exit()

    if '--version' in argumentList:
        print("")
        print(" version v0.2.0")
        print(" last update: 16th Nov,2021")
        print(" distributor: karan51ngh")
        print(" code name: alpha release")
        print(" MIT open source license")
        exit()

    if '-v' in argumentList:
        print("")
        print(" version v0.2.0")
        print(" last update: 16th Nov,2021")
        print(" distributor: karan51ngh")
        print(" code name: alpha release")
        print(" MIT open source license")
        exit()

    if len(sys.argv) < 2:
        print("")
        print(" WRONG FORMAT!!!")
        print("")
        print(" use --help option to get help")
        print("")
        exit()

    if '-d' in argumentList:
        arr[0] = 1
    if '-c' in argumentList:
        arr[1] = 1
    if '-cd' in argumentList:
        arr[0] = 1
        arr[1] = 1
    if '-dc' in argumentList:
        arr[0] = 1
        arr[1] = 1
    return arr
