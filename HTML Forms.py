#  Q 2
# Task 1 
<!DOCTYPE html>
<html>
<head>
    <title>Email Input Example</title>
</head>
<body>
    <form>
        <label for="email">Email Address:</label>
        <input type="email" id="email" name="email" placeholder="Enter your email" required>
        <br><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>

# Task 2
<!DOCTYPE html>
<html>
<head>
    <title>Number Input Example</title>
</head>
<body>
    <form>
        <label for="quantity">Quantity:</label>
        <input type="number" id="quantity" name="quantity" placeholder="Enter a quantity" min="1" max="100" step="1" required>
        <br><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>

# Task 3
<!DOCTYPE html>
<html>
<head>
    <title>Date Input Example</title>
</head>
<body>
    <form>
        <label for="date">Select Date:</label>
        <input type="date" id="date" name="date" placeholder="Select a date" min="2023-01-01" max="2024-12-31" required>
        <br><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>

# Task 4
<!DOCTYPE html>
<html>
<head>
    <title>Range Input Example</title>
</head>
<body>
    <form>
        <label for="rating">Rating:</label>
        <input type="range" id="rating" name="rating" min="1" max="10" oninput="this.nextElementSibling.value = this.value">
        <output>5</output>
        <br><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>

# Task 5
<!DOCTYPE html>
<html>
<head>
    <title>Color Input Example</title>
</head>
<body>
    <form>
        <label for="color">Choose Color:</label>
        <input type="color" id="color" name="color" value="#ff0000">
        <br><br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>

# Q 2
# Task 1
<!DOCTYPE html>
<html>
<head>
    <title>Comprehensive Form</title>
</head>
<body>
    <form>
        <label for="language">Favorite Programming Language:</label>
        <select id="language" name="language">
            <option value="python">Python</option>
            <option value="javascript">JavaScript</option>
            <option value="java">Java</option>
            <option value="csharp">C#</option>
        </select>
        <br><br>

        <label>Level of Expertise:</label>
        <input type="radio" id="beginner" name="expertise" value="beginner">
        <label for="beginner">Beginner</label>
        <input type="radio" id="intermediate" name="expertise" value="intermediate">
        <label for="intermediate">Intermediate</label>
        <input type="radio" id="advanced" name="expertise" value="advanced">
        <label for="advanced">Advanced</label>
        <br><br>

        <label>Preferred Development Platforms:</label>
        <input type="checkbox" id="web" name="platform" value="web">
        <label for="web">Web</label>
        <input type="checkbox" id="mobile" name="platform" value="mobile">
        <label for="mobile">Mobile</label>
        <input type="checkbox" id="desktop" name="platform" value="desktop">
        <label for="desktop">Desktop</label>
        <br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>

# Task 2
<!DOCTYPE html>
<html>
<head>
    <title>Accessible Form</title>
</head>
<body>
    <form>
        <label for="language">Favorite Programming Language:</label>
        <select id="language" name="language" aria-label="Favorite Programming Language">
            <option value="python">Python</option>
            <option value="javascript">JavaScript</option>
            <option value="java">Java</option>
            <option value="csharp">C#</option>
        </select>
        <br><br>

        <fieldset>
            <legend>Level of Expertise:</legend>
            <input type="radio" id="beginner" name="expertise" value="beginner" aria-label="Beginner">
            <label for="beginner">Beginner</label>
            <input type="radio" id="intermediate" name="expertise" value="intermediate" aria-label="Intermediate">
            <label for="intermediate">Intermediate</label>
            <input type="radio" id="advanced" name="expertise" value="advanced" aria-label="Advanced">
            <label for="advanced">Advanced</label>
        </fieldset>
        <br><br>

        <fieldset>
            <legend>Preferred Development Platforms:</legend>
            <input type="checkbox" id="web" name="platform" value="web" aria-label="Web">
            <label for="web">Web</label>
            <input type="checkbox" id="mobile" name="platform" value="mobile" aria-label="Mobile">
            <label for="mobile">Mobile</label>
            <input type="checkbox" id="desktop" name="platform" value="desktop" aria-label="Desktop">
            <label for="desktop">Desktop</label>
        </fieldset>
        <br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>


