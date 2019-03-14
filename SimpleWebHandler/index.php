<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>DEML 0.3 beta TEST</title>
</head>

<style>
    *{
        font-family: sans-serif;
    }
    form{
        text-align: center;
    }
    textarea{
        width: 50%;
        height: 60vh;
        background-color: #282c34;
        border: none;
        outline: none;
        color:white;
        font-weight: 700;
    }    
</style>
<body>
    <form action="output.php" method="post">
       <h1>DEML TEST</h1>
        <textarea id="deml" name="deml-code" id=""></textarea>
        <br>
        <input type="submit">
    </form>
</body>
</html>