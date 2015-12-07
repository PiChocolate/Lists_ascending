# Lists_ascending
'''06.12.2015'''
'''Unification of the two lists into one serial'''
the_first_list = list(input('Enter the first series of numbers'
                            ' without spaces and commas: '))
the_second_list = list(input('Enter the second series of numbers'
                            ' without spaces and commas: '))
the_final_list = the_first_list + the_second_list
the_final_list.sort()
print('Your number ascending: ', the_final_list)
input('\n\nPress "Enter" to exit')
