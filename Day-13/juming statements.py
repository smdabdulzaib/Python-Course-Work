

#break is used to terminate the loop when a certain condition is met. It allows you to exit the loop prematurely, regardless of whether the loop's condition is still true. This can be useful in situations where you want to stop iterating once you've found what you're looking for or when a specific event occurs.
for i in range(1,11):
    if i==5:
        break
    print(i)


#continue is used to skip the current iteration of the loop and move on to the next iteration. When the continue statement is encountered, the rest of the code inside the loop for that particular iteration is skipped, and the loop proceeds with the next iteration. This can be useful when you want to ignore certain values or conditions while still continuing to process other iterations.
for i in range(1,11):
    if i==5:
        continue
    print(i)

