# GEEKBRAINS HOMEWORK  LESSON 1


# 1

# str1 = "abc"
# num1 = 123
# str2 = input("Enter name <<< ")
# num2 = int(input("Enter number <<< "))
# print("name >>> ", str2)
# print("number >>> ", num2)
# print("str1 >>> ", str1)
# print("num1 >>> ", num1)


# 2

# usInput = int(input("Enter time in seconds <<< "))
# seconds = (usInput%60)
# minutes = (usInput//60)%60
# hours = (usInput//3600)
# if hours > 99:
#     print("Hours value was clipped")
#     hours = hours%99
# print(f"{hours}:{minutes}:{seconds}")
# print('{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds)))
# я посчитал неспортивным вводить datetime


# 3

# usInput = input("Enter number <<<")
# result = int(usInput) + int(usInput+usInput) + int(usInput+usInput+usInput)
# print ("Result >>> ", result)


# 4

# usInput = int(input("Enter number <<< "))
# someList = []
# while True:
#     someList.append(usInput % 10)
#     usInput = usInput // 10
#     if usInput == 0:
#         break
# someList = sorted(someList, reverse=True)
# print(someList[0])


# 5

# income = int(input("Enter income <<< "))
# expenses = int(input("Enter expenses <<< "))
# if income > expenses:
#     print("All is good. Income > expenses")
#     rentabel = income / expenses
#     print("Profits ratio is ", rentabel)
#     ppl = int(input("Enter number of workers <<< "))
#     print("Incomes by a single worker ", income / ppl)
# else:
#     print("FIRMA UBITOCHNA ZAKRIVAEMSYA NA")


# 6

# print("Nu sho pobegaem?")
# startedKm = int(input("Enter first result <<< "))
# wantedKm = int(input("Enter wanted result <<< "))
# i = 2
# newRes = startedKm
# while True:
#     newRes = newRes * 1.10
#     if newRes <= wantedKm:
#         i += 1
#     else:
#         break
# print("TI PROBEZHISH", wantedKm, "KM NA DEN NOMER ", i)
