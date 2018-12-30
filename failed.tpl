    <!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8" />
    <title>Traditional Turkish Desserts</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="style.css">
    <link rel="icon" href="inkscape/logo.png">
</head>

<body style="background-color: beige"> 
    <nav class="navbar navbar-inverse">
        <ul class="nav-bar-1">
            <li class="nav-bar-2">
                <a class="active" href="index.html">Home</a>
            </li>
            <li class="nav-bar-2">
                <a href="milk.html">Desserts Made With Milk</a>
            </li>
            <li class="nav-bar-2">
                <a href="syrup.html">Desserts Made With Syrup</a>
            </li>
        </ul>
    </nav>

    <section>
        
        <h1 class="h1"><img class="logo-left" src="inkscape/logo.png" alt="logo">Traditional Turkish Desserts<img class="logo-right" src="inkscape/logo.png" alt="logo"></h1>
        <h2>Login Failed. Try Again </h2>
		<div style="margin-left:30px;">
            <form action="/login" method="post" 
            style="font: bold 20px Times;" >
            Username: <input name="username" type="text"  />
            Password: <input name="password" type="password" />
            <input class="recipe-milk-button-home" value="Login" type="submit" />
        </form>
        </div>
		<div style="margin-left:30px;">
            <form action="/comment" method="post"
            style="font: bold 20px Times;" >
            Comment: <input name="comment" type="text"  />
			Show my user name:
			<input type="radio" name="show" value="yes" checked> Yes
			<input type="radio" name="show" value="no"> No<br>
            <input class="recipe-milk-button-home" value="Comment" type="submit" />
        </form>
        </div>
		
		<div>
			<h2>Comments</h2>

		</div>
		
    </section>
</body>

</html>
    