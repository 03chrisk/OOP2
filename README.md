# OOP - 2023/24 - Assignment 2

This is the base repository for assignment 2.
Please follow the instructions given in the [PDF](https://brightspace.rug.nl/content/enforced/243046-WBAI045-05.2023-2024.1/assignment%202_v1.1.pdf) for the content of the exercise.

## How to carry out your assignment

**PLEASE FOLLOW THESE STEPS:**

1. Use this template and create a private repository:
   ![](use_template.png)
2. Please add your partner and `oop-otoz` to the collaborators.
3. Create a new branch called `submission` **before adding any files**.
4. Add your code in the `main` branch (**IF YOU DO NOT ADD ANYTHING, THE PULL REQUEST WILL NOT WORK**).
5. Make sure that Actions are allowed: Settings -> Actions -> General -> Allow all actions and workflows.
6. Create a pull request from the `main` branch to your `submission` branch and check that your changes are captured.
7. Now finish your solution.
8. When you are ready to submit, add `oop-otoz` to the reviewers.

**Notes:**

- **Leave the \*\***init\***\*.py files untouched**.
- Do not move the `main.py` files.
- Do not move `requirements.txt`.
- Make the pull request AFTER SUBMITTING SOME CHANGES.

Below this line, you can write your report to motivate your design choices.

## Submission

The code should be submitted on GitHub by opening a Pull Request from the `main` branch on to the `submission` branch. This means that `submission` is the base branch and `main` the compare branch. **Make sure to push your code only to `main`!**

There are automated checks that verify that your submission is correct:

1. Deadline - checks that the last commit in a PR was made before the deadline.
2. Reproducibility - downloads libraries included in `requirements.txt` and runs `python3 main.py`. If your code does not throw any errors, it will be marked as reproducible. **Make sure it is reproducible before submission!**
3. Style - runs `flake8` on your code to ensure adherence to style guides.
4. Tests - runs `unittest` on your tests in `part_1/tests` to make sure all tests succeed.

---

## Your report

# Part 1

## Class Codemaker

Constructor:

The first method in the class is the constructor, which does not take any arguments and it returns None. This class has three attributes, symbols, code_length and secret_code and we decided to set all three to private. This is because these attributes should not be accessed or changed by the users thus setting them to private signals that they should be handled with care. Instead we added getters with the use of the property decorator to make it possible for us to access these values from different classes. For the secret code we also created a setter as it is necessary for our tests.

Generate code:

This method randomly generates a code, only using the colors that are specified in the list symbols. The method does not take any arguments and returns a list with the generated code. We set it to private as we only use it in the codemaker class when initializing the secret_code attribute. 
 
## Class Codebreaker

Make guess:

This method will prompt the user for input until they enter a valid code. There are no arguments for this method and it returns the list with the user’s guess. We decided to keep this method public as we call it in the mastermind class so we have to be able to access it from outside of the codebreaker class. 

## Class Mastermind

Constructor:

The constructor takes an integer as argument, which is the maximum number of attempts and it does not return anything (None). The class has three attributes, a codemaker, a codebreaker and max_attempts. We set all three attributes to private as the users do not have to access them and they should not be changed when the game is running. For these attributes we added getters with the property decorator. 

Evaluate guess:

This method takes the user’s guess as the argument and returns a tuple of integers, which is the number of correct positions and symbols in the user’s guess. We set this method to private as we only use it in the mastermind class and the user’s also do not have to have access to it.

Play:

This method handles the game by getting input and evaluating the user’s guess. The method play does not take arguments and it also does not return anything. This method is public as we use it outside of the class, in the main file. 


# Part 2

## 2.1

In addition to our already existing model from assignment 1, we added an abstract base class called MachineLearningModel that holds the blueprint for methods every ml model should have. These include train, predict and a getter for the coefficients.

With these changes in mind we had to adjust the type hints in regression plotter and model saver to MachineLearningModel from Any. We also made the MultipleLinearRegression class inherit from the abstract base class.

## 2.2

The next change we made was implementing the @property decorator for private attributes in the MultipleLinearRegression class. Using the decorator makes getting and setting attributes easier for the user since they don’t have to specifically call get_attribute() and set_attribute() methods. 

To implement this we changed the attribute setters by decorating them with the @attribute.setter decorator. We do not have an @attribute.getter decorator as the @property decorator functions as the getter and we only return the value of the attribute rather than also modifying or formatting it. Then finally we had to change all instances in the codebase where we called the getters and setters to reflect the new @property decorator implementation. 


## 2.3
For implementing Lasso and Ridge regression we added another class called regularized regression, which inherits from the multiple linear regression class. Both Lasso and Ridge inherit from the regularized regression class. 

## Regularized regression class

Constructor:

This method takes as input two floats, an integer and a string and returns None. The class has four attributes, alpha which is the learning rate, lambda which determines the strength of the regularization, number of iterations and the initiation strategy. We set all the attributes to private and we added setters and getters for all of them to be able to access them and change the values when necessary, even in a different class. We decided to make them weak private as it still signals that these variables should be handled with care while making it easier to use them in the subclasses of our codebase. For the setters and getters we used the property decorator. But by making them private we evade changing these values by accident, thus making them more protected and showing that they have to be accessed with care. 

Initialize coefficients:

This method takes an integer as an argument and returns a np.ndarray. Based on the initial strategy attribute, this method initializes the coefficients either with numbers from a normal or from a uniform distribution. We set this method to private as the user does not have to be able to access it, this method is called in the public train method of the class.  

Train:

This method takes two np.ndarrays, which are X_train and y_train and returns None. Apart from training the model, in this method we also call several methods: for calculating loss, for calculating the MAE and for calculating the gradient. As instructed in the assignment, we also logged the necessary information before updating the parameters. This method is public as we use it outside of the class. 

Calculate loss and MAE:

These methods take as argument the residuals as a np.ndarray and they return a float. We set these to private as we only call them in the train method and they do not have to be accessed otherwise. 

Abstract methods:

Calculate regularization penalty and calculate gradient are private abstract methods. Calculate gradient takes as arguments two np.ndarrays and returns one, while calculate regularization penalty does not take any arguments and returns a float. These methods are abstract as we do not implement them in this class, only in the children classes and they are private as they are not accessed from outside of the class. 

## Lasso regression class and Ridge regression class

In these classes we only implement two functions each as they inherit from the regularized regression class. These two functions calculate regularization penalty and calculate gradient and the arguments and returns are as it has been described above. In the calculated regularization penalty method, for the lasso regression we implement the L1 regularization penalty and for ridge the L2. We set these methods to private as we only call them in the train method thus we (neither the user) do not have to have access to them directly. 
