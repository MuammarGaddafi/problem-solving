# LETS LEARN C + +    +++++++++++++++++++++++++



## FIRST OF ALL, why the main function in cpp returns an int, exactly a 0 ? : 

![WhatsApp Image 2025-09-03 at 01 36 27_a8fabfbf](https://github.com/user-attachments/assets/ead26f75-4936-4e43-8b5d-af94dd646e77)

For example for shell scripting :

./myProgram

if [ $? -eq 0 ]; then

  echo "Success!"
  
else

  echo "Failure!"

Here, $? captures the return value from main(). And that’s why it’s not just a number, it’s a signal of success, a contract with the OS
