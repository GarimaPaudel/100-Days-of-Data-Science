# 100-Days-of-Data-Science
Welcome to my 100-Days-of-Data-Science Repository

## Day 1 - Variables and Strings in Python
- 1️⃣ Creating Variables and checking data type with type() function.
- 2️⃣ Learnt about two important data types; Integer and String
- 3️⃣ Changing data types
- 4️⃣ String as Array
- 5️⃣ Striping, Slicing, Splitting, Concatenating, replacing , formatting and indexing in string

## Day 2 - Conditionals and Loops
- 1️⃣ Conditionals🔗:
    - Utilizing the if statement to execute code based on a condition.
    - Employing elif to add more conditions to the decision-making process.
    - Falling back on the else statement for actions when no conditions are met.
- 2️⃣ Loops🔄:
   - For loops to iterate through sequences like lists, tuples, and more.
   - range() function for controlled iterations.
   - Embracing the efficiency of while loops for repeated execution until a condition becomes false.

## Day 3 - Python's Fundamental Data Structures
- 1️⃣  Lists: mutable data structure, changeable, ordered sequence of elements inside square brackets[ ].
   - Explored the versatile world of lists
   - dynamic arrays that can hold a mix of data types.
   - Used functions like 'len()', sum(), max(), min(), sorted()`append()`, `insert()`,'extend()', `remove()` , etc. to manipulate elements.
   -  Performed slicing techniques.
- 2️⃣  Tuples: Dived into the immutable realm of tuples
   - inside  brackets().
   - similar to lists, but their values cannot be changed after creation and doesnot support item reassignment.
   - Perfect for protecting important data!
- 3️⃣ Dictionaries: A dictionary is a collection which is unordered, changeable and indexed.
   -  In python, dictionaries are written with curly brackets, and they have keys and values.
   - Elements are in the form of key-value pairs.
   -  Provides fast data retrieval.
   - Learned to add, modify, and access elements using keys.
   -  Also learned about nested dictionaries.
- 4️⃣ Sets: Set is an unordered collection data type that is iterable, mutable and has no duplicate elements.
   - Python's set class represents the mathematical notion of a set.
   - This is based on a data structure known as hash table.
   - Explored the world of sets, unordered collections of unique elements.
   - Utilized functions like `add()`, 'clear()', `remove()`, issubset() etc. ,
   - Set operations like union, difference and intersection.
   - Eliminates duplicates.

## Day 4 - Functions is Python
 - 1️⃣ Defining Functions: Functions are defined using the def keyword, followed by a name and parentheses. They can take parameters, which are placeholders for data we'll use inside the function.
 - 2️⃣  Function Calls: We call functions by using their names followed by parentheses. We can pass arguments to functions, which are the actual data we want to operate on.
 - 3️⃣ Return Statements: Functions can return values using the return statement. This allows us to capture the output of a function and use it elsewhere in our code.
 - 4️⃣ Types of Arguments: Functions can have 🔹 Default Arguments 🔹 Positional Arguments 🔹 Keyword Arguments 🔹 Arbitary Arguments
 - 5️⃣ Variable Scope: I learned about the concept of variable scope. Variables defined inside a function have local scope, while those defined outside have global scope. It's essential to understand how scope affects variable accessibility.
 - 6️⃣ Lambda Functions: I explored lambda functions, which are concise, anonymous functions often used for simple operations. They're created using the lambda keyword.
 - 7️⃣ Recursion: I delved into recursive functions, where a function calls itself. It's a powerful technique that can be used to solve complex problems.

## Day 5 - Object Oriented Concepts
 - 🔷 Object-Oriented Programming is a programming paradigm that organizes code into reusable, self-contained objects. These objects are instances of classes, which are essentially blueprints for creating objects.
 - 🔷 Python is a versatile and popular programming language that supports OOP principles.
 - 1️⃣ Classes and Objects: I gained insights into the essence of classes as blueprints for creating objects. This paradigm allows me to encapsulate data and behavior within elegant structures.
 - 2️⃣ Attributes and Methods: The foundation of OOP, attributes hold data while methods define actions. This modular approach enhances code organization and readability.
 - 3️⃣ Constructors: With the __init__ method, I unlocked the ability to initialize objects and set their initial attributes right upon creation.
 - 4️⃣ Destructors: Managing resource cleanup is crucial, and the __del__ method lets me take care of that when objects are no longer needed.
 - 5️⃣ str() Function: This function lets me customize how an object is represented as a string, enhancing clarity and debugging.
 - 6️⃣ Inheritance: The concept of creating specialized classes, derived from existing ones, fascinated me. It promotes code reuse and empowers me to build hierarchies of related classes.
 - 7️⃣ Access Modifiers: I explored the world of access modifiers, including public, private, and protected member access. These modifiers offer a structured way to control interaction with class attributes and methods.

## Day 6 - More Object Oriented Concepts
 - 1️⃣ Method Overriding: Method overriding is the ability of a subclass to provide a specific implementation for a method that is already defined in its superclass.
 - 2️⃣ Method Resolution Order(MRO): Method Resolution Order determines the sequence in which classes are searched for a requested method. It follows the C3 linearization algorithm.
 - 3️⃣ Polymorphism: Polymorphism allows objects of different classes to be treated as objects of a common base class, leading to code that can work with objects of multiple types. It means the same function name (but different signatures) being used for different types.
 - 4️⃣ Duck Typing: Duck typing is a concept where the type or class of an object is determined by its behavior (methods and properties) rather than its explicit type.
 - 5️⃣ Encapsulation: It describes the idea of wrapping data and the methods that work on data within one unit.

## Day 7 - Exception Handling and File Handling
 - 1️⃣ Exception Handling: An exception is an event that occurs during the execution of a program that disrupts the normal flow of instructions. It can be caused by various reasons, such as invalid input, resource unavailability, or unexpected behavior.
     - Try-Except Block: The primary mechanism to handle exceptions in Python is the try-except block. It allows us to wrap a block of code that might raise exceptions, and then specify how to handle those exceptions.
     - Else Clause: The else clause can be added after all except clauses and will execute if no exception occurs within the try block.
     - Finally Clause: The finally clause is used to specify code that will be executed no matter what, whether an exception occurred or not.
     - Raising Exceptions: You can explicitly raise exceptions using the raise statement. This is useful when you want to signal an error condition yourself.
     - Custom Exceptions: We can create our own custom exception classes by inheriting from existing exception classes. This can help us categorize and handle specific errors in our code.
 - 2️⃣ File Handling
     -  Opening and Closing Files:
        - open() function: Used to open a file, it returns a file object.
        - close() method: Used to close the file when you're done with it.
    - File Modes:
       -  'r': Read mode (default).
       - 'w': Write mode, truncating the file if it already exists.
       - a': Append mode, adding data to the end of the file if it exists.
       - 'x': Exclusive creation mode, creating a new file if it doesn't exist.
       - 'b': Binary mode, used for working with binary files.
       - 't': Text mode (default), used for working with text files.
    - Reading from Files:
       - read(): Reads the entire content of the file.
       -  readline(): Reads a single line from the file.
       -  readlines(): Reads all lines into a list.
    - Writing to Files:
      - write(): Writes a string to the file.
      -  writelines(): Writes a list of strings to the file.
    - Context Managers (with Statement): A safer way to handle files using the with statement. It automatically handles opening and closing of the file.

## Day 8 - NumPy
  -  Advantages of NumPy over Python Lists: NumPy offers lightning-fast array operations and efficient memory usage, making it a go-to choice for numerical computations and data manipulation.
  -  Key Functions and Attributes: I got hands-on with np.array() to create arrays, and explored attributes like array.shape() and array.size for shape and size information. The dtype attribute helped me manage data types effortlessly.
  -  Array Manipulation: I learned to manipulate arrays with functions like transpose, np.empty, np.ones, and np.arange(). Reshaping arrays using array.reshape(), array.flatten(), and array.ravel() proved incredibly useful for data restructuring.
  -  Array Slicing and Indexing: NumPy's array slicing capabilities blew my mind! From extracting specific elements to working with slices, I've gained a solid understanding of accessing and manipulating array data.
  -  Mathematical Operations: I explored functions like np.std(), np.log(), and basic arithmetic operations (add, subtract, multiply, divide) on arrays.
  -   Trigonometric and String Operations: The library surprised me with its versatility. I experimented with trigonometric functions and even string operations using NumPy arrays.

## Day 9 - Pandas
- Pandas is a Python library used for working with data sets.It is a powerful Python library that provides data manipulation, analysis, and cleaning tools and is widely used in data science, machine learning, and any data-related tasks. I leant about:
  -  Constructing DataFrames
  -  Concept of csv data and working with them
  -  Indexing using column name, rowindex and rowindex, column index and Slicing
  -  Find null values
  -  several functions like head(), tail(), describe(), info(),isnull(), value_counts(), unique(), and so on.
  
## Day 10 - More Pandas
 - With the read_json() function, I've been able to effortlessly load JSON data into Pandas dataframes, providing me with a structured, tabular format to work with. And there is also to_json() method and it lets me seamlessly convert Pandas dataframes back into JSON format, making data exchange a breeze.
 - One tool that has truly dazzled me is the json_normalize() function. It's like having a decoder for nested JSON structures! This function flattens nested JSON data into a neat and tidy dataframe
 - Also ventured into Pandas' read_html() function. With this gem, I can effortlessly extract HTML tables from web pages and transform them into Pandas dataframes. This is an invaluable skill for converting messy web data into structured, analyzable formats. Plus, the to_html() method allows me to reverse the process, seamlessly converting dataframes back into HTML tables.

## Day 11 - Handling Null Values
- 1️⃣ Deletion or Removal:
  -  Listwise Deletion: It implies removing entire rows with at least one null value. I realized that this approach is suitable when the null values are relatively rare and not systematically distributed. We use .dropna() to do this.
.dropna(axis = 0) for deletion of rows
  - Column Dropping: If a column contains a high proportion of null values and is not crucial for analysis, you can consider dropping the column altogether.
.dropna(axis = 1) for deletion of columns
- 2️⃣ Imputation:
Imputation involves replacing null values with estimated or inferred values. This helps to retain data points and maintain the structure of the dataset.
  -  Mean/Median Imputation: Replace null values with the mean or median of the non-null values in the same column. This method is suitable for numerical data.
  -  Mode Imputation: Replace null values with the mode (most frequent value) of the non-null values in the column. This method is suitable for categorical data.
  -  Interpolation: For time-series or sequential data, null values can be estimated using interpolation methods like linear interpolation.

## Day 12 - Matplotlib Library
- label, title, xlabel, ylabel, xticks, yticks, plt.show()
-  linewidth, marker, markersize, and markeredgecolor, shorhand notation, saving the graph
- Bargraph
- Piechart
- Histograms
- Box and Whisker Plots
- Visualized the gas_prices,csv and fifa_data.csv data using Matplotlib

## Day 13 - Seaborn Library
  - 1️⃣ Line Plot : Explored trends and relationships between variables over time or categories. Customized colors, markers, and labels for clear insights.

  - 2️⃣ Bar Plot : Learned the art of comparing categorical data and showcasing frequency distributions. Leveraged hues and stacked bars to enhance understanding.

  - 3️⃣ Pair Plot : Discovered the power of visualizing pairwise relationships among multiple numerical variables.

  - 4️⃣ Dist Plot : Combined histograms and kernel density estimates for insightful data distribution visualization. Customized colors, line styles, and plot types to convey information effectively.

  - 5️⃣ Scatter Plot : Relationships between two numerical variables with the elegance of scatter plots. Used colors, markers, and sizes to enhance visual representation.

  - 6️⃣ Heatmap : Embraced the world of 2D matrix data visualization using colors to highlight correlations, relationships, and patterns. A fantastic tool for understanding large datasets.

## Day 14 - Linear Algebra
### Followed Course "Linear Algebra for Machine Learning and Data Science" by DeepLearning.AI : [Link to course](https://coursera.org/share/4ba5d65a3df9d87e99e10296a3030624)
  - System of Sentences, System of Information
  - Sytem of Equations
  - Linear and Non Linear Equations
  - System of Linear Equations as Lines
  - Linear Dependence and Linear Independence
  - Relation of Determinant and Singularity

## Day 15 - Linear Algebra
  -  Solve a system of linear equations using the elimination method.
  -  Use a matrix to represent a system of linear equations and solve it using matrix row reduction.
  -  Solve a system of linear equations by calculating the matrix in the row echelon form.
  -  Calculate the rank of a system of linear equations and use the rank to determine the number of solutions of the system.

## Day 16 - Linear Algebra
  -  Perform common operations on vectors like sum, difference, and dot product.
  -  Multiply matrices and vectors.
  -  Represent a system of linear equations as a linear transformation on a vector.
  -  Calculate the inverse of a matrix, if it exists.
  -  Neural Networks and Matrices

## Day 17 - Linear Algebra
  -  Interpret the determinant of a matrix as an area and calculate determinant of an inverse of a matrix and a product of matrices.
  -  Determine the bases and span of vectors.
  -   Find eigenbases for a special type of linear transformations commonly used in machine learning.
  -   Calculate the eignenvalues and eigenvectors of a linear transformation (matrix).

## Day 18 - Calculus
### Followed Course "Calculus for Machine Learning and Data Science" by DeepLearning.AI : [Link to course](https://coursera.org/share/0eb4398a2ae0be79a014cccf78cdb366)
  -  Machine Learning motivation
  -  Motivation to derivatives
  -  Derivatives and Tangents
  -  Slopes, maxima and minima
  -  Concept of Derivatives
  -  Approximation of Derivatives
  -  Derivatives and their notation
  -  and some common derivatives

## Day 19 - Calculus
  - Derivative of trigonometric functions
  - Meaning of the Exponential(e)
  - The derivative of e^x, logx
  - Existence of the derivative

## Day 20 - Calculus
 - 🔶 Properties of Derivatives:
    - Multiplication By scalars
    - The Sum rule
    - The Product Rule
    - The Chain Rule
 - 🔶 Optimization
    -  Introduction to Optimization
    - Optimization of squared loss: one powerline problem, the two powerline problem, and the three powerline problem.

 ## Day 21 - Calculus
  - 1️⃣ Optimization of Log Loss
  - 2️⃣ Tangent Planes
  - 3️⃣ Partial Derivatives
  - 4️⃣ Gradients
  - 5️⃣ Gradients and maxima/minima
  - 6️⃣ Optimization with gradients

## Day 22 - Calculus
  - 1️⃣ Optimization using Gradient Descent in One Variable
  - 2️⃣ Optimization using Gradient Descent in Two Variables
  - 3️⃣ Optimization using Gradient Descent - Least Square
  - 4️⃣ Optimization using Gradient Descent - Least Square with Multiple Observations

## Day 23 - Ongoing
